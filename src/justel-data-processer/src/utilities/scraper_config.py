"""
Configuration file for JUSTEL Web Scraper

Modify these settings to customize the scraper behavior.
"""

# File paths
INPUT_CSV = "excel/input.csv"
OUTPUT_DIR = "input_html"
LOG_DIR = "logs"

# CSV column configuration
URL_COLUMN = "url_justel"
DOCUMENT_ID_COLUMN = "document_id"

# Scraping settings
DEFAULT_DELAY = 2.0  # Seconds between requests
REQUEST_TIMEOUT = 15  # Seconds to wait for page load
LANGUAGE_WAIT = 3     # Seconds to wait after clicking language button

# Browser settings
HEADLESS_MODE = True
BROWSER_WINDOW_SIZE = "1920,1080"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"

# Test mode settings
TEST_MODE = False
TEST_LIMIT = 10

# Language button selectors (in order of preference)
LANGUAGE_SELECTORS = [
    "a.nav__language-button.active[href*='language=fr']",
    "a[href*='language=fr']",
    "a[href*='lang=fr']",
    "a.language-fr",
    "a[title*='français']",
    "a[title*='French']"
]

# XPath selectors for language buttons containing text
LANGUAGE_TEXT_SELECTORS = [
    "//a[contains(text(), 'FR')]",
    "//a[contains(text(), 'Français')]",
    "//a[contains(text(), 'French')]"
]

# French language detection keywords
FRENCH_KEYWORDS = ['français', 'article', 'chapitre', 'titre', 'loi', 'décret']

# Regex patterns for legislation ID extraction
LEGISLATION_ID_PATTERNS = [
    r'/(\d{10})/',      # ID in middle of path
    r'/(\d{10})$',      # ID at end of path
    r'=(\d{10})$',      # ID as parameter value
    r'numac=(\d{10})'   # ID in numac parameter
]

# File naming
HTML_FILE_EXTENSION = ".html"
LOG_FILE_PREFIX = "justel_scraper_"
LOG_FILE_EXTENSION = ".log"

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 5  # Seconds between retries

# Chrome options
CHROME_OPTIONS = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu",
    "--disable-extensions",
    "--disable-plugins",
    "--disable-images",  # Faster loading
    "--disable-javascript",  # May need to be removed if JS is required
]

# Logging configuration
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR, CRITICAL
