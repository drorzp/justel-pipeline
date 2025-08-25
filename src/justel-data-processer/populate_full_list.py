#!/usr/bin/env python3
"""
Script to populate full-list.xlsx with new URLs from Justel
Based on the last date in the existing file, scrapes actual article URLs
from search result pages for all days from the next day until today.
"""

import pandas as pd
from datetime import datetime, timedelta
import re
import os
import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin


def extract_date_from_url(url):
    """Extract date from a Justel URL"""
    # Try to extract from pd_search parameter
    if 'pd_search=' in url:
        match = re.search(r'pd_search=(\d{4}-\d{1,2}-\d{1,2})', url)
        if match:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
    
    # Try to extract from pdd parameter (start date)
    if 'pdd=' in url:
        match = re.search(r'pdd=(\d{4}-\d{1,2}-\d{1,2})', url)
        if match:
            return datetime.strptime(match.group(1), '%Y-%m-%d')
    
    return None


def scrape_article_urls_from_page(page_url, max_retries=3):
    """
    Scrape article URLs from a Justel search results page
    
    Args:
        page_url: URL of the search results page
        max_retries: Maximum number of retry attempts
    
    Returns:
        List of article URLs found on the page
    """
    article_urls = []
    base_url = "https://www.ejustice.just.fgov.be/cgi_wet/"
    
    for attempt in range(max_retries):
        try:
            # Add headers to avoid being blocked
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(page_url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all article links with class "button button-outlined read-more"
            article_links = soup.find_all('a', class_='button button-outlined read-more')
            
            for link in article_links:
                href = link.get('href')
                if href and 'article.pl' in href:
                    # Convert relative URL to absolute URL
                    full_url = urljoin(base_url, href)
                    article_urls.append(full_url)
            
            # If we found URLs or the page explicitly has no results, return
            if article_urls or "Aucun résultat trouvé" in response.text or "Geen resultaten gevonden" in response.text:
                return article_urls
                
        except requests.exceptions.RequestException as e:
            print(f"  Attempt {attempt + 1} failed for {page_url}: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retrying
            else:
                print(f"  Failed to scrape {page_url} after {max_retries} attempts")
    
    return article_urls


def scrape_urls_for_date_range(start_date, end_date, max_pages_per_day=100):
    """
    Scrape Justel article URLs for a date range
    
    Args:
        start_date: datetime object for start date
        end_date: datetime object for end date
        max_pages_per_day: Maximum number of pages to check per day (default 100)
    
    Returns:
        List of article URLs
    """
    all_article_urls = []
    
    # Format dates for URL
    start_str = start_date.strftime('%Y-%m-%d')
    end_str = end_date.strftime('%Y-%m-%d')
    
    print(f"  Scraping pages for date range {start_str} to {end_str}...")
    
    # Check pages until we find an empty one
    for page in range(1, max_pages_per_day + 1):
        page_url = (
            f"https://www.ejustice.just.fgov.be/cgi_wet/list.pl?"
            f"language=fr&sum_date=&page={page}&trier=promulgation&"
            f"pdd={start_str}&pdf={end_str}&fr=F&choix1=et&choix2=et"
        )
        
        # Scrape this page
        article_urls = scrape_article_urls_from_page(page_url)
        
        if article_urls:
            all_article_urls.extend(article_urls)
            print(f"    Page {page}: Found {len(article_urls)} articles")
        else:
            # Stop immediately on first empty page
            print(f"    Page {page}: No results - stopping")
            break
        
        # Show progress every 10 pages
        if page % 10 == 0:
            print(f"    Progress: {page}/{max_pages_per_day} pages checked, {len(all_article_urls)} articles found so far")
        
        # Small delay to be respectful to the server
        time.sleep(0.3)
    
    return all_article_urls


def main():
    # Path to the CSV file (changed from Excel for better performance)
    csv_path = './data/csv_data/full-list.csv'
    excel_path = './data/csv_data/full-list.xlsx'
    
    # Check if CSV exists, if not try to convert from Excel
    if not os.path.exists(csv_path):
        if os.path.exists(excel_path):
            print(f"Converting Excel to CSV for better performance...")
            df = pd.read_excel(excel_path)
            df.to_csv(csv_path, index=False)
            print(f"Converted to CSV: {csv_path}")
        else:
            print(f"Error: Neither {csv_path} nor {excel_path} found")
            return
    
    # Read just the last line from CSV (now that it's sorted!)
    print(f"Reading last row from {csv_path} (sorted file)...")
    
    with open(csv_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        row_count = len(lines) - 1  # Subtract header
        if row_count > 0:
            last_line = lines[-1].strip()
            # Parse CSV line (assuming URL is first column)
            last_url = last_line.split(',')[0].strip('"')
        else:
            last_url = None
    
    print(f"Found {row_count} existing URLs")
    
    # Get the last URL and extract date
    if last_url:
        print(f"\nLast URL in file:")
        print(f"{last_url[:100]}...")
        
        last_date = extract_date_from_url(last_url)
        
        if last_date:
            print(f"Extracted date from last URL: {last_date.strftime('%Y-%m-%d')}")
        else:
            print("Could not extract date from last URL")
            print("Please specify a start date manually")
            return
    else:
        print("No existing URLs found. Please specify a start date manually")
        return
    
    # Calculate next day after last date
    start_date = last_date + timedelta(days=1)
    
    # Use today as end date
    end_date = datetime.now()
    
    print(f"\nScraping article URLs from {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    # Scrape article URLs for the entire date range at once (much more efficient!)
    print(f"\nProcessing entire date range in one request...")
    all_new_urls = scrape_urls_for_date_range(start_date, end_date, max_pages_per_day=100)
    
    print(f"\nTotal new article URLs scraped: {len(all_new_urls)}")
    
    if len(all_new_urls) > 0:
        # Remove duplicates if any
        all_new_urls = list(set(all_new_urls))
        print(f"Unique new URLs after removing duplicates: {len(all_new_urls)}")
        
        # Sort the new URLs by date before appending
        print(f"Sorting {len(all_new_urls)} new URLs by date...")
        def get_sort_date(url):
            date = extract_date_from_url(url)
            return date if date else datetime.min
        
        all_new_urls.sort(key=get_sort_date)
        
        # Append sorted new URLs to the CSV (which is already sorted)
        print(f"Appending {len(all_new_urls)} sorted URLs to {csv_path}...")
        
        # Check if file ends with newline, if not add one
        with open(csv_path, 'rb') as f:
            f.seek(-1, 2)  # Go to last byte
            last_char = f.read(1)
            needs_newline = last_char != b'\n'
        
        with open(csv_path, 'a', encoding='utf-8') as f:
            # Add newline if the file doesn't end with one
            if needs_newline:
                f.write('\n')
            for url in all_new_urls:
                f.write(f'{url}\n')
        
        new_total = row_count + len(all_new_urls)
        print(f"Successfully saved {new_total} total URLs")
        
        # Show summary
        print(f"\nSummary:")
        print(f"- Previous total: {row_count} URLs")
        print(f"- Added: {len(all_new_urls)} new article URLs")
        print(f"- New total: {new_total} URLs")
        print(f"- Date range covered: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    else:
        print("No new article URLs to add")


if __name__ == "__main__":
    main()