#!/usr/bin/env python3
"""
hardcoded_jsons.py - Hardcoded JSON structures for edge case documents

These documents have complex structural problems that are difficult to fix
programmatically, so we use pre-processed correct JSON instead.

Documents included:
- 2020030910: Has duplicate CHAPITRE V nodes
- 1999036088: Has duplicate article numbers

To update these JSONs:
1. Load the existing JSON from output/24/
2. Manually fix the structural issues
3. Paste the corrected JSON in the appropriate function below
"""

def get_json_2020030910():
    """
    Return corrected JSON for document 2020030910.
    This document has duplicate CHAPITRE V nodes that need to be merged.
    """
    # PASTE THE COMPLETE CORRECTED JSON HERE
    # You can load output/24/2020030910.json, fix the duplicate CHAPITRE V issue,
    # and paste the entire corrected structure here
    return {
        "document_metadata": {
            "document_number": "2020030910",
            "title": "27 AVRIL 2020. - Décret contenant le règlement définitif du budget de la Communauté française pour l'année budgétaire 2009",
            "publication_date": "2020-06-03",
            "source": "Communauté française",
            "page_number": 38714,
            "dossier_number": "2020-04-27/22",
            "effective_date": "2020-06-13",
            "end_validity_date": "",
            "language": "fr",
            "document_type": "DECRET",
            "status": "active",
            "version_info": {
            "archived_versions_count": 0,
            "archived_versions_url": "",
            "execution_orders_count": 0,
            "execution_orders_url": ""
            },
            "official_justel_url": "https://www.ejustice.just.fgov.be/eli/decret/2020/04/27/2020030910/justel",
            "official_publication_pdf_url": "https://www.ejustice.just.fgov.be/mopdf/2020/06/03_1.pdf#Page12",
            "consolidated_pdf_url": "https://www.ejustice.just.fgov.be/img_l/pdf/2020/04/27/2020030910_F.pdf"
        },
        "preamble": "Le Parlement de la Communauté française a adopté et Nous, Gouvernement, sanctionnons ce qui suit :",
        "abrogation_info": {},
        "document_hierarchy": [
            {
            "type": "section",
            "label": "PREMIERE PARTIE. SERVICES D'ADMINISTRATION GENERALE DU MINISTERE DE LA COMMUNAUTE FRANCAISE - ANNEE BUDGETAIRE 2009",
            "metadata": {
                "title_type": "PREMIERE PARTIE.",
                "title_content": "SERVICES D'ADMINISTRATION GENERALE DU MINISTERE DE LA COMMUNAUTE FRANCAISE - ANNEE BUDGETAIRE 2009",
                "rank": 3
            },
            "children": [
                {
                "type": "chapitre",
                "label": "CHAPITRE Ier. Engagements effectués en exécution du budget",
                "metadata": {
                    "title_type": "CHAPITRE Ier.",
                    "title_content": "Engagements effectués en exécution du budget",
                    "rank": 2
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 1er",
                    "metadata": {
                        "article_range": "1er",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "1er",
                        "anchor_id": "art_1er",
                        "content": {
                        "main_text_raw": "Les crédits d'engagement alloués par décrets budgétaires pour l'année budgétaire 2009, s'élèvent à 73.900.000 euros (annexe tableau 2.2.1 colonne 2) § 2 Fixation des engagements à charge des crédits dissociés",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-1er\"><header class=\"article-header\"><h2 class=\"article-number\">Article 1er</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les crédits d'engagement alloués par décrets budgétaires pour l'année budgétaire 2009, s'élèvent à 73.900.000 euros (annexe tableau 2.2.1 colonne 2) § 2 Fixation des engagements à charge des crédits dissociés</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.095393"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 2",
                    "metadata": {
                        "article_range": "2",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "2",
                        "anchor_id": "art_2",
                        "content": {
                        "main_text_raw": "Les engagements de dépenses imputés à charge de ces crédits s'élèvent à 68.846.523,37 euros (annexe tableau 2.2.1 colonne 5).",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-2\"><header class=\"article-header\"><h2 class=\"article-number\">Article 2</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les engagements de dépenses imputés à charge de ces crédits s'élèvent à 68.846.523,37 euros (annexe tableau 2.2.1 colonne 5).</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.095498"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 3",
                    "metadata": {
                        "article_range": "3",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "3",
                        "anchor_id": "art_3",
                        "content": {
                        "main_text_raw": "Les crédits d'engagement disponibles à la fin de l'année budgétaire s'élèvent à 5.053.476,63 euros (annexe tableau 2.2.1 colonne 7). Conformément aux dispositions des articles 34 et 35 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991, ce montant est annulé. (annexe tableau 2.2.1 colonne 9). § 3. Fixation des fonds budgétaires (crédits variables) d'engagement",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-3\"><header class=\"article-header\"><h2 class=\"article-number\">Article 3</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>Fixation des fonds budgétaires (crédits variables) d'engagement</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.095600"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 4",
                    "metadata": {
                        "article_range": "4",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "4",
                        "anchor_id": "art_4",
                        "content": {
                        "main_text_raw": "Les crédits variables d'engagement affectés pour les engagements de l'année budgétaire 2009 s'élèvent à 72.335.284,14 euros (annexe tableau 2.2.4 engagements colonne 3). Le solde de départ au 1er janvier 2009, augmenté des réductions de visas sur années antérieures étant de + 75.031.309,00 euros (annexe tableau 2.2.4 engagements colonne 2), le disponible en engagements à charge des crédits variables s'élève pour l'année 2009 à 147.366.593,14 euros (annexe tableau 2.2.4 engagements colonne 4). Par dérogation au § 4 de l'article 45 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991, les articles 5,15,27, 39,40,et 47 du décret du 12 décembre 2008 contenant le budget général des dépenses de la Communauté française de l'année budgétaire 2009 ont autorisé des avances de trésorerie et la situation débitrice de certains crédits variables. § 4. Fixation des engagements à charge des fonds budgétaires (crédits variables)",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-4\"><header class=\"article-header\"><h2 class=\"article-number\">Article 4</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-4\"><h3 class=\"paragraph-marker\">§ 4.</h3><div class=\"paragraph-content\"><p>Fixation des engagements à charge des fonds budgétaires (crédits variables)</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.095746"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 5",
                    "metadata": {
                        "article_range": "5",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "5",
                        "anchor_id": "art_5",
                        "content": {
                        "main_text_raw": "Les engagements de dépenses à charge des crédits variables d'engagement de l'année budgétaire 2009 s'élèvent à 70.348.674,53 euros (annexe tableau 2.2.4 engagements colonne 5)",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-5\"><header class=\"article-header\"><h2 class=\"article-number\">Article 5</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les engagements de dépenses à charge des crédits variables d'engagement de l'année budgétaire 2009 s'élèvent à 70.348.674,53 euros (annexe tableau 2.2.4 engagements colonne 5)</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.095834"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 6",
                    "metadata": {
                        "article_range": "6",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "6",
                        "anchor_id": "art_6",
                        "content": {
                        "main_text_raw": "Par suite des dispositions contenues dans les articles 4 et 5 ci-dessus, le disponible en engagement - crédits variables s'élève à la fin de l'année budgétaire 2009 à 77.017.918,61 euros (annexe tableau 2.2.4 engagements colonne 6). Ce solde sera reporté à l'année budgétaire suivante.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-6\"><header class=\"article-header\"><h2 class=\"article-number\">Article 6</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Par suite des dispositions contenues dans les articles 4 et 5 ci-dessus, le disponible en engagement - crédits variables s'élève à la fin de l'année budgétaire 2009 à 77.017.918,61 euros (annexe tableau 2.2.4 engagements colonne 6). Ce solde sera reporté à l'année budgétaire suivante.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.095938"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "chapitre",
                "label": "CHAPITRE II. Recettes et dépenses effectuées en exécution du budget",
                "metadata": {
                    "title_type": "CHAPITRE II.",
                    "title_content": "Recettes et dépenses effectuées en exécution du budget",
                    "rank": 2
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 7",
                    "metadata": {
                        "article_range": "7",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "7",
                        "anchor_id": "art_7",
                        "content": {
                        "main_text_raw": "Les prévisions de recettes en faveur de la Communauté française s'élèvent pour l'année budgétaire 2009 à la somme de 7.992.881.000 euros (annexe tableau 2.2.2 colonne 2) Ce montant se décompose de la manière suivante (en euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- recettes fiscales et générales courantes : <td valign=\"top\">7.992.806.000 <tr><td valign=\"top\">- recettes fiscales et générales en capital : <td valign=\"top\">75.000</td></td></tr></td></td></tr></table>",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-7\"><header class=\"article-header\"><h2 class=\"article-number\">Article 7</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les prévisions de recettes en faveur de la Communauté française s'élèvent pour l'année budgétaire 2009 à la somme de 7.992.881.000 euros (annexe tableau 2.2.2 colonne 2) Ce montant se décompose de la manière suivante (en euros)</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- recettes fiscales et générales courantes : <td valign=\"top\">7.992.806.000 <tr><td valign=\"top\">- recettes fiscales et générales en capital : <td valign=\"top\">75.000</td></td></tr></td></td></tr></table></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096102"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 8",
                    "metadata": {
                        "article_range": "8",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "8",
                        "anchor_id": "art_8",
                        "content": {
                        "main_text_raw": "Les recettes budgétaires de l'année 2009 s'élèvent à 7.997.088.491,20 euros (annexe tableau 2.2.2 colonne 4). Ce montant se décompose de la manière suivante: (en euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- recettes fiscales et générales courantes : <td valign=\"top\">7.997.012.072,62 <tr><td valign=\"top\">- recettes fiscales et générales en capital : <td valign=\"top\">76.418,58</td></td></tr></td></td></tr></table>",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-8\"><header class=\"article-header\"><h2 class=\"article-number\">Article 8</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les recettes budgétaires de l'année 2009 s'élèvent à 7.997.088.491,20 euros (annexe tableau 2.2.2 colonne 4). Ce montant se décompose de la manière suivante: (en euros)</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- recettes fiscales et générales courantes : <td valign=\"top\">7.997.012.072,62 <tr><td valign=\"top\">- recettes fiscales et générales en capital : <td valign=\"top\">76.418,58</td></td></tr></td></td></tr></table></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096274"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 9",
                    "metadata": {
                        "article_range": "9",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "9",
                        "anchor_id": "art_9",
                        "content": {
                        "main_text_raw": "Les droits constatés à recouvrer à la clôture de l'année budgétaire s'élèvent à 0 euros (annexe tableau 2.2.2 colonne 5) Ce montant se décompose de la manière suivante a. droits annulés ou portés en surséance indéfinie (annexe tableau 2.2.2 colonne 6) (en euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- recettes fiscales et générales courantes : <td valign=\"top\"> <tr><td valign=\"top\">- recettes fiscales et générales en capital <td valign=\"top\"> </td></td></tr></td></td></tr></table> b. droits reportés à l'année budgétaire 2010 (annexe tableau 2.2.2 colonne 7) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- recettes fiscales et générales courantes : <td valign=\"top\"> <tr><td valign=\"top\">- recettes fiscales et générales en capital <td valign=\"top\"> </td></td></tr></td></td></tr></table> § 2. Fixation des crédits de dépenses",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-9\"><header class=\"article-header\"><h2 class=\"article-number\">Article 9</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>Fixation des crédits de dépenses</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096381"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 10",
                    "metadata": {
                        "article_range": "10",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "10",
                        "anchor_id": "art_10",
                        "content": {
                        "main_text_raw": "Les décrets budgétaires concernant l'année budgétaire 2009 ont accordé 8.354.668.000 euros pour l'ordonnancement des dépenses et les ont répartis de la manière suivante: (annexe tableau 2.2.3 colonne 2). (en euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">59.069.000 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">8.295.599.000</td></td></tr></td></td></tr></table>",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-10\"><header class=\"article-header\"><h2 class=\"article-number\">Article 10</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les décrets budgétaires concernant l'année budgétaire 2009 ont accordé 8.354.668.000 euros pour l'ordonnancement des dépenses et les ont répartis de la manière suivante: (annexe tableau 2.2.3 colonne 2). (en euros)</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">59.069.000 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">8.295.599.000</td></td></tr></td></td></tr></table></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096504"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 11",
                    "metadata": {
                        "article_range": "11",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "11",
                        "anchor_id": "art_11",
                        "content": {
                        "main_text_raw": "Les autorisations de dépenses résultant de l'article 10 sont augmentées des crédits reportés de l'année budgétaire précédente pour un montant de 207.844.702,67 euros en vertu des articles 34 et 35 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991 se décomposant comme suit (annexe tableau 2.2.4 colonne 3): <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\"> <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">207.844.702,67</td></td></tr></td></td></tr></table>",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-11\"><header class=\"article-header\"><h2 class=\"article-number\">Article 11</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les autorisations de dépenses résultant de l'article 10 sont augmentées des crédits reportés de l'année budgétaire précédente pour un montant de 207.844.702,67 euros en vertu des articles 34 et 35 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991 se décomposant comme suit (annexe tableau 2.2.4 colonne 3):</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\"> <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">207.844.702,67</td></td></tr></td></td></tr></table></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096638"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 12",
                    "metadata": {
                        "article_range": "12",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "12",
                        "anchor_id": "art_12",
                        "content": {
                        "main_text_raw": "- En vertu des articles 10 et 11 qui précèdent, le total des autorisations de dépenses allouées disponibles pour l'année budgétaire 2009 s'élève à 8.562.512.702,67 euros (annexe tableau 2.2.3, colonne 4). Ces autorisations de dépenses se répartissent comme suit: (en euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">59.069.000 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">8.503.443.702,67</td></td></tr></td></td></tr></table> § 3. Fixation de la situation des dépenses",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-12\"><header class=\"article-header\"><h2 class=\"article-number\">Article 12</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>Fixation de la situation des dépenses</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096736"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 13",
                    "metadata": {
                        "article_range": "13",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "13",
                        "anchor_id": "art_13",
                        "content": {
                        "main_text_raw": "Les dépenses imputées à charge de l'année budgétaire 2009 se montent à 8.280.733.265,80 euros (annexe tableau 2.2.3, colonnes 5,6 et 7), se répartissant entre: <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\"> <td valign=\"top\">Prestations d'années antérieures <td valign=\"top\">Prestations d'années courantes <td valign=\"top\">Dépenses totales <tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">16.768.449,93 <td valign=\"top\">38.177.959,55 <td valign=\"top\">54.946.409,48 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">122.752.211,57 <td valign=\"top\">8.103.034.644,75 <td valign=\"top\">8.225.786.856,32 <tr><td valign=\"top\">total <td valign=\"top\">139.520.661,50 <td valign=\"top\">8.141.212.604,30 <td valign=\"top\">8.280.733.265,80</td></td></td></td></tr></td></td></td></td></tr></td></td></td></td></tr></td></td></td></td></tr></table>",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-13\"><header class=\"article-header\"><h2 class=\"article-number\">Article 13</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les dépenses imputées à charge de l'année budgétaire 2009 se montent à 8.280.733.265,80 euros (annexe tableau 2.2.3, colonnes 5,6 et 7), se répartissant entre:</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\"> <td valign=\"top\">Prestations d'années antérieures <td valign=\"top\">Prestations d'années courantes <td valign=\"top\">Dépenses totales <tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">16.768.449,93 <td valign=\"top\">38.177.959,55 <td valign=\"top\">54.946.409,48 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">122.752.211,57 <td valign=\"top\">8.103.034.644,75 <td valign=\"top\">8.225.786.856,32 <tr><td valign=\"top\">total <td valign=\"top\">139.520.661,50 <td valign=\"top\">8.141.212.604,30 <td valign=\"top\">8.280.733.265,80</td></td></td></td></tr></td></td></td></td></tr></td></td></td></td></tr></td></td></td></td></tr></table></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096849"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 14",
                    "metadata": {
                        "article_range": "14",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "14",
                        "anchor_id": "art_14",
                        "content": {
                        "main_text_raw": "De ce montant, il a été justifié à la Cour des Comptes un montant de 8.280.733.265,80 euros dont: <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">54.946.409,48 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">8.225.786.856,32</td></td></tr></td></td></tr></table> (annexe tableau 2.2.3, colonne 8)",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-14\"><header class=\"article-header\"><h2 class=\"article-number\">Article 14</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>De ce montant, il a été justifié à la Cour des Comptes un montant de 8.280.733.265,80 euros dont:</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">54.946.409,48 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">8.225.786.856,32</td></td></tr></td></td></tr></table></div><p>(annexe tableau 2.2.3, colonne 8)</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.096962"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 15",
                    "metadata": {
                        "article_range": "15",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "15",
                        "anchor_id": "art_15",
                        "content": {
                        "main_text_raw": "Il résulte de la comparison des articles 13 et 14 qu'il n'y a aucune dépense à régulariser en application de l'article 79 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991 (annexe tableau 2.2.3, colonne 9). § 4. Règlement des crédits",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-15\"><header class=\"article-header\"><h2 class=\"article-number\">Article 15</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-4\"><h3 class=\"paragraph-marker\">§ 4.</h3><div class=\"paragraph-content\"><p>Règlement des crédits</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097046"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 16",
                    "metadata": {
                        "article_range": "16",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "16",
                        "anchor_id": "art_16",
                        "content": {
                        "main_text_raw": "La comparaison entre les autorisations de dépenses (article 12) et les opérations imputées (article 13) fait ressortir une différence pour l'année budgétaire 2009 de 281.779.436,87 euros se répartissant comme suit: <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">4.122.590,52 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">277.656.846,35</td></td></tr></td></td></tr></table>",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-16\"><header class=\"article-header\"><h2 class=\"article-number\">Article 16</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>La comparaison entre les autorisations de dépenses (article 12) et les opérations imputées (article 13) fait ressortir une différence pour l'année budgétaire 2009 de 281.779.436,87 euros se répartissant comme suit:</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">4.122.590,52 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">277.656.846,35</td></td></tr></td></td></tr></table></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097162"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 17",
                    "metadata": {
                        "article_range": "17",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "17",
                        "anchor_id": "art_17",
                        "content": {
                        "main_text_raw": "Pour couvrir les dépenses de l'année budgétaire 2009 effectuées au-delà ou en l'absence de crédits, il est accordé des crédits complémentaires s'élevant à 54.648.483,46 euros dont: <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">0 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">54.648.483,46</td></td></tr></td></td></tr></table> Ces crédits sont répartis ainsi que mentionné à l'annexe tableau 2.2.6, colonne 2.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-17\"><header class=\"article-header\"><h2 class=\"article-number\">Article 17</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Pour couvrir les dépenses de l'année budgétaire 2009 effectuées au-delà ou en l'absence de crédits, il est accordé des crédits complémentaires s'élevant à 54.648.483,46 euros dont:</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">0 <tr><td valign=\"top\">Crédits non dissociés <td valign=\"top\">54.648.483,46</td></td></tr></td></td></tr></table></div><p>Ces crédits sont répartis ainsi que mentionné à l'annexe tableau 2.2.6, colonne 2.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097290"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 18",
                    "metadata": {
                        "article_range": "18",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "18",
                        "anchor_id": "art_18",
                        "content": {
                        "main_text_raw": "Par suite des dispositions contenues dans les articles 16 et 17, le montant des crédits disponibles au 31 décembre 2009 comprend: (annexe tableau 2.2.3, colonnes 11 et 12). (En euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\"> <td valign=\"top\">Crédits d'ordonnancement <td valign=\"top\">Crédits non dissociés <td valign=\"top\">total <tr><td valign=\"top\">Crédits à annuler <td valign=\"top\">4.122.590,52 <td valign=\"top\">86.433.373,89 <td valign=\"top\">90.555.964,41 <tr><td valign=\"top\">Crédits à reporter à l'année budgétaire suivante <td valign=\"top\"> <td valign=\"top\">245.871.955,92 <td valign=\"top\">245.871.955,92</td></td></td></td></tr></td></td></td></td></tr></td></td></td></td></tr></table> § 5. Résultat général des recettes et des dépenses du budget 2009",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-18\"><header class=\"article-header\"><h2 class=\"article-number\">Article 18</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-5\"><h3 class=\"paragraph-marker\">§ 5.</h3><div class=\"paragraph-content\"><p>Résultat général des recettes et des dépenses du budget 2009</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097383"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 19",
                    "metadata": {
                        "article_range": "19",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "19",
                        "anchor_id": "art_19",
                        "content": {
                        "main_text_raw": "Le résultat général du budget de l'année budgétaire 2009 se présente comme suit: Les recettes s'élèvent à 7.997.088.491,20 euros Les dépenses s'élèvent à 8.280.733.265,80 euros En conclusion, compte non tenu des crédits variables et de la section particulière, les dépenses excèdent les recettes de 283.644.744,60 euros",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-19\"><header class=\"article-header\"><h2 class=\"article-number\">Article 19</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le résultat général du budget de l'année budgétaire 2009 se présente comme suit: Les recettes s'élèvent à 7.997.088.491,20 euros Les dépenses s'élèvent à 8.280.733.265,80 euros En conclusion, compte non tenu des crédits variables et de la section particulière, les dépenses excèdent les recettes de 283.644.744,60 euros</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.097491"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "chapitre",
                "label": "CHAPITRE III. Recettes et dépenses relatives aux fonds budgétaires (crédits variables)",
                "metadata": {
                    "title_type": "CHAPITRE III.",
                    "title_content": "Recettes et dépenses relatives aux fonds budgétaires (crédits variables)",
                    "rank": 2
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 20",
                    "metadata": {
                        "article_range": "20",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "20",
                        "anchor_id": "art_20",
                        "content": {
                        "main_text_raw": "Les recettes imputées de cette nature s'élèvent pour l'année budgétaire 2009 à 72.335.284,14 euros (annexe tableau 2.2.2 recettes affectées colonne 4) dont <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">Recettes courantes <td valign=\"top\">72.062.244,72 <tr><td valign=\"top\">Recettes en capital <td valign=\"top\">273.039,42</td></td></tr></td></td></tr></table> § 2. Fixation des fonds budgétaires (crédits variables) d'ordonnancement",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-20\"><header class=\"article-header\"><h2 class=\"article-number\">Article 20</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>Fixation des fonds budgétaires (crédits variables) d'ordonnancement</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097576"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 21",
                    "metadata": {
                        "article_range": "21",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "21",
                        "anchor_id": "art_21",
                        "content": {
                        "main_text_raw": "Les crédits variables d'ordonnancement affectés pour les ordonnancements de l'année budgétaire 2009 s'élèvent à 72.335.284,14 (annexe tableau 2.2.4 ordonnancements colonne 3) Le solde de départ au 1 janvier 2009 étant de 81.866.595,05 euros le disponible en ordonnancement sur les crédits variables s'élève à 154.201.879,19 euros (annexe tableau 2.2.4 ordonnancement colonne 4). Par dérogation au § 4 de l'article 45 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991, les articles 5,15,27, 39,40,et 47 du décret du 12 décembre 2008 contenant le budget général des dépenses de la Communauté française de l'année budgétaire 2009 ont autorisé des avances de trésorerie et la situation débitrice de certains crédits variables § 3. Fixation des dépenses à charge des crédits variables",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-21\"><header class=\"article-header\"><h2 class=\"article-number\">Article 21</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>Fixation des dépenses à charge des crédits variables</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097700"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 22",
                    "metadata": {
                        "article_range": "22",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "22",
                        "anchor_id": "art_22",
                        "content": {
                        "main_text_raw": "Les ordonnancements imputés à charge des crédits variables d'ordonnancement de l'année budgétaire 2009 s'élèvent à 64.382.745,50 euros (annexe tableau 2.2.4 ordonnancements colonne 5).",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-22\"><header class=\"article-header\"><h2 class=\"article-number\">Article 22</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les ordonnancements imputés à charge des crédits variables d'ordonnancement de l'année budgétaire 2009 s'élèvent à 64.382.745,50 euros (annexe tableau 2.2.4 ordonnancements colonne 5).</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097782"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 23",
                    "metadata": {
                        "article_range": "23",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "23",
                        "anchor_id": "art_23",
                        "content": {
                        "main_text_raw": "Par suite des dispositions contenues dans les articles 21 et 22 ci-dessus, le disponible en ordonnancements - crédits variables s'élève à la fin de l'année budgétaire 2009 à 89.819.133,69 euros (annexe tableau 2.2.4 ordonnancements colonne 6). Ce solde sera reporté à l'année budgétaire suivante.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-23\"><header class=\"article-header\"><h2 class=\"article-number\">Article 23</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Par suite des dispositions contenues dans les articles 21 et 22 ci-dessus, le disponible en ordonnancements - crédits variables s'élève à la fin de l'année budgétaire 2009 à 89.819.133,69 euros (annexe tableau 2.2.4 ordonnancements colonne 6). Ce solde sera reporté à l'année budgétaire suivante.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.097878"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "chapitre",
                "label": "CHAPITRE IV. Recettes et dépenses effectuées en exécution de la section particulière du budget",
                "metadata": {
                    "title_type": "CHAPITRE IV.",
                    "title_content": "Recettes et dépenses effectuées en exécution de la section particulière du budget",
                    "rank": 2
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 24",
                    "metadata": {
                        "article_range": "24",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "24",
                        "anchor_id": "art_24",
                        "content": {
                        "main_text_raw": "Les décrets budgétaires de l'année 2009 ont évalué les recettes et dépenses pour la section particulière du budget de la Communauté française ainsi qu'il suit: (en euros) <table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- Recettes <td valign=\"top\">0 <tr><td valign=\"top\">- Dépenses <td valign=\"top\">0</td></td></tr></td></td></tr></table> (annexe tableau 2.2.5 colonnes 2,3).",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-24\"><header class=\"article-header\"><h2 class=\"article-number\">Article 24</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les décrets budgétaires de l'année 2009 ont évalué les recettes et dépenses pour la section particulière du budget de la Communauté française ainsi qu'il suit: (en euros)</p><div class=\"missing-table-placeholder\"><table border=\"1\" class=\"legal-table\"><tr><td valign=\"top\">- Recettes <td valign=\"top\">0 <tr><td valign=\"top\">- Dépenses <td valign=\"top\">0</td></td></tr></td></td></tr></table></div><p>(annexe tableau 2.2.5 colonnes 2,3).</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.098000"
                        },
                        "has_preserved_tables": True
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 25",
                    "metadata": {
                        "article_range": "25",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "25",
                        "anchor_id": "art_25",
                        "content": {
                        "main_text_raw": "Le solde disponible au 1er janvier 2009 s'élevait à - 2.923.724,08 euros (annexe tableau 2.2.5 colonne 8) Aucune recette n'a été encaissée (annexe tableau 2.2.5, colonne 4)",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-25\"><header class=\"article-header\"><h2 class=\"article-number\">Article 25</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le solde disponible au 1er janvier 2009 s'élevait à - 2.923.724,08 euros (annexe tableau 2.2.5 colonne 8) Aucune recette n'a été encaissée (annexe tableau 2.2.5, colonne 4)</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.098081"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 26",
                    "metadata": {
                        "article_range": "26",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "26",
                        "anchor_id": "art_26",
                        "content": {
                        "main_text_raw": "Aucune dépense n'a été imputée (annexe tableau 2.2.5, colonne 5). Il n'existe donc aucune dépense restant à régulariser pour lesquelles il est fait application de l'article 79 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991 (annexe tableau 2.2.5, colonne 6).",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-26\"><header class=\"article-header\"><h2 class=\"article-number\">Article 26</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Aucune dépense n'a été imputée (annexe tableau 2.2.5, colonne 5). Il n'existe donc aucune dépense restant à régulariser pour lesquelles il est fait application de l'article 79 des lois sur la comptabilité de l'Etat coordonnées le 17 juillet 1991 (annexe tableau 2.2.5, colonne 6).</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.098177"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 27",
                    "metadata": {
                        "article_range": "27",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "27",
                        "anchor_id": "art_27",
                        "content": {
                        "main_text_raw": "La différence entre les recettes perçues et les dépenses imputées dans l'année budgétaire s'élève à 0 euros (annexe tableau 2.2.5, colonne 7). Compte tenu du total disponible pour les dépenses de l'année budgétaire 2009, tel que déterminé à l'article 25 et des dépenses reprises à l'article 26, le solde disponible au 31 décembre 2009 à la section particulière du budget de la Communauté française s'établit à - 2.923.724,08 euros (annexe tableau 2.2.5 colonne 10). Il sera reporté à l'année budgétaire suivante.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-27\"><header class=\"article-header\"><h2 class=\"article-number\">Article 27</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>La différence entre les recettes perçues et les dépenses imputées dans l'année budgétaire s'élève à 0 euros (annexe tableau 2.2.5, colonne 7). Compte tenu du total disponible pour les dépenses de l'année budgétaire 2009, tel que déterminé à l'article 25 et des dépenses reprises à l'article 26, le solde disponible au 31 décembre 2009 à la section particulière du budget de la Communauté française s'établit à - 2.923.724,08 euros (annexe tableau 2.2.5 colonne 10). Il sera reporté à l'année budgétaire suivante.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.098296"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "chapitre",
                "label": "CHAPITRE V. Résultat global",
                "metadata": {
                    "title_type": "CHAPITRE V.",
                    "title_content": "Résultat global",
                    "rank": 2
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 28",
                    "metadata": {
                        "article_range": "28",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "28",
                        "anchor_id": "art_28",
                        "content": {
                        "main_text_raw": "Tous services réunis, budget, crédits variables et section particulière, compte tenu des articles 19, 21, 22 et 27 du présent décret, le résultat global du budget 2009 se présente comme suit (en euros): Budget sensu stricto: - 283.644.774,60 crédits variables: + 7.952.538,64 section particulière: 0 Total: - 275.692.235,96",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-28\"><header class=\"article-header\"><h2 class=\"article-number\">Article 28</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Tous services réunis, budget, crédits variables et section particulière, compte tenu des articles 19, 21, 22 et 27 du présent décret, le résultat global du budget 2009 se présente comme suit (en euros): Budget sensu stricto:</p><ul class=\"hyphenated-items\"><li class=\"hyphenated-item\"><span class=\"item-text\">283.644.774,60 crédits variables: + 7.952.538,64 section particulière: 0 Total:</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">275.692.235,96</span></li></ul></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.098482"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                }
            ]
            },
            {
            "type": "section",
            "label": "DEUXIEME PARTIE. - OPERATIONS EFFECTUEES EN EXECUTION DES BUDGETS DES SERVICES A GESTION SEPAREE DE LA COMMUNAUTE FRANCAISE",
            "metadata": {
                "title_type": "DEUXIEME PARTIE.",
                "title_content": "- OPERATIONS EFFECTUEES EN EXECUTION DES BUDGETS DES SERVICES A GESTION SEPAREE DE LA COMMUNAUTE FRANCAISE",
                "rank": 3
            },
            "children": [
                {
                "type": "chapitre",
                "label": "CHAPITRE I. Recettes et dépenses effectuées en exécution des budgets des services à gestion séparée du ministère de la Communauté française",
                "metadata": {
                    "title_type": "CHAPITRE I.",
                    "title_content": "Recettes et dépenses effectuées en exécution des budgets des services à gestion séparée du ministère de la Communauté française",
                    "rank": 2
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 29",
                    "metadata": {
                        "article_range": "29",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "29",
                        "anchor_id": "art_29",
                        "content": {
                        "main_text_raw": "Les prévisions de recettes annuelles s'élèvent à 436.513.402,26 euros (annexe tableau 2.3 colonne 2) Les recettes pour l'année budgétaire 2009 s'élèvent à 517.206.707,40 euros. Le solde disponible au 1er janvier de l'année s'élève à 305.135.167,15 euros. Les recettes de l'année et le disponible au 1er janvier constituent un disponible pour les dépenses de l'année 2009 de 822.341.874,55 euros. § 2. fixation des dépenses",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-29\"><header class=\"article-header\"><h2 class=\"article-number\">Article 29</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>fixation des dépenses</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.098593"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 30",
                    "metadata": {
                        "article_range": "30",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "30",
                        "anchor_id": "art_30",
                        "content": {
                        "main_text_raw": "Les prévisions de dépenses s'élèvent à 416.102.538,06 euros (annexe tableau 2.3 colonne 3). Les dépenses sont fixées à la somme de 461.075.753,24 euros (annexe tableau 2.3 colonne 5). § 3. résultat budgétaire",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-30\"><header class=\"article-header\"><h2 class=\"article-number\">Article 30</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>résultat budgétaire</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 1,
                            "provision_count": 0,
                            "has_tables": True,
                            "generation_timestamp": "2025-08-19T14:05:18.098675"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 31",
                    "metadata": {
                        "article_range": "31",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "31",
                        "anchor_id": "art_31",
                        "content": {
                        "main_text_raw": "Par suite des articles 29 et 30, le résultat budgétaire de l'année est fixé au montant de 56.130.954,46 euros. Le disponible au 31 décembre 2009 est fixé au montant de 361.266.121,31 euros; Il sera reporté à l'exercice budgétaire suivant.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-31\"><header class=\"article-header\"><h2 class=\"article-number\">Article 31</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Par suite des articles 29 et 30, le résultat budgétaire de l'année est fixé au montant de 56.130.954,46 euros. Le disponible au 31 décembre 2009 est fixé au montant de 361.266.121,31 euros; Il sera reporté à l'exercice budgétaire suivant.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.098767"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "TROISIEME PARTIE. ORGANISMES D'INTERET PUBLIC DE LA CATEGORIE A",
                "metadata": {
                    "title_type": "TROISIEME PARTIE.",
                    "title_content": "ORGANISMES D'INTERET PUBLIC DE LA CATEGORIE A",
                    "rank": 3
                },
                "children": []
                }
            ]
            },
            {
            "type": "annexe",
            "label": "ANNEXE.",
            "metadata": {
                "title_type": "ANNEXE.",
                "title_content": "",
                "rank": 1
            },
            "children": [
                {
                "type": "article",
                "label": "Article N",
                "metadata": {
                    "article_range": "N",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "N",
                    "anchor_id": "art_N",
                    "content": {
                    "main_text_raw": "(Image non reprise pour des raisons techniques, voir M.B. du 03-06-2020, p. 38719)",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-N\"><header class=\"article-header\"><h2 class=\"article-number\">Article N</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>(Image non reprise pour des raisons techniques, voir M.B. du 03-06-2020, p. 38719)</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.098843"
                    }
                    }
                },
                "footnotes": [],
                "footnote_references": []
                }
            ]
            }
        ],
        "references": {
            "modifies": [],
            "modified_by": []
        },
        "external_links": {
            "official_links": [],
            "parliamentary_work": []
        },
        "extraction_metadata": {
            "extraction_date": "2025-08-19T14:05:18.099152",
            "source_file": "2020030910.md",
            "sections_included": [
            "document_metadata",
            "document_hierarchy",
            "references"
            ],
            "sections_excluded": [
            "articles",
            "legal_references",
            "modification_history"
            ],
            "completeness_flags": {
            "all_articles_extracted": True,
            "footnotes_linked": True,
            "hierarchical_structure_complete": True,
            "metadata_complete": True,
            "is_minimal_document": False,
            "preamble_extracted": True,
            "is_abrogated_document": False
            }
        }
    }


def get_json_1999036088():
    """
    Return corrected JSON for document 1999036088.
    This document has duplicate article numbers that need to be fixed.
    """
    # PASTE THE COMPLETE CORRECTED JSON HERE
    # You can load output/24/1999036088.json, fix the duplicate articles,
    # and paste the entire corrected structure here
    return {
        "document_metadata": {
            "document_number": "1999036088",
            "title": "8 JUIN 1999. - Arrêté du Gouvernement flamand établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables. (TRADUCTION). (NOTE : Consultation des versions antérieures à partir du 10-09-1999 et mise à jour au 11-09-2024)",
            "publication_date": "1999-09-10",
            "source": "Communauté flamande",
            "page_number": 33886,
            "dossier_number": "1999-06-08/76",
            "effective_date": "1999-09-20",
            "end_validity_date": "",
            "language": "fr",
            "document_type": "ARRETE",
            "status": "active",
            "version_info": {
            "archived_versions_count": 0,
            "archived_versions_url": "",
            "execution_orders_count": 0,
            "execution_orders_url": ""
            },
            "official_justel_url": "https://www.ejustice.just.fgov.be/eli/arrete/1999/06/08/1999036088/justel",
            "official_publication_pdf_url": "https://www.ejustice.just.fgov.be/mopdf/1999/09/10_1.pdf#Page51",
            "consolidated_pdf_url": "https://www.ejustice.just.fgov.be/img_l/pdf/1999/06/08/1999036088_F.pdf"
        },
        "preamble": "Le Gouvernement flamand,  \nVu le décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables, modifié par les décrets des 20 décembre 1996 et 16 mars 1999;  \nVu l'accord du Ministre flamand, chargé du Budget, donné le 1er juin 1999;  \nVu les lois sur le Conseil d'Etat, coordonnées le 12 janvier 1973, notamment l'article 3, § 1er, modifié par les lois des 4 juillet 1989 et 4 août 1996;  \nVu l'urgence;  \nConsidérant que les décrets du 20 décembre 1996 et du 16 mars 1999 ont modifié le décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables, que ces modifications nécessitent une adaptation urgente de l'arrêté du Gouvernement flamand du 6 juillet 1994 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables, plus particulièrement pour ce qui concerne les définitions et l'instauration de règles de procédure en cas de leasing;  \nConsidérant que le décret du 14 juillet 1998 portant agrément et subventionnement des associations et des structures d'aide sociale dans le secteur des soins à domicile est entré en vigueur le 1er janvier 1999; que cette entrée en vigueur a une incidence sur l'arrêté précité du Gouvernement flamand du 6 juillet 1994; que les notions \"centre de services local\", \"centre de services régional\" et \"centre de court séjour\" ont été instaurés par le décret du 14 juillet 1998, nécessitant une adaptation immédiate de l'arrêté précité du 6 juillet 1994; que, par analogie avec les structures destinées aux personnes âgées, et en vue d'une affectation politiquement justifiée des subventions d'investissement, il faut inscrire d'urgence dans la réglementation que les structures dans le cadre des soins à domicile doivent veiller à l'établissement d'un plan stratégique des soins;  \nSur la proposition du Ministre flamand, chargé des Finances, du Budget et de la Politique de la Santé;  \nAprès délibération,  \nArrête :",
        "abrogation_info": {},
        "document_hierarchy": [
            {
            "type": "chapitre",
            "label": "CHAPITRE I. Dispositions générales.",
            "metadata": {
                "title_type": "CHAPITRE I.",
                "title_content": "Dispositions générales.",
                "rank": 2
            },
            "children": [
                {
                "type": "article",
                "label": "Article 1",
                "metadata": {
                    "article_range": "1",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "1",
                    "anchor_id": "art_1",
                    "content": {
                    "main_text_raw": "Au sens du présent arrêté, il convient d'entendre par: 1° Fonds: l'agence autonomisée interne dotée de la personnalité juridique \" Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden \"; 2° administration fonctionnellement compétente: suivant le cas, le Département Soins, l'agence autonomisée interne sans personnalité juridique \" Grandir \", l'agence autonomisée interne dotée de la personnalité juridique \" Zorg en Gezondheid \" (Soin et Santé), l'agence autonomisée interne dotée de la personnalité juridique \" Grandir Régie \" ou... \" Vlaams Agentschap voor Personen met een Handicap \" (Agence flamande pour les personnes handicapées); 3° demandeur: personne morale agréée ou répondant aux conditions légales pour organiser des soins et des services dans le cadre des matières personnalisables et qui introduit une demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement; 4° investissement: coûts de construction, de travaux d'agrandissement et de transformation, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres; 5° programmation: le planning relatif aux structures sur la base de critères géographiques, démographiques ou autres. Ces critères font l'objet de réglementations par catégorie d'investissement; 6° subvention d'investissement: subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur, conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables; 7° garantie d'investissement: la garantie du remboursement des emprunts contractés en vue de la réalisation de l'investissement, pour la partie des dépenses de capital non admise au bénéfice des subventions d'investissement; 8° promesse de subvention: l'obligation contractée en vue d'accorder une subvention d'investissement à un investissement et ayant fait l'objet d'un engagement à charge du budget de l'exercice en cours; 9°... 10° financier: une société de leasing ou un établissement de crédit ayant a obtenu l'agrément visé à l'article 7 de la loi du 22 mars 1993 relative au statut et au contrôle des établissements de crédit, et les sociétés y liées au sens de l'article 11 du Code des Sociétés, ainsi que tout autre établissement de crédit qui ressortit à un autre Etat membre de l'Union européenne et qui, conformément au Titre III de la loi précitée du 22 mars 1993, peut exercer ses activités sur le territoire belge ou la Banque d'Investissement européenne; 11° Ministre: le Ministre flamand chargé de l'assistance aux personnes et le Ministre flamand chargé de la politique de la santé; 12° Décret: le décret du 23 février 1994 relatif à l'Infrastructure affectée aux matières personnalisables; 13° plan maître: esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs, y compris un plan financier en proportion de l'exploitation prévue 14° projet: l'objet de l'investissement envisagé, tel que décrit dans le plan maître, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée; 15°... 16° Plan financier: une projection appuyée de chiffres réalistes du financement de l'investissement projeté indiquant les avoirs propres, les subventions d'investissement, les emprunts, les amortissements, les recettes et les dépenses ainsi qu'une estimation des résultats d'exploitation; 17° construction neuve: une nouvelle construction à destination propre, autonome et fonctionnelle dans le cadre des matières personnalisables; une construction neuve comprend toujours un gros oeuvre; 18° extension: une construction partiellement neuve complétant une construction existante à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affectée à une destination fonctionnelle, la construction neuve s'alignant en termes fonctionnels sur la construction existante; 19° achat: l'acquisition d'un immeuble susceptible d'être affecté à une destination fonctionnelle dans le cadre des matières personnalisables; 20° transformation: toute intervention matérielle à l'exception de l'extension ainsi que des travaux d'entretien ou des travaux de remplacement indispensables à cause de l'usure, visant l'amélioration ou la rénovation d'un immeuble à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affecté à une destination fonctionnelle. 21° Hôpitaux généraux: les hôpitaux visés à l'article 2 de la loi sur les hôpitaux, coordonnée le 7 août 1987, à l'exception des hôpitaux psychiatriques et des hôpitaux disposant exclusivement de services spécialisés pour le traitement et la réadaptation fonctionnelle (indice Sp), en liaison ou non avec des services d'hospitalisation ordinaire (indice H) ou des services neuro-psychiatriques pour le traitement de patients adultes (indice T) ou des services gériatriques (indice G); 22° centre de services locaux: un centre, tel que visé à l'article 9 du Décret sur les soins résidentiels du 15 février 2019;; 23° centre de convalescence: un centre tel que visé à l'article 28 du décret sur les soins résidentiels du 15 février 2019; 24° centre de soins de jour: un centre, tel que visé à l'article 23 du Décret sur les soins résidentiels du 15 février 2019; 25° centre de court séjour de type 2: un centre, tel que visé à l'article 26, § 1er, alinéa deux, 2°, du décret sur les soins résidentiels du 15 février 2019; 26° centre de court séjour de type 3: un centre, tel que visé à l'article 26, § 1er, alinéa deux, 3°, du décret sur les soins résidentiels du 15 février 2019; 27° centre d'accueil de jour: un centre d'accueil de jour d'un service d'aide aux familles, tel que visé aux articles 13 et 14 du décret sur les soins résidentiels du 15 février 2019; 28° centre pour troubles du développement: une structure agréée conformément à l'article 4 de l'arrêté du Gouvernement flamand du 16 juin 1998 réglant l'agrément et le subventionnement des centres pour troubles du développement; 28° bis... 29° structures d'aide à la jeunesse: les structures agréées visées à l'article 2 de l'arrêté du Gouvernement flamand du 5 avril 2019 relatif aux conditions d'agrément et aux normes de subventionnement des structures d'aide à la jeunesse et les centres de confiance pour enfants maltraités, visés à l'arrêté du Gouvernement flamand du 17 novembre 2017 relatif à l'agrément et au subventionnement des centres de confiance pour enfants maltraités et de l'organisation partenaire; 30° équipement médical: tout le matériel médical et médico-technique utilisé dans les hôpitaux pour le diagnostic, le traitement ou la surveillance de patients, à l'exception du matériel médical et médico-technique non subventionnable, lié aux honoraires, que l'on utilise pour le diagnostic et le traitement. Les articles de consommation ne sont pas subventionnés; 31° services autorisés de placement familial: les services autorisés, visés à l'article 10 du décret du 29 juin 2012 portant organisation du placement familial; 32° \" plafond de construction calculé \": dix sixièmes de la subvention d'investissement arrêtée dans la promesse de subvention, calculés conformément aux montants de base visés dans les arrêtés sectoriels; 33° investisseur: un tiers qui agit en tant que maître d'ouvrage du projet et qui met le projet à disposition du demandeur. Ce tiers peut être une personne physique ou une personne morale.",
                    "numbered_provisions": [
                        {
                        "number": "1°",
                        "text": "[1 Fonds: l'agence autonomisée interne dotée de la personnalité juridique \" Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden \"",
                        "sub_items": []
                        },
                        {
                        "number": "2°",
                        "text": "[1",
                        "sub_items": []
                        },
                        {
                        "number": "3°",
                        "text": "[4 demandeur: personne morale agréée ou répondant aux conditions légales pour organiser des soins et des services dans le cadre des matières personnalisables et qui introduit une demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement",
                        "sub_items": []
                        },
                        {
                        "number": "4°",
                        "text": "[4 investissement: coûts de construction, de travaux d'agrandissement et de transformation, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres",
                        "sub_items": []
                        },
                        {
                        "number": "5°",
                        "text": "programmation: le planning relatif aux structures sur la base de critères géographiques, démographiques ou autres. Ces critères font l'objet de réglementations par catégorie d'investissement",
                        "sub_items": []
                        },
                        {
                        "number": "6°",
                        "text": "[4 subvention d'investissement: subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur, conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables",
                        "sub_items": []
                        },
                        {
                        "number": "7°",
                        "text": "garantie d'investissement: la garantie du remboursement des emprunts contractés en vue de la réalisation de l'investissement, pour la partie des dépenses de capital non admise au bénéfice des subventions d'investissement",
                        "sub_items": []
                        },
                        {
                        "number": "8°",
                        "text": "promesse de subvention: l'obligation contractée en vue d'accorder une subvention d'investissement à un investissement et ayant fait l'objet d'un engagement à charge du budget de l'exercice en cours",
                        "sub_items": []
                        },
                        {
                        "number": "9°",
                        "text": "[7...",
                        "sub_items": []
                        },
                        {
                        "number": "10°",
                        "text": "[1",
                        "sub_items": []
                        },
                        {
                        "number": "11°",
                        "text": "[1 Ministre: le Ministre flamand chargé de l'assistance aux personnes et le Ministre flamand chargé de la politique de la santé",
                        "sub_items": []
                        },
                        {
                        "number": "12°",
                        "text": "Décret: le décret du 23 février 1994 relatif à l'Infrastructure affectée aux matières personnalisables",
                        "sub_items": []
                        },
                        {
                        "number": "13°",
                        "text": "[4 plan maître: esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs, y compris un plan financier en proportion de l'exploitation prévue",
                        "sub_items": []
                        },
                        {
                        "number": "14°",
                        "text": "[4 projet: l'objet de l'investissement envisagé, tel que décrit dans le plan maître, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée",
                        "sub_items": []
                        },
                        {
                        "number": "15°",
                        "text": "[7...",
                        "sub_items": []
                        },
                        {
                        "number": "16°",
                        "text": "Plan financier: une projection appuyée de chiffres réalistes du financement de l'investissement projeté indiquant les avoirs propres, les subventions d'investissement, les emprunts, les amortissements, les recettes et les dépenses ainsi qu'une estimation des résultats d'exploitation",
                        "sub_items": []
                        },
                        {
                        "number": "17°",
                        "text": "construction neuve: une nouvelle construction à destination propre, autonome et fonctionnelle dans le cadre des matières personnalisables",
                        "sub_items": []
                        },
                        {
                        "number": "18°",
                        "text": "extension: une construction partiellement neuve complétant une construction existante à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affectée à une destination fonctionnelle, la construction neuve s'alignant en termes fonctionnels sur la construction existante",
                        "sub_items": []
                        },
                        {
                        "number": "19°",
                        "text": "achat: l'acquisition d'un immeuble susceptible d'être affecté à une destination fonctionnelle dans le cadre des matières personnalisables",
                        "sub_items": []
                        },
                        {
                        "number": "20°",
                        "text": "transformation: toute intervention matérielle à l'exception de l'extension ainsi que des travaux d'entretien ou des travaux de remplacement indispensables à cause de l'usure, visant l'amélioration ou la rénovation d'un immeuble à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affecté à une destination fonctionnelle.",
                        "sub_items": []
                        },
                        {
                        "number": "21°",
                        "text": "Hôpitaux généraux: les hôpitaux visés à l'article 2 de la loi sur les hôpitaux, coordonnée le 7 août 1987, à l'exception des hôpitaux psychiatriques et des hôpitaux disposant exclusivement de services spécialisés pour le traitement et la réadaptation fonctionnelle (indice Sp), en liaison ou non avec des services d'hospitalisation ordinaire (indice H) ou des services neuro-psychiatriques pour le traitement de patients adultes (indice T) ou des services gériatriques (indice G)",
                        "sub_items": []
                        },
                        {
                        "number": "22°",
                        "text": "[2",
                        "sub_items": []
                        },
                        {
                        "number": "23°",
                        "text": "[2",
                        "sub_items": []
                        },
                        {
                        "number": "24°",
                        "text": "[2",
                        "sub_items": []
                        },
                        {
                        "number": "25°",
                        "text": "[7",
                        "sub_items": []
                        },
                        {
                        "number": "26°",
                        "text": "[7",
                        "sub_items": []
                        },
                        {
                        "number": "27°",
                        "text": "[7",
                        "sub_items": []
                        },
                        {
                        "number": "28°",
                        "text": "[15 centre pour troubles du développement: une structure agréée conformément à l'article 4 de l'arrêté du Gouvernement flamand du 16 juin 1998 réglant l'agrément et le subventionnement des centres pour troubles du développement",
                        "sub_items": []
                        },
                        {
                        "number": "28°",
                        "text": "bis [6",
                        "sub_items": []
                        },
                        {
                        "number": "29°",
                        "text": "[15 structures d'aide à la jeunesse: les structures agréées visées à l'article 2 de l'arrêté du Gouvernement flamand du 5 avril 2019 relatif aux conditions d'agrément et aux normes de subventionnement des structures d'aide à la jeunesse",
                        "sub_items": []
                        },
                        {
                        "number": "30°",
                        "text": "[5 équipement médical: tout le matériel médical et médico-technique utilisé dans les hôpitaux pour le diagnostic, le traitement ou la surveillance de patients, à l'exception du matériel médical et médico-technique non subventionnable, lié aux honoraires, que l'on utilise pour le diagnostic et le traitement. Les articles de consommation ne sont pas subventionnés",
                        "sub_items": []
                        },
                        {
                        "number": "31°",
                        "text": "services autorisés de placement familial: les services autorisés, visés à l'article 10 du décret du 29 juin 2012 portant organisation du placement familial",
                        "sub_items": []
                        },
                        {
                        "number": "32°",
                        "text": "\" plafond de construction calculé \": dix sixièmes de la subvention d'investissement arrêtée dans la promesse de subvention, calculés conformément aux montants de base visés dans les arrêtés sectoriels",
                        "sub_items": []
                        },
                        {
                        "number": "33°",
                        "text": "investisseur: un tiers qui agit en tant que maître d'ouvrage du projet et qui met le projet à disposition du demandeur. Ce tiers peut être une personne physique ou une personne morale.",
                        "sub_items": []
                        }
                    ],
                    "main_text": "<article class=\"legal-article\" id=\"art-1\"><header class=\"article-header\"><h2 class=\"article-number\">Article 1</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Au sens du présent arrêté, il convient d'entendre par:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">[1 Fonds: l'agence autonomisée interne dotée de la personnalité juridique &quot; Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden &quot;</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">[1</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">[4 demandeur: personne morale agréée ou répondant aux conditions légales pour organiser des soins et des services dans le cadre des matières personnalisables et qui introduit une demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">[4 investissement: coûts de construction,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"investissement : coûts de construction, de travaux d'agrandissement et de transformation, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">de travaux d'agrandissement et de transformation</span>, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres</span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">programmation: le planning relatif aux structures sur la base de critères géographiques, démographiques ou autres. Ces critères font l'objet de réglementations par catégorie d'investissement</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">[4 subvention d'investissement: subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur, conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">garantie d'investissement: la garantie du remboursement des emprunts contractés en vue de la réalisation de l'investissement, pour la partie des dépenses de capital non admise au bénéfice des subventions d'investissement</span></li><li class=\"provision\" data-number=\"8°\"><span class=\"provision-text\">promesse de subvention: l'obligation contractée en vue d'accorder une subvention d'investissement à un investissement et ayant fait l'objet d'un engagement à charge du budget de l'exercice en cours</span></li><li class=\"provision\" data-number=\"9°\"><span class=\"provision-text\">[7<span class=\"footnote-ref\" data-footnote-id=\"16\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023051209#Art.22\" data-article-dossier-number=\"\">...</span></span></li><li class=\"provision\" data-number=\"10°\"><span class=\"provision-text\">[1</span></li><li class=\"provision\" data-number=\"11°\"><span class=\"provision-text\">[1 Ministre: le Ministre flamand chargé de l'assistance aux personnes et le Ministre flamand chargé de la politique de la santé</span></li><li class=\"provision\" data-number=\"12°\"><span class=\"provision-text\">Décret: le décret du 23 février 1994 relatif à l'Infrastructure affectée aux matières personnalisables</span></li><li class=\"provision\" data-number=\"13°\"><span class=\"provision-text\">[4 plan maître: esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"plan maître : esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs, y compris un plan financier en proportion de l'exploitation prévue\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">y compris un plan financier en proportion de l'exploitation prévue</span></span></li><li class=\"provision\" data-number=\"14°\"><span class=\"provision-text\">[4 projet: l'objet de l'investissement envisagé,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"projet : l'objet de l'investissement envisagé, tel que décrit dans le plan maître, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">tel que décrit dans le plan maître</span>, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée</span></li><li class=\"provision\" data-number=\"15°\"><span class=\"provision-text\">[7<span class=\"footnote-ref\" data-footnote-id=\"16\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023051209#Art.22\" data-article-dossier-number=\"\">...</span></span></li><li class=\"provision\" data-number=\"16°\"><span class=\"provision-text\">Plan financier: une projection appuyée de chiffres réalistes du financement de l'investissement projeté indiquant les avoirs propres, les subventions d'investissement, les emprunts, les amortissements, les recettes et les dépenses ainsi qu'une estimation des résultats d'exploitation</span></li><li class=\"provision\" data-number=\"17°\"><span class=\"provision-text\">construction neuve: une nouvelle construction à destination propre, autonome et fonctionnelle dans le cadre des matières personnalisables</span></li><li class=\"provision\" data-number=\"18°\"><span class=\"provision-text\">extension: une construction partiellement neuve complétant une construction existante à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affectée à une destination fonctionnelle, la construction neuve s'alignant en termes fonctionnels sur la construction existante</span></li><li class=\"provision\" data-number=\"19°\"><span class=\"provision-text\">achat: l'acquisition d'un immeuble susceptible d'être affecté à une destination fonctionnelle dans le cadre des matières personnalisables</span></li><li class=\"provision\" data-number=\"20°\"><span class=\"provision-text\">transformation: toute intervention matérielle à l'exception de l'extension ainsi que des travaux d'entretien ou des travaux de remplacement indispensables à cause de l'usure, visant l'amélioration ou la rénovation d'un immeuble à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affecté à une destination fonctionnelle.</span></li><li class=\"provision\" data-number=\"21°\"><span class=\"provision-text\">Hôpitaux généraux: les hôpitaux visés à l'article 2 de la loi sur les hôpitaux, coordonnée le 7 août 1987, à l'exception des hôpitaux psychiatriques et des hôpitaux disposant exclusivement de services spécialisés pour le traitement et la réadaptation fonctionnelle (indice Sp), en liaison ou non avec des services d'hospitalisation ordinaire (indice H) ou des services neuro-psychiatriques pour le traitement de patients adultes (indice T) ou des services gériatriques (indice G)</span></li><li class=\"provision\" data-number=\"22°\"><span class=\"provision-text\">[2</span></li><li class=\"provision\" data-number=\"23°\"><span class=\"provision-text\">[2</span></li><li class=\"provision\" data-number=\"24°\"><span class=\"provision-text\">[2</span></li><li class=\"provision\" data-number=\"25°\"><span class=\"provision-text\">[7</span></li><li class=\"provision\" data-number=\"26°\"><span class=\"provision-text\">[7</span></li><li class=\"provision\" data-number=\"27°\"><span class=\"provision-text\">[7</span></li><li class=\"provision\" data-number=\"28°\"><span class=\"provision-text\">[15 centre pour troubles du développement: une structure agréée conformément à l'article 4 de l'arrêté du Gouvernement flamand du 16 juin 1998 réglant l'agrément et le subventionnement des centres pour troubles du développement</span></li></ol><p class=\"intro-text\">ellement compétente: suivant le cas, le<span class=\"footnote-ref\" data-footnote-id=\"16\" data-referenced-text=\"Département Soins\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023051209#Art.22\" data-article-dossier-number=\"\">Département Soins</span>, l'agence autonomisée interne sans personnalité juridique<span class=\"footnote-ref\" data-footnote-id=\"14\" data-referenced-text=\"&quot; Grandir &quot;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021031210#Art.2\" data-article-dossier-number=\"\">&quot; Grandir &quot;</span>, l'agence autonomisée interne dotée de la personnalité juridique &quot; Zorg en Gezondheid &quot; (Soin et Santé), l'agence autonomisée interne dotée de la personnalité juridique<span class=\"footnote-ref\" data-footnote-id=\"14\" data-referenced-text=\"&quot; Grandir Régie &quot;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021031210#Art.2\" data-article-dossier-number=\"\">&quot; Grandir Régie &quot;</span>ou<span class=\"footnote-ref\" data-footnote-id=\"16\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023051209#Art.22\" data-article-dossier-number=\"\">...</span>&quot; Vlaams Agentschap voor Personen met een Handicap &quot; (Agence flamande pour les personnes handicapées); 3° demandeur: personne morale agréée ou répondant aux conditions légales pour organiser des soins et des services dans le cadre des matières personnalisables et qui introduit une demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement; 4° investissement: coûts de construction,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"investissement : coûts de construction, de travaux d'agrandissement et de transformation, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">de travaux d'agrandissement et de transformation</span>, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres; 5° programmation: le planning relatif aux structures sur la base de critères géographiques, démographiques ou autres. Ces critères font l'objet de réglementations par catégorie d'investissement; 6° subvention d'investissement: subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"subvention d'investissement : subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur, conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables;</span>7° garantie d'investissement: la garantie du remboursement des emprunts contractés en vue de la réalisation de l'investissement, pour la partie des dépenses de capital non admise au bénéfice des subventions d'investissement; 8° promesse de subvention: l'obligation contractée en vue d'accorder une subvention d'investissement à un investissement et ayant fait l'objet d'un engagement à charge du budget de l'exercice en cours; 9°... 10° financier: une société de leasing ou un établissement de crédit ayant a obtenu l'agrément visé à l'article 7 de la loi du 22 mars 1993 relative au statut et au contrôle des établissements de crédit, et les sociétés y liées au sens de l'article 11 du Code des Sociétés, ainsi que tout autre établissement de crédit qui ressortit à un autre Etat membre de l'Union européenne et qui, conformément au Titre III de la loi précitée du 22 mars 1993, peut exercer ses activités sur le territoire belge<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"ou la Banque d'Investissement européenne\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2010060405#Art.3\" data-article-dossier-number=\"\">ou la Banque d'Investissement européenne</span>; 11° Ministre: le Ministre flamand chargé de l'assistance aux personnes et le Ministre flamand chargé de la politique de la santé; 12° Décret: le décret du 23 février 1994 relatif à l'Infrastructure affectée aux matières personnalisables; 13° plan maître: esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"plan maître : esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs, y compris un plan financier en proportion de l'exploitation prévue\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">y compris un plan financier en proportion de l'exploitation prévue</span>14° projet: l'objet de l'investissement envisagé, tel que décrit dans le plan maître,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"projet : l'objet de l'investissement envisagé, tel que décrit dans le plan maître, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.5\" data-article-dossier-number=\"\">pour lequel une subvention d'investissement ou une garantie d'investissement est demandée;</span>15°... 16° Plan financier: une projection appuyée de chiffres réalistes du financement de l'investissement projeté indiquant les avoirs propres, les subventions d'investissement, les emprunts, les amortissements, les recettes et les dépenses ainsi qu'une estimation des résultats d'exploitation; 17° construction neuve: une nouvelle construction à destination propre, autonome et fonctionnelle dans le cadre des matières personnalisables; une construction neuve comprend toujours un gros oeuvre; 18° extension: une construction partiellement neuve complétant une construction existante à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affectée à une destination fonctionnelle, la construction neuve s'alignant en termes fonctionnels sur la construction existante; 19° achat: l'acquisition d'un immeuble susceptible d'être affecté à une destination fonctionnelle dans le cadre des matières personnalisables; 20° transformation: toute intervention matérielle à l'exception de l'extension ainsi que des travaux d'entretien ou des travaux de remplacement indispensables à cause de l'usure, visant l'amélioration ou la rénovation d'un immeuble à destination fonctionnelle dans le cadre des matières personnalisables ou susceptible d'être affecté à une destination fonctionnelle. 21° Hôpitaux généraux: les hôpitaux visés à l'article 2 de la loi sur les hôpitaux, coordonnée le 7 août 1987, à l'exception des hôpitaux psychiatriques et des hôpitaux disposant exclusivement de services spécialisés pour le traitement et la réadaptation fonctionnelle (indice Sp), en liaison ou non avec des services d'hospitalisation ordinaire (indice H) ou des services neuro-psychiatriques pour le traitement de patients adultes (indice T) ou des services gériatriques (indice G); 22° centre de services locaux: un centre, tel que visé à l'article 9 du Décret sur les soins résidentiels du 15 février 2019;; 23° centre de convalescence: un centre tel que visé à l'article 28 du décret sur les soins résidentiels du 15 février 2019; 24° centre de soins de jour: un centre, tel que visé à l'article 23 du Décret sur les soins résidentiels du 15 février 2019; 25° centre de court séjour de type 2: un centre, tel que visé à l'article 26, § 1er, alinéa deux, 2°, du décret sur les soins résidentiels du 15 février 2019; 26° centre de court séjour de type 3: un centre, tel que visé à l'article 26, § 1er, alinéa deux, 3°, du décret sur les soins résidentiels du 15 février 2019; 27° centre d'accueil de jour: un centre d'accueil de jour d'un service d'aide aux familles, tel que visé aux articles 13 et 14 du décret sur les soins résidentiels du 15 février 2019;:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"28°\"><span class=\"provision-text\">bis [6</span></li><li class=\"provision\" data-number=\"29°\"><span class=\"provision-text\">[15 structures d'aide à la jeunesse: les structures agréées visées à l'article 2 de l'arrêté du Gouvernement flamand du 5 avril 2019 relatif aux conditions d'agrément et aux normes de subventionnement des structures d'aide à la jeunesse</span></li><li class=\"provision\" data-number=\"30°\"><span class=\"provision-text\">[5 équipement médical: tout le matériel médical et médico-technique utilisé dans les hôpitaux pour le diagnostic, le traitement ou la surveillance de patients,<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"équipement médical : tout le matériel médical et médico-technique utilisé dans les hôpitaux pour le diagnostic, le traitement ou la surveillance de patients, à l'exception du matériel médical et médico-technique non subventionnable, lié aux honoraires, que l'on utilise pour le diagnostic et le traitement. Les articles de consommation ne sont pas subventionnés;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.3\" data-article-dossier-number=\"\">à l'exception du matériel médical et médico-technique non subventionnable</span>, lié aux honoraires, que l'on utilise pour le diagnostic et le traitement. Les articles de consommation ne sont pas subventionnés</span></li><li class=\"provision\" data-number=\"31°\"><span class=\"provision-text\">services autorisés de placement familial: les services autorisés, visés à l'article 10 du décret du 29 juin 2012 portant organisation du placement familial</span></li><li class=\"provision\" data-number=\"32°\"><span class=\"provision-text\">&quot; plafond de construction calculé &quot;: dix sixièmes de la subvention d'investissement arrêtée dans la promesse de subvention, calculés conformément aux montants de base visés dans les arrêtés sectoriels</span></li><li class=\"provision\" data-number=\"33°\"><span class=\"provision-text\">investisseur: un tiers qui agit en tant que maître d'ouvrage du projet et qui met le projet à disposition du demandeur.<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"33° investisseur : un tiers qui agit en tant que maître d'ouvrage du projet et qui met le projet à disposition du demandeur. Ce tiers peut être une personne physique ou une personne morale.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019051767#Art.1\" data-article-dossier-number=\"\">Ce tiers peut être une personne physique ou une personne morale.</span></span></li></ol></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 34,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.291736"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 1, 006; En vigueur : 03-10-2008>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2008-05-30/39",
                        "article_number": "art. 1",
                        "sequence_number": "006",
                        "full_reference": "AGF [2008-05-30/39]"
                    },
                    "effective_date": "03-10-2008",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.1"
                    },
                    {
                    "footnote_number": "2",
                    "footnote_content": "(2)<AGF [2009-07-24/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2009072426), art. 40, 009; En vigueur : 01-01-2010>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2009-07-24/26",
                        "article_number": "art. 40",
                        "sequence_number": "009",
                        "full_reference": "AGF [2009-07-24/26]"
                    },
                    "effective_date": "01-01-2010",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2009072426",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2009072426#Art.40"
                    },
                    {
                    "footnote_number": "3",
                    "footnote_content": "(3)<AGF [2010-06-04/05](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2010060405), art. 3, 010; En vigueur : 05-07-2010>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2010-06-04/05",
                        "article_number": "art. 3",
                        "sequence_number": "010",
                        "full_reference": "AGF [2010-06-04/05]"
                    },
                    "effective_date": "05-07-2010",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2010060405",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2010060405#Art.3"
                    },
                    {
                    "footnote_number": "4",
                    "footnote_content": "(4)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 5, 016; En vigueur : 19-12-2011>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2011-11-10/07",
                        "article_number": "art. 5",
                        "sequence_number": "016",
                        "full_reference": "AGF [2011-11-10/07]"
                    },
                    "effective_date": "19-12-2011",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.5"
                    },
                    {
                    "footnote_number": "5",
                    "footnote_content": "(5)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 3, 017; En vigueur : 25-04-2014>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2014-02-14/26",
                        "article_number": "art. 3",
                        "sequence_number": "017",
                        "full_reference": "AGF [2014-02-14/26]"
                    },
                    "effective_date": "25-04-2014",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.3"
                    },
                    {
                    "footnote_number": "6",
                    "footnote_content": "(6)<AGF [2014-09-05/12](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512), art. 1, 018; En vigueur : 13-11-2014>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2014-09-05/12",
                        "article_number": "art. 1",
                        "sequence_number": "018",
                        "full_reference": "AGF [2014-09-05/12]"
                    },
                    "effective_date": "13-11-2014",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512#Art.1"
                    },
                    {
                    "footnote_number": "7",
                    "footnote_content": "(7)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 1, 020; En vigueur : 20-03-2016>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2016-01-15/17",
                        "article_number": "art. 1",
                        "sequence_number": "020",
                        "full_reference": "AGF [2016-01-15/17]"
                    },
                    "effective_date": "20-03-2016",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.1"
                    },
                    {
                    "footnote_number": "8",
                    "footnote_content": "(8)<AGF [2019-05-17/67](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767), art. 1, 024; En vigueur : 19-09-2019>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-05-17/67",
                        "article_number": "art. 1",
                        "sequence_number": "024",
                        "full_reference": "AGF [2019-05-17/67]"
                    },
                    "effective_date": "19-09-2019",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767#Art.1"
                    },
                    {
                    "footnote_number": "9",
                    "footnote_content": "(9)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 17,1°, 025; En vigueur : 01-01-2020>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-12-13/06",
                        "article_number": "art. 17",
                        "sequence_number": "1°",
                        "full_reference": "AGF [2019-12-13/06]"
                    },
                    "effective_date": "01-01-2020",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.17"
                    },
                    {
                    "footnote_number": "10",
                    "footnote_content": "(10)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 17,2°, 025; En vigueur : 01-01-2019>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-12-13/06",
                        "article_number": "art. 17",
                        "sequence_number": "2°",
                        "full_reference": "AGF [2019-12-13/06]"
                    },
                    "effective_date": "01-01-2019",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.17"
                    },
                    {
                    "footnote_number": "11",
                    "footnote_content": "(11)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 17,3°,4°, 025; En vigueur : 01-01-2020>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-12-13/06",
                        "article_number": "art. 17",
                        "sequence_number": "3°",
                        "full_reference": "AGF [2019-12-13/06]"
                    },
                    "effective_date": "01-01-2020",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.17"
                    },
                    {
                    "footnote_number": "12",
                    "footnote_content": "(12)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 17,5°, 025; En vigueur : 31-12-2025>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-12-13/06",
                        "article_number": "art. 17",
                        "sequence_number": "5°",
                        "full_reference": "AGF [2019-12-13/06]"
                    },
                    "effective_date": "31-12-2025",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.17"
                    },
                    {
                    "footnote_number": "13",
                    "footnote_content": "(13)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 17,6°, 025; En vigueur : 01-01-2020>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-12-13/06",
                        "article_number": "art. 17",
                        "sequence_number": "6°",
                        "full_reference": "AGF [2019-12-13/06]"
                    },
                    "effective_date": "01-01-2020",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.17"
                    },
                    {
                    "footnote_number": "14",
                    "footnote_content": "(14)<AGF [2021-03-12/10](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021031210), art. 2, 027; En vigueur : 18-04-2019>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2021-03-12/10",
                        "article_number": "art. 2",
                        "sequence_number": "027",
                        "full_reference": "AGF [2021-03-12/10]"
                    },
                    "effective_date": "18-04-2019",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021031210",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021031210#Art.2"
                    },
                    {
                    "footnote_number": "15",
                    "footnote_content": "(15)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 1, 028; En vigueur : 20-09-2021>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2021-07-16/32",
                        "article_number": "art. 1",
                        "sequence_number": "028",
                        "full_reference": "AGF [2021-07-16/32]"
                    },
                    "effective_date": "20-09-2021",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.1"
                    },
                    {
                    "footnote_number": "16",
                    "footnote_content": "(16)<AGF [2023-05-12/09](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023051209), art. 22, 031; En vigueur : 10-07-2023>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2023-05-12/09",
                        "article_number": "art. 22",
                        "sequence_number": "031",
                        "full_reference": "AGF [2023-05-12/09]"
                    },
                    "effective_date": "10-07-2023",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023051209",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023051209#Art.22"
                    },
                    {
                    "footnote_number": "17",
                    "footnote_content": "(17)<AGF [2024-06-21/21](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121), art. 1, 032; En vigueur : 01-04-2024>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2024-06-21/21",
                        "article_number": "art. 1",
                        "sequence_number": "032",
                        "full_reference": "AGF [2024-06-21/21]"
                    },
                    "effective_date": "01-04-2024",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121#Art.1"
                    },
                    {
                    "footnote_number": "18",
                    "footnote_content": "(18)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 1, 034; En vigueur : 01-01-2025>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2024-07-19/42",
                        "article_number": "art. 1",
                        "sequence_number": "034",
                        "full_reference": "AGF [2024-07-19/42]"
                    },
                    "effective_date": "01-01-2025",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.1"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "1",
                    "text_position": 61,
                    "referenced_text": "Fonds : l'agence autonomisée interne dotée de la personnalité juridique \" Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden \";",
                    "embedded_law_references": [],
                    "bracket_pattern": "[1 Fonds : l'agence autonomisée interne dotée de la personnalité juridique \" Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden \";]1"
                    },
                    {
                    "reference_number": "16",
                    "text_position": 282,
                    "referenced_text": "Département Soins",
                    "embedded_law_references": [],
                    "bracket_pattern": "[16 Département Soins]16"
                    },
                    {
                    "reference_number": "14",
                    "text_position": 365,
                    "referenced_text": "\" Grandir \"",
                    "embedded_law_references": [],
                    "bracket_pattern": "[14 \" Grandir \"]14"
                    },
                    {
                    "reference_number": "14",
                    "text_position": 553,
                    "referenced_text": "\" Grandir Régie \"",
                    "embedded_law_references": [],
                    "bracket_pattern": "[14 \" Grandir Régie \"]14"
                    },
                    {
                    "reference_number": "16",
                    "text_position": 581,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[16 ...]16"
                    },
                    {
                    "reference_number": "4",
                    "text_position": 703,
                    "referenced_text": "demandeur : personne morale agréée ou répondant aux conditions légales pour organiser des soins et des services dans le cadre des matières personnalisables et qui introduit une demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 demandeur : personne morale agréée ou répondant aux conditions légales pour organiser des soins et des services dans le cadre des matières personnalisables et qui introduit une demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement;]4"
                    },
                    {
                    "reference_number": "4",
                    "text_position": 977,
                    "referenced_text": "investissement : coûts de construction, de travaux d'agrandissement et de transformation, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 investissement : coûts de construction, de travaux d'agrandissement et de transformation, d'achat d'infrastructure, d'équipement ou d'appareillage, à l'exception de l'achat de terres;]4"
                    },
                    {
                    "reference_number": "4",
                    "text_position": 1369,
                    "referenced_text": "subvention d'investissement : subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur, conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 subvention d'investissement : subvention en tant que contribution directe ou indirecte au coût du projet ou le financement de l'investissement par un demandeur, conformément aux dispositions du décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables;]4"
                    },
                    {
                    "reference_number": "7",
                    "text_position": 2099,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[7 ...]7"
                    },
                    {
                    "reference_number": "3",
                    "text_position": 2613,
                    "referenced_text": "ou la Banque d'Investissement européenne",
                    "embedded_law_references": [],
                    "bracket_pattern": "[3 ou la Banque d'Investissement européenne]3"
                    },
                    {
                    "reference_number": "1",
                    "text_position": 2669,
                    "referenced_text": "Ministre : le Ministre flamand chargé de l'assistance aux personnes et le Ministre flamand chargé de la politique de la santé;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[1 Ministre : le Ministre flamand chargé de l'assistance aux personnes et le Ministre flamand chargé de la politique de la santé;]1"
                    },
                    {
                    "reference_number": "4",
                    "text_position": 2918,
                    "referenced_text": "plan maître : esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs, y compris un plan financier en proportion de l'exploitation prévue",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 plan maître : esquisse descriptive et globale avec estimation des frais du projet envisagé ou des projets envisagés, mentionnant le groupe cible, la capacité, les délais d'exécution et développements futurs, y compris un plan financier en proportion de l'exploitation prévue]4"
                    },
                    {
                    "reference_number": "4",
                    "text_position": 3204,
                    "referenced_text": "projet : l'objet de l'investissement envisagé, tel que décrit dans le plan maître, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 projet : l'objet de l'investissement envisagé, tel que décrit dans le plan maître, pour lequel une subvention d'investissement ou une garantie d'investissement est demandée;]4"
                    },
                    {
                    "reference_number": "7",
                    "text_position": 3389,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[7 ...]7"
                    },
                    {
                    "reference_number": "9",
                    "text_position": 5223,
                    "referenced_text": "centre de services locaux : un centre, tel que visé à l'article 9 du Décret sur les soins résidentiels du 15 février 2019 ;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[9 centre de services locaux : un centre, tel que visé à l'article 9 du Décret sur les soins résidentiels du 15 février 2019 ;]9"
                    },
                    {
                    "reference_number": "17",
                    "text_position": 5366,
                    "referenced_text": "centre de convalescence : un centre tel que visé à l'article 28 du décret sur les soins résidentiels du 15 février 2019;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[17 centre de convalescence : un centre tel que visé à l'article 28 du décret sur les soins résidentiels du 15 février 2019;]17"
                    },
                    {
                    "reference_number": "11",
                    "text_position": 5507,
                    "referenced_text": "centre de soins de jour : un centre, tel que visé à l'article 23 du Décret sur les soins résidentiels du 15 février 2019 ;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[11 centre de soins de jour : un centre, tel que visé à l'article 23 du Décret sur les soins résidentiels du 15 février 2019 ;]11"
                    },
                    {
                    "reference_number": "11",
                    "text_position": 5650,
                    "referenced_text": "centre de court séjour de type 2 : un centre, tel que visé à l'article 26, § 1er, alinéa deux, 2°, du décret sur les soins résidentiels du 15 février 2019 ;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[11 centre de court séjour de type 2 : un centre, tel que visé à l'article 26, § 1er, alinéa deux, 2°, du décret sur les soins résidentiels du 15 février 2019 ;]11"
                    },
                    {
                    "reference_number": "12",
                    "text_position": 5827,
                    "referenced_text": "centre de court séjour de type 3 : un centre, tel que visé à l'article 26, § 1er, alinéa deux, 3°, du décret sur les soins résidentiels du 15 février 2019 ;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[12 centre de court séjour de type 3 : un centre, tel que visé à l'article 26, § 1er, alinéa deux, 3°, du décret sur les soins résidentiels du 15 février 2019 ;]12"
                    },
                    {
                    "reference_number": "13",
                    "text_position": 6004,
                    "referenced_text": "centre d'accueil de jour : un centre d'accueil de jour d'un service d'aide aux familles, tel que visé aux articles 13 et 14 du décret sur les soins résidentiels du 15 février 2019 ;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[13 centre d'accueil de jour : un centre d'accueil de jour d'un service d'aide aux familles, tel que visé aux articles 13 et 14 du décret sur les soins résidentiels du 15 février 2019 ;]13"
                    },
                    {
                    "reference_number": "15",
                    "text_position": 6202,
                    "referenced_text": "centre pour troubles du développement : une structure agréée conformément à l'article 4 de l'arrêté du Gouvernement flamand du 16 juin 1998 réglant l'agrément et le subventionnement des centres pour troubles du développement",
                    "embedded_law_references": [],
                    "bracket_pattern": "[15 centre pour troubles du développement : une structure agréée conformément à l'article 4 de l'arrêté du Gouvernement flamand du 16 juin 1998 réglant l'agrément et le subventionnement des centres pour troubles du développement]15"
                    },
                    {
                    "reference_number": "15",
                    "text_position": 6449,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[15 ...]15"
                    },
                    {
                    "reference_number": "15",
                    "text_position": 6469,
                    "referenced_text": "structures d'aide à la jeunesse : les structures agréées visées à l'article 2 de l'arrêté du Gouvernement flamand du 5 avril 2019 relatif aux conditions d'agrément et aux normes de subventionnement des structures d'aide à la jeunesse",
                    "embedded_law_references": [],
                    "bracket_pattern": "[15 structures d'aide à la jeunesse : les structures agréées visées à l'article 2 de l'arrêté du Gouvernement flamand du 5 avril 2019 relatif aux conditions d'agrément et aux normes de subventionnement des structures d'aide à la jeunesse]15"
                    },
                    {
                    "reference_number": "18",
                    "text_position": 6710,
                    "referenced_text": "et les centres de confiance pour enfants maltraités, visés à l'arrêté du Gouvernement flamand du 17 novembre 2017 relatif à l'agrément et au subventionnement des centres de confiance pour enfants maltraités et de l'organisation partenaire",
                    "embedded_law_references": [],
                    "bracket_pattern": "[18 et les centres de confiance pour enfants maltraités, visés à l'arrêté du Gouvernement flamand du 17 novembre 2017 relatif à l'agrément et au subventionnement des centres de confiance pour enfants maltraités et de l'organisation partenaire]18"
                    },
                    {
                    "reference_number": "5",
                    "text_position": 6963,
                    "referenced_text": "équipement médical : tout le matériel médical et médico-technique utilisé dans les hôpitaux pour le diagnostic, le traitement ou la surveillance de patients, à l'exception du matériel médical et médico-technique non subventionnable, lié aux honoraires, que l'on utilise pour le diagnostic et le traitement. Les articles de consommation ne sont pas subventionnés;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[5 équipement médical : tout le matériel médical et médico-technique utilisé dans les hôpitaux pour le diagnostic, le traitement ou la surveillance de patients, à l'exception du matériel médical et médico-technique non subventionnable, lié aux honoraires, que l'on utilise pour le diagnostic et le traitement. Les articles de consommation ne sont pas subventionnés;]5"
                    },
                    {
                    "reference_number": "6",
                    "text_position": 7333,
                    "referenced_text": "31° services autorisés de placement familial : les services autorisés, visés à l'article 10 du décret du 29 juin 2012 portant organisation du placement familial;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[6 31° services autorisés de placement familial : les services autorisés, visés à l'article 10 du décret du 29 juin 2012 portant organisation du placement familial;]6"
                    },
                    {
                    "reference_number": "7",
                    "text_position": 7502,
                    "referenced_text": "32° \" plafond de construction calculé \" : dix sixièmes de la subvention d'investissement arrêtée dans la promesse de subvention, calculés conformément aux montants de base visés dans les arrêtés sectoriels;",
                    "embedded_law_references": [],
                    "bracket_pattern": "[7 32° \" plafond de construction calculé \" : dix sixièmes de la subvention d'investissement arrêtée dans la promesse de subvention, calculés conformément aux montants de base visés dans les arrêtés sectoriels;]7"
                    },
                    {
                    "reference_number": "8",
                    "text_position": 7716,
                    "referenced_text": "33° investisseur : un tiers qui agit en tant que maître d'ouvrage du projet et qui met le projet à disposition du demandeur. Ce tiers peut être une personne physique ou une personne morale.",
                    "embedded_law_references": [],
                    "bracket_pattern": "[8 33° investisseur : un tiers qui agit en tant que maître d'ouvrage du projet et qui met le projet à disposition du demandeur. Ce tiers peut être une personne physique ou une personne morale.]8"
                    }
                ]
                },
                {
                "type": "article",
                "label": "Article 2",
                "metadata": {
                    "article_range": "2",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "2",
                    "anchor_id": "art_2",
                    "content": {
                    "main_text_raw": "Le présent arrêté s'applique à tous les demandeurs qui entrent en ligne de compte pour une subvention d'investissement ou une garantie d'investissement.",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-2\"><header class=\"article-header\"><h2 class=\"article-number\">Article 2</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le présent arrêté s'applique à tous les<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"demandeurs\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.6\" data-article-dossier-number=\"\">demandeurs</span>qui entrent en ligne de compte pour une subvention d'investissement ou une garantie d'investissement.</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.291936"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 6, 016; En vigueur : 19-12-2011>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2011-11-10/07",
                        "article_number": "art. 6",
                        "sequence_number": "016",
                        "full_reference": "AGF [2011-11-10/07]"
                    },
                    "effective_date": "19-12-2011",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.6"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "1",
                    "text_position": 40,
                    "referenced_text": "demandeurs",
                    "embedded_law_references": [],
                    "bracket_pattern": "[1 demandeurs]1"
                    }
                ]
                },
                {
                "type": "article",
                "label": "Article 2bis",
                "metadata": {
                    "article_range": "2bis",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "2bis",
                    "anchor_id": "art_2bis",
                    "content": {
                    "main_text_raw": "Le demandeur ne peut obtenir de subvention d'investissement ou de garantie d'investissement que lorsqu'il satisfait aux conditions suivantes: 1° il est agréé ou il satisfait aux conditions légales pour organiser des soins et services dans le cadre des matières personnalisables, visés à l'article 2, 1°, du décret; 2° il dispose d'un droit de jouissance du projet, tel que visé à l'article 12 du décret. Lorsque le demandeur et le détenteur des droits réels du terrain sur lequel un projet est prévu sont deux personnes différentes, il ne peut y avoir de parenté illégitime mutuelle, telle que visée à l'article 2ter. 3° il assure l'application de la réglementation relative aux marchés publics pour les investissements relevant du champ d'application matériel de la réglementation précitée.",
                    "numbered_provisions": [
                        {
                        "number": "1°",
                        "text": "il est agréé ou il satisfait aux conditions légales pour organiser des soins et services dans le cadre des matières personnalisables, visés à l'article 2,",
                        "sub_items": []
                        },
                        {
                        "number": "2°",
                        "text": "il dispose d'un droit de jouissance du projet, tel que visé à [2 l'article 12",
                        "sub_items": []
                        },
                        {
                        "number": "3°",
                        "text": "il assure l'application de la réglementation relative aux marchés publics pour les investissements relevant du champ d'application matériel de la réglementation précitée.",
                        "sub_items": []
                        }
                    ],
                    "main_text": "<article class=\"legal-article\" id=\"art-2bis\"><header class=\"article-header\"><h2 class=\"article-number\">Article 2bis</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Le demandeur ne peut obtenir de subvention d'investissement ou de garantie d'investissement que lorsqu'il satisfait aux conditions suivantes:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">il est agréé ou il satisfait aux conditions légales pour organiser des soins et services dans le cadre des matières personnalisables, visés à l'article 2,</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">il dispose d'un droit de jouissance du projet, tel que visé à [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"l'article 12\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.2\" data-article-dossier-number=\"\">l'article 12</span></span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">il assure l'application de la réglementation relative aux marchés publics pour les investissements relevant du champ d'application matériel de la réglementation précitée.</span></li></ol></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 3,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.292343"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<Inséré par AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 7, 016; En vigueur : 19-12-2011>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2011-11-10/07",
                        "article_number": "art. 7",
                        "sequence_number": "016",
                        "full_reference": "AGF [2011-11-10/07]"
                    },
                    "effective_date": "19-12-2011",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.7"
                    },
                    {
                    "footnote_number": "2",
                    "footnote_content": "(2)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 2, 020; En vigueur : 20-03-2016>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2016-01-15/17",
                        "article_number": "art. 2",
                        "sequence_number": "020",
                        "full_reference": "AGF [2016-01-15/17]"
                    },
                    "effective_date": "20-03-2016",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.2"
                    },
                    {
                    "footnote_number": "3",
                    "footnote_content": "(3)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 1, 022; En vigueur : 11-10-2018>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2018-07-06/25",
                        "article_number": "art. 1",
                        "sequence_number": "022",
                        "full_reference": "AGF [2018-07-06/25]"
                    },
                    "effective_date": "11-10-2018",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.1"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "2",
                    "text_position": 389,
                    "referenced_text": "l'article 12",
                    "embedded_law_references": [],
                    "bracket_pattern": "[2 l'article 12]2"
                    },
                    {
                    "reference_number": "3",
                    "text_position": 637,
                    "referenced_text": "3° il assure l'application de la réglementation relative aux marchés publics pour les investissements relevant du champ d'application matériel de la réglementation précitée.",
                    "embedded_law_references": [],
                    "bracket_pattern": "[3 3° il assure l'application de la réglementation relative aux marchés publics pour les investissements relevant du champ d'application matériel de la réglementation précitée.]3"
                    }
                ]
                },
                {
                "type": "article",
                "label": "Article 2ter",
                "metadata": {
                    "article_range": "2ter",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "2ter",
                    "anchor_id": "art_2ter",
                    "content": {
                    "main_text_raw": "Le demandeur et le propriétaire du terrain sur lequel un projet est exécuté ou le demandeur et le détenteur des droits réels sur le terrain sur lequel le projet est exécuté, sont supposés avoir une parenté illégitime mutuelle lorsque le propriétaire du terrain ou le détenteur des droits réels sur le terrain est une personne physique ou une société de personnalité juridique telle que visée au Code des Sociétés, à l'exception d'une société coopérative agréée conformément à l'article 5 de la loi du 20 juillet 1955 portant institution d'un Conseil national de la Coopération,, et lorsque l'un a la compétence directe ou indirecte de droit ou de fait d'exercer une influence décisive auprès de l'autre en matière de la désignation de la majorité des membres de l'organe administratif ou de l'orientation politique. La parenté illégitime est de droit et est présumée irréfragable lorsque: 1° le propriétaire du terrain ou le détenteur des droits réels sur le terrain est en possession de la majorité des droits de vote liés au total des droits de participation du demandeur; 2° le demandeur est en possession de la majorité des droits de vote liés au total des effets du propriétaire du terrain ou du détenteur des droits réels sur le terrain; 3° la majorité des administrateurs du propriétaire du terrain ou le détenteur des droits réels sur le terrain, ou les actionnaires du propriétaire du terrain ou du détenteur des droits réels sur le terrain, détient ou détiennent, à titre personnel, seul ou ensemble, la majorité des droits de vote liés aux droits de participation du demandeur; 4° la majorité des administrateurs ou des membres du demandeur détient ou détiennent, à titre personnel, seul ou ensemble, la majorité des droits de vote liés aux effets du propriétaire du terrain ou du détenteur des droits réels sur le terrain; 5° le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou la majorité de ses administrateurs ou de ses actionnaires ou de ses ayant droits économiques a ou ont le droit de désigner ou de licencier la majorité des administrateurs du demandeur; 6° le demandeur ou la majorité de ses administrateurs ou de ses membres ou de ses ayant droits économiques a ou ont le droit de désigner ou de licencier la majorité des administrateurs du propriétaire du terrain ou du détenteur des droits réels sur le terrain; 7° le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou la majorité de ses administrateurs ou de ses actionnaires ou de ses ayant droits économiques dispose ou disposent, en vertu des statuts du demandeur ou en vertu d'un contrat conclu, de la compétence d'exercer une influence décisive sur la désignation de la majorité de l'organe administratif ou sur l'orientation politique; 8° le demandeur ou la majorité de ses administrateurs, de ses membres ou de ses ayant droits économiques dispose ou disposent, en vertu des statuts du propriétaire du terrain ou du détenteur des droits réels sur le terrain ou en vertu d'un contrat conclu, de la compétence d'exercer une influence décisive sur la désignation de la majorité de l'organe administratif ou sur l'orientation politique; 9° le propriétaire du terrain ou le détenteur des droits réels sur le terrain, ses administrateurs ou ses actionnaires ont fait valoir des droits de vote lors de l'avant-dernière et dernière assemblée générale du demandeur qui représentent la majorité des droits de vote liés aux actions représentées pendant ces assemblées générales; 10° le demandeur, ses administrateurs ou ses actionnaires ont fait valoir des droits de vote lors de l'avant-dernière et dernière assemblée générale du propriétaire du terrain ou du détenteur des droits réels sur le terrain qui représentent la majorité des droits de vote liés aux actions représentées pendant ces assemblées générales; 11° le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur sont sous une direction centrale. Il est supposé qu'ils sont sous une direction centrale lorsque: a) la direction centrale résulte des statuts du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, et du demandeur d'autre part, ou d'un contrat entre toutes les entités concernées; b) les organes administratifs du propriétaire du terrain ou respectivement du détenteur des droits réels sur le terrain et du demandeur, ainsi que de l'entité exerçant la direction générale, sont composés pour la majorité des mêmes personnes; c) la majorité des actions ou des droits d'adhésion du propriétaire du terrain, respectivement du détenteur des droits réels sur le terrain et du demandeur, ainsi que de l'entité exerçant la direction générale, sont entre les mains des mêmes personnes; 12° le propriétaire du terrain ou le détenteur des droits réels sur le terrain exerce une influence directe ou indirecte significative sur l'orientation de la politique du demandeur en prenant une participation d'au moins dix pour cent dans l'adhésion du demandeur; 13° le demandeur exerce une influence directe ou indirecte significative sur l'orientation de la politique du propriétaire du terrain ou du détenteur des droits réels sur le terrain en prenant une participation d'au moins dix pour cent dans le capital du propriétaire du terrain ou du détenteur des droits réels sur le terrain; 14° les administrateurs ou les actionnaires du demandeur d'une part, et le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou ses administrateurs ou les actionnaires d'autre part, sont des consanguins ou parents jusqu'au deuxième degré ou des conjoints. Pour l'application de cette disposition, les personnes qui ont conclu un contrat de vie commune légal sont assimilées à des conjoints. L'incompatibilité est censée s'arrêter à la suite du décès de la personne par qui elle a été créée, du divorce ou de la cessation du contrat de vie commune légal. Pour l'évaluation des cas, visés à l'alinéa deux, il n'est pas important que: 1° les administrateurs ou les actionnaires du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, ou les administrateurs ou membres du demandeur d'autre part, agissent seuls ou ensemble. Sauf preuve du contraire, des personnes qui sont au même moment administrateur ou actionnaire du propriétaire du terrain ou du détenteur des droits réels sur le terrain et administrateur ou membre du demandeur, sont supposés agir ensemble; 2° la parenté de manière directe ou indirecte, avec interposition d'autres entités ou de personnes intermédiaires, est réalisée; 3° des droits de vote sont suspendus ou soumis à une limitation de la valeur de vote. La parenté illégitime peut en fait être supposée par le Fonds sur la base d'autres éléments que les éléments, visés à l'alinéa deux. Cette supposition est réfutable par le demandeur. Le Fonds dispose de la possibilité de demander, à n'importe quel stade de la procédure, des données complémentaires au demandeur sur la parenté entre le demandeur et le propriétaire du terrain ou le détenteur des droits réels sur le terrain. Le Fonds dispose de la possibilité de demander, à n'importe quel stade de la procédure, des données complémentaires au demandeur sur la validité de son lien juridique avec le demandeur et le propriétaire du terrain ou le détenteur des droits réels sur le terrain et sur la conformité au marché des indemnités basées sur ce lien juridique.",
                    "numbered_provisions": [
                        {
                        "number": "1°",
                        "text": "le propriétaire du terrain ou le détenteur des droits réels sur le terrain est en possession de la majorité des droits de vote liés au total des droits de participation du demandeur",
                        "sub_items": []
                        },
                        {
                        "number": "2°",
                        "text": "le demandeur est en possession de la majorité des droits de vote liés au total des effets du propriétaire du terrain ou du détenteur des droits réels sur le terrain",
                        "sub_items": []
                        },
                        {
                        "number": "3°",
                        "text": "la majorité des administrateurs du propriétaire du terrain ou le détenteur des droits réels sur le terrain, ou les actionnaires du propriétaire du terrain ou du détenteur des droits réels sur le terrain, détient ou détiennent, à titre personnel, seul ou ensemble, la majorité des droits de vote liés aux droits de participation du demandeur",
                        "sub_items": []
                        },
                        {
                        "number": "4°",
                        "text": "la majorité des administrateurs ou des membres du demandeur détient ou détiennent, à titre personnel, seul ou ensemble, la majorité des droits de vote liés aux effets du propriétaire du terrain ou du détenteur des droits réels sur le terrain",
                        "sub_items": []
                        },
                        {
                        "number": "5°",
                        "text": "le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou la majorité de ses administrateurs ou de ses actionnaires ou de ses ayant droits économiques a ou ont le droit de désigner ou de licencier la majorité des administrateurs du demandeur",
                        "sub_items": []
                        },
                        {
                        "number": "6°",
                        "text": "le demandeur ou la majorité de ses administrateurs ou de ses membres ou de ses ayant droits économiques a ou ont le droit de désigner ou de licencier la majorité des administrateurs du propriétaire du terrain ou du détenteur des droits réels sur le terrain",
                        "sub_items": []
                        },
                        {
                        "number": "7°",
                        "text": "le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou la majorité de ses administrateurs ou de ses actionnaires ou de ses ayant droits économiques dispose ou disposent, en vertu des statuts du demandeur ou en vertu d'un contrat conclu, de la compétence d'exercer une influence décisive sur la désignation de la majorité de l'organe administratif ou sur l'orientation politique",
                        "sub_items": []
                        },
                        {
                        "number": "8°",
                        "text": "le demandeur ou la majorité de ses administrateurs, de ses membres ou de ses ayant droits économiques dispose ou disposent, en vertu des statuts du propriétaire du terrain ou du détenteur des droits réels sur le terrain ou en vertu d'un contrat conclu, de la compétence d'exercer une influence décisive sur la désignation de la majorité de l'organe administratif ou sur l'orientation politique",
                        "sub_items": []
                        },
                        {
                        "number": "9°",
                        "text": "le propriétaire du terrain ou le détenteur des droits réels sur le terrain, ses administrateurs ou ses actionnaires ont fait valoir des droits de vote lors de l'avant-dernière et dernière assemblée générale du demandeur qui représentent la majorité des droits de vote liés aux actions représentées pendant ces assemblées générales",
                        "sub_items": []
                        },
                        {
                        "number": "10°",
                        "text": "le demandeur, ses administrateurs ou ses actionnaires ont fait valoir des droits de vote lors de l'avant-dernière et dernière assemblée générale du propriétaire du terrain ou du détenteur des droits réels sur le terrain qui représentent la majorité des droits de vote liés aux actions représentées pendant ces assemblées générales",
                        "sub_items": []
                        },
                        {
                        "number": "11°",
                        "text": "le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur sont sous une direction centrale. Il est supposé qu'ils sont sous une direction centrale lorsque:",
                        "sub_items": []
                        },
                        {
                        "number": "12°",
                        "text": "le propriétaire du terrain ou le détenteur des droits réels sur le terrain exerce une influence directe ou indirecte significative sur l'orientation de la politique du demandeur en prenant une participation d'au moins dix pour cent dans l'adhésion du demandeur",
                        "sub_items": []
                        },
                        {
                        "number": "13°",
                        "text": "le demandeur exerce une influence directe ou indirecte significative sur l'orientation de la politique du propriétaire du terrain ou du détenteur des droits réels sur le terrain en prenant une participation d'au moins dix pour cent dans le capital du propriétaire du terrain ou du détenteur des droits réels sur le terrain",
                        "sub_items": []
                        },
                        {
                        "number": "14°",
                        "text": "les administrateurs ou les actionnaires du demandeur d'une part, et le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou ses administrateurs ou les actionnaires d'autre part, sont des consanguins ou parents jusqu'au deuxième degré ou des conjoints. Pour l'application de cette disposition, les personnes qui ont conclu un contrat de vie commune légal sont assimilées à des conjoints. L'incompatibilité est censée s'arrêter à la suite du décès de la personne par qui elle a été créée, du divorce ou de la cessation du contrat de vie commune légal.",
                        "sub_items": []
                        },
                        {
                        "number": "1°",
                        "text": "les administrateurs ou les actionnaires du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, ou les administrateurs ou membres du demandeur d'autre part, agissent seuls ou ensemble. Sauf preuve du contraire, des personnes qui sont au même moment administrateur ou actionnaire du propriétaire du terrain ou du détenteur des droits réels sur le terrain et administrateur ou membre du demandeur, sont supposés agir ensemble",
                        "sub_items": []
                        },
                        {
                        "number": "2°",
                        "text": "la parenté de manière directe ou indirecte, avec interposition d'autres entités ou de personnes intermédiaires, est réalisée",
                        "sub_items": []
                        },
                        {
                        "number": "3°",
                        "text": "des droits de vote sont suspendus ou soumis à une limitation de la valeur de vote.",
                        "sub_items": []
                        }
                    ],
                    "main_text": "<article class=\"legal-article\" id=\"art-2ter\"><header class=\"article-header\"><h2 class=\"article-number\">Article 2ter</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Le demandeur et le propriétaire du terrain sur lequel un projet est exécuté ou le demandeur et le détenteur des droits réels sur le terrain sur lequel le projet est exécuté, sont supposés avoir une parenté illégitime mutuelle lorsque le propriétaire du terrain ou le détenteur des droits réels sur le terrain est une personne physique ou<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"une société de personnalité juridique telle que visée au Code des Sociétés, à l'exception d'une société coopérative agréée conformément à l'article 5 de la loi du 20 juillet 1955 portant institution d'un Conseil national de la Coopération,\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.2\" data-article-dossier-number=\"\">une société de personnalité juridique telle que visée au Code des Sociétés, à l'exception d'une société coopérative agréée conformément à l'article 5 de la loi du 20 juillet 1955 portant institution d'un Conseil national de la Coopération,</span>, et lorsque l'un a la compétence directe ou indirecte de droit ou de fait d'exercer une influence décisive auprès de l'autre en matière de la désignation de la majorité des membres de l'organe administratif ou de l'orientation politique. La parenté illégitime est de droit et est présumée irréfragable lorsque:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">le propriétaire du terrain ou le détenteur des droits réels sur le terrain est en possession de la majorité des droits de vote liés au total des droits de participation du demandeur</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le demandeur est en possession de la majorité des droits de vote liés au total des effets du propriétaire du terrain ou du détenteur des droits réels sur le terrain</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">la majorité des administrateurs du propriétaire du terrain ou le détenteur des droits réels sur le terrain, ou les actionnaires du propriétaire du terrain ou du détenteur des droits réels sur le terrain, détient ou détiennent, à titre personnel, seul ou ensemble, la majorité des droits de vote liés aux droits de participation du demandeur</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">la majorité des administrateurs ou des membres du demandeur détient ou détiennent, à titre personnel, seul ou ensemble, la majorité des droits de vote liés aux effets du propriétaire du terrain ou du détenteur des droits réels sur le terrain</span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou la majorité de ses administrateurs ou de ses actionnaires ou de ses ayant droits économiques a ou ont le droit de désigner ou de licencier la majorité des administrateurs du demandeur</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">le demandeur ou la majorité de ses administrateurs ou de ses membres ou de ses ayant droits économiques a ou ont le droit de désigner ou de licencier la majorité des administrateurs du propriétaire du terrain ou du détenteur des droits réels sur le terrain</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou la majorité de ses administrateurs ou de ses actionnaires ou de ses ayant droits économiques dispose ou disposent, en vertu des statuts du demandeur ou en vertu d'un contrat conclu, de la compétence d'exercer une influence décisive sur la désignation de la majorité de l'organe administratif ou sur l'orientation politique</span></li><li class=\"provision\" data-number=\"8°\"><span class=\"provision-text\">le demandeur ou la majorité de ses administrateurs, de ses membres ou de ses ayant droits économiques dispose ou disposent, en vertu des statuts du propriétaire du terrain ou du détenteur des droits réels sur le terrain ou en vertu d'un contrat conclu, de la compétence d'exercer une influence décisive sur la désignation de la majorité de l'organe administratif ou sur l'orientation politique</span></li><li class=\"provision\" data-number=\"9°\"><span class=\"provision-text\">le propriétaire du terrain ou le détenteur des droits réels sur le terrain, ses administrateurs ou ses actionnaires ont fait valoir des droits de vote lors de l'avant-dernière et dernière assemblée générale du demandeur qui représentent la majorité des droits de vote liés aux actions représentées pendant ces assemblées générales</span></li><li class=\"provision\" data-number=\"10°\"><span class=\"provision-text\">le demandeur, ses administrateurs ou ses actionnaires ont fait valoir des droits de vote lors de l'avant-dernière et dernière assemblée générale du propriétaire du terrain ou du détenteur des droits réels sur le terrain qui représentent la majorité des droits de vote liés aux actions représentées pendant ces assemblées générales</span></li><li class=\"provision\" data-number=\"11°\"><span class=\"provision-text\">le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur sont sous une direction centrale. Il est supposé qu'ils sont sous une direction centrale lorsque:</span></li><li class=\"provision\" data-number=\"12°\"><span class=\"provision-text\">le propriétaire du terrain ou le détenteur des droits réels sur le terrain exerce une influence directe ou indirecte significative sur l'orientation de la politique du demandeur en prenant une participation d'au moins dix pour cent dans l'adhésion du demandeur</span></li><li class=\"provision\" data-number=\"13°\"><span class=\"provision-text\">le demandeur exerce une influence directe ou indirecte significative sur l'orientation de la politique du propriétaire du terrain ou du détenteur des droits réels sur le terrain en prenant une participation d'au moins dix pour cent dans le capital du propriétaire du terrain ou du détenteur des droits réels sur le terrain</span></li><li class=\"provision\" data-number=\"14°\"><span class=\"provision-text\">les administrateurs ou les actionnaires du demandeur d'une part, et le propriétaire du terrain ou le détenteur des droits réels sur le terrain ou ses administrateurs ou les actionnaires d'autre part, sont des consanguins ou parents jusqu'au deuxième degré ou des conjoints. Pour l'application de cette disposition, les personnes qui ont conclu un contrat de vie commune légal sont assimilées à des conjoints. L'incompatibilité est censée s'arrêter à la suite du décès de la personne par qui elle a été créée, du divorce ou de la cessation du contrat de vie commune légal.</span></li></ol><p class=\"intro-text\">Pour l'évaluation des cas, visés à l'alinéa deux, il n'est pas important que:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les administrateurs ou les actionnaires du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, ou les administrateurs ou membres du demandeur d'autre part, agissent seuls ou ensemble. Sauf preuve du contraire, des personnes qui sont au même moment administrateur ou actionnaire du propriétaire du terrain ou du détenteur des droits réels sur le terrain et administrateur ou membre du demandeur, sont supposés agir ensemble</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">la parenté de manière directe ou indirecte, avec interposition d'autres entités ou de personnes intermédiaires, est réalisée</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">des droits de vote sont suspendus ou soumis à une limitation de la valeur de vote.</span></li></ol><p class=\"closing-text\">La parenté illégitime peut en fait être supposée par le Fonds sur la base d'autres éléments que les éléments, visés à l'alinéa deux. Cette supposition est réfutable par le demandeur. Le Fonds dispose de la possibilité de demander, à n'importe quel stade de la procédure, des données complémentaires au demandeur sur la parenté entre le demandeur et le propriétaire du terrain ou le détenteur des droits réels sur le terrain. Le Fonds dispose de la possibilité de demander, à n'importe quel stade de la procédure, des données complémentaires au demandeur sur la validité de son lien juridique avec le demandeur et le propriétaire du terrain ou le détenteur des droits réels sur le terrain et sur la conformité au marché des indemnités basées sur ce lien juridique.</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 17,
                        "has_tables": True,
                        "generation_timestamp": "2025-08-19T14:05:18.294434"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<Inséré par AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 8, 016; En vigueur : 19-12-2011>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2011-11-10/07",
                        "article_number": "art. 8",
                        "sequence_number": "016",
                        "full_reference": "AGF [2011-11-10/07]"
                    },
                    "effective_date": "19-12-2011",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.8"
                    },
                    {
                    "footnote_number": "2",
                    "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 2, 022; En vigueur : 11-10-2018>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2018-07-06/25",
                        "article_number": "art. 2",
                        "sequence_number": "022",
                        "full_reference": "AGF [2018-07-06/25]"
                    },
                    "effective_date": "11-10-2018",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.2"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "2",
                    "text_position": 342,
                    "referenced_text": "une société de personnalité juridique telle que visée au Code des Sociétés, à l'exception d'une société coopérative agréée conformément à l'article 5 de la loi du 20 juillet 1955 portant institution d'un Conseil national de la Coopération,",
                    "embedded_law_references": [],
                    "bracket_pattern": "[2 une société de personnalité juridique telle que visée au Code des Sociétés, à l'exception d'une société coopérative agréée conformément à l'article 5 de la loi du 20 juillet 1955 portant institution d'un Conseil national de la Coopération,]2"
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE II. Promesse de subvention.",
            "metadata": {
                "title_type": "CHAPITRE II.",
                "title_content": "Promesse de subvention.",
                "rank": 2
            },
            "children": [
                {
                "type": "section",
                "label": "Section 1. Disposition générale.",
                "metadata": {
                    "title_type": "Section 1.",
                    "title_content": "Disposition générale.",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 3",
                    "metadata": {
                        "article_range": "3",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "3",
                        "anchor_id": "art_3",
                        "content": {
                        "main_text_raw": "Chaque demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement doit être adressée au Fonds, à l'exception de la demande dans la phase du plan stratégique en matière de soins, mentionnée à l'article 5, qui est introduite auprès de l'administration fonctionnellement compétente, mentionnée à l'article 5. Sous peine d'irrecevabilité, la demande doit être introduite par les organes compétents du demandeur.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-3\"><header class=\"article-header\"><h2 class=\"article-number\">Article 3</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"Chaque demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement doit être adressée au Fonds, à l'exception de la demande dans la phase du plan stratégique en matière de soins, mentionnée à l'article 5, qui est introduite auprès de l'administration fonctionnellement compétente, mentionnée à l'article 5.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.2\" data-article-dossier-number=\"\">Chaque demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement doit être adressée au Fonds, à l'exception de la demande dans la phase du plan stratégique en matière de soins, mentionnée à l'article 5, qui est introduite auprès de l'administration fonctionnellement compétente, mentionnée à l'article 5.</span>Sous peine d'irrecevabilité, la demande doit être introduite par les organes compétents<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.9\" data-article-dossier-number=\"\">du demandeur</span>.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.294608"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 2, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 2",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.2"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 9, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 9",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.9"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "1",
                        "text_position": 0,
                        "referenced_text": "Chaque demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement doit être adressée au Fonds, à l'exception de la demande dans la phase du plan stratégique en matière de soins, mentionnée à l'article 5, qui est introduite auprès de l'administration fonctionnellement compétente, mentionnée à l'article 5.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 Chaque demande d'octroi d'une subvention d'investissement ou d'une garantie d'investissement doit être adressée au Fonds, à l'exception de la demande dans la phase du plan stratégique en matière de soins, mentionnée à l'article 5, qui est introduite auprès de l'administration fonctionnellement compétente, mentionnée à l'article 5.]1"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 428,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 4",
                    "metadata": {
                        "article_range": "4",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "4",
                        "anchor_id": "art_4",
                        "content": {
                        "main_text_raw": "§ 1er. Toute demande d'obtention d'une promesse de subvention comporte: 1° pour les demandeurs autres que les demandeurs visés aux points 2° à 9° inclus: a) le procès-verbal signé de la réunion des organes compétents du demandeur contenant la décision de demander une subvention d'investissement et, le cas échéant, une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires, démontrant que le demandeur est une personne morale n'ayant aucun but lucratif; c) la demande d'approbation du plan maître; d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; 2° pour les hôpitaux généraux: a) le procès-verbal signé de la réunion des organes compétents du demandeur contenant la décision de demander une subvention d'investissement et, le cas échéant, une garantie d'investissement; b) les actes, statuts ou documents nécessaires démontrant que le demandeur est soit une administration locale ou provinciale, soit une association sans but lucratif ou une fondation d'intérêt public au sens de la loi du 27 juin 1921 relative aux associations sans but lucratif, aux associations internationales sans but lucratif et aux fondations, soit une société, contrôlée par la loi du 12 août 1911, octroyant la personnalité juridique aux universités de Bruxelles ou Louvain ou par le décret du 22 décembre 1995, portant modification de divers décrets relatifs à l' \" Universiteit Antwerpen \" et par le décret du 4 avril 2003 portant dispositions visant à créer une \" Universiteit Antwerpen \" et portant modification du décret du 22 décembre 1995 portant modification de divers décrets relatifs à l' \" Universiteit Antwerpen \"; c) la demande d'approbation du plan maître; d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; 3° pour les centres de soins de jour: a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises; c) la demande d'approbation du plan maître; d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; 4° pour les centres de services locaux: a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises; c) la demande d'approbation du plan maître; d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; [5° pour les structures d'aide à la jeunesse, les centres pour troubles du développement et les services autorisés de placement familial: a) le procès-verbal signé de la réunion des organes compétents du demandeur contenant la décision de demander une subvention d'investissement et, le cas échéant, une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires, faisant apparaître que le demandeur est une personne morale n'ayant aucun but lucratif; c) la demande d'approbation du plan stratégique des soins.] <AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 2, 003;**En vigueur:**01-01-2002> d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; 6° pour les emplacements d'accueil d'enfants visés à l'article 2, alinéa 1er, 3°, du décret du 20 avril 2012 portant organisation de l'accueil de bébés et de bambins: a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires démontrant que le demandeur est doté de la personnalité juridique à finalité sociale; c) la demande d'approbation du plan maître. d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; 7° pour les centres de court séjour de type 2: a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises; c) la demande d'approbation du plan maître; d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet; 8° pour les centres d'accueil de jour: a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires dont il ressort que le demandeur revêt une forme juridique, telle que visée à l'article 42, alinéa premier du Décret sur les soins résidentiels du 15 février 2019 ou telle que visée dans un arrêté d'exécution, visé à l'article 42, alinéa deux, du Décret sur les soins résidentiels du 15 février 2019; c) la demande d'approbation du plan maître; d) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet. 9° pour les centres de convalescence: a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises; c) la demande d'approbation du plan maître; d) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet. § 2....",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "pour les [3 demandeurs",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "à",
                            "sub_items": []
                            },
                            {
                            "number": "9°",
                            "text": "inclus",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "pour les hôpitaux généraux:",
                            "sub_items": []
                            },
                            {
                            "number": "3°",
                            "text": "[3",
                            "sub_items": []
                            },
                            {
                            "number": "4°",
                            "text": "[3",
                            "sub_items": []
                            },
                            {
                            "number": "5°",
                            "text": "pour [5",
                            "sub_items": []
                            },
                            {
                            "number": "6°",
                            "text": "pour les emplacements d'accueil d'enfants visés à l'article 2, alinéa 1er,",
                            "sub_items": []
                            },
                            {
                            "number": "7°",
                            "text": "pour les centres de court séjour de type 2:",
                            "sub_items": []
                            },
                            {
                            "number": "8°",
                            "text": "pour les centres d'accueil de jour:",
                            "sub_items": []
                            },
                            {
                            "number": "9°",
                            "text": "pour les centres de convalescence:",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-4\"><header class=\"article-header\"><h2 class=\"article-number\">Article 4</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p class=\"intro-text\">Toute demande d'obtention d'une promesse de subvention comporte: 1° pour les<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"demandeurs\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.10\" data-article-dossier-number=\"\">demandeurs</span>autres que les demandeurs visés aux points:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"9°\"><span class=\"provision-text\">inclus</span></li></ol><p class=\"intro-text\">: a) le procès-verbal signé de la réunion des organes compétents<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.10\" data-article-dossier-number=\"\">du demandeur</span>contenant la décision de demander une subvention d'investissement et, le cas échéant, une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires,\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.4\" data-article-dossier-number=\"\">la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires,</span>démontrant que<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.10\" data-article-dossier-number=\"\">le demandeur</span>est une personne morale n'ayant aucun but lucratif; c) la demande d'approbation du plan maître; d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet;:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">pour les hôpitaux généraux:</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">pour les emplacements d'accueil d'enfants visés à l'article 2, alinéa 1er,</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">pour les centres de court séjour de type 2:</span></li><li class=\"provision\" data-number=\"8°\"><span class=\"provision-text\">pour les centres d'accueil de jour:</span></li><li class=\"provision\" data-number=\"9°\"><span class=\"provision-text\">pour les centres de convalescence:</span></li></ol><p class=\"closing-text\">a) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement; b) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises; c) la demande d'approbation du plan maître; d) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet.</p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"6\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.3\" data-article-dossier-number=\"\">...</span></p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 2,
                            "provision_count": 11,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.297740"
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "standard",
                            "law_type": "AGF",
                            "dossier_number": "2002-04-19/45",
                            "article_number": "2",
                            "sequence_number": "003",
                            "effective_date": "01-01-2002",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945",
                            "full_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 2, 003;**En vigueur:**01-01-2002>",
                            "prefix": "",
                            "raw_dossier": "2002-04-19/45",
                            "raw_article": "2",
                            "start_pos": 3495,
                            "end_pos": 3651,
                            "matched_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 2, 003;**En vigueur:**01-01-2002>"
                            }
                        ]
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 3, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 3",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.3"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2009-07-24/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2009072426), art. 41, 009; En vigueur : 01-01-2010>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2009-07-24/26",
                            "article_number": "art. 41",
                            "sequence_number": "009",
                            "full_reference": "AGF [2009-07-24/26]"
                        },
                        "effective_date": "01-01-2010",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2009072426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2009072426#Art.41"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 10, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 10",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.10"
                        },
                        {
                        "footnote_number": "4",
                        "footnote_content": "(4)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 4, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 4",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.4"
                        },
                        {
                        "footnote_number": "5",
                        "footnote_content": "(5)<AGF [2014-09-05/12](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512), art. 2, 018; En vigueur : 13-11-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-09-05/12",
                            "article_number": "art. 2",
                            "sequence_number": "018",
                            "full_reference": "AGF [2014-09-05/12]"
                        },
                        "effective_date": "13-11-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512#Art.2"
                        },
                        {
                        "footnote_number": "6",
                        "footnote_content": "(6)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 3, 020; En vigueur : 20-03-2016>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-01-15/17",
                            "article_number": "art. 3",
                            "sequence_number": "020",
                            "full_reference": "AGF [2016-01-15/17]"
                        },
                        "effective_date": "20-03-2016",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.3"
                        },
                        {
                        "footnote_number": "7",
                        "footnote_content": "(7)<AGF [2016-11-18/10](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016111810), art. 1, 021; En vigueur : 01-01-2017>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-11-18/10",
                            "article_number": "art. 1",
                            "sequence_number": "021",
                            "full_reference": "AGF [2016-11-18/10]"
                        },
                        "effective_date": "01-01-2017",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016111810",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016111810#Art.1"
                        },
                        {
                        "footnote_number": "8",
                        "footnote_content": "(8)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 3, 022; En vigueur : 11-10-2018>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2018-07-06/25",
                            "article_number": "art. 3",
                            "sequence_number": "022",
                            "full_reference": "AGF [2018-07-06/25]"
                        },
                        "effective_date": "11-10-2018",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.3"
                        },
                        {
                        "footnote_number": "9",
                        "footnote_content": "(9)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 18,1°,2°, 025; En vigueur : 01-01-2020>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2019-12-13/06",
                            "article_number": "art. 18",
                            "sequence_number": "1°",
                            "full_reference": "AGF [2019-12-13/06]"
                        },
                        "effective_date": "01-01-2020",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.18"
                        },
                        {
                        "footnote_number": "10",
                        "footnote_content": "(10)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 18,4°, 025; En vigueur : 01-01-2020>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2019-12-13/06",
                            "article_number": "art. 18",
                            "sequence_number": "4°",
                            "full_reference": "AGF [2019-12-13/06]"
                        },
                        "effective_date": "01-01-2020",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.18"
                        },
                        {
                        "footnote_number": "11",
                        "footnote_content": "(11)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 18,5°, 025; En vigueur : 01-01-2020>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2019-12-13/06",
                            "article_number": "art. 18",
                            "sequence_number": "5°",
                            "full_reference": "AGF [2019-12-13/06]"
                        },
                        "effective_date": "01-01-2020",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.18"
                        },
                        {
                        "footnote_number": "12",
                        "footnote_content": "(12)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 18,6°, 025; En vigueur : 31-12-2025>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2019-12-13/06",
                            "article_number": "art. 18",
                            "sequence_number": "6°",
                            "full_reference": "AGF [2019-12-13/06]"
                        },
                        "effective_date": "31-12-2025",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.18"
                        },
                        {
                        "footnote_number": "13",
                        "footnote_content": "(13)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 2, 028; En vigueur : 20-09-2021>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2021-07-16/32",
                            "article_number": "art. 2",
                            "sequence_number": "028",
                            "full_reference": "AGF [2021-07-16/32]"
                        },
                        "effective_date": "20-09-2021",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.2"
                        },
                        {
                        "footnote_number": "14",
                        "footnote_content": "(14)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 1, 029; En vigueur : 12-08-2022>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2022-05-06/08",
                            "article_number": "art. 1",
                            "sequence_number": "029",
                            "full_reference": "AGF [2022-05-06/08]"
                        },
                        "effective_date": "12-08-2022",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.1"
                        },
                        {
                        "footnote_number": "15",
                        "footnote_content": "(15)<AGF [2024-06-21/21](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121), art. 2, 032; En vigueur : 01-04-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-06-21/21",
                            "article_number": "art. 2",
                            "sequence_number": "032",
                            "full_reference": "AGF [2024-06-21/21]"
                        },
                        "effective_date": "01-04-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121#Art.2"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "3",
                        "text_position": 87,
                        "referenced_text": "demandeurs",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 demandeurs]3"
                        },
                        {
                        "reference_number": "9",
                        "text_position": 103,
                        "referenced_text": "autres que les demandeurs visés aux points 2° à 9° inclus",
                        "embedded_law_references": [],
                        "bracket_pattern": "[9 autres que les demandeurs visés aux points 2° à 9° inclus]9"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 233,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 du demandeur]3"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 453,
                        "referenced_text": "la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires,",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires,]4"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 710,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 921,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 du demandeur]3"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 1124,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 le demandeur]3"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 1908,
                        "referenced_text": "la demande d'approbation du plan maître ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 la demande d'approbation du plan maître ;]8"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 1957,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "9",
                        "text_position": 2078,
                        "referenced_text": "pour les centres de soins de jour :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[9 pour les centres de soins de jour :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;]9"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 2446,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "10",
                        "text_position": 2567,
                        "referenced_text": "pour les centres de services locaux :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[10 pour les centres de services locaux :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;]10"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 2936,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "13",
                        "text_position": 3063,
                        "referenced_text": "les structures d'aide à la jeunesse, les centres pour troubles du développement",
                        "embedded_law_references": [],
                        "bracket_pattern": "[13 les structures d'aide à la jeunesse, les centres pour troubles du développement]13"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 3269,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 du demandeur]3"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 3409,
                        "referenced_text": "la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires,",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires,]4"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 3558,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 le demandeur]3"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 3850,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "7",
                        "text_position": 3964,
                        "referenced_text": "6° pour les emplacements d'accueil d'enfants visés à l'article 2, alinéa 1er, 3°, du décret du 20 avril 2012 portant organisation de l'accueil de bébés et de bambins :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires démontrant que le demandeur est doté de la personnalité juridique à finalité sociale ;  \nc) la demande d'approbation du plan maître.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[7 6° pour les emplacements d'accueil d'enfants visés à l'article 2, alinéa 1er, 3°, du décret du 20 avril 2012 portant organisation de l'accueil de bébés et de bambins :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires démontrant que le demandeur est doté de la personnalité juridique à finalité sociale ;  \nc) la demande d'approbation du plan maître.]7"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 4592,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "11",
                        "text_position": 4706,
                        "referenced_text": "7° pour les centres de court séjour de type 2 :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[11 7° pour les centres de court séjour de type 2 :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;]11"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 5085,
                        "referenced_text": "d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) la preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet ;]14"
                        },
                        {
                        "reference_number": "11",
                        "text_position": 5199,
                        "referenced_text": "8° pour les centres d'accueil de jour :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires dont il ressort que le demandeur revêt une forme juridique, telle que visée à l'article 42, alinéa premier du Décret sur les soins résidentiels du 15 février 2019 ou telle que visée dans un arrêté d'exécution, visé à l'article 42, alinéa deux, du Décret sur les soins résidentiels du 15 février 2019 ;  \nc) la demande d'approbation du plan maître;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[11 8° pour les centres d'accueil de jour :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ou les actes, statuts ou documents nécessaires dont il ressort que le demandeur revêt une forme juridique, telle que visée à l'article 42, alinéa premier du Décret sur les soins résidentiels du 15 février 2019 ou telle que visée dans un arrêté d'exécution, visé à l'article 42, alinéa deux, du Décret sur les soins résidentiels du 15 février 2019 ;  \nc) la demande d'approbation du plan maître;]11"
                        },
                        {
                        "reference_number": "14",
                        "text_position": 5916,
                        "referenced_text": "d) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[14 d) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet.]14"
                        },
                        {
                        "reference_number": "15",
                        "text_position": 6035,
                        "referenced_text": "9° pour les centres de convalescence :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;  \nd) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[15 9° pour les centres de convalescence :  \na) le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander une subvention d'investissement et éventuellement une garantie d'investissement ;  \nb) la mention du numéro d'entreprise de la Banque-Carrefour des Entreprises ;  \nc) la demande d'approbation du plan maître ;  \nd) une preuve d'une demande recevable du permis d'urbanisme ou du permis d'environnement pour le projet.]15"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 6521,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 ...]6"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 2. Procédure.",
                "metadata": {
                    "title_type": "Section 2.",
                    "title_content": "Procédure.",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "sous-section",
                    "label": "Sous-section A. <AGF 2002-04-19,45, art. 3, 003;**En vigueur :**01-01-2002> Procédure spécifique pour [2 ...]2 [1] [3 les structures d'aide à la jeunesse, les centres pour troubles du développement]3 et les services autorisés de placement familial][1].",
                    "metadata": {
                        "title_type": "Sous-section A.",
                        "title_content": "<AGF 2002-04-19,45, art. 3, 003;**En vigueur :**01-01-2002> Procédure spécifique pour [2 ...]2 [1] [3 les structures d'aide à la jeunesse, les centres pour troubles du développement]3 et les services autorisés de placement familial][1].",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 5",
                        "metadata": {
                            "article_range": "5",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "5",
                            "anchor_id": "art_5",
                            "content": {
                            "main_text_raw": "Pour... Les structures d'aide à la jeunesse, les centres pour troubles du développement et les services autorisés de placement familial, la demande d'obtention d'une promesse de subvention comporte deux phases. Dans une première phase, le demandeur doit présenter pour approbation un plan définissant les aspects de soins stratégiques du plan maître.... les structures d'aide à la jeunesse, les centres pour troubles du développement et les services autorisés de placement familial introduisent ce plan auprès de l'agence autonomisée interne \" Grandir Régie \". <AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 4, 003;**En vigueur:**01-01-2002> La demande d'approbation du plan stratégique des soins comporte: 1° le procès-verbal signé de la réunion des organes compétents du demandeur contenant la décision d'approuver et de déposer le plan stratégique des soins...; 2° le plan stratégique des soins. Le plan stratégique des soins définit au moins: a) la situation actuelle en termes d'offre de soins, d'infrastructure, de localisation et de partenariats; b) les perspectives concernant les mêmes éléments, le rôle à jouer dans la région; c) les arguments permettant d'étayer l'opportunité et la faisabilité de ces perspectives sur la base d'une analyse approfondie du milieu comportant une projection des besoins en soins et de l'offre de soins, une adéquation avec d'autres prestataires de soins dans le domaine pertinent et une auto-évaluation approfondie de la position du demandeur; d) les conditions à remplir pour réaliser les perspectives; e) une description de l'ensemble des investissements que le demandeur souhaite faire dans les dix ans à venir avec mention du groupe-cible et de la capacité planifiée par élément. alinéa 4 abrogé",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "le procès-verbal signé de la réunion des organes compétents [2 du demandeur",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le plan stratégique des soins.",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-5\"><header class=\"article-header\"><h2 class=\"article-number\">Article 5</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Pour<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.5\" data-article-dossier-number=\"\">...</span><span class=\"footnote-ref\" data-footnote-id=\"6\" data-referenced-text=\"Les structures d'aide à la jeunesse, les centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021071632#Art.4\" data-article-dossier-number=\"\">Les structures d'aide à la jeunesse, les centres pour troubles du développement</span><span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et les services autorisés de placement familial\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014090512#Art.4\" data-article-dossier-number=\"\">et les services autorisés de placement familial</span>, la demande d'obtention d'une promesse de subvention comporte deux phases. Dans une première phase,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.11\" data-article-dossier-number=\"\">le demandeur</span>doit présenter pour approbation un plan définissant les aspects de soins stratégiques du plan maître....<span class=\"footnote-ref\" data-footnote-id=\"6\" data-referenced-text=\"les structures d'aide à la jeunesse, les centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021071632#Art.4\" data-article-dossier-number=\"\">les structures d'aide à la jeunesse, les centres pour troubles du développement</span>et les services autorisés de placement familial introduisent ce plan auprès de l'agence autonomisée interne<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"&quot; Grandir Régie &quot;\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021031210#Art.3\" data-article-dossier-number=\"\">&quot; Grandir Régie &quot;</span>.<span class=\"legal-citation legal-citation-standard\" data-citation-type=\"standard\" data-dossier-number=\"2002-04-19/45\" data-article-number=\"4\" data-law-type=\"AGF\" data-effective-date=\"01-01-2002\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2002041945\">&lt;AGF 2002-04-19/45, art. 4, 003; En vigueur : 01-01-2002&gt;</span>La demande d'approbation du plan stratégique des soins comporte:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">le procès-verbal signé de la réunion des organes compétents [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.11\" data-article-dossier-number=\"\">du demandeur</span></span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le plan stratégique des soins.</span></li></ol><p class=\"closing-text\">..; 2° le plan stratégique des soins. Le plan stratégique des soins définit au moins: a) la situation actuelle en termes d'offre de soins, d'infrastructure, de localisation et de partenariats; b) les perspectives concernant les mêmes éléments, le rôle à jouer dans la région; c) les arguments permettant d'étayer l'opportunité et la faisabilité de ces perspectives sur la base d'une analyse approfondie du milieu comportant une projection des besoins en soins et de l'offre de soins, une adéquation avec d'autres prestataires de soins dans le domaine pertinent et une auto-évaluation approfondie de la position du demandeur; d) les conditions à remplir pour réaliser les perspectives; e) une description de l'ensemble des investissements que le demandeur souhaite faire dans les dix ans à venir avec mention du groupe-cible et de la capacité planifiée par élément. alinéa 4 abrogé</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 2,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.298421"
                            },
                            "enhanced_citations": [
                                {
                                "citation_type": "standard",
                                "law_type": "AGF",
                                "dossier_number": "2002-04-19/45",
                                "article_number": "4",
                                "sequence_number": "003",
                                "effective_date": "01-01-2002",
                                "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945",
                                "full_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 4, 003;**En vigueur:**01-01-2002>",
                                "prefix": "",
                                "raw_dossier": "2002-04-19/45",
                                "raw_article": "4",
                                "start_pos": 561,
                                "end_pos": 717,
                                "matched_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 4, 003;**En vigueur:**01-01-2002>"
                                }
                            ]
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 4, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 4",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.4"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 11, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 11",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.11"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2014-09-05/12](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512), art. 4, 018; En vigueur : 13-11-2014>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2014-09-05/12",
                                "article_number": "art. 4",
                                "sequence_number": "018",
                                "full_reference": "AGF [2014-09-05/12]"
                            },
                            "effective_date": "13-11-2014",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512#Art.4"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 5, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 5",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.5"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2021-03-12/10](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021031210), art. 3, 027; En vigueur : 18-04-2019>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2021-03-12/10",
                                "article_number": "art. 3",
                                "sequence_number": "027",
                                "full_reference": "AGF [2021-03-12/10]"
                            },
                            "effective_date": "18-04-2019",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021031210",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021031210#Art.3"
                            },
                            {
                            "footnote_number": "6",
                            "footnote_content": "(6)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 4, 028; En vigueur : 20-09-2021>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2021-07-16/32",
                                "article_number": "art. 4",
                                "sequence_number": "028",
                                "full_reference": "AGF [2021-07-16/32]"
                            },
                            "effective_date": "20-09-2021",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.4"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "4",
                            "text_position": 5,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "6",
                            "text_position": 18,
                            "referenced_text": "Les structures d'aide à la jeunesse, les centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[6 Les structures d'aide à la jeunesse, les centres pour troubles du développement]6"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 255,
                            "referenced_text": "le demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 le demandeur]2"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 379,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "6",
                            "text_position": 388,
                            "referenced_text": "les structures d'aide à la jeunesse, les centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[6 les structures d'aide à la jeunesse, les centres pour troubles du développement]6"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 473,
                            "referenced_text": "et les services autorisés de placement familial",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 et les services autorisés de placement familial]3"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 586,
                            "referenced_text": "\" Grandir Régie \"",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 \" Grandir Régie \"]5"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 905,
                            "referenced_text": "du demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 du demandeur]2"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 1001,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 1629,
                            "referenced_text": "du demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 du demandeur]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 1769,
                            "referenced_text": "le demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 le demandeur]2"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 1899,
                            "referenced_text": "alinéa 4 abrogé",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 alinéa 4 abrogé]1"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 6",
                        "metadata": {
                            "article_range": "6",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "6",
                            "anchor_id": "art_6",
                            "content": {
                            "main_text_raw": "Pour l'établissement du plan stratégique en matière de soins, le demandeur doit faire usage des modèles mis à la disposition par l'administration fonctionnellement compétente. Le demandeur peut faire usage des données mises à la disposition par l'administration fonctionnellement compétente. L'administration fonctionnellement compétente peut demander des renseignements supplémentaires au demandeur. Dans les quatorze jours calendaires de la réception de la demande d'approbation du plan stratégique en matière de soins, l'administration fonctionnellement compétente envoie un accusé de réception au demandeur, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La date de recevabilité est la date de réception de la demande recevable. Une demande est recevable si les conditions suivantes sont remplies: 1°... 2° la demande contient les pièces nécessaires, mentionnées à l'article 4, § 1er, 5°, et les pièces, mentionnées à l'article 5; 3° à l'élaboration du plan stratégique en matière de soins les modèles, mentionnés à l'alinéa premier, ont été utilisés.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "[4...",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "la demande contient les pièces nécessaires, mentionnées à l'article 4, § 1er, [3",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "à l'élaboration du plan stratégique en matière de soins les modèles, mentionnés à l'alinéa premier, ont été utilisés.",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-6\"><header class=\"article-header\"><h2 class=\"article-number\">Article 6</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Pour l'établissement du plan stratégique en matière de soins, le demandeur doit faire usage des modèles mis à la disposition par l'administration fonctionnellement compétente. Le demandeur peut faire usage des données mises à la disposition par l'administration fonctionnellement compétente. L'administration fonctionnellement compétente peut demander des renseignements supplémentaires au demandeur. Dans les quatorze jours calendaires de la réception de la demande d'approbation du plan stratégique en matière de soins, l'administration fonctionnellement compétente envoie un accusé de réception au demandeur, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La date de recevabilité est la date de réception de la demande recevable. Une demande est recevable si les conditions suivantes sont remplies:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">[4<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.4\" data-article-dossier-number=\"\">...</span></span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">la demande contient les pièces nécessaires, mentionnées à l'article 4, § 1er, [3</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">à l'élaboration du plan stratégique en matière de soins les modèles, mentionnés à l'alinéa premier, ont été utilisés.</span></li></ol></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 3,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.298836"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 4, 022; En vigueur : 11-10-2018>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-07-06/25",
                                "article_number": "art. 4",
                                "sequence_number": "022",
                                "full_reference": "AGF [2018-07-06/25]"
                            },
                            "effective_date": "11-10-2018",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.4"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 186,
                            "referenced_text": "Le demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 Le demandeur]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 353,
                            "referenced_text": "peut",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 peut]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 407,
                            "referenced_text": "au demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 au demandeur]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 625,
                            "referenced_text": "au demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 au demandeur]2"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 894,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 986,
                            "referenced_text": "5°",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 5°]3"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 7",
                        "metadata": {
                            "article_range": "7",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "7",
                            "anchor_id": "art_7",
                            "content": {
                            "main_text_raw": "L'administration fonctionnellement compétente établit une note d'évaluation. Dans les quarante jours calendaires de la date de recevabilité, l'administration fonctionnellement compétente transmet la note d'évaluation au demandeur. Le demandeur dispose d'un délai de quarante jours calendaires, à compter de la réception de la note d'évaluation, pour introduire une note de réaction auprès de l'administration fonctionnellement compétente ou pour annoncer à l'administration fonctionnellement compétente qu'il effectuera une adaptation approfondie de son plan stratégique en matière de soins. Lorsque le demandeur décide d'adapter le plan stratégique en matière de soins de manière approfondie, la procédure recommence depuis le début.",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-7\"><header class=\"article-header\"><h2 class=\"article-number\">Article 7</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>L'administration fonctionnellement compétente établit une note d'évaluation. Dans les quarante jours calendaires de la date de recevabilité,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"l'administration fonctionnellement compétente transmet la note d'évaluation au demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.5\" data-article-dossier-number=\"\">l'administration fonctionnellement compétente transmet la note d'évaluation au demandeur</span>. Le demandeur dispose d'un délai de quarante jours calendaires, à compter de la réception de la note d'évaluation, pour introduire une note de réaction auprès de l'administration fonctionnellement compétente ou pour annoncer à l'administration fonctionnellement compétente qu'il effectuera une adaptation approfondie de son plan stratégique en matière de soins. Lorsque le demandeur décide d'adapter le plan stratégique en matière de soins de manière approfondie, la procédure recommence depuis le début.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.299033"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 6, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 6",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.6"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 13, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 13",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.13"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 5, 017; En vigueur : 25-04-2014>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2014-02-14/26",
                                "article_number": "art. 5",
                                "sequence_number": "017",
                                "full_reference": "AGF [2014-02-14/26]"
                            },
                            "effective_date": "25-04-2014",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.5"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "3",
                            "text_position": 145,
                            "referenced_text": "l'administration fonctionnellement compétente transmet la note d'évaluation au demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 l'administration fonctionnellement compétente transmet la note d'évaluation au demandeur]3"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 8",
                        "metadata": {
                            "article_range": "8",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "8",
                            "anchor_id": "art_8",
                            "content": {
                            "main_text_raw": "Dans les quinze jours calendrier de la réception de la note de réaction, ou, à défaut de note de réaction dans le délai imparti, dans les quinze jours calendrier de l'expiration de ce délai, l'administration fonctionnellement compétente fait parvenir le dossier concerné... à la Commission de la stratégie des soins pour Les structures d'aide à la jeunesse, les centres pour troubles du développement et les services autorisés de placement familial. La commission compétente inscrit le dossier à l'ordre du jour. Le dossier contient le plan stratégique des soins introduit, la note d'évaluation et la note de réaction éventuelle. <AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 6, 003;**En vigueur:**01-01-2002>",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-8\"><header class=\"article-header\"><h2 class=\"article-number\">Article 8</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Dans les quinze jours calendrier de la réception de la note de réaction, ou, à défaut de note de réaction dans le délai imparti, dans les quinze jours calendrier de l'expiration de ce délai,<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"l'administration fonctionnellement compétente\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.7\" data-article-dossier-number=\"\">l'administration fonctionnellement compétente</span>fait parvenir le dossier concerné<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.7\" data-article-dossier-number=\"\">...</span>à la Commission de la stratégie des soins pour<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"Les structures d'aide à la jeunesse, les centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021071632#Art.5\" data-article-dossier-number=\"\">Les structures d'aide à la jeunesse, les centres pour troubles du développement</span>et les services autorisés de placement familial.<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"La commission compétente inscrit le dossier à l'ordre du jour.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.7\" data-article-dossier-number=\"\">La commission compétente inscrit le dossier à l'ordre du jour.</span>Le dossier contient le plan stratégique des soins introduit,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"la note d'évaluation\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.14\" data-article-dossier-number=\"\">la note d'évaluation</span>et la note de réaction éventuelle.<span class=\"legal-citation legal-citation-standard\" data-citation-type=\"standard\" data-dossier-number=\"2002-04-19/45\" data-article-number=\"6\" data-law-type=\"AGF\" data-effective-date=\"01-01-2002\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2002041945\">&lt;AGF 2002-04-19/45, art. 6, 003; En vigueur : 01-01-2002&gt;</span></p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.299280"
                            },
                            "enhanced_citations": [
                                {
                                "citation_type": "standard",
                                "law_type": "AGF",
                                "dossier_number": "2002-04-19/45",
                                "article_number": "6",
                                "sequence_number": "003",
                                "effective_date": "01-01-2002",
                                "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945",
                                "full_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 6, 003;**En vigueur:**01-01-2002>",
                                "prefix": "",
                                "raw_dossier": "2002-04-19/45",
                                "raw_article": "6",
                                "start_pos": 630,
                                "end_pos": 786,
                                "matched_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 6, 003;**En vigueur:**01-01-2002>"
                                }
                            ]
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 7, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 7",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.7"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 14, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 14",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.14"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2014-09-05/12](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512), art. 5, 018; En vigueur : 13-11-2014>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2014-09-05/12",
                                "article_number": "art. 5",
                                "sequence_number": "018",
                                "full_reference": "AGF [2014-09-05/12]"
                            },
                            "effective_date": "13-11-2014",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512#Art.5"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 7, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 7",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.7"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 5, 028; En vigueur : 20-09-2021>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2021-07-16/32",
                                "article_number": "art. 5",
                                "sequence_number": "028",
                                "full_reference": "AGF [2021-07-16/32]"
                            },
                            "effective_date": "20-09-2021",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.5"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "1",
                            "text_position": 191,
                            "referenced_text": "l'administration fonctionnellement compétente",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 l'administration fonctionnellement compétente]1"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 276,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 336,
                            "referenced_text": "Les structures d'aide à la jeunesse, les centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 Les structures d'aide à la jeunesse, les centres pour troubles du développement]5"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 474,
                            "referenced_text": "La commission compétente inscrit le dossier à l'ordre du jour.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 La commission compétente inscrit le dossier à l'ordre du jour.]1"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 603,
                            "referenced_text": "la note d'évaluation",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 la note d'évaluation]2"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 9",
                        "metadata": {
                            "article_range": "9",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "9",
                            "anchor_id": "art_9",
                            "content": {
                            "main_text_raw": "Au sein des [...] Commissions de la stratégie des soins, visées à l'article 8, siègent trois membres internes et trois membres externes. <AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 7, 003;**En vigueur:**01-01-2002> Les trois membres internes appartiennent au Département Soin... par une agence du domaine politique de l'Aide Sociale, de la Santé publique et de la Famille et sont désignés par le Ministre.... Au sein de la Commission de la Stratégie des soins pour les structures d'aide à la jeunesse, les centres pour troubles du développement et les services autorisés de placement familial, un membre externe appartient au conseil consultatif compétent pour le traitement de recours ou de moyens de défense en matière d'agrément des structures d'aide à la jeunesse, en matière d'agrément des centres pour troubles du développemen ou en matière d'autorisation de services de placement familial. Deux membres externes sont désignés en raison de leur expertise en matière de l'aide à la jeunesse, en matière des centres pour troubles du développement ou en matière de placement familial. En fonction des dossiers à traiter lors des réunions des [...] Commissions de la stratégie des soins, les membres externes sont désignés sur une liste approuvée par le Ministre. <AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 7, 003;**En vigueur:**01-01-2002> Les Commissions de la stratégie des soins établissent un règlement d'ordre intérieur réglant le fonctionnement, la désignation des membres externes et les incompatibilités. Le Ministre approuve le règlement d'ordre intérieur. L'administration fonctionnellement compétente assure le secrétariat des Commissions de la stratégie des soins. L'administration fonctionnellement compétente fournit aux Commissions de la stratégie des soins les renseignements nécessaires à son fonctionnement.",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-9\"><header class=\"article-header\"><h2 class=\"article-number\">Article 9</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Au sein des [<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.15\" data-article-dossier-number=\"\">...</span>] Commissions de la stratégie des soins, visées à l'article 8, siègent trois membres internes et trois membres externes.<span class=\"legal-citation legal-citation-standard\" data-citation-type=\"standard\" data-dossier-number=\"2002-04-19/45\" data-article-number=\"7\" data-law-type=\"AGF\" data-effective-date=\"01-01-2002\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2002041945\">&lt;AGF 2002-04-19/45, art. 7, 003; En vigueur : 01-01-2002&gt;</span>Les trois membres internes appartiennent<span class=\"footnote-ref\" data-footnote-id=\"7\" data-referenced-text=\"au Département Soin\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023051209#Art.23\" data-article-dossier-number=\"\">au Département Soin</span>...<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"par une agence du domaine politique de l'Aide Sociale, de la Santé publique et de la Famille\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.8\" data-article-dossier-number=\"\">par une agence du domaine politique de l'Aide Sociale, de la Santé publique et de la Famille</span>et sont désignés par le Ministre.... Au sein de la Commission de la Stratégie des soins<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"pour les structures d'aide à la jeunesse, les centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.8\" data-article-dossier-number=\"\">pour les structures d'aide à la jeunesse, les centres pour troubles du développement</span>et les services autorisés de placement familial, un membre externe appartient au conseil consultatif compétent pour le traitement de recours ou de moyens de défense<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"en matière d'agrément des structures d'aide à la jeunesse, en matière d'agrément des centres pour troubles du développemen\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.8\" data-article-dossier-number=\"\">en matière d'agrément des structures d'aide à la jeunesse, en matière d'agrément des centres pour troubles du développemen</span>ou en matière d'autorisation de services de placement familial. Deux membres externes sont désignés en raison de leur expertise<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"en matière de l'aide à la jeunesse, en matière des centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.8\" data-article-dossier-number=\"\">en matière de l'aide à la jeunesse, en matière des centres pour troubles du développement</span>ou en matière de placement familial. En fonction des dossiers à traiter lors des réunions des [...] Commissions de la stratégie des soins, les membres externes sont désignés sur une liste approuvée par le Ministre.<span class=\"legal-citation legal-citation-standard\" data-citation-type=\"standard\" data-dossier-number=\"2002-04-19/45\" data-article-number=\"7\" data-law-type=\"AGF\" data-effective-date=\"01-01-2002\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2002041945\">&lt;AGF 2002-04-19/45, art. 7, 003; En vigueur : 01-01-2002&gt;</span>Les Commissions de la stratégie des soins établissent un règlement d'ordre intérieur réglant le fonctionnement, la désignation des membres externes et les incompatibilités. Le Ministre approuve le règlement d'ordre intérieur.<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"L'administration fonctionnellement compétente\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.8\" data-article-dossier-number=\"\">L'administration fonctionnellement compétente</span>assure le secrétariat des Commissions de la stratégie des soins. L'administration fonctionnellement compétente fournit aux Commissions de la stratégie des soins les renseignements nécessaires à son fonctionnement.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.299681"
                            },
                            "enhanced_citations": [
                                {
                                "citation_type": "standard",
                                "law_type": "AGF",
                                "dossier_number": "2002-04-19/45",
                                "article_number": "7",
                                "sequence_number": "003",
                                "effective_date": "01-01-2002",
                                "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945",
                                "full_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 7, 003;**En vigueur:**01-01-2002>",
                                "prefix": "",
                                "raw_dossier": "2002-04-19/45",
                                "raw_article": "7",
                                "start_pos": 137,
                                "end_pos": 293,
                                "matched_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 7, 003;**En vigueur:**01-01-2002>"
                                },
                                {
                                "citation_type": "standard",
                                "law_type": "AGF",
                                "dossier_number": "2002-04-19/45",
                                "article_number": "7",
                                "sequence_number": "003",
                                "effective_date": "01-01-2002",
                                "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945",
                                "full_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 7, 003;**En vigueur:**01-01-2002>",
                                "prefix": "",
                                "raw_dossier": "2002-04-19/45",
                                "raw_article": "7",
                                "start_pos": 1345,
                                "end_pos": 1501,
                                "matched_text": "<AGF [2002-04-19/45](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2002041945), art. 7, 003;**En vigueur:**01-01-2002>"
                                }
                            ]
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 8, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 8",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.8"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 15, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 15",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.15"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2014-09-05/12](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512), art. 6, 018; En vigueur : 13-11-2014>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2014-09-05/12",
                                "article_number": "art. 6",
                                "sequence_number": "018",
                                "full_reference": "AGF [2014-09-05/12]"
                            },
                            "effective_date": "13-11-2014",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512#Art.6"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 8, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 8",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.8"
                            },
                            {
                            "footnote_number": "6",
                            "footnote_content": "(6)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 6, 028; En vigueur : 20-09-2021>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2021-07-16/32",
                                "article_number": "art. 6",
                                "sequence_number": "028",
                                "full_reference": "AGF [2021-07-16/32]"
                            },
                            "effective_date": "20-09-2021",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.6"
                            },
                            {
                            "footnote_number": "7",
                            "footnote_content": "(7)<AGF [2023-05-12/09](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023051209), art. 23, 031; En vigueur : 10-07-2023>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2023-05-12/09",
                                "article_number": "art. 23",
                                "sequence_number": "031",
                                "full_reference": "AGF [2023-05-12/09]"
                            },
                            "effective_date": "10-07-2023",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023051209",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023051209#Art.23"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "7",
                            "text_position": 338,
                            "referenced_text": "au Département Soin",
                            "embedded_law_references": [],
                            "bracket_pattern": "[7 au Département Soin]7"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 363,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 ...]2"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 372,
                            "referenced_text": "par une agence du domaine politique de l'Aide Sociale, de la Santé publique et de la Famille",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 par une agence du domaine politique de l'Aide Sociale, de la Santé publique et de la Famille]1"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 506,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 572,
                            "referenced_text": "pour les structures d'aide à la jeunesse, les centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 pour les structures d'aide à la jeunesse, les centres pour troubles du développement]5"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 827,
                            "referenced_text": "en matière d'agrément des structures d'aide à la jeunesse, en matière d'agrément des centres pour troubles du développemen",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 en matière d'agrément des structures d'aide à la jeunesse, en matière d'agrément des centres pour troubles du développemen]5"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 1083,
                            "referenced_text": "en matière de l'aide à la jeunesse, en matière des centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 en matière de l'aide à la jeunesse, en matière des centres pour troubles du développement]5"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 1786,
                            "referenced_text": "L'administration fonctionnellement compétente",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 L'administration fonctionnellement compétente]1"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 1902,
                            "referenced_text": "L'administration fonctionnellement compétente",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 L'administration fonctionnellement compétente]1"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 10",
                        "metadata": {
                            "article_range": "10",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "10",
                            "anchor_id": "art_10",
                            "content": {
                            "main_text_raw": "La Commission de la stratégie des soins visées à l'article 8 a pour mission de conseiller le Ministre sur les plans stratégiques des soins introduits. alinéa 2 abrogé",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-10\"><header class=\"article-header\"><h2 class=\"article-number\">Article 10</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"La Commission\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.9\" data-article-dossier-number=\"\">La Commission</span>de la stratégie des soins visées à l'article 8 a pour mission de conseiller le Ministre sur les plans stratégiques des soins introduits.<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"alinéa 2 abrogé\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.9\" data-article-dossier-number=\"\">alinéa 2 abrogé</span></p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.299820"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 9, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 9",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.9"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 9, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 9",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.9"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 0,
                            "referenced_text": "La Commission",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 La Commission]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 66,
                            "referenced_text": "a",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 a]2"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 163,
                            "referenced_text": "alinéa 2 abrogé",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 alinéa 2 abrogé]1"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 11",
                        "metadata": {
                            "article_range": "11",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "11",
                            "anchor_id": "art_11",
                            "content": {
                            "main_text_raw": "L'avis de la Commission de la Stratégie des soins, ensemble avec le plan en matière de soins soumis, la note d'évaluation et l'éventuelle note de réaction, est envoyé au ministre dans les quinze jours calendaires de l'avis rendu. Le Ministre prend une décision d'approbation complète ou partielle ou de désapprobation du plan stratégique en matière de soins dans les quinze jours calendaires de la réception de l'avis de la Commission de la Stratégie des soins. La décision du ministre est communiquée au Fonds par l'administration fonctionnellement compétente et elle est envoyée... au demandeur.",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-11\"><header class=\"article-header\"><h2 class=\"article-number\">Article 11</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>L'avis de la Commission de la Stratégie des soins, ensemble avec le plan en matière de soins soumis,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"la note d'évaluation\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.16\" data-article-dossier-number=\"\">la note d'évaluation</span>et l'éventuelle note de réaction, est envoyé au ministre dans les quinze jours calendaires de l'avis rendu. Le Ministre prend une décision d'approbation complète ou partielle ou de désapprobation du plan stratégique en matière de soins dans les quinze jours calendaires de la réception de l'avis de la Commission de la Stratégie des soins. La décision du ministre est communiquée au Fonds par l'administration fonctionnellement compétente et elle est envoyée<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.6\" data-article-dossier-number=\"\">...</span><span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"au demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.16\" data-article-dossier-number=\"\">au demandeur</span>.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.300040"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 10, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 10",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.10"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 16, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 16",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.16"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 6, 017; En vigueur : 25-04-2014>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2014-02-14/26",
                                "article_number": "art. 6",
                                "sequence_number": "017",
                                "full_reference": "AGF [2014-02-14/26]"
                            },
                            "effective_date": "25-04-2014",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.6"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 105,
                            "referenced_text": "la note d'évaluation",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 la note d'évaluation]2"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 590,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 ...]3"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 599,
                            "referenced_text": "au demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 au demandeur]2"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 12",
                        "metadata": {
                            "article_range": "12",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "12",
                            "anchor_id": "art_12",
                            "content": {
                            "main_text_raw": "L'indemnité accordée aux membres externes visés à l'article 9, est déterminée par le ministre et est à charge de l'administration fonctionnellement compétente.",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-12\"><header class=\"article-header\"><h2 class=\"article-number\">Article 12</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>L'indemnité accordée aux membres externes visés à l'article 9, est déterminée par le ministre et est à charge<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"de l'administration fonctionnellement compétente\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.11\" data-article-dossier-number=\"\">de l'administration fonctionnellement compétente</span>.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.300152"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 11, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 11",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.11"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "1",
                            "text_position": 110,
                            "referenced_text": "de l'administration fonctionnellement compétente",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 de l'administration fonctionnellement compétente]1"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 13",
                        "metadata": {
                            "article_range": "13",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "13",
                            "anchor_id": "art_13",
                            "content": {
                            "main_text_raw": "Après approbation du plan stratégique des soins, le demandeur peut, dans la deuxième phase de sa demande d'obtention d'une promesse de subvention, soumettre pour approbation au Fonds l'aspect technique et financier du plan maître, conformément aux articles 15 à 16 inclus.......",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-13\"><header class=\"article-header\"><h2 class=\"article-number\">Article 13</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Après approbation du plan stratégique des soins,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.17\" data-article-dossier-number=\"\">le demandeur</span>peut, dans la deuxième phase de sa demande d'obtention d'une promesse de subvention, soumettre pour approbation<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"au Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.12\" data-article-dossier-number=\"\">au Fonds</span>l'aspect technique et financier du plan maître, conformément aux articles 15 à<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"16\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.10\" data-article-dossier-number=\"\">16</span>inclus<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.7\" data-article-dossier-number=\"\">...</span>....</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.300317"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 12, 006; En vigueur : 03-10-2008>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2008-05-30/39",
                                "article_number": "art. 12",
                                "sequence_number": "006",
                                "full_reference": "AGF [2008-05-30/39]"
                            },
                            "effective_date": "03-10-2008",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.12"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 17, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 17",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.17"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 7, 017; En vigueur : 25-04-2014>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2014-02-14/26",
                                "article_number": "art. 7",
                                "sequence_number": "017",
                                "full_reference": "AGF [2014-02-14/26]"
                            },
                            "effective_date": "25-04-2014",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.7"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 10, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 10",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.10"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 49,
                            "referenced_text": "le demandeur",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 le demandeur]2"
                            },
                            {
                            "reference_number": "1",
                            "text_position": 179,
                            "referenced_text": "au Fonds",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 au Fonds]1"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 272,
                            "referenced_text": "16",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 16]4"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 288,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 ...]3"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 297,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "type": "sous-section",
                    "label": "Sous-section B. Procédure ordinaire.",
                    "metadata": {
                        "title_type": "Sous-section B.",
                        "title_content": "Procédure ordinaire.",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 14",
                        "metadata": {
                            "article_range": "14",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "14",
                            "anchor_id": "art_14",
                            "content": {
                            "main_text_raw": "Les demandeurs qui ne relèvent pas de l'application des articles 5 à 13 inclus, introduisent un plan maître complet.",
                            "numbered_provisions": [],
                            "main_text": "<article class=\"legal-article\" id=\"art-14\"><header class=\"article-header\"><h2 class=\"article-number\">Article 14</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Les<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"demandeurs\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.18\" data-article-dossier-number=\"\">demandeurs</span>qui ne relèvent pas de l'application des articles 5 à 13 inclus, introduisent un plan maître complet.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.300418"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 18, 016; En vigueur : 19-12-2011>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2011-11-10/07",
                                "article_number": "art. 18",
                                "sequence_number": "016",
                                "full_reference": "AGF [2011-11-10/07]"
                            },
                            "effective_date": "19-12-2011",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.18"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "1",
                            "text_position": 4,
                            "referenced_text": "demandeurs",
                            "embedded_law_references": [],
                            "bracket_pattern": "[1 demandeurs]1"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 15",
                        "metadata": {
                            "article_range": "15",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "15",
                            "anchor_id": "art_15",
                            "content": {
                            "main_text_raw": "La demande d'approbation du plan maître et de la promesse de subvention pour des activités contient les pièces et données suivantes: 1° un formulaire d'identification rempli sur la base d'un modèle mis à disposition par le Fonds. Ce formulaire d'identification contient les rubriques suivantes: a) une déclaration du demandeur qu'il va respecter les dispositions relatives à la subvention de construction, visées à l'arrêté d'affectation VIPA du 31 mai 2024; b) les données d'identification de la structure; c) les données d'identification de la personne de contact pour le dossier; d) une description succincte du projet; e) l'endroit du projet: adresse et données cadastrales; f) le statut juridique des bâtiments ou du terrain sur lequel le projet sera réalisé; g) la nature des activités; h) les capacités du projet; i) si d'application, la confirmation de l'engagement à l'intégration d'art, mentionné dans la réglementation relative à l'intégration d'oeuvres d'art dans les bâtiments des services publics et services y assimilés, et des établissements, associations et institutions qui relèvent de la Communauté flamande; j) un accord sur le programme initial d'exigences et l'engagement vis-à-vis de la construction durable; k) les données d'identification du coordinateur responsable de répondre aux exigences de performance objectivement évaluables en matière de confort et d'usage d'énergie, d'eau et de matériaux; l) la référence à un document dont il ressort que le plan maître peut être exécuté conformément aux dispositions de l'article 11, § 1er, du décret; m) pour ce qui est les structures de l'aide à la jeunesse, les centres pour troubles du développement et des services de placement familial autorisés: la référence au plan stratégique en matière de soins approuvé par le Ministre; n) la déclaration sur honneur sur le projet pour lequel une promesse de subvention est demandée, pour l'application de, suivant le cas: 1) l'article 27 de l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables; 2) l'article 11 de l'arrêté du Gouvernement flamand du 10 septembre 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour l'aide sociale générale; 3) l'article 14 de l'arrêté du Gouvernement flamand du 4 mars 2011 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour le secteur des établissements de soins destinés à des familles avec des enfants; 4) l'article 15 de l'arrêté du Gouvernement flamand du 10 septembre 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les soins de santé préventifs et ambulants; 5) l'article 12 de l'arrêté du Gouvernement flamand du 18 juin 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les structures agréées et les services autorisés par Grandir régie; 6) l'article 16 de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins; 7) l'article 14 de l'arrêté du Gouvernement flamand du 13 décembre 2019 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour certaines structures de soins résidentiels, modifiant diverses dispositions y afférentes suite au décret sur les soins résidentiels du 15 février 2019 et modifiant l'article 5 de l'arrêté du Gouvernement flamand du 5 juin 2009 portant création d'une commission technique pour la sécurité incendie dans les structures du Bien-être, de la Santé publique et de la Famille; 2° le procès-verbal signé de la réunion des organes compétents du demandeur, comprenant la décision d'approuver et de soumettre le plan maître; 3° une preuve que le demandeur bénéficie ou bénéficiera d'un droit de jouissance, tel que visé à l'article 12 du décret; 4° une évaluation de l'infrastructure existante du demandeur, avec des explications sur l'historique, le concept architectural, la valeur patrimoniale éventuelle, la fonctionnalité, la viabilité et l'efficacité énergétique; 5° une note conceptuelle du plan maître, comportant: a) une description de la totalité des investissements prévus pour les dix prochaines années, assortie: 1) de la vision sur l'infrastructure de soins avec une description du/des groupe(s)-cible(s) et de la/des capacité(s); 2) éventuellement une répartition en projets et en phases, les délais d'exécution et les montants d'investissement estimés; b) au niveau du/des site(s): des esquisses globales, sur lesquelles figurent les éléments suivants: 1) l'aménagement de terrains, bâtiments et parkings, et les plans de zonage y afférents; 2) la situation des différents services de la structure, et l'interconnexion entre les services; 3) une analyse des flux d'habitants, de visiteurs, de personnels et de biens; 6° un rapport de l'avant-trajet parcouru par le demandeur: a) un aperçu du suivi donné aux observations issues des discussions préalables avec le Fonds et la/les administration(s) fonctionnellement compétente(s); b) un rapport des discussions sur le plan maître et le projet avec les intéressés internes du demandeur tels que personnels et habitants; 7° une note conceptuelle contenant le concept architectural du projet: une description du concept architectural et fonctionnel, entre autres une description de l'accès et de la circulation, les subdivisions fonctionnelles, public-privé, la flexibilité du concept, les possibilités d'élargissement éventuelles et l'étalement en phases des travaux; 8° les plans du projet: a) un plan d'implantation à l'échelle 1/500; b) plans de surface à l'échelle 1/100, lors d'une transformation, il est ajouté un plan indiquant les travaux de la transformation par rapport à la situation existante; c) façades et sections; d) un plan détaillé de chaque type de chambre; 9° le programme initial d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux, et la note conceptuelle sur les aspects physiques et techniques de la construction. Un programme d'exigences est un document de base fixant les objectifs et les exigences de prestation liés à un projet en matière de confort et d'usage d'énergie, d'eau et de matériaux. Les valeurs limites de confort objectivement évaluables et les exigences techniques spécifiques sont mentionnées par type de local. Le Ministre arrête les exigences minimales et les conditions en matière de confort et d'usage d'énergie, d'eau et de matériaux; 10° les documents suivants attestant qu'il s'agit d'une construction durable: a) une liste avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds; b) des études ou avis à l'appui des critères indiqués de durabilité; 11° un avis du service d'incendie compétent ou un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent; 12° l'estimation des frais du projet, différenciée par genre de frais, par forme de soins, et répartie en au moins quatre parties: gros oeuvre, équipement technique, finition, équipement et mobilier amovibles, étant entendu que: a) une transformation requiert toujours une estimation détaillée; b) l'estimation est toujours hors tva et frais généraux; c) les coûts de construction estimés sont indiqués par m|F2, par genre de coût et par forme de soins; 13° les aperçus des superficies brutes et nettes. Le calcul des superficies brutes et nettes porte sur un aperçu de la superficie fonctionnelle existante et future du demandeur. L'aperçu des superficies nettes porte sur une liste des superficies nettes des espaces fonctionnels du projet; 14° un plan financier pour les investissements visés, détaillé pour le projet, assorti d'un bilan, d'un compte d'exploitation et d'un compte de pertes et profits; 15° en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter du présent arrêté, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté: a) le dernier compte annuel approuvé du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; b) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du demandeur, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; c) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; d) une déclaration dont l'original est signé par l'entier conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, et par le demandeur d'autre part, qu'il n'existe pas de parenté illégitime entre le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur, tel que visé aux articles 2bis et 2ter du présent arrêté; 16° s'il s'agit d'un projet avec autofinancement entier sans promesse de subvention préalable, tel que visé à l'article 8 du décret, les données démontrant que le demandeur dispose des moyens financiers nécessaires qui sont requis en vue de l'autofinancement entier du projet. 17° si un investisseur réalise le projet et le met à disposition du demandeur: a) l'accord du demandeur et de l'investisseur de respecter les modalités financières supplémentaires imposées par le Fonds. Ces modalités, qui sont mentionnées conformément à l'article 20, § 1er, dans la promesse de subvention, ont rapport: 1) à la façon dont le Fonds paie la subvention d'investissement; 2) à la comptabilisation de la subvention d'investissement dans la base de calcul de l'indemnité périodique dont le demandeur est redevable à l'égard de l'investisseur; b) b) une déclaration de l'investisseur qu'il va respecter les règles relatives à la subvention de construction, visées à l'Arrêté d'affectation du 31 mai 2024, et qu'il veillera à ce que lors de chaque transfert, le nouveau propriétaire respecte également ces règles; c) une référence à des documents qui démontrent que le demandeur et l'investisseur se sont mis d'accord sur les modalités nécessaires en matière de la gestion et de l'entretien raisonnables du bien subventionné pendant la période minimale concrète, visée à l'article 12 du décret, en ce qui concerne les biens immobiliers subventionnés et les biens mobiliers subventionnés, pendant une période de cinq ans en ce qui concerne l'équipement médical ou l'équipement spécial et pendant une période de dix ans pour les autres biens mobiliers; 18° une attestation T.V.A. ou une décision préalable du Service Public Fédéral Finances avec mention du pourcentage T.V.A. qui s'applique concrètement aux travaux du projet ou, le cas échéant, à l'achat. Les pièces et données visées à l'alinéa premier, 4° à 6° inclus, constituent le plan maître. Les pièces et données visées à l'alinéa premier, 7° à 18° inclus, constituent le plan de projet.] L'attestation T.V.A. ou la décision préalable, visée à l'alinéa premier, 18°, n'est pas une exigence formelle à la recevabilité du dossier, visée à l'article 19, § 1er, et peut être envoyée au Fonds ultérieurement. L'attestation T.V.A. ou la décision préalable, visée à l'alinéa premier, 18°, est nécessaire pour soumettre le dossier à l'avis de l'Inspection des Finances conformément àà l'article 19, § 4, sauf pour ces dossiers d'achat auxquels le régime T.V.A. ne s'applique pas. Le demandeur soumet la demande par voie électronique via la plateforme mise à disposition par le Fonds. Si le demandeur ne respecte pas les règles, visées à l'alinéa 1er, 17°, b), les sanctions, visées à l'Arrêté d'affectation du 31 mai 2024 s'appliquent également à l'investisseur.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "un formulaire d'identification rempli sur la base d'un modèle mis à disposition par le Fonds. Ce formulaire d'identification contient les rubriques suivantes:",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le procès-verbal signé de la réunion des organes compétents du demandeur, comprenant la décision d'approuver et de soumettre le plan maître",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "[2 une preuve que le demandeur bénéficie ou bénéficiera d'un droit de jouissance, tel que visé à l'article 12 du décret",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "une évaluation de l'infrastructure existante du demandeur, avec des explications sur l'historique, le concept architectural, la valeur patrimoniale éventuelle, la fonctionnalité, la viabilité et l'efficacité énergétique",
                                "sub_items": []
                                },
                                {
                                "number": "5°",
                                "text": "une note conceptuelle du plan maître, comportant:",
                                "sub_items": []
                                },
                                {
                                "number": "6°",
                                "text": "un rapport de l'avant-trajet parcouru par le demandeur:",
                                "sub_items": []
                                },
                                {
                                "number": "7°",
                                "text": "une note conceptuelle contenant le concept architectural du projet: une description du concept architectural et fonctionnel, entre autres une description de l'accès et de la circulation, les subdivisions fonctionnelles, public-privé, la flexibilité du concept, les possibilités d'élargissement éventuelles et l'étalement en phases des travaux",
                                "sub_items": []
                                },
                                {
                                "number": "8°",
                                "text": "les plans du projet:",
                                "sub_items": []
                                },
                                {
                                "number": "9°",
                                "text": "le programme initial d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux, et la note conceptuelle sur les aspects physiques et techniques de la construction. Un programme d'exigences est un document de base fixant les objectifs et les exigences de prestation liés à un projet en matière de confort et d'usage d'énergie, d'eau et de matériaux. Les valeurs limites de confort objectivement évaluables et les exigences techniques spécifiques sont mentionnées par type de local. Le Ministre arrête les exigences minimales et les conditions en matière de confort et d'usage d'énergie, d'eau et de matériaux",
                                "sub_items": []
                                },
                                {
                                "number": "10°",
                                "text": "les documents suivants attestant qu'il s'agit d'une construction durable:",
                                "sub_items": []
                                },
                                {
                                "number": "11°",
                                "text": "un avis du service d'incendie compétent ou un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent",
                                "sub_items": []
                                },
                                {
                                "number": "12°",
                                "text": "l'estimation des frais du projet, différenciée par genre de frais, par forme de soins, et répartie en au moins quatre parties: gros oeuvre, équipement technique, finition, équipement et mobilier amovibles, étant entendu que:",
                                "sub_items": []
                                },
                                {
                                "number": "13°",
                                "text": "les aperçus des superficies brutes et nettes. Le calcul des superficies brutes et nettes porte sur un aperçu de la superficie fonctionnelle existante et future du demandeur. L'aperçu des superficies nettes porte sur une liste des superficies nettes des espaces fonctionnels du projet",
                                "sub_items": []
                                },
                                {
                                "number": "14°",
                                "text": "un plan financier pour les investissements visés, détaillé pour le projet, assorti d'un bilan, d'un compte d'exploitation et d'un compte de pertes et profits",
                                "sub_items": []
                                },
                                {
                                "number": "15°",
                                "text": "en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter du présent arrêté, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté:",
                                "sub_items": []
                                },
                                {
                                "number": "16°",
                                "text": "s'il s'agit d'un projet avec autofinancement entier sans promesse de subvention préalable, tel que visé à l'article 8 du décret, les données démontrant que le demandeur dispose des moyens financiers nécessaires qui sont requis en vue de l'autofinancement entier du projet.",
                                "sub_items": []
                                },
                                {
                                "number": "17°",
                                "text": "si un investisseur réalise le projet et le met à disposition du demandeur:",
                                "sub_items": []
                                },
                                {
                                "number": "18°",
                                "text": "une attestation T.V.A. ou une décision préalable du Service Public Fédéral Finances avec mention du pourcentage T.V.A. qui s'applique concrètement aux travaux du projet ou, le cas échéant, à l'achat.",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "6°",
                                "text": "inclus, constituent le plan maître.",
                                "sub_items": []
                                },
                                {
                                "number": "7°",
                                "text": "à",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-15\"><header class=\"article-header\"><h2 class=\"article-number\">Article 15</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">La demande d'approbation du plan maître et de la promesse de subvention pour des activités contient les pièces et données suivantes:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">un formulaire d'identification rempli sur la base d'un modèle mis à disposition par le Fonds. Ce formulaire d'identification contient les rubriques suivantes:</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le procès-verbal signé de la réunion des organes compétents du demandeur, comprenant la décision d'approuver et de soumettre le plan maître</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">[2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"une preuve que le demandeur bénéficie ou bénéficiera d'un droit de jouissance, tel que visé à l'article 12 du décret\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.5\" data-article-dossier-number=\"\">une preuve que le demandeur bénéficie ou bénéficiera d'un droit de jouissance, tel que visé à l'article 12 du décret</span></span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">une évaluation de l'infrastructure existante du demandeur, avec des explications sur l'historique, le concept architectural, la valeur patrimoniale éventuelle, la fonctionnalité, la viabilité et l'efficacité énergétique</span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">une note conceptuelle du plan maître, comportant:</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">un rapport de l'avant-trajet parcouru par le demandeur:</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">une note conceptuelle contenant le concept architectural du projet: une description du concept architectural et fonctionnel, entre autres une description de l'accès et de la circulation, les subdivisions fonctionnelles, public-privé, la flexibilité du concept, les possibilités d'élargissement éventuelles et l'étalement en phases des travaux</span></li><li class=\"provision\" data-number=\"8°\"><span class=\"provision-text\">les plans du projet:</span></li><li class=\"provision\" data-number=\"9°\"><span class=\"provision-text\">le programme initial d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux, et la note conceptuelle sur les aspects physiques et techniques de la construction. Un programme d'exigences est un document de base fixant les objectifs et les exigences de prestation liés à un projet en matière de confort et d'usage d'énergie, d'eau et de matériaux. Les valeurs limites de confort objectivement évaluables et les exigences techniques spécifiques sont mentionnées par type de local. Le Ministre arrête les exigences minimales et les conditions en matière de confort et d'usage d'énergie, d'eau et de matériaux</span></li><li class=\"provision\" data-number=\"10°\"><span class=\"provision-text\">les documents suivants attestant qu'il s'agit d'une construction durable:</span></li><li class=\"provision\" data-number=\"11°\"><span class=\"provision-text\">un avis du service d'incendie compétent ou un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent</span></li><li class=\"provision\" data-number=\"12°\"><span class=\"provision-text\">l'estimation des frais du projet, différenciée par genre de frais, par forme de soins, et répartie en au moins quatre parties: gros oeuvre, équipement technique, finition, équipement et mobilier amovibles, étant entendu que:</span></li><li class=\"provision\" data-number=\"13°\"><span class=\"provision-text\">les aperçus des superficies brutes et nettes. Le calcul des superficies brutes et nettes porte sur un aperçu de la superficie fonctionnelle existante et future du demandeur. L'aperçu des superficies nettes porte sur une liste des superficies nettes des espaces fonctionnels du projet</span></li><li class=\"provision\" data-number=\"14°\"><span class=\"provision-text\">un plan financier pour les investissements visés, détaillé pour le projet, assorti d'un bilan, d'un compte d'exploitation et d'un compte de pertes et profits</span></li><li class=\"provision\" data-number=\"15°\"><span class=\"provision-text\">en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter du présent arrêté, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté:</span></li><li class=\"provision\" data-number=\"16°\"><span class=\"provision-text\">s'il s'agit d'un projet avec autofinancement entier sans promesse de subvention préalable, tel que visé à l'article 8 du décret, les données démontrant que le demandeur dispose des moyens financiers nécessaires qui sont requis en vue de l'autofinancement entier du projet.</span></li><li class=\"provision\" data-number=\"17°\"><span class=\"provision-text\">si un investisseur réalise le projet et le met à disposition du demandeur:</span></li><li class=\"provision\" data-number=\"18°\"><span class=\"provision-text\">une attestation T.V.A. ou une décision préalable du Service Public Fédéral Finances avec mention du pourcentage T.V.A. qui s'applique concrètement aux travaux du projet ou, le cas échéant, à l'achat.</span></li></ol><p class=\"intro-text\">Les pièces et données visées à l'alinéa premier,:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">inclus, constituent le plan maître.</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">à</span></li></ol><p class=\"closing-text\">6° inclus, constituent le plan maître. Les pièces et données visées à l'alinéa premier, 7° à 18° inclus, constituent le plan de projet.] L'attestation T.V.A. ou la décision préalable, visée à l'alinéa premier, 18°, n'est pas une exigence formelle à la recevabilité du dossier, visée à l'article 19, § 1er, et peut être envoyée au Fonds ultérieurement. L'attestation T.V.A. ou la décision préalable, visée à l'alinéa premier, 18°, est nécessaire pour soumettre le dossier à l'avis de l'Inspection des Finances conformément àà l'article 19, § 4, sauf pour ces dossiers d'achat auxquels le régime T.V.A. ne s'applique pas. Le demandeur soumet la demande par voie électronique via la plateforme mise à disposition par le Fonds. Si le demandeur ne respecte pas les règles, visées à l'alinéa 1er, 17°, b), les sanctions, visées à l'Arrêté d'affectation du 31 mai 2024 s'appliquent également à l'investisseur.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 21,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.304319"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 11, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 11",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.11"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 5, 022; En vigueur : 11-10-2018>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-07-06/25",
                                "article_number": "art. 5",
                                "sequence_number": "022",
                                "full_reference": "AGF [2018-07-06/25]"
                            },
                            "effective_date": "11-10-2018",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.5"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2019-05-17/67](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767), art. 2, 024; En vigueur : 19-09-2019>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-05-17/67",
                                "article_number": "art. 2",
                                "sequence_number": "024",
                                "full_reference": "AGF [2019-05-17/67]"
                            },
                            "effective_date": "19-09-2019",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767#Art.2"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 19, 025; En vigueur : 01-01-2020>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-12-13/06",
                                "article_number": "art. 19",
                                "sequence_number": "025",
                                "full_reference": "AGF [2019-12-13/06]"
                            },
                            "effective_date": "01-01-2020",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.19"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 7, 028; En vigueur : 20-09-2021>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2021-07-16/32",
                                "article_number": "art. 7",
                                "sequence_number": "028",
                                "full_reference": "AGF [2021-07-16/32]"
                            },
                            "effective_date": "20-09-2021",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.7"
                            },
                            {
                            "footnote_number": "6",
                            "footnote_content": "(6)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 2, 029; En vigueur : 12-08-2022>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2022-05-06/08",
                                "article_number": "art. 2",
                                "sequence_number": "029",
                                "full_reference": "AGF [2022-05-06/08]"
                            },
                            "effective_date": "12-08-2022",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.2"
                            },
                            {
                            "footnote_number": "7",
                            "footnote_content": "(7)<AGF [2024-05-31/16](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116), art. 9, 033; En vigueur : 01-08-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-05-31/16",
                                "article_number": "art. 9",
                                "sequence_number": "033",
                                "full_reference": "AGF [2024-05-31/16]"
                            },
                            "effective_date": "01-08-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116#Art.9"
                            },
                            {
                            "footnote_number": "8",
                            "footnote_content": "(8)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 2, 034; En vigueur : 21-09-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-07-19/42",
                                "article_number": "art. 2",
                                "sequence_number": "034",
                                "full_reference": "AGF [2024-07-19/42]"
                            },
                            "effective_date": "21-09-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.2"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "7",
                            "text_position": 308,
                            "referenced_text": "une déclaration du demandeur qu'il va respecter les dispositions relatives à la subvention de construction, visées à l'arrêté d'affectation VIPA du 31 mai 2024",
                            "embedded_law_references": [],
                            "bracket_pattern": "[7 une déclaration du demandeur qu'il va respecter les dispositions relatives à la subvention de construction, visées à l'arrêté d'affectation VIPA du 31 mai 2024]7"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 1644,
                            "referenced_text": "les structures de l'aide à la jeunesse, les centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 les structures de l'aide à la jeunesse, les centres pour troubles du développement]5"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 2006,
                            "referenced_text": "l'article 27 de l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables ;",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 l'article 27 de l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables ;]3"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 3312,
                            "referenced_text": "Grandir régie",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 Grandir régie]5"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 3538,
                            "referenced_text": "7) l'article 14 de l'arrêté du Gouvernement flamand du 13 décembre 2019 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour certaines structures de soins résidentiels, modifiant diverses dispositions y afférentes suite au décret sur les soins résidentiels du 15 février 2019 et modifiant l'article 5 de l'arrêté du Gouvernement flamand du 5 juin 2009 portant création d'une commission technique pour la sécurité incendie dans les structures du Bien-être, de la Santé publique et de la Famille ;",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 7) l'article 14 de l'arrêté du Gouvernement flamand du 13 décembre 2019 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour certaines structures de soins résidentiels, modifiant diverses dispositions y afférentes suite au décret sur les soins résidentiels du 15 février 2019 et modifiant l'article 5 de l'arrêté du Gouvernement flamand du 5 juin 2009 portant création d'une commission technique pour la sécurité incendie dans les structures du Bien-être, de la Santé publique et de la Famille ;]4"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 4238,
                            "referenced_text": "une preuve que le demandeur bénéficie ou bénéficiera d'un droit de jouissance, tel que visé à l'article 12 du décret",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 une preuve que le demandeur bénéficie ou bénéficiera d'un droit de jouissance, tel que visé à l'article 12 du décret]2"
                            },
                            {
                            "reference_number": "7",
                            "text_position": 10776,
                            "referenced_text": "b) une déclaration de l'investisseur qu'il va respecter les règles relatives à la subvention de construction, visées à l'Arrêté d'affectation du 31 mai 2024, et qu'il veillera à ce que lors de chaque transfert, le nouveau propriétaire respecte également ces règles",
                            "embedded_law_references": [],
                            "bracket_pattern": "[7 b) une déclaration de l'investisseur qu'il va respecter les règles relatives à la subvention de construction, visées à l'Arrêté d'affectation du 31 mai 2024, et qu'il veillera à ce que lors de chaque transfert, le nouveau propriétaire respecte également ces règles]7"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 11942,
                            "referenced_text": "7° à 18°",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 7° à 18°]3"
                            },
                            {
                            "reference_number": "8",
                            "text_position": 12312,
                            "referenced_text": "pour soumettre le dossier à l'avis de l'Inspection des Finances conformément à",
                            "embedded_law_references": [],
                            "bracket_pattern": "[8 pour soumettre le dossier à l'avis de l'Inspection des Finances conformément à]8"
                            },
                            {
                            "reference_number": "6",
                            "text_position": 12497,
                            "referenced_text": "Le demandeur soumet la demande par voie électronique via la plateforme mise à disposition par le Fonds.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[6 Le demandeur soumet la demande par voie électronique via la plateforme mise à disposition par le Fonds.]6"
                            },
                            {
                            "reference_number": "7",
                            "text_position": 12608,
                            "referenced_text": "Si le demandeur ne respecte pas les règles, visées à l'alinéa 1er, 17°, b), les sanctions, visées à l'Arrêté d'affectation du 31 mai 2024 s'appliquent également à l'investisseur.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[7 Si le demandeur ne respecte pas les règles, visées à l'alinéa 1er, 17°, b), les sanctions, visées à l'Arrêté d'affectation du 31 mai 2024 s'appliquent également à l'investisseur.]7"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 16",
                        "metadata": {
                            "article_range": "16",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "16",
                            "anchor_id": "art_16",
                            "content": {
                            "main_text_raw": "La demande d'une promesse de subvention ne peut avoir trait qu'à un achat lorsque ce dernier est suivi d'une transformation. Dans ce cas, la demande contient les documents suivants: 1° les documents visés à l'article 15, alinéa premier, 1° et 2° et 4° à 16° inclus; 2° la promesse de vente ou le compromis à condition suspensive; 3° une attestation du sol conformément à la réglementation relative à l'assainissement du sol. Par dérogation à l'alinéa premier, pour les secteurs de l'aide sociale générale, des soins de santé préventifs et ambulatoires, de l'assistance spéciale à la jeunesse et des services autorisés de placement familial, et des établissements de soins destinés à des familles avec des enfants, un achat sans transformation est possible pour un centre de services local pour un centre d'accueil de jour, pour un centre de soins de jour, pour un centre de convalescence, pour un centre de court séjour de type 2..., et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables. Dans ce cas, la demande de promesse de subvention doit comprendre les documents suivants: 1° les documents visés à l'article 15, alinéa premier, 1° et 2° et 4° à 10° inclus, et 13° à 16° inclus, du présent arrêté; 2° la promesse de vente ou le compromis à condition suspensive; 3° une attestation du sol conformément à la réglementation relative à l'assainissement du sol; 4° le permis de bâtir ou le permis d'environnement et le rapport de prévention incendie y afférent du bâtiment à acheter. 5° si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux: le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds. L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes: 1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire; 2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant; 3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain. Lorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition: 1° les cahiers des charges; 2° le dossier d'attribution par adjudication, comprenant: a) le procès-verbal de l'ouverture des inscriptions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix motivé de l'entrepreneur ou du fournisseur. En cas de modification de fonction du bâtiment en question, la demande est complétée, en ce qui concerne l'affectation future, d'un avis du service des pompiers compétent ou d'un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent;]",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "les documents visés à l'article 15, alinéa premier,",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "16°",
                                "text": "inclus",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "la promesse de vente ou le compromis à condition suspensive",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "une attestation du sol conformément à la réglementation relative à l'assainissement du sol.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les documents visés à l'article 15, alinéa premier,",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "10°",
                                "text": "inclus, et",
                                "sub_items": []
                                },
                                {
                                "number": "13°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "16°",
                                "text": "inclus, du présent arrêté",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "la promesse de vente ou le compromis à condition suspensive",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "une attestation du sol conformément à la réglementation relative à l'assainissement du sol",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "le permis de bâtir [2 ou le permis d'environnement",
                                "sub_items": []
                                },
                                {
                                "number": "5°",
                                "text": "si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux: le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le demandeur n'a jamais été propriétaire du bâtiment en question auparavant",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les cahiers des charges",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le dossier d'attribution par adjudication, comprenant:",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-16\"><header class=\"article-header\"><h2 class=\"article-number\">Article 16</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">La demande d'une promesse de subvention ne peut avoir trait qu'à un achat lorsque ce dernier est suivi d'une transformation. Dans ce cas, la demande contient les documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les documents visés à l'article 15, alinéa premier,</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"16°\"><span class=\"provision-text\">inclus</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">la promesse de vente ou le compromis à condition suspensive</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">une attestation du sol conformément à la réglementation relative à l'assainissement du sol.</span></li></ol><p class=\"intro-text\">Par dérogation à l'alinéa premier, pour les secteurs de l'aide sociale générale, des soins de santé préventifs et ambulatoires, de l'assistance spéciale à la jeunesse et des services autorisés de placement familial, et des établissements de soins destinés à des familles avec des enfants, un achat sans transformation est possible pour un centre de services local pour un centre d'accueil de jour, pour un centre de soins de jour,<span class=\"footnote-ref\" data-footnote-id=\"6\" data-referenced-text=\"pour un centre de convalescence,\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024062121#Art.3\" data-article-dossier-number=\"\">pour un centre de convalescence,</span>pour un centre de court séjour de type 2<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019121306#Art.20\" data-article-dossier-number=\"\">...</span>,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018112314#Art.36\" data-article-dossier-number=\"\">et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables</span>. Dans ce cas, la demande de promesse de subvention doit comprendre les documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les documents visés à l'article 15, alinéa premier,</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"10°\"><span class=\"provision-text\">inclus, et</span></li><li class=\"provision\" data-number=\"13°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"16°\"><span class=\"provision-text\">inclus, du présent arrêté</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">la promesse de vente ou le compromis à condition suspensive</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">une attestation du sol conformément à la réglementation relative à l'assainissement du sol</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">le permis de bâtir [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"ou le permis d'environnement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.6\" data-article-dossier-number=\"\">ou le permis d'environnement</span></span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux: le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.</span></li></ol><p class=\"intro-text\">L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le demandeur n'a jamais été propriétaire du bâtiment en question auparavant</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.</span></li></ol><p class=\"intro-text\">Lorsque le deuxième alinéa, 5°,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes : 1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire ; 2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant ; 3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain. Lorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition : 1° les cahiers des charges ; 2° le dossier d'attribution par adjudication, comprenant : a) le procès-verbal de l'ouverture des inscriptions ; b) toutes les offres ; c) les rapports du contrôle des offres ; d) le choix motivé de l'entrepreneur ou du fournisseur.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.6\" data-article-dossier-number=\"\">est d'application</span>, le demandeur tient les documents suivants à disposition:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les cahiers des charges</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le dossier d'attribution par adjudication, comprenant:</span></li></ol><p class=\"closing-text\">a) le procès-verbal de l'ouverture des inscriptions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix motivé de l'entrepreneur ou du fournisseur. En cas de modification de fonction du bâtiment en question, la demande est complétée, en ce qui concerne l'affectation future, d'un avis du service des pompiers compétent ou d'un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent;]</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 23,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.306911"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 12, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 12",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.12"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 6, 022; En vigueur : 11-10-2018>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-07-06/25",
                                "article_number": "art. 6",
                                "sequence_number": "022",
                                "full_reference": "AGF [2018-07-06/25]"
                            },
                            "effective_date": "11-10-2018",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.6"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2018-11-23/14](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018112314), art. 36, 023; En vigueur : 07-01-2019>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-11-23/14",
                                "article_number": "art. 36",
                                "sequence_number": "023",
                                "full_reference": "AGF [2018-11-23/14]"
                            },
                            "effective_date": "07-01-2019",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018112314",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018112314#Art.36"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 20, 025; En vigueur : 01-01-2019>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-12-13/06",
                                "article_number": "art. 20",
                                "sequence_number": "025",
                                "full_reference": "AGF [2019-12-13/06]"
                            },
                            "effective_date": "01-01-2019",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.20"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 21, 025; En vigueur : 01-01-2020>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-12-13/06",
                                "article_number": "art. 21",
                                "sequence_number": "025",
                                "full_reference": "AGF [2019-12-13/06]"
                            },
                            "effective_date": "01-01-2020",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.21"
                            },
                            {
                            "footnote_number": "6",
                            "footnote_content": "(6)<AGF [2024-06-21/21](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121), art. 3, 032; En vigueur : 01-04-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-06-21/21",
                                "article_number": "art. 3",
                                "sequence_number": "032",
                                "full_reference": "AGF [2024-06-21/21]"
                            },
                            "effective_date": "01-04-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024062121#Art.3"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "6",
                            "text_position": 875,
                            "referenced_text": "pour un centre de convalescence,",
                            "embedded_law_references": [],
                            "bracket_pattern": "[6 pour un centre de convalescence,]6"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 958,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 968,
                            "referenced_text": "et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables]3"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 1809,
                            "referenced_text": "ou le permis d'environnement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 ou le permis d'environnement]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 1916,
                            "referenced_text": "5° si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux : le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 5° si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux : le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 2195,
                            "referenced_text": "L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes :  \n1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire ;  \n2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant ;  \n3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.  \nLorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition :  \n1° les cahiers des charges ;  \n2° le dossier d'attribution par adjudication, comprenant :  \na) le procès-verbal de l'ouverture des inscriptions ;  \nb) toutes les offres ;  \nc) les rapports du contrôle des offres ;  \nd) le choix motivé de l'entrepreneur ou du fournisseur.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes :  \n1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire ;  \n2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant ;  \n3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.  \nLorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition :  \n1° les cahiers des charges ;  \n2° le dossier d'attribution par adjudication, comprenant :  \na) le procès-verbal de l'ouverture des inscriptions ;  \nb) toutes les offres ;  \nc) les rapports du contrôle des offres ;  \nd) le choix motivé de l'entrepreneur ou du fournisseur.]2"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 16 DROIT FUTUR",
                        "metadata": {
                            "article_range": "16 DROIT FUTUR",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "16 DROIT FUTUR",
                            "anchor_id": "art_16 DROIT FUTUR",
                            "content": {
                            "main_text_raw": "La demande d'une promesse de subvention ne peut avoir trait qu'à un achat lorsque ce dernier est suivi d'une transformation. Dans ce cas, la demande contient les documents suivants: 1° les documents visés à l'article 15, alinéa premier, 1° et 2° et 4° à 16° inclus; 2° la promesse de vente ou le compromis à condition suspensive; 3° une attestation du sol conformément à la réglementation relative à l'assainissement du sol. Par dérogation à l'alinéa premier, pour les secteurs de l'aide sociale générale, des soins de santé préventifs et ambulatoires, des structures de l'aide à la jeunesse, des centres pour troubles du développement et des services autorisés de placement familial, et de l'accueil d'enfants, un achat sans transformation est possible pour un centre de services local pour un centre d'accueil de jour, pour un centre de soins de jour, pour un centre de court séjour de type 2, pour un centre de court séjour de type 3..., et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables. Dans ce cas, la demande de promesse de subvention doit comprendre les documents suivants: 1° les documents visés à l'article 15, alinéa premier, 1° et 2° et 4° à 10° inclus, et 13° à 16° inclus, du présent arrêté; 2° la promesse de vente ou le compromis à condition suspensive; 3° une attestation du sol conformément à la réglementation relative à l'assainissement du sol; 4° le permis de bâtir ou le permis d'environnement et le rapport de prévention incendie y afférent du bâtiment à acheter. 5° si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux: le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds. L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes: 1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire; 2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant; 3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain. Lorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition: 1° les cahiers des charges; 2° le dossier d'attribution par adjudication, comprenant: a) le procès-verbal de l'ouverture des inscriptions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix motivé de l'entrepreneur ou du fournisseur. En cas de modification de fonction du bâtiment en question, la demande est complétée, en ce qui concerne l'affectation future, d'un avis du service des pompiers compétent ou d'un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent;]",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "les documents visés à l'article 15, alinéa premier,",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "16°",
                                "text": "inclus",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "la promesse de vente ou le compromis à condition suspensive",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "une attestation du sol conformément à la réglementation relative à l'assainissement du sol.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les documents visés à l'article 15, alinéa premier,",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "et",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "10°",
                                "text": "inclus, et",
                                "sub_items": []
                                },
                                {
                                "number": "13°",
                                "text": "à",
                                "sub_items": []
                                },
                                {
                                "number": "16°",
                                "text": "inclus, du présent arrêté",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "la promesse de vente ou le compromis à condition suspensive",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "une attestation du sol conformément à la réglementation relative à l'assainissement du sol",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "le permis de bâtir [2 ou le permis d'environnement",
                                "sub_items": []
                                },
                                {
                                "number": "5°",
                                "text": "si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux: le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le demandeur n'a jamais été propriétaire du bâtiment en question auparavant",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les cahiers des charges",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le dossier d'attribution par adjudication, comprenant:",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-16 DROIT FUTUR\"><header class=\"article-header\"><h2 class=\"article-number\">Article 16 DROIT FUTUR</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">La demande d'une promesse de subvention ne peut avoir trait qu'à un achat lorsque ce dernier est suivi d'une transformation. Dans ce cas, la demande contient les documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les documents visés à l'article 15, alinéa premier,</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"16°\"><span class=\"provision-text\">inclus</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">la promesse de vente ou le compromis à condition suspensive</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">une attestation du sol conformément à la réglementation relative à l'assainissement du sol.</span></li></ol><p class=\"intro-text\">Par dérogation à l'alinéa premier, pour les secteurs de l'aide sociale générale, des soins de santé préventifs et ambulatoires,<span class=\"footnote-ref\" data-footnote-id=\"7\" data-referenced-text=\"des structures de l'aide à la jeunesse, des centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021071632#Art.8\" data-article-dossier-number=\"\">des structures de l'aide à la jeunesse, des centres pour troubles du développement</span>et des services autorisés de placement familial, et<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"de l'accueil d'enfants\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.3\" data-article-dossier-number=\"\">de l'accueil d'enfants</span>, un achat sans transformation est possible pour un centre de services local pour un centre d'accueil de jour, pour un centre de soins de jour,<span class=\"footnote-ref\" data-footnote-id=\"6\" data-referenced-text=\"pour un centre de court séjour de type 2, pour un centre de court séjour de type 3\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019121306#Art.22\" data-article-dossier-number=\"\">pour un centre de court séjour de type 2, pour un centre de court séjour de type 3</span><span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019121306#Art.20\" data-article-dossier-number=\"\">...</span>,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018112314#Art.36\" data-article-dossier-number=\"\">et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables</span>. Dans ce cas, la demande de promesse de subvention doit comprendre les documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les documents visés à l'article 15, alinéa premier,</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">et</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"10°\"><span class=\"provision-text\">inclus, et</span></li><li class=\"provision\" data-number=\"13°\"><span class=\"provision-text\">à</span></li><li class=\"provision\" data-number=\"16°\"><span class=\"provision-text\">inclus, du présent arrêté</span></li></ol><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">la promesse de vente ou le compromis à condition suspensive</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">une attestation du sol conformément à la réglementation relative à l'assainissement du sol</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">le permis de bâtir [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"ou le permis d'environnement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.6\" data-article-dossier-number=\"\">ou le permis d'environnement</span></span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux: le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.</span></li></ol><p class=\"intro-text\">L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le demandeur n'a jamais été propriétaire du bâtiment en question auparavant</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.</span></li></ol><p class=\"intro-text\">Lorsque le deuxième alinéa, 5°,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes : 1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire ; 2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant ; 3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain. Lorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition : 1° les cahiers des charges ; 2° le dossier d'attribution par adjudication, comprenant : a) le procès-verbal de l'ouverture des inscriptions ; b) toutes les offres ; c) les rapports du contrôle des offres ; d) le choix motivé de l'entrepreneur ou du fournisseur.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.6\" data-article-dossier-number=\"\">est d'application</span>, le demandeur tient les documents suivants à disposition:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les cahiers des charges</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le dossier d'attribution par adjudication, comprenant:</span></li></ol><p class=\"closing-text\">a) le procès-verbal de l'ouverture des inscriptions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix motivé de l'entrepreneur ou du fournisseur. En cas de modification de fonction du bâtiment en question, la demande est complétée, en ce qui concerne l'affectation future, d'un avis du service des pompiers compétent ou d'un rapport des pourparlers avec le service d'incendie compétent, signé par le demandeur et transmis pour information au service d'incendie compétent;]</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 23,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.309416"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 12, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 12",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.12"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 6, 022; En vigueur : 11-10-2018>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-07-06/25",
                                "article_number": "art. 6",
                                "sequence_number": "022",
                                "full_reference": "AGF [2018-07-06/25]"
                            },
                            "effective_date": "11-10-2018",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.6"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2018-11-23/14](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018112314), art. 36, 023; En vigueur : 07-01-2019>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-11-23/14",
                                "article_number": "art. 36",
                                "sequence_number": "023",
                                "full_reference": "AGF [2018-11-23/14]"
                            },
                            "effective_date": "07-01-2019",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018112314",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018112314#Art.36"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 20, 025; En vigueur : 01-01-2019>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-12-13/06",
                                "article_number": "art. 20",
                                "sequence_number": "025",
                                "full_reference": "AGF [2019-12-13/06]"
                            },
                            "effective_date": "01-01-2019",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.20"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 21, 025; En vigueur : 01-01-2020>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-12-13/06",
                                "article_number": "art. 21",
                                "sequence_number": "025",
                                "full_reference": "AGF [2019-12-13/06]"
                            },
                            "effective_date": "01-01-2020",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.21"
                            },
                            {
                            "footnote_number": "6",
                            "footnote_content": "(6)<AGF [2019-12-13/06](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306), art. 22, 025; En vigueur : 31-12-2025>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2019-12-13/06",
                                "article_number": "art. 22",
                                "sequence_number": "025",
                                "full_reference": "AGF [2019-12-13/06]"
                            },
                            "effective_date": "31-12-2025",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019121306#Art.22"
                            },
                            {
                            "footnote_number": "7",
                            "footnote_content": "(7)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 8, 028; En vigueur : 20-09-2021>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2021-07-16/32",
                                "article_number": "art. 8",
                                "sequence_number": "028",
                                "full_reference": "AGF [2021-07-16/32]"
                            },
                            "effective_date": "20-09-2021",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.8"
                            },
                            {
                            "footnote_number": "8",
                            "footnote_content": "(8)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 3, 034; En vigueur : 21-09-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-07-19/42",
                                "article_number": "art. 3",
                                "sequence_number": "034",
                                "full_reference": "AGF [2024-07-19/42]"
                            },
                            "effective_date": "21-09-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.3"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "7",
                            "text_position": 567,
                            "referenced_text": "des structures de l'aide à la jeunesse, des centres pour troubles du développement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[7 des structures de l'aide à la jeunesse, des centres pour troubles du développement]7"
                            },
                            {
                            "reference_number": "8",
                            "text_position": 706,
                            "referenced_text": "de l'accueil d'enfants",
                            "embedded_law_references": [],
                            "bracket_pattern": "[8 de l'accueil d'enfants]8"
                            },
                            {
                            "reference_number": "6",
                            "text_position": 881,
                            "referenced_text": "pour un centre de court séjour de type 2, pour un centre de court séjour de type 3",
                            "embedded_law_references": [],
                            "bracket_pattern": "[6 pour un centre de court séjour de type 2, pour un centre de court séjour de type 3]6"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 973,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 ...]4"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 983,
                            "referenced_text": "et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 et pour une structure telle que visée à l'arrêté du Gouvernement flamand du 23 novembre 2018 fixant la subvention d'investissement et les normes techniques et physiques de construction pour certaines structures destinées aux personnes handicapées et modifiant l'article 16 de l'arrêté du Gouvernement flamand du 8 juin 1999 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables]3"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 1824,
                            "referenced_text": "ou le permis d'environnement",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 ou le permis d'environnement]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 1931,
                            "referenced_text": "5° si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux : le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 5° si l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux : le procès-verbal de réception provisoire ou définitive du bâtiment et un aperçu des attributions qui est établi sur la base d'un modèle mis à disposition par le Fonds.]2"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 2210,
                            "referenced_text": "L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes :  \n1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire ;  \n2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant ;  \n3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.  \nLorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition :  \n1° les cahiers des charges ;  \n2° le dossier d'attribution par adjudication, comprenant :  \na) le procès-verbal de l'ouverture des inscriptions ;  \nb) toutes les offres ;  \nc) les rapports du contrôle des offres ;  \nd) le choix motivé de l'entrepreneur ou du fournisseur.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 L'achat sans transformation visé à l'alinéa deux, doit répondre à toutes les conditions suivantes :  \n1° il s'agit d'un bâtiment prêt à l'usage. Lorsque l'achat est effectué avec transfert de propriété à la suite d'un marché public pour des travaux, la promesse de vente ou le compromis à condition suspensive date d'après la date du procès-verbal de réception provisoire ;  \n2° le demandeur n'a jamais été propriétaire du bâtiment en question auparavant ;  \n3° l'achat du bâtiment comprend également l'achat du terrain sur lequel le bâtiment concerné est érigé, sauf si le demandeur était déjà le propriétaire du terrain.  \nLorsque le deuxième alinéa, 5°, est d'application, le demandeur tient les documents suivants à disposition :  \n1° les cahiers des charges ;  \n2° le dossier d'attribution par adjudication, comprenant :  \na) le procès-verbal de l'ouverture des inscriptions ;  \nb) toutes les offres ;  \nc) les rapports du contrôle des offres ;  \nd) le choix motivé de l'entrepreneur ou du fournisseur.]2"
                            }
                        ]
                        },
                        {
                        "type": "article",
                        "label": "Article 17",
                        "metadata": {
                            "article_range": "17",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "17",
                            "anchor_id": "art_17",
                            "content": {
                            "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 13, 020; En vigueur: 20-03-2016>",
                            "numbered_provisions": [],
                            "abrogation_status": "abrogé",
                            "main_text": "<article class=\"legal-article\" id=\"art-17\"><header class=\"article-header\"><h2 class=\"article-number\">Article 17</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"13\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 13, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.309540"
                            },
                            "legal_citation": {
                                "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 13, 020; En vigueur: 20-03-2016",
                                "urls": [
                                "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                                ]
                            },
                            "enhanced_citations": [
                                {
                                "citation_type": "abrogation",
                                "law_type": "AGF",
                                "dossier_number": "2016-01-15/17",
                                "article_number": "13",
                                "sequence_number": "020",
                                "effective_date": "20-03-2016",
                                "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                                "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 13, 020; En vigueur: 20-03-2016>",
                                "prefix": "Abrogé par",
                                "raw_dossier": "2016-01-15/17",
                                "raw_article": "13",
                                "start_pos": 0,
                                "end_pos": 166,
                                "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 13, 020; En vigueur: 20-03-2016>"
                                }
                            ]
                            }
                        },
                        "footnotes": [],
                        "footnote_references": []
                        },
                        {
                        "type": "article",
                        "label": "Article 18",
                        "metadata": {
                            "article_range": "18",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "18",
                            "anchor_id": "art_18",
                            "content": {
                            "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 14, 020; En vigueur: 20-03-2016>",
                            "numbered_provisions": [],
                            "abrogation_status": "abrogé",
                            "main_text": "<article class=\"legal-article\" id=\"art-18\"><header class=\"article-header\"><h2 class=\"article-number\">Article 18</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"14\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 14, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 0,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.309652"
                            },
                            "legal_citation": {
                                "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 14, 020; En vigueur: 20-03-2016",
                                "urls": [
                                "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                                ]
                            },
                            "enhanced_citations": [
                                {
                                "citation_type": "abrogation",
                                "law_type": "AGF",
                                "dossier_number": "2016-01-15/17",
                                "article_number": "14",
                                "sequence_number": "020",
                                "effective_date": "20-03-2016",
                                "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                                "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 14, 020; En vigueur: 20-03-2016>",
                                "prefix": "Abrogé par",
                                "raw_dossier": "2016-01-15/17",
                                "raw_article": "14",
                                "start_pos": 0,
                                "end_pos": 166,
                                "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 14, 020; En vigueur: 20-03-2016>"
                                }
                            ]
                            }
                        },
                        "footnotes": [],
                        "footnote_references": []
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 3. Instruction et avis.",
                "metadata": {
                    "title_type": "Section 3.",
                    "title_content": "Instruction et avis.",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 19",
                    "metadata": {
                        "article_range": "19",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "19",
                        "anchor_id": "art_19",
                        "content": {
                        "main_text_raw": "§ 1er. Le Fonds examine si la demande visée à l'article 4, et pour ce qui concerne des structures de l'aide à la jeunesse, des centres pour troubles du développement et les services autorisés de placement familial et la demande visée à l'article 13 répondent aux dispositions respectivement des articles 4, 13 à 16 inclus, et établit une estimation des incidences financières du projet sur les exercices budgétaires successifs. Dans les trente jours calendaires de la réception de la demande, telle que visé à l'alinéa premier, le Fonds envoie un accusé de réception au demandeur, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La recevabilité implique que la demande remplit les exigences formelles mentionnées au premier alinéa. La date de recevabilité est la date de réception de la demande recevable. Le Fonds peut poser des questions supplémentaires au demandeur afin de pouvoir décider de la recevabilité de la demande. Le délai visé à l'alinéa 2 est suspendu jusqu'à ce que le demandeur ait répondu aux questions supplémentaires. Si le demandeur ne fournit pas les renseignements complémentaires au Fonds dans un délai d'un an, la demande visée à l'alinéa 1er est réputée inexistante. Dans ce cas, le Fonds en informe le demandeur § 2. Dans les dix jours calendaires de la date de recevabilité de la demande, mentionnée à l'article 4, et pour... des structures de l'aide à la jeunesse, des centres pour troubles du développement et les services autorisés de placement familial, après la date de recevabilité de la demande, mentionnée à l'article 13, le Fonds prend l'avis: 1° de l'administration fonctionnellement compétente sur les aspects de fond, entre autres sur les normes d'agrément, les conditions de qualité, la programmation et le demandeur, sur les priorités entre les demandes des différents demandeurs, et, pour... des structures de l'aide à la jeunesse, des centres pour troubles du développement et les services autorisés de placement familial, sur la conformité au plan stratégique en matière de soins approuvé; 2° d'un ou plusieurs fonctionnaires mis à la disposition du Fonds, sur les aspects financiers, sur la conformité aux normes techniques et physiques de la construction, les aspects techniques et l'estimation du coût et, s'il s'agit d'une demande d'une promesse de subvention pour l'acquisition d'immeubles, sur la valeur vénale des immeubles, et sur le contrôle de la parenté, visée aux articles 2bis et 2ter.] § 3. Les administrations fonctionnellement compétentes et les fonctionnaires visés au § 2 peuvent demander des informations supplémentaires au demandeur. Ils remettent leur avis au Fonds dans les cent vingt jours calendaires de la réception de la demande d'avis. § 4. Sur la base des différents avis, visés au § 3, le Fonds prépare pour chaque projet un avis et un projet de décision, qu'il soumet, accompagnés des avis précités, à l'Inspection des Finances, qui rend notamment avis sur la cohérence des promesses de subvention au sein du budget pluriannuel par secteur de la Communauté flamande. Sur la base de l'avis précité de l'Inspection des Finances, le Fonds présente son avis et son projet de décision au ministre..",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "de l'administration fonctionnellement compétente sur les aspects de fond, entre autres sur les normes d'agrément, les conditions de qualité, la programmation et [2 le demandeur",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "d'un ou plusieurs fonctionnaires mis à la disposition du Fonds, sur les aspects financiers, sur la conformité aux normes techniques et physiques de la construction, les aspects techniques et l'estimation du coût et, s'il s'agit d'une demande d'une promesse de subvention pour l'acquisition d'immeubles, sur la valeur vénale des immeubles [2, et sur le contrôle de la parenté, visée aux articles 2bis et 2ter",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-19\"><header class=\"article-header\"><h2 class=\"article-number\">Article 19</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p>Le Fonds examine si la demande visée à l'article 4, et pour ce qui concerne<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"des structures de l'aide à la jeunesse, des centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.15\" data-article-dossier-number=\"\">des structures de l'aide à la jeunesse, des centres pour troubles du développement</span>et les services autorisés de placement familial et la demande visée à l'article 13 répondent aux dispositions respectivement des articles 4, 13 à 16 inclus, et établit une estimation des incidences financières du projet sur les exercices budgétaires successifs. Dans les<span class=\"footnote-ref\" data-footnote-id=\"7\" data-referenced-text=\"trente\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.3\" data-article-dossier-number=\"\">trente</span>jours calendaires de la réception de la demande, telle que visé à l'alinéa premier, le Fonds envoie un accusé de réception<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"au demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.23\" data-article-dossier-number=\"\">au demandeur</span>, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La recevabilité implique que la demande remplit les exigences formelles mentionnées au premier alinéa. La date de recevabilité est la date de réception de la demande recevable.<span class=\"footnote-ref\" data-footnote-id=\"7\" data-referenced-text=\"Le Fonds peut poser des questions supplémentaires au demandeur afin de pouvoir décider de la recevabilité de la demande. Le délai visé à l'alinéa 2 est suspendu jusqu'à ce que le demandeur ait répondu aux questions supplémentaires.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.3\" data-article-dossier-number=\"\">Le Fonds peut poser des questions supplémentaires au demandeur afin de pouvoir décider de la recevabilité de la demande. Le délai visé à l'alinéa 2 est suspendu jusqu'à ce que le demandeur ait répondu aux questions supplémentaires.</span><span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"Si le demandeur ne fournit pas les renseignements complémentaires au Fonds dans un délai d'un an, la demande visée à l'alinéa 1er est réputée inexistante. Dans ce cas, le Fonds en informe le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.4\" data-article-dossier-number=\"\">Si le demandeur ne fournit pas les renseignements complémentaires au Fonds dans un délai d'un an, la demande visée à l'alinéa 1er est réputée inexistante. Dans ce cas, le Fonds en informe le demandeur</span></p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p class=\"intro-text\">Dans les dix jours calendaires de la date de recevabilité de la demande, mentionnée à l'article 4, et pour<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.15\" data-article-dossier-number=\"\">...</span><span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"des structures de l'aide à la jeunesse, des centres pour troubles du développement\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.15\" data-article-dossier-number=\"\">des structures de l'aide à la jeunesse, des centres pour troubles du développement</span>et les services autorisés de placement familial, après la date de recevabilité de la demande, mentionnée à l'article 13, le Fonds prend l'avis:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">de l'administration fonctionnellement compétente sur les aspects de fond, entre autres sur les normes d'agrément, les conditions de qualité, la programmation et [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.23\" data-article-dossier-number=\"\">le demandeur</span></span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">d'un ou plusieurs fonctionnaires mis à la disposition du Fonds, sur les aspects financiers, sur la conformité aux normes techniques et physiques de la construction, les aspects techniques et l'estimation du coût et, s'il s'agit d'une demande d'une promesse de subvention pour l'acquisition d'immeubles, sur la valeur vénale des immeubles [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\", et sur le contrôle de la parenté, visée aux articles 2bis et 2ter\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.23\" data-article-dossier-number=\"\">, et sur le contrôle de la parenté, visée aux articles 2bis et 2ter</span></span></li></ol><p class=\"closing-text\">e fond, entre autres sur les normes d'agrément, les conditions de qualité, la programmation et le demandeur, sur les priorités entre les demandes des différents demandeurs, et, pour... des structures de l'aide à la jeunesse, des centres pour troubles du développement et les services autorisés de placement familial, sur la conformité au plan stratégique en matière de soins approuvé; 2° d'un ou plusieurs fonctionnaires mis à la disposition du Fonds, sur les aspects financiers, sur la conformité aux normes techniques et physiques de la construction, les aspects techniques et l'estimation du coût et, s'il s'agit d'une demande d'une promesse de subvention pour l'acquisition d'immeubles, sur la valeur vénale des immeubles, et sur le contrôle de la parenté, visée aux articles 2bis et 2ter.]</p></div></section><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>Les administrations fonctionnellement compétentes et les fonctionnaires visés au § 2 peuvent demander des informations supplémentaires<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"au demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.23\" data-article-dossier-number=\"\">au demandeur</span>. Ils remettent leur avis au Fonds dans les<span class=\"footnote-ref\" data-footnote-id=\"6\" data-referenced-text=\"cent vingt\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2021071632#Art.9\" data-article-dossier-number=\"\">cent vingt</span>jours calendaires de la réception de la demande d'avis.</p></div></section><section class=\"paragraph\" id=\"para-4\"><h3 class=\"paragraph-marker\">§ 4.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"Sur la base des différents avis, visés au § 3, le Fonds prépare pour chaque projet un avis et un projet de décision, qu'il soumet, accompagnés des avis précités, à l'Inspection des Finances, qui rend notamment avis sur la cohérence des promesses de subvention au sein du budget pluriannuel par secteur de la Communauté flamande. Sur la base de l'avis précité de l'Inspection des Finances, le Fonds présente son avis et son projet de décision au ministre.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.4\" data-article-dossier-number=\"\">Sur la base des différents avis, visés au § 3, le Fonds prépare pour chaque projet un avis et un projet de décision, qu'il soumet, accompagnés des avis précités, à l'Inspection des Finances, qui rend notamment avis sur la cohérence des promesses de subvention au sein du budget pluriannuel par secteur de la Communauté flamande. Sur la base de l'avis précité de l'Inspection des Finances, le Fonds présente son avis et son projet de décision au ministre.</span>.</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 4,
                            "provision_count": 2,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.311054"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 16, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 16",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.16"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 23, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 23",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.23"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-09-05/12](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512), art. 10, 018; En vigueur : 13-11-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-09-05/12",
                            "article_number": "art. 10",
                            "sequence_number": "018",
                            "full_reference": "AGF [2014-09-05/12]"
                        },
                        "effective_date": "13-11-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014090512#Art.10"
                        },
                        {
                        "footnote_number": "5",
                        "footnote_content": "(5)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 15, 020; En vigueur : 20-03-2016>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-01-15/17",
                            "article_number": "art. 15",
                            "sequence_number": "020",
                            "full_reference": "AGF [2016-01-15/17]"
                        },
                        "effective_date": "20-03-2016",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.15"
                        },
                        {
                        "footnote_number": "6",
                        "footnote_content": "(6)<AGF [2021-07-16/32](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632), art. 9, 028; En vigueur : 20-09-2021>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2021-07-16/32",
                            "article_number": "art. 9",
                            "sequence_number": "028",
                            "full_reference": "AGF [2021-07-16/32]"
                        },
                        "effective_date": "20-09-2021",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2021071632#Art.9"
                        },
                        {
                        "footnote_number": "7",
                        "footnote_content": "(7)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 3, 029; En vigueur : 12-08-2022>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2022-05-06/08",
                            "article_number": "art. 3",
                            "sequence_number": "029",
                            "full_reference": "AGF [2022-05-06/08]"
                        },
                        "effective_date": "12-08-2022",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.3"
                        },
                        {
                        "footnote_number": "8",
                        "footnote_content": "(8)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 4, 034; En vigueur : 21-09-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-07-19/42",
                            "article_number": "art. 4",
                            "sequence_number": "034",
                            "full_reference": "AGF [2024-07-19/42]"
                        },
                        "effective_date": "21-09-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.4"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "5",
                        "text_position": 87,
                        "referenced_text": "des structures de l'aide à la jeunesse, des centres pour troubles du développement",
                        "embedded_law_references": [],
                        "bracket_pattern": "[5 des structures de l'aide à la jeunesse, des centres pour troubles du développement]5"
                        },
                        {
                        "reference_number": "7",
                        "text_position": 455,
                        "referenced_text": "trente",
                        "embedded_law_references": [],
                        "bracket_pattern": "[7 trente]7"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 590,
                        "referenced_text": "au demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 au demandeur]2"
                        },
                        {
                        "reference_number": "7",
                        "text_position": 890,
                        "referenced_text": "Le Fonds peut poser des questions supplémentaires au demandeur afin de pouvoir décider de la recevabilité de la demande. Le délai visé à l'alinéa 2 est suspendu jusqu'à ce que le demandeur ait répondu aux questions supplémentaires.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[7 Le Fonds peut poser des questions supplémentaires au demandeur afin de pouvoir décider de la recevabilité de la demande. Le délai visé à l'alinéa 2 est suspendu jusqu'à ce que le demandeur ait répondu aux questions supplémentaires.]7"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 1127,
                        "referenced_text": "Si le demandeur ne fournit pas les renseignements complémentaires au Fonds dans un délai d'un an, la demande visée à l'alinéa 1er est réputée inexistante. Dans ce cas, le Fonds en informe le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 Si le demandeur ne fournit pas les renseignements complémentaires au Fonds dans un délai d'un an, la demande visée à l'alinéa 1er est réputée inexistante. Dans ce cas, le Fonds en informe le demandeur]8"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 1451,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 ...]4"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 1463,
                        "referenced_text": "des structures de l'aide à la jeunesse, des centres pour troubles du développement",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 des structures de l'aide à la jeunesse, des centres pour troubles du développement]6"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1866,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1937,
                        "referenced_text": "demandeurs",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 demandeurs]2"
                        },
                        {
                        "reference_number": "5",
                        "text_position": 1963,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[5 ...]5"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 1976,
                        "referenced_text": "des structures de l'aide à la jeunesse, des centres pour troubles du développement",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 des structures de l'aide à la jeunesse, des centres pour troubles du développement]6"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 2528,
                        "referenced_text": ", et sur le contrôle de la parenté, visée aux articles 2bis et 2ter",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 , et sur le contrôle de la parenté, visée aux articles 2bis et 2ter]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 2751,
                        "referenced_text": "au demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 au demandeur]2"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 2812,
                        "referenced_text": "cent vingt",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 cent vingt]6"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 2898,
                        "referenced_text": "Sur la base des différents avis, visés au § 3, le Fonds prépare pour chaque projet un avis et un projet de décision, qu'il soumet, accompagnés des avis précités, à l'Inspection des Finances, qui rend notamment avis sur la cohérence des promesses de subvention au sein du budget pluriannuel par secteur de la Communauté flamande. Sur la base de l'avis précité de l'Inspection des Finances, le Fonds présente son avis et son projet de décision au ministre.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 Sur la base des différents avis, visés au § 3, le Fonds prépare pour chaque projet un avis et un projet de décision, qu'il soumet, accompagnés des avis précités, à l'Inspection des Finances, qui rend notamment avis sur la cohérence des promesses de subvention au sein du budget pluriannuel par secteur de la Communauté flamande. Sur la base de l'avis précité de l'Inspection des Finances, le Fonds présente son avis et son projet de décision au ministre.]8"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 4. Décision [1 ...]1",
                "metadata": {
                    "title_type": "Section 4.",
                    "title_content": "Décision [1 ...]1",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 20",
                    "metadata": {
                        "article_range": "20",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "20",
                        "anchor_id": "art_20",
                        "content": {
                        "main_text_raw": "§ 1er. En cas d'avis favorable du Fonds, le Fonds soumet à la signature du Ministre dans les quinze jours calendrier de l'avis, un projet de lettre acceptant le plan maître du demandeur. L'acceptation du plan maître ne constitue pas un engagement à accorder une promesse de subvention à tous les projets figurant au plan maître. En même temps, un projet de promesse de subvention est soumis à la signature du Ministre. Le Fonds doit être en possession de l'autorisation urbanistique ou du permis d'environnement pour le projet, avant que la promesse de subvention pour le projet puisse être accordée..] La promesse de subvention contient notamment le plan maître et le projet auquel la promesse de subvention se rapporte, les remarques éventuelles et la date de prise d'effet de la validité de la promesse de subvention...., en cas de force majeure, Le délai de validité de la promesse de la subvention peut être prolongé: 1° par le Fonds, si ce délai de validité est prolongé de deux ans maximum; 2° par le ministre, si ce délai de validité est prolongé de plus de deux ans. Si un investisseur réalise le projet et le met à la disposition du demandeur, des modalités financières supplémentaires peuvent être intégrées dans la promesse de subvention. Ces modalités peuvent avoir rapport: 1° aux modalités de paiement de la subvention d'investissement par le Fonds par dérogation aux dispositions de la section 4 du Chapitre III; 2° à la comptabilisation de la subvention d'investissement dans la base de calcul de l'indemnité périodique dont le demandeur est redevable à l'égard de l'investisseur. § 2. En cas d'avis défavorable du Fonds, le Fonds soumet un projet de lettre au Ministre..., qui précise les motifs du refus d'une promesse de subvention. § 2bis.... § 3. Le demandeur est informé... soit de la promesse de subvention soit de la décision négative motivée, par une lettre recommandée à la poste. § 4. Au plus tard nonante jours calendaires avant l'ordre de commencement des travaux qui portent sur le projet, le demandeur peut demander une modification de la promesse de subvention auprès du Fonds. Cette demande de dérogation est motivée de manière circonstanciée et comprend les documents modifiés par rapport à la demande relative à la promesse de subvention initiale. Si le montant de la demande de la nouvelle promesse de subvention dépasse de plus de 10% le montant de la promesse de subvention initiale, les articles 19 et 20, §§ 1er à 3 inclus, s'appliquent par analogue à la procédure de modification de la promesse de subvention, étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances, visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros. Si le montant de la demande de la nouvelle promesse de subvention dépasse au maximum de 10% le montant de la promesse de subvention initiale, les articles 19 et 20, §§ 1er à 3 inclus, s'appliquent par analogue à la procédure de modification de la promesse de subvention, étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros. Le projet de décision sur la promesse de subvention modifiée est établi par le Fonds et soumis au Ministre pour décision. § 5. Le montant de la promesse de subvention est adapté par le Fonds à l'indice de la construction qui est valable au moment de l'ordre de commencement des travaux ou du placement de la commande, conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels. Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, au moment de l'ordre de commencement des travaux, et conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels, le montant de la promesse de subvention est ajusté par le Fonds d'une modification de l'indice, calculée comme suit: SLO x 50 % x (iAB/iSLO -1), où: 1° SLO: le montant de la promesse de subvention, à savoir la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention; 2° iAB: l'indice de construction dans l'année de l'ordre de commencement des travaux. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué; 3° iSLO: l'indice de construction dans l'année de la promesse de subvention. Pour l'infrastructure avec un ordre de commencement des travaux en 2021, la modification de l'indice visée à l'alinéa 2 est calculée selon l'indice de construction de 2022. Si l'ordre de commencement a été donné avant le 1er janvier 2023, la modification de l'indice visée à l'alinéa 2 correspond au minimum au montant de l'indice tel que calculé de la manière applicable avant le 1er janvier 2023. Le montant de la promesse de subvention indexé conformément au présent paragraphe, constitue la base de tous les éléments suivants: 1° le paiement des tranches de subvention 1 à 5, visées à la section 4; 2° le calcul du plafond de construction. La différence positive éventuelle entre la modification de l'indice, visée à l'alinéa 2, et le montant de l'indice calculé de la manière applicable avant le 1er janvier 2023, est payée selon le rythme et la part des tranches de subvention qui n'ont pas encore été payées.",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "par le Fonds, si ce délai de validité est prolongé de deux ans maximum",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "par le ministre, si ce délai de validité est prolongé de plus de deux ans",
                            "sub_items": []
                            },
                            {
                            "number": "1°",
                            "text": "aux modalités de paiement de la subvention d'investissement par le Fonds par dérogation aux dispositions de la section 4 du Chapitre III",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "à la comptabilisation de la subvention d'investissement dans la base de calcul de l'indemnité périodique dont le demandeur est redevable à l'égard de l'investisseur.",
                            "sub_items": []
                            },
                            {
                            "number": "1°",
                            "text": "SLO: le montant de la promesse de subvention, à savoir la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "iAB: l'indice de construction dans l'année de l'ordre de commencement des travaux. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué",
                            "sub_items": []
                            },
                            {
                            "number": "3°",
                            "text": "iSLO: l'indice de construction dans l'année de la promesse de subvention.",
                            "sub_items": []
                            },
                            {
                            "number": "1°",
                            "text": "le paiement des tranches de subvention 1 à 5, visées à la section 4",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "le calcul du plafond de construction.",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-20\"><header class=\"article-header\"><h2 class=\"article-number\">Article 20</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p class=\"intro-text\">En cas d'avis favorable<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"du Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">du Fonds</span>,<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"le Fonds soumet\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.18\" data-article-dossier-number=\"\">le Fonds soumet</span>à la signature<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"du Ministre\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.18\" data-article-dossier-number=\"\">du Ministre</span>dans les quinze jours calendrier de l'avis, un projet de lettre acceptant le plan maître<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.24\" data-article-dossier-number=\"\">du demandeur</span>. L'acceptation du plan maître ne constitue pas un engagement à accorder une promesse de subvention à tous les projets figurant au plan maître.<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"En même temps, un projet de promesse de subvention est soumis à la signature du Ministre. Le Fonds doit être en possession de l'autorisation urbanistique ou du permis d'environnement pour le projet, avant que la promesse de subvention pour le projet puisse être accordée.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.7\" data-article-dossier-number=\"\">En même temps, un projet de promesse de subvention est soumis à la signature du Ministre. Le Fonds doit être en possession de l'autorisation urbanistique ou du permis d'environnement pour le projet, avant que la promesse de subvention pour le projet puisse être accordée.</span>.] La promesse de subvention contient notamment le plan maître et le projet auquel la promesse de subvention se rapporte, les remarques éventuelles et la date de prise d'effet de la validité de la promesse de subvention<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">...</span>., en cas de force majeure, Le délai de validité de la promesse de la subvention peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai de validité est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre,<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"Le délai de validité de la promesse de la subvention peut être prolongé : 1° par le Fonds, si ce délai de validité est prolongé de deux ans maximum ; 2° par le ministre, si ce délai de validité est prolongé de plus de deux ans\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">si ce délai de validité est prolongé de plus de deux ans</span></span></li></ol><p class=\"intro-text\">. Si un investisseur réalise le projet et le met à la disposition du demandeur, des modalités financières supplémentaires peuvent être intégrées dans la promesse de subvention. Ces modalités peuvent avoir rapport:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">aux modalités de paiement de la subvention d'investissement par le Fonds par dérogation aux dispositions de la section 4 du Chapitre III</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">à la comptabilisation de la subvention d'investissement dans la base de calcul de l'indemnité périodique dont le demandeur est redevable à l'égard de l'investisseur.</span></li></ol></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>En cas d'avis défavorable<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"du Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">du Fonds</span>,<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"le Fonds soumet\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.18\" data-article-dossier-number=\"\">le Fonds soumet</span>un projet de lettre<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"au Ministre\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.18\" data-article-dossier-number=\"\">au Ministre</span><span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">...</span>, qui précise les motifs du refus d'une promesse de subvention.</p></div></section><section class=\"paragraph\" id=\"para-2bis\"><h3 class=\"paragraph-marker\">§ 2bis.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">...</span></p></div></section><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.24\" data-article-dossier-number=\"\">Le demandeur</span>est informé<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">...</span>soit de la promesse de subvention soit de la décision négative motivée, par une lettre recommandée à la poste.</p></div></section><section class=\"paragraph\" id=\"para-4\"><h3 class=\"paragraph-marker\">§ 4.</h3><div class=\"paragraph-content\"><p>Au plus tard nonante jours calendaires avant l'ordre de commencement des travaux qui portent sur le projet, le demandeur peut demander une<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"modification\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">modification</span>de la promesse de subvention auprès<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"du Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">du Fonds</span>. Cette demande de dérogation est motivée de manière circonstanciée et comprend les documents modifiés par rapport à la demande relative à la promesse de subvention initiale. Si le montant de la demande de la nouvelle promesse de subvention dépasse de plus de 10% le montant de la promesse de subvention initiale, les articles 19 et 20, §§ 1er à 3 inclus, s'appliquent par analogue à la procédure de modification de la promesse de subvention<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\", étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances, visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">, étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances, visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros</span>. Si le montant de la demande de la nouvelle promesse de subvention dépasse au maximum de 10% le montant de la promesse de subvention initiale, les articles 19 et 20, §§ 1er à 3 inclus, s'appliquent par analogue à la procédure de modification de la promesse de subvention, étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros. Le projet de décision sur la promesse de subvention modifiée est établi par le Fonds et soumis<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"au Ministre\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039#Art.18\" data-article-dossier-number=\"\">au Ministre</span>pour décision.</p></div></section><section class=\"paragraph\" id=\"para-5\"><h3 class=\"paragraph-marker\">§ 5.</h3><div class=\"paragraph-content\"><p class=\"intro-text\"><span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"§ 5. Le montant de la promesse de subvention est adapté par le Fonds à l'indice de la construction qui est valable au moment de l'ordre de commencement des travaux ou du placement de la commande, conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517#Art.16\" data-article-dossier-number=\"\">Le montant de la promesse de subvention est adapté par le Fonds à l'indice de la construction qui est valable au moment de l'ordre de commencement des travaux ou du placement de la commande, conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels.</span>Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, au moment de l'ordre de commencement des travaux, et conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels, le montant de la promesse de subvention est<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"ajusté par le Fonds d'une modification de l'indice\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">ajusté par le Fonds d'une modification de l'indice</span>, calculée comme suit:<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"SLO x 50 % x (iAB/iSLO -1)\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">SLO x 50 % x (iAB/iSLO -1)</span>, où:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">SLO: le montant de la promesse de subvention, à savoir la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">iAB: l'indice de construction dans l'année de l'ordre de commencement des travaux. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">iSLO: l'indice de construction dans l'année de la promesse de subvention.</span></li></ol><p class=\"intro-text\">Pour l'infrastructure avec un ordre de commencement des travaux en 2021, la<span class=\"footnote-ref\" data-footnote-id=\"8\" data-referenced-text=\"modification\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.5\" data-article-dossier-number=\"\">modification</span>de l'indice visée à l'alinéa 2 est calculée selon l'indice de construction de 2022. Si l'ordre de commencement a été donné avant le 1er janvier 2023, la modification de l'indice visée à l'alinéa 2 correspond au minimum au montant de l'indice tel que calculé de la manière applicable avant le 1er janvier 2023. Le montant de la promesse de subvention indexé conformément au présent paragraphe, constitue la base de tous les éléments suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">le paiement des tranches de subvention 1 à 5, visées à la section 4</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le calcul du plafond de construction.</span></li></ol><p class=\"closing-text\">La différence positive éventuelle entre la modification de l'indice, visée à l'alinéa 2, et le montant de l'indice calculé de la manière applicable avant le 1er janvier 2023, est payée selon le rythme et la part des tranches de subvention qui n'ont pas encore été payées.</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 6,
                            "provision_count": 9,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.314512"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 18, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 18",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.18"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 24, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 24",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.24"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 10, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 10",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.10"
                        },
                        {
                        "footnote_number": "4",
                        "footnote_content": "(4)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 16, 020; En vigueur : 20-03-2016>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-01-15/17",
                            "article_number": "art. 16",
                            "sequence_number": "020",
                            "full_reference": "AGF [2016-01-15/17]"
                        },
                        "effective_date": "20-03-2016",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.16"
                        },
                        {
                        "footnote_number": "5",
                        "footnote_content": "(5)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 7, 022; En vigueur : 11-10-2018>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2018-07-06/25",
                            "article_number": "art. 7",
                            "sequence_number": "022",
                            "full_reference": "AGF [2018-07-06/25]"
                        },
                        "effective_date": "11-10-2018",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.7"
                        },
                        {
                        "footnote_number": "6",
                        "footnote_content": "(6)<AGF [2019-05-17/67](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767), art. 3, 024; En vigueur : 19-09-2019>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2019-05-17/67",
                            "article_number": "art. 3",
                            "sequence_number": "024",
                            "full_reference": "AGF [2019-05-17/67]"
                        },
                        "effective_date": "19-09-2019",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767#Art.3"
                        },
                        {
                        "footnote_number": "7",
                        "footnote_content": "(7)<AGF [2023-01-13/05](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023011305), art. 1, 030; En vigueur : 01-01-2023>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2023-01-13/05",
                            "article_number": "art. 1",
                            "sequence_number": "030",
                            "full_reference": "AGF [2023-01-13/05]"
                        },
                        "effective_date": "01-01-2023",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023011305",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023011305#Art.1"
                        },
                        {
                        "footnote_number": "8",
                        "footnote_content": "(8)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 5, 034; En vigueur : 21-09-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-07-19/42",
                            "article_number": "art. 5",
                            "sequence_number": "034",
                            "full_reference": "AGF [2024-07-19/42]"
                        },
                        "effective_date": "21-09-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.5"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "8",
                        "text_position": 31,
                        "referenced_text": "du Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 du Fonds]8"
                        },
                        {
                        "reference_number": "1",
                        "text_position": 46,
                        "referenced_text": "le Fonds soumet",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 le Fonds soumet]1"
                        },
                        {
                        "reference_number": "1",
                        "text_position": 82,
                        "referenced_text": "du Ministre",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 du Ministre]1"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 188,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        },
                        {
                        "reference_number": "5",
                        "text_position": 351,
                        "referenced_text": "En même temps, un projet de promesse de subvention est soumis à la signature du Ministre. Le Fonds doit être en possession de l'autorisation urbanistique ou du permis d'environnement pour le projet, avant que la promesse de subvention pour le projet puisse être accordée.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[5 En même temps, un projet de promesse de subvention est soumis à la signature du Ministre. Le Fonds doit être en possession de l'autorisation urbanistique ou du permis d'environnement pour le projet, avant que la promesse de subvention pour le projet puisse être accordée.]5"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 856,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 ...]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 891,
                        "referenced_text": "Le délai de validité de la promesse de la subvention peut être prolongé :  \n1° par le Fonds, si ce délai de validité est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai de validité est prolongé de plus de deux ans",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 Le délai de validité de la promesse de la subvention peut être prolongé :  \n1° par le Fonds, si ce délai de validité est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai de validité est prolongé de plus de deux ans]8"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 1133,
                        "referenced_text": "Si un investisseur réalise le projet et le met à la disposition du demandeur, des modalités financières supplémentaires peuvent être intégrées dans la promesse de subvention. Ces modalités peuvent avoir rapport :  \n1° aux modalités de paiement de la subvention d'investissement par le Fonds par dérogation aux dispositions de la section 4 du Chapitre III ;  \n2° à la comptabilisation de la subvention d'investissement dans la base de calcul de l'indemnité périodique dont le demandeur est redevable à l'égard de l'investisseur.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 Si un investisseur réalise le projet et le met à la disposition du demandeur, des modalités financières supplémentaires peuvent être intégrées dans la promesse de subvention. Ces modalités peuvent avoir rapport :  \n1° aux modalités de paiement de la subvention d'investissement par le Fonds par dérogation aux dispositions de la section 4 du Chapitre III ;  \n2° à la comptabilisation de la subvention d'investissement dans la base de calcul de l'indemnité périodique dont le demandeur est redevable à l'égard de l'investisseur.]6"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 1699,
                        "referenced_text": "du Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 du Fonds]8"
                        },
                        {
                        "reference_number": "1",
                        "text_position": 1714,
                        "referenced_text": "le Fonds soumet",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 le Fonds soumet]1"
                        },
                        {
                        "reference_number": "1",
                        "text_position": 1755,
                        "referenced_text": "au Ministre",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 au Ministre]1"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 1772,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 ...]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 1858,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 ...]8"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1874,
                        "referenced_text": "Le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 Le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 1904,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 2679,
                        "referenced_text": ", étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances, visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 , étant entendu qu'il n'y a pas d'intervention de l'Inspection des Finances, visée à l'article 19, § 4, à moins que le montant de subvention s'élève à au moins 250 000 euros]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 3180,
                        "referenced_text": "l'Inspection des Finances",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 l'Inspection des Finances]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 3237,
                        "referenced_text": ", à moins que le montant de subvention s'élève à au moins 250 000 euros",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 , à moins que le montant de subvention s'élève à au moins 250 000 euros]8"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 3447,
                        "referenced_text": "§ 5. Le montant de la promesse de subvention est adapté par le Fonds à l'indice de la construction qui est valable au moment de l'ordre de commencement des travaux ou du placement de la commande, conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 § 5. Le montant de la promesse de subvention est adapté par le Fonds à l'indice de la construction qui est valable au moment de l'ordre de commencement des travaux ou du placement de la commande, conformément aux dispositions et aux règles de calcul visées aux arrêtés sectoriels.]4"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 4012,
                        "referenced_text": "ajusté par le Fonds d'une modification de l'indice",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 ajusté par le Fonds d'une modification de l'indice]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 4091,
                        "referenced_text": "SLO x 50 % x (iAB/iSLO -1)",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 SLO x 50 % x (iAB/iSLO -1)]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 4647,
                        "referenced_text": "modification",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 modification]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 4820,
                        "referenced_text": "modification",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 modification]8"
                        },
                        {
                        "reference_number": "8",
                        "text_position": 5280,
                        "referenced_text": "modification",
                        "embedded_law_references": [],
                        "bracket_pattern": "[8 modification]8"
                        }
                    ]
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE III. [1 \\- Exécution du projet et paiement de la subvention d'investissement.]1",
            "metadata": {
                "title_type": "CHAPITRE III.",
                "title_content": "[1 \\- Exécution du projet et paiement de la subvention d'investissement.]1",
                "rank": 2
            },
            "children": [
                {
                "type": "section",
                "label": "Section 1. [1 \\- Ordre de commencement des travaux, du placement de la commande ou de la passation de l'acte authentique.]1",
                "metadata": {
                    "title_type": "Section 1.",
                    "title_content": "[1 \\- Ordre de commencement des travaux, du placement de la commande ou de la passation de l'acte authentique.]1",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 21",
                    "metadata": {
                        "article_range": "21",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "21",
                        "anchor_id": "art_21",
                        "content": {
                        "main_text_raw": "Après réception de la promesse de subvention, le demandeur ou l'investisseur peuvent donner l'ordre d'entamer les travaux, il peut passer la commande ou faire passer l'acte authentique de l'achat. Après avoir ordonné d'entamer les travaux ou avoir passé la commande ou avoir passé l'acte authentique précité, le demandeur ou l'investisseur remettent sans tarder copie de l'ordre, de la commande ou de l'acte authentique au Fonds.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-21\"><header class=\"article-header\"><h2 class=\"article-number\">Article 21</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Après réception de la promesse de subvention,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur ou l'investisseur peuvent donner l'ordre\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019051767#Art.4\" data-article-dossier-number=\"\">le demandeur ou l'investisseur peuvent donner l'ordre</span>d'entamer les travaux, il peut passer la commande ou faire passer l'acte authentique de l'achat. Après avoir ordonné d'entamer les travaux ou avoir passé la commande ou avoir passé l'acte authentique précité,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur ou l'investisseur remettent sans tarder copie de l'ordre\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019051767#Art.4\" data-article-dossier-number=\"\">le demandeur ou l'investisseur remettent sans tarder copie de l'ordre</span>, de la commande ou de l'acte authentique au Fonds.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.314727"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 17, 020; En vigueur : 20-03-2016>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-01-15/17",
                            "article_number": "art. 17",
                            "sequence_number": "020",
                            "full_reference": "AGF [2016-01-15/17]"
                        },
                        "effective_date": "20-03-2016",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.17"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2019-05-17/67](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767), art. 4, 024; En vigueur : 19-09-2019>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2019-05-17/67",
                            "article_number": "art. 4",
                            "sequence_number": "024",
                            "full_reference": "AGF [2019-05-17/67]"
                        },
                        "effective_date": "19-09-2019",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767#Art.4"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 50,
                        "referenced_text": "le demandeur ou l'investisseur peuvent donner l'ordre",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur ou l'investisseur peuvent donner l'ordre]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 320,
                        "referenced_text": "le demandeur ou l'investisseur remettent sans tarder copie de l'ordre",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur ou l'investisseur remettent sans tarder copie de l'ordre]2"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 2. [1 \\- Paiement de la subvention d'investissement pour l'achat.]1",
                "metadata": {
                    "title_type": "Section 2.",
                    "title_content": "[1 \\- Paiement de la subvention d'investissement pour l'achat.]1",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 22",
                    "metadata": {
                        "article_range": "22",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "22",
                        "anchor_id": "art_22",
                        "content": {
                        "main_text_raw": "Pour un projet d'achat avec ou sans transformation, 90 % de la subvention d'investissement est versé après soumission de l'acte authentique d'achat auprès du Fonds. Au plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'acte authentique d'achat, le demandeur peut demander auprès du Fonds le paiement des 10 % restants de la subvention d'investissement. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Lors de sa demande, visée à l'alinéa 2, le demandeur transmet les pièces suivantes au Fonds: 1° un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention, et sur l'ensemble des modifications apportées par rapport à la promesse de subvention, sur le plan physique, technique, conceptuel et fonctionnel de la construction; 2° un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux; 3° une évaluation du projet, préparée sur la base du modèle fourni par le Fonds. Lors de sa demande, visée à l'alinéa 2, le demandeur tient à disposition du Fonds les données de consommation d'énergie et d'eau. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "par le ministre, si ce délai est prolongé de plus de deux ans.",
                            "sub_items": []
                            },
                            {
                            "number": "1°",
                            "text": "un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention, et sur l'ensemble des modifications apportées par rapport à la promesse de subvention, sur le plan physique, technique, conceptuel et fonctionnel de la construction",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux",
                            "sub_items": []
                            },
                            {
                            "number": "3°",
                            "text": "une évaluation du projet, préparée sur la base du modèle fourni par le Fonds.",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-22\"><header class=\"article-header\"><h2 class=\"article-number\">Article 22</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Pour un projet d'achat avec ou sans transformation, 90 % de la subvention d'investissement est versé après soumission de l'acte authentique d'achat auprès du Fonds. Au plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'acte authentique d'achat, le demandeur peut demander auprès du Fonds le paiement des 10 % restants de la subvention d'investissement. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre, si ce délai est prolongé de plus de deux ans.</span></li></ol><p class=\"intro-text\">Lors de sa demande,<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"Pour un projet d'achat avec ou sans transformation, 90 % de la subvention d'investissement est versé après soumission de l'acte authentique d'achat auprès du Fonds. Au plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'acte authentique d'achat, le demandeur peut demander auprès du Fonds le paiement des 10 % restants de la subvention d'investissement. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Lors de sa demande, visée à l'alinéa 2, le demandeur transmet les pièces suivantes au Fonds : 1° un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention, et sur l'ensemble des modifications apportées par rapport à la promesse de subvention, sur le plan physique, technique, conceptuel et fonctionnel de la construction ; 2° un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux ; 3° une évaluation du projet, préparée sur la base du modèle fourni par le Fonds. Lors de sa demande, visée à l'alinéa 2, le demandeur tient à disposition du Fonds les données de consommation d'énergie et d'eau. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.6\" data-article-dossier-number=\"\">visée à l'alinéa 2</span>, le demandeur transmet les pièces suivantes au Fonds:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention,<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"Pour un projet d'achat avec ou sans transformation, 90 % de la subvention d'investissement est versé après soumission de l'acte authentique d'achat auprès du Fonds. Au plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'acte authentique d'achat, le demandeur peut demander auprès du Fonds le paiement des 10 % restants de la subvention d'investissement. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Lors de sa demande, visée à l'alinéa 2, le demandeur transmet les pièces suivantes au Fonds : 1° un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention, et sur l'ensemble des modifications apportées par rapport à la promesse de subvention, sur le plan physique, technique, conceptuel et fonctionnel de la construction ; 2° un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux ; 3° une évaluation du projet, préparée sur la base du modèle fourni par le Fonds. Lors de sa demande, visée à l'alinéa 2, le demandeur tient à disposition du Fonds les données de consommation d'énergie et d'eau. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.6\" data-article-dossier-number=\"\">et sur l'ensemble des modifications apportées par rapport à la promesse de subvention</span>, sur le plan physique, technique, conceptuel et fonctionnel de la construction</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">une évaluation du projet, préparée sur la base du modèle fourni par le Fonds.</span></li></ol><p class=\"closing-text\">Lors de sa demande, visée à l'alinéa 2, le demandeur tient à disposition du Fonds les données de consommation d'énergie et d'eau. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 5,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.315545"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 6, 034; En vigueur : 21-09-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-07-19/42",
                            "article_number": "art. 6",
                            "sequence_number": "034",
                            "full_reference": "AGF [2024-07-19/42]"
                        },
                        "effective_date": "21-09-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.6"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "1",
                        "text_position": 0,
                        "referenced_text": "Pour un projet d'achat avec ou sans transformation, 90 % de la subvention d'investissement est versé après soumission de l'acte authentique d'achat auprès du Fonds.  \nAu plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'acte authentique d'achat, le demandeur peut demander auprès du Fonds le paiement des 10 % restants de la subvention d'investissement. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans.  \nLors de sa demande, visée à l'alinéa 2, le demandeur transmet les pièces suivantes au Fonds :  \n1° un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention, et sur l'ensemble des modifications apportées par rapport à la promesse de subvention, sur le plan physique, technique, conceptuel et fonctionnel de la construction ;  \n2° un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux ;  \n3° une évaluation du projet, préparée sur la base du modèle fourni par le Fonds.  \nLors de sa demande, visée à l'alinéa 2, le demandeur tient à disposition du Fonds les données de consommation d'énergie et d'eau.  \nLes demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 Pour un projet d'achat avec ou sans transformation, 90 % de la subvention d'investissement est versé après soumission de l'acte authentique d'achat auprès du Fonds.  \nAu plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'acte authentique d'achat, le demandeur peut demander auprès du Fonds le paiement des 10 % restants de la subvention d'investissement. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans.  \nLors de sa demande, visée à l'alinéa 2, le demandeur transmet les pièces suivantes au Fonds :  \n1° un rapport sur la manière dont le demandeur a donné suite aux remarques formulées relativement à la promesse de subvention, et sur l'ensemble des modifications apportées par rapport à la promesse de subvention, sur le plan physique, technique, conceptuel et fonctionnel de la construction ;  \n2° un programme final des exigences en matière de confort et d'utilisation d'énergie, d'eau et de matériaux ;  \n3° une évaluation du projet, préparée sur la base du modèle fourni par le Fonds.  \nLors de sa demande, visée à l'alinéa 2, le demandeur tient à disposition du Fonds les données de consommation d'énergie et d'eau.  \nLes demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant]1"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 3. [1 \\- Paiement de la subvention d'investissement uniquement destinée à l'équipement et au mobilier.]1",
                "metadata": {
                    "title_type": "Section 3.",
                    "title_content": "[1 \\- Paiement de la subvention d'investissement uniquement destinée à l'équipement et au mobilier.]1",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 23",
                    "metadata": {
                        "article_range": "23",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "23",
                        "anchor_id": "art_23",
                        "content": {
                        "main_text_raw": "La subvention d'investissement uniquement destinée à l'équipement et au mobilier est payée après approbation des livraisons par le Fonds et après la remise des documents suivants au Fonds: 1° le procès-verbal de la réception provisoire; 2° le décompte final. 3° une preuve que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Le demandeur soumet les documents par voie électronique via la plateforme mise à disposition par le Fonds. Le demandeur présente le compte final au plus tard trois ans après la commande. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans.. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "le procès-verbal de la réception provisoire",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "le décompte final.",
                            "sub_items": []
                            },
                            {
                            "number": "3°",
                            "text": "une preuve que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret.",
                            "sub_items": []
                            },
                            {
                            "number": "1°",
                            "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "par le ministre, si ce délai est prolongé de plus de deux ans.",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-23\"><header class=\"article-header\"><h2 class=\"article-number\">Article 23</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">La subvention d'investissement uniquement destinée à l'équipement et au mobilier est payée après approbation des livraisons par le Fonds et après la remise des documents suivants au Fonds:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">le procès-verbal de la réception provisoire</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le décompte final.</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">une preuve que le demandeur bénéficie d'un droit de jouissance,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"3° une preuve que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.9\" data-article-dossier-number=\"\">tel que visé à l'article 12 du décret.</span></span></li></ol><p class=\"intro-text\">Le demandeur soumet les documents par voie électronique via la plateforme mise à disposition par le Fonds. Le demandeur présente le compte final au plus tard trois ans après la commande. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre,<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.7\" data-article-dossier-number=\"\">si ce délai est prolongé de plus de deux ans.</span></span></li></ol><p class=\"closing-text\">. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 5,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.316169"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 17, 020; En vigueur : 20-03-2016>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-01-15/17",
                            "article_number": "art. 17",
                            "sequence_number": "020",
                            "full_reference": "AGF [2016-01-15/17]"
                        },
                        "effective_date": "20-03-2016",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.17"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 9, 022; En vigueur : 11-10-2018>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2018-07-06/25",
                            "article_number": "art. 9",
                            "sequence_number": "022",
                            "full_reference": "AGF [2018-07-06/25]"
                        },
                        "effective_date": "11-10-2018",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.9"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 5, 029; En vigueur : 12-08-2022>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2022-05-06/08",
                            "article_number": "art. 5",
                            "sequence_number": "029",
                            "full_reference": "AGF [2022-05-06/08]"
                        },
                        "effective_date": "12-08-2022",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.5"
                        },
                        {
                        "footnote_number": "4",
                        "footnote_content": "(4)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 7, 034; En vigueur : 21-09-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-07-19/42",
                            "article_number": "art. 7",
                            "sequence_number": "034",
                            "full_reference": "AGF [2024-07-19/42]"
                        },
                        "effective_date": "21-09-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.7"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "1",
                        "text_position": 0,
                        "referenced_text": "La subvention d'investissement uniquement destinée à l'équipement et au mobilier est payée après approbation des livraisons par le Fonds et après la remise des documents suivants au Fonds :  \n1° le procès-verbal de la réception provisoire ;  \n2° le décompte final.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 La subvention d'investissement uniquement destinée à l'équipement et au mobilier est payée après approbation des livraisons par le Fonds et après la remise des documents suivants au Fonds :  \n1° le procès-verbal de la réception provisoire ;  \n2° le décompte final.]1"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 272,
                        "referenced_text": "3° une preuve que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 3° une preuve que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret.]2"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 578,
                        "referenced_text": "En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans.]4"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 823,
                        "referenced_text": "Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.]4"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 4. [1 \\- Paiement de la subvention d'investissement.]1",
                "metadata": {
                    "title_type": "Section 4.",
                    "title_content": "[1 \\- Paiement de la subvention d'investissement.]1",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "sous-section",
                    "label": "Sous-section 1re. [1 \\- Paiement de la première tranche.]1",
                    "metadata": {
                        "title_type": "Sous-section 1re.",
                        "title_content": "[1 \\- Paiement de la première tranche.]1",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 24",
                        "metadata": {
                            "article_range": "24",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "24",
                            "anchor_id": "art_24",
                            "content": {
                            "main_text_raw": "Après réception d'une première facture de l'entrepreneur, \" et au plus tard cinq ans après l'ordre de démarrage des travaux le demandeur peut demander auprès du Fonds le paiement de la première tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Le demandeur joint à sa demande visée à l'alinéa premier: 1° le document prouvant que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé; 2° une copie de la première facture; 3° un aperçu des attributions. Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds. Après approbation par le Fonds, 25% de la subvention d'investissement est payé.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "par le ministre, si ce délai est prolongé de plus de deux ans",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "le document prouvant que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "une copie de la première facture",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "un aperçu des attributions. Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-24\"><header class=\"article-header\"><h2 class=\"article-number\">Article 24</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Après réception d'une première facture de l'entrepreneur,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"&quot; et au plus tard cinq ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.6\" data-article-dossier-number=\"\">&quot; et au plus tard cinq ans après l'ordre de démarrage des travaux</span>le demandeur peut demander auprès du Fonds le paiement de la première tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre, si ce délai est prolongé de plus de deux ans</span></li></ol><p class=\"intro-text\">. Le demandeur joint à sa demande visée à l'alinéa premier:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">le document prouvant que le demandeur bénéficie d'un droit de jouissance,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur joint à sa demande visée à l'alinéa premier : 1° le document prouvant que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé ; 2° une copie de la première facture ; 3° un aperçu des attributions. Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.10\" data-article-dossier-number=\"\">tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun</span>, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">une copie de la première facture</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">un aperçu des attributions.<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur joint à sa demande visée à l'alinéa premier : 1° le document prouvant que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé ; 2° une copie de la première facture ; 3° un aperçu des attributions. Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.10\" data-article-dossier-number=\"\">Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds</span></span></li></ol><p class=\"closing-text\">. Après approbation par le Fonds, 25% de la subvention d'investissement est payé.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 5,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.316912"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 10, 022; En vigueur : 11-10-2018>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-07-06/25",
                                "article_number": "art. 10",
                                "sequence_number": "022",
                                "full_reference": "AGF [2018-07-06/25]"
                            },
                            "effective_date": "11-10-2018",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.10"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 6, 029; En vigueur : 12-08-2022>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2022-05-06/08",
                                "article_number": "art. 6",
                                "sequence_number": "029",
                                "full_reference": "AGF [2022-05-06/08]"
                            },
                            "effective_date": "12-08-2022",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.6"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "3",
                            "text_position": 62,
                            "referenced_text": "\" et au plus tard cinq ans après l'ordre de démarrage des travaux",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3]\" et au plus tard cinq ans après l'ordre de démarrage des travaux][3]"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 265,
                            "referenced_text": "En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans]4"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 509,
                            "referenced_text": "Le demandeur joint à sa demande visée à l'alinéa premier :  \n1° le document prouvant que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé ;  \n2° une copie de la première facture ;  \n3° un aperçu des attributions. Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 Le demandeur joint à sa demande visée à l'alinéa premier :  \n1° le document prouvant que le demandeur bénéficie d'un droit de jouissance, tel que visé à l'article 12 du décret. Lorsqu'un acte authentique est requis suivant le droit commun, il s'agit d'un acte authentique, autrement il s'agit d'un acte enregistré sous seing privé ;  \n2° une copie de la première facture ;  \n3° un aperçu des attributions. Cet aperçu est établi sur la base d'un modèle mis à disposition par le Fonds]2"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 1085,
                            "referenced_text": "Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.]4"
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "type": "sous-section",
                    "label": "Sous-section 2. [1 \\- Paiement de la deuxième tranche.]1",
                    "metadata": {
                        "title_type": "Sous-section 2.",
                        "title_content": "[1 \\- Paiement de la deuxième tranche.]1",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 25",
                        "metadata": {
                            "article_range": "25",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "25",
                            "anchor_id": "art_25",
                            "content": {
                            "main_text_raw": "Lorsque 50 % des travaux sont terminés sur la base du plafond de construction calculé et au plus tard cinq ans après l'ordre de démarrage des travaux, le demandeur peut demander auprès du Fonds le paiement de la deuxième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ansr.]Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants: 1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel; 2° un aperçu des travaux exécutés et envisagés; 3° les factures ou états d'avancement transmis par l'entrepreneur; 4° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds; 5° une estimation actualisée suivant les différents types de travaux et par forme de soins; 6° un programme actualisé d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux; 7° les documents suivants attestant qu'il s'agit d'une construction durable: a) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds; b) études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB). Le demandeur tient les documents suivants à disposition: 1° les cahiers des charges; 2° le dossier d'attribution par adjudication, comprenant: a) le procès-verbal de l'ouverture des soumissions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur; Après contrôle par le Fonds, 25% de la subvention d'investissement est payé. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "par le ministre, si ce délai est prolongé de plus de deux ans",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "un aperçu des travaux exécutés et envisagés",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "les factures ou états d'avancement transmis par l'entrepreneur",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds",
                                "sub_items": []
                                },
                                {
                                "number": "5°",
                                "text": "une estimation actualisée suivant les différents types de travaux et par forme de soins",
                                "sub_items": []
                                },
                                {
                                "number": "6°",
                                "text": "un programme actualisé d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux",
                                "sub_items": []
                                },
                                {
                                "number": "7°",
                                "text": "les documents suivants attestant qu'il s'agit d'une construction durable:",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les cahiers des charges",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le dossier d'attribution par adjudication, comprenant:",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-25\"><header class=\"article-header\"><h2 class=\"article-number\">Article 25</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Lorsque 50 % des travaux sont terminés sur la base du plafond de construction calculé<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"et au plus tard cinq ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.7\" data-article-dossier-number=\"\">et au plus tard cinq ans après l'ordre de démarrage des travaux</span>, le demandeur peut demander auprès du Fonds le paiement de la deuxième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.9\" data-article-dossier-number=\"\">si ce délai est prolongé de plus de deux ans</span></span></li></ol><p class=\"intro-text\">r.]Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants : 1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel ; 2° un aperçu des travaux exécutés et envisagés ; 3° les factures ou états d'avancement transmis par l'entrepreneur ; 4° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds ; 5° une estimation actualisée suivant les différents types de travaux et par forme de soins ; 6° un programme actualisé d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux ; 7° les documents suivants attestant qu'il s'agit d'une construction durable : a) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds ; b) études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB). Le demandeur tient les documents suivants à disposition : 1° les cahiers des charges ; 2° le dossier d'attribution par adjudication, comprenant : a) le procès-verbal de l'ouverture des soumissions ; b) toutes les offres ; c) les rapports du contrôle des offres ; d) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur ; Après contrôle par le Fonds, 25% de la subvention d'investissement est payé.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.7\" data-article-dossier-number=\"\">et de toutes les modifications ayant été apportées par rapport à la promesse de subvention</span>, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">un aperçu des travaux exécutés et envisagés</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">les factures ou états d'avancement transmis par l'entrepreneur</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds</span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">une estimation actualisée suivant les différents types de travaux et par forme de soins</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">un programme actualisé d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">les documents suivants attestant qu'il s'agit d'une construction durable:</span></li></ol><p class=\"intro-text\">a) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds; b) études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB). Le demandeur tient les documents suivants à disposition:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les cahiers des charges</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le dossier d'attribution par adjudication, comprenant:</span></li></ol><p class=\"closing-text\">a) le procès-verbal de l'ouverture des soumissions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur; Après contrôle par le Fonds, 25% de la subvention d'investissement est payé. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 11,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.318422"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 17, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 17",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.17"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 7, 029; En vigueur : 12-08-2022>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2022-05-06/08",
                                "article_number": "art. 7",
                                "sequence_number": "029",
                                "full_reference": "AGF [2022-05-06/08]"
                            },
                            "effective_date": "12-08-2022",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.7"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 9, 034; En vigueur : 21-09-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-07-19/42",
                                "article_number": "art. 9",
                                "sequence_number": "034",
                                "full_reference": "AGF [2024-07-19/42]"
                            },
                            "effective_date": "21-09-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.9"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 90,
                            "referenced_text": "et au plus tard cinq ans après l'ordre de démarrage des travaux",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 et au plus tard cinq ans après l'ordre de démarrage des travaux]2"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 290,
                            "referenced_text": "En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans]3"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 530,
                            "referenced_text": "Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants :  \n1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel ;  \n2° un aperçu des travaux exécutés et envisagés ;  \n3° les factures ou états d'avancement transmis par l'entrepreneur ;  \n4° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds ;  \n5° une estimation actualisée suivant les différents types de travaux et par forme de soins ;  \n6° un programme actualisé d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux ;  \n7° les documents suivants attestant qu'il s'agit d'une construction durable :  \na) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds ;  \nb) études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB).  \nLe demandeur tient les documents suivants à disposition :  \n1° les cahiers des charges ;  \n2° le dossier d'attribution par adjudication, comprenant :  \na) le procès-verbal de l'ouverture des soumissions ;  \nb) toutes les offres ;  \nc) les rapports du contrôle des offres ;  \nd) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur ;  \nAprès contrôle par le Fonds, 25% de la subvention d'investissement est payé.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2  \nLe demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants :  \n1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel ;  \n2° un aperçu des travaux exécutés et envisagés ;  \n3° les factures ou états d'avancement transmis par l'entrepreneur ;  \n4° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds ;  \n5° une estimation actualisée suivant les différents types de travaux et par forme de soins ;  \n6° un programme actualisé d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux ;  \n7° les documents suivants attestant qu'il s'agit d'une construction durable :  \na) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds ;  \nb) études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB).  \nLe demandeur tient les documents suivants à disposition :  \n1° les cahiers des charges ;  \n2° le dossier d'attribution par adjudication, comprenant :  \na) le procès-verbal de l'ouverture des soumissions ;  \nb) toutes les offres ;  \nc) les rapports du contrôle des offres ;  \nd) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur ;  \nAprès contrôle par le Fonds, 25% de la subvention d'investissement est payé.]2"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 2225,
                            "referenced_text": "Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.]3"
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "type": "sous-section",
                    "label": "Sous-section 3. [1 \\- Paiement de la troisième tranche.]1",
                    "metadata": {
                        "title_type": "Sous-section 3.",
                        "title_content": "[1 \\- Paiement de la troisième tranche.]1",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 26",
                        "metadata": {
                            "article_range": "26",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "26",
                            "anchor_id": "art_26",
                            "content": {
                            "main_text_raw": "Lorsque 75% des travaux sont terminés sur la base du plafond de construction calculé et au plus tard cinq ans après l'ordre de démarrage des travaux, le demandeur peut demander auprès du Fonds le paiement de la troisième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans..]Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants: 1° les factures transmises par l'entrepreneur; 2° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds. Après contrôle par le Fonds, 25% de la subvention d'investissement est payé. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "par le ministre, si ce délai est prolongé de plus de deux ans.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les factures transmises par l'entrepreneur",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds.",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-26\"><header class=\"article-header\"><h2 class=\"article-number\">Article 26</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Lorsque 75% des travaux sont terminés sur la base du plafond de construction calculé<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"et au plus tard cinq ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.8\" data-article-dossier-number=\"\">et au plus tard cinq ans après l'ordre de démarrage des travaux</span>, le demandeur peut demander auprès du Fonds le paiement de la troisième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.10\" data-article-dossier-number=\"\">si ce délai est prolongé de plus de deux ans.</span></span></li></ol><p class=\"intro-text\">.]Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les factures transmises par l'entrepreneur</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds.</span></li></ol><p class=\"closing-text\">Après contrôle par le Fonds, 25% de la subvention d'investissement est payé. Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 4,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.319065"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 17, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 17",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.17"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 8, 029; En vigueur : 12-08-2022>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2022-05-06/08",
                                "article_number": "art. 8",
                                "sequence_number": "029",
                                "full_reference": "AGF [2022-05-06/08]"
                            },
                            "effective_date": "12-08-2022",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.8"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 10, 034; En vigueur : 21-09-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-07-19/42",
                                "article_number": "art. 10",
                                "sequence_number": "034",
                                "full_reference": "AGF [2024-07-19/42]"
                            },
                            "effective_date": "21-09-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.10"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 89,
                            "referenced_text": "et au plus tard cinq ans après l'ordre de démarrage des travaux",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 et au plus tard cinq ans après l'ordre de démarrage des travaux]2"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 290,
                            "referenced_text": "En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans.]3"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 530,
                            "referenced_text": "Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants :  \n1° les factures transmises par l'entrepreneur ;  \n2° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds.  \nAprès contrôle par le Fonds, 25% de la subvention d'investissement est payé.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2  \nLe demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants :  \n1° les factures transmises par l'entrepreneur ;  \n2° un aperçu des attributions, établi au vu d'un modèle mis à disposition par le Fonds.  \nAprès contrôle par le Fonds, 25% de la subvention d'investissement est payé.]2"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 851,
                            "referenced_text": "Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.]3"
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "type": "sous-section",
                    "label": "Sous-section 4. [1 \\- Paiement de la quatrième tranche.]1",
                    "metadata": {
                        "title_type": "Sous-section 4.",
                        "title_content": "[1 \\- Paiement de la quatrième tranche.]1",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 27",
                        "metadata": {
                            "article_range": "27",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "27",
                            "anchor_id": "art_27",
                            "content": {
                            "main_text_raw": "Après la mise en service de l'infrastructure en question et au plus tard cinq ans après l'ordre de démarrage des travaux, le demandeur peut demander auprès du Fonds le paiement de la quatrième tranche de la subvention d'investissement pour travaux...... Lors de la demande, il mentionne la date de la mise en service. En cas de force majeure, et sur requête motivée du demandeur, le délai visé à l'alinéa 1er peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Le Fonds évalue le dossier, entre autres la conformité à la promesse de subvention, la conformité à la législation relative aux marchés publics et l'avancement des travaux. Après évaluation positive par le Fonds, 15 % de la subvention d'investissement est payé.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "par le ministre, si ce délai est prolongé de plus de deux ans",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-27\"><header class=\"article-header\"><h2 class=\"article-number\">Article 27</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Après la mise en service de l'infrastructure en question<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"et au plus tard cinq ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.9\" data-article-dossier-number=\"\">et au plus tard cinq ans après l'ordre de démarrage des travaux</span>, le demandeur peut demander auprès du Fonds le paiement de la quatrième tranche de la subvention d'investissement pour travaux<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.11\" data-article-dossier-number=\"\">...</span>... Lors de la demande, il mentionne la date de la mise en service. En cas de force majeure, et sur requête motivée du demandeur, le délai visé à l'alinéa 1er peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"En cas de force majeure, et sur requête motivée du demandeur, le délai visé à l'alinéa 1er peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.11\" data-article-dossier-number=\"\">si ce délai est prolongé de plus de deux ans</span></span></li></ol><p class=\"closing-text\">. Le Fonds évalue le dossier, entre autres la conformité à la promesse de subvention, la conformité à la législation relative aux marchés publics et l'avancement des travaux. Après évaluation positive par le Fonds, 15 % de la subvention d'investissement est payé.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 2,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.319527"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 17, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 17",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.17"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 9, 029; En vigueur : 12-08-2022>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2022-05-06/08",
                                "article_number": "art. 9",
                                "sequence_number": "029",
                                "full_reference": "AGF [2022-05-06/08]"
                            },
                            "effective_date": "12-08-2022",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.9"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 11, 034; En vigueur : 21-09-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-07-19/42",
                                "article_number": "art. 11",
                                "sequence_number": "034",
                                "full_reference": "AGF [2024-07-19/42]"
                            },
                            "effective_date": "21-09-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.11"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "2",
                            "text_position": 61,
                            "referenced_text": "et au plus tard cinq ans après l'ordre de démarrage des travaux",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 et au plus tard cinq ans après l'ordre de démarrage des travaux]2"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 261,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 ...]3"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 342,
                            "referenced_text": "En cas de force majeure, et sur requête motivée du demandeur, le délai visé à l'alinéa 1er peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 En cas de force majeure, et sur requête motivée du demandeur, le délai visé à l'alinéa 1er peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans]3"
                            },
                            {
                            "reference_number": "3",
                            "text_position": 864,
                            "referenced_text": "Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.]3"
                            }
                        ]
                        }
                    ]
                    },
                    {
                    "type": "sous-section",
                    "label": "Sous-section 5. [1 \\- Paiement de la cinquième tranche.]1",
                    "metadata": {
                        "title_type": "Sous-section 5.",
                        "title_content": "[1 \\- Paiement de la cinquième tranche.]1",
                        "rank": 4
                    },
                    "children": [
                        {
                        "type": "article",
                        "label": "Article 28",
                        "metadata": {
                            "article_range": "28",
                            "rank": 5
                        },
                        "article_content": {
                            "article_number": "28",
                            "anchor_id": "art_28",
                            "content": {
                            "main_text_raw": "Au plus tôt un an après la mise en service de l'infrastructure en question et au plus tard six ans après l'ordre de démarrage des travaux, le demandeur peut demander auprès du Fonds le paiement de la cinquième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants: 1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel; 2° un décompte final, comportant: a) l'état final du projet, par parcelle et par partie. Les parties sont le gros oeuvre, l'équipement technique, la finition et l'équipement et le mobilier amovibles; b) le coût final de construction du projet par type de travaux et par forme de soins; c) les factures ou états d'avancement transmis par l'entrepreneur; 3° un aperçu définitif des attributions, établi au vu d'un modèle mis à disposition par le Fonds; 4° une preuve du paiement de l'oeuvre d'art ou des oeuvres d'art en cas d'application de la réglementation relative à l'intégration d'oeuvres d'art dans les bâtiments des services publics et services y assimilés, et des établissements, associations et institutions subventionnés par l'autorité et relevant de la Communauté flamande; 5° un programme définitif d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux; 6° les documents suivants attestant qu'il s'agit d'une construction durable: a) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds; b) une lettre d'accord du demandeur que le programme d'exigences a été rempli, conformément aux exigences minimales du Ministre, et qu'il a suffisamment été tenu compte des exigences et avis; c) des études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB); 7° une évaluation du projet, établie au vu d'un modèle mis à disposition par le Fonds; 8° en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté: a) le dernier compte annuel approuvé du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; b) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du demandeur, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; c) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; d) une déclaration dont l'original est signé par l'entier conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, et par le demandeur d'autre part, qu'il n'existe pas de parenté illégitime entre le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur, tel que visé aux articles 2bis et 2ter du présent arrêté; 9°... Le demandeur tient les documents suivants à disposition: 1° les cahiers des charges; 2° le dossier d'attribution par adjudication, comprenant: a) le procès-verbal de l'ouverture des soumissions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur; 3° le procès-verbal de la réception provisoire ou définitive; 4° les données de consommation d'énergie et d'eau. Le Fonds établit une évaluation finale du dossier. Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.] Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, un supplément d'indice est accordé après l'évaluation finale positive visée à l'alinéa 5. Le supplément d'indice visé à l'alinéa 6 est calculé comme suit: [-5 (Image non reprise pour des raisons techniques, voir M.B. du 11-09-2024, p. 107330) IS = SLO x 50% x (indexAB + indexIGN/indexSLO -2) - IV, où: 1° IS: supplément d'indice; 2° SLO: la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention; 3° iIGN: l'indice de construction dans l'année de la mise en service; 4° iAB: l'indice de construction dans l'année de l'ordre de commencement. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué; 5° iSLO: l'indice de construction dans l'année de la promesse de subvention; 6° IV: une modification de l'indice telle que visée à l'article 20, § 5. Pour les demandeurs qui ont donné un ordre de commencement avant le 1er janvier 2023, la somme du supplément d'indice et de la modification de l'indice, visée à l'article 20, § 5, correspond au minimum au montant calculé à l'aide de la formule suivante: SLO x 100 % x (iAB/iSLO -1). Pour l'infrastructure avec un ordre de commencement en 2021, l'indice de construction de 2022 est utilisé pour le calcul de ce minimum. Si le minimum précité n'est pas atteint, le supplément d'indice visé à l'alinéa 6 est ajusté. Le supplément d'indice visé à l'alinéa 6 peut ensuite également être adapté sur la base des factures soumises à titre de justification des tranches de paiement. Un supplément d'indice tel que visé à l'alinéa 6 qui est positif, est ajouté au solde de la subvention d'investissement. Un supplément d'indice tel que visé à l'alinéa 6 qui est négatif, est réglé avec le solde ou est récupéré.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "numbered_provisions": [
                                {
                                "number": "1°",
                                "text": "par le Fonds, si ce délai est prolongé de deux ans maximum",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "par le ministre, si ce délai est prolongé de plus de deux ans",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "un décompte final, comportant:",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "un aperçu définitif des attributions, établi au vu d'un modèle mis à disposition par le Fonds",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "une preuve du paiement de l'oeuvre d'art ou des oeuvres d'art en cas d'application de la réglementation relative à l'intégration d'oeuvres d'art dans les bâtiments des services publics et services y assimilés, et des établissements, associations et institutions subventionnés par l'autorité et relevant de la Communauté flamande",
                                "sub_items": []
                                },
                                {
                                "number": "5°",
                                "text": "un programme définitif d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux",
                                "sub_items": []
                                },
                                {
                                "number": "6°",
                                "text": "les documents suivants attestant qu'il s'agit d'une construction durable:",
                                "sub_items": []
                                },
                                {
                                "number": "7°",
                                "text": "une évaluation du projet, établie au vu d'un modèle mis à disposition par le Fonds",
                                "sub_items": []
                                },
                                {
                                "number": "8°",
                                "text": "en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté:",
                                "sub_items": []
                                },
                                {
                                "number": "9°",
                                "text": "[2...",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "les cahiers des charges",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "le dossier d'attribution par adjudication, comprenant:",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "le procès-verbal de la réception provisoire ou définitive",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "les données de consommation d'énergie et d'eau.",
                                "sub_items": []
                                },
                                {
                                "number": "1°",
                                "text": "IS: supplément d'indice",
                                "sub_items": []
                                },
                                {
                                "number": "2°",
                                "text": "SLO: la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention",
                                "sub_items": []
                                },
                                {
                                "number": "3°",
                                "text": "iIGN: l'indice de construction dans l'année de la mise en service",
                                "sub_items": []
                                },
                                {
                                "number": "4°",
                                "text": "iAB: l'indice de construction dans l'année de l'ordre de commencement. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué",
                                "sub_items": []
                                },
                                {
                                "number": "5°",
                                "text": "iSLO: l'indice de construction dans l'année de la promesse de subvention",
                                "sub_items": []
                                },
                                {
                                "number": "6°",
                                "text": "IV: une [5 modification",
                                "sub_items": []
                                }
                            ],
                            "main_text": "<article class=\"legal-article\" id=\"art-28\"><header class=\"article-header\"><h2 class=\"article-number\">Article 28</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Au plus tôt un an après la mise en service de l'infrastructure en question<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et au plus tard six ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.10\" data-article-dossier-number=\"\">et au plus tard six ans après l'ordre de démarrage des travaux</span>, le demandeur peut demander auprès du Fonds le paiement de la cinquième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">par le Fonds, si ce délai est prolongé de deux ans maximum</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">par le ministre,<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé : 1° par le Fonds, si ce délai est prolongé de deux ans maximum ; 2° par le ministre, si ce délai est prolongé de plus de deux ans\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.12\" data-article-dossier-number=\"\">si ce délai est prolongé de plus de deux ans</span></span></li></ol><p class=\"intro-text\">. Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"modification\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.12\" data-article-dossier-number=\"\">modification</span>s ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">un décompte final, comportant:</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">un aperçu définitif des attributions, établi au vu d'un modèle mis à disposition par le Fonds</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">une preuve du paiement de l'oeuvre d'art ou des oeuvres d'art en cas d'application de la réglementation relative à l'intégration d'oeuvres d'art dans les bâtiments des services publics et services y assimilés, et des établissements, associations et institutions subventionnés par l'autorité et relevant de la Communauté flamande</span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">un programme définitif d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">les documents suivants attestant qu'il s'agit d'une construction durable:</span></li><li class=\"provision\" data-number=\"7°\"><span class=\"provision-text\">une évaluation du projet, établie au vu d'un modèle mis à disposition par le Fonds</span></li><li class=\"provision\" data-number=\"8°\"><span class=\"provision-text\">en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté:</span></li><li class=\"provision\" data-number=\"9°\"><span class=\"provision-text\">[2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.11\" data-article-dossier-number=\"\">...</span></span></li></ol><p class=\"intro-text\">lus tôt un an après la mise en service de l'infrastructure en question<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et au plus tard six ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.10\" data-article-dossier-number=\"\">et au plus tard six ans après l'ordre de démarrage des travaux</span>, le demandeur peut demander auprès du Fonds le paiement de la cinquième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">les cahiers des charges</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le dossier d'attribution par adjudication, comprenant:</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">le procès-verbal de la réception provisoire ou définitive</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">les données de consommation d'énergie et d'eau.</span></li></ol><p class=\"intro-text\">Le Fonds établit une évaluation finale du dossier.<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023011305#Art.2\" data-article-dossier-number=\"\">Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.</span>] Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, un supplément d'indice est accordé après l'évaluation finale positive visée à l'alinéa 5. Le supplément d'indice visé à l'alinéa 6 est calculé comme suit: [-5 (Image non reprise pour des raisons techniques, voir M.B. du 11-09-2024, p. 107330) IS = SLO x 50% x (indexAB + indexIGN/indexSLO -2) - IV, où:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">IS: supplément d'indice</span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">SLO: la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">iIGN: l'indice de construction dans l'année de la mise en service</span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">iAB: l'indice de construction dans l'année de l'ordre de commencement. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué</span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">iSLO: l'indice de construction dans l'année de la promesse de subvention</span></li><li class=\"provision\" data-number=\"6°\"><span class=\"provision-text\">IV: une [5<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"modification\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.12\" data-article-dossier-number=\"\">modification</span></span></li></ol><p class=\"closing-text\">s la mise en service de l'infrastructure en question et au plus tard six ans après l'ordre de démarrage des travaux, le demandeur peut demander auprès du Fonds le paiement de la cinquième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants: 1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les modifications ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel; 2° un décompte final, comportant: a) l'état final du projet, par parcelle et par partie. Les parties sont le gros oeuvre, l'équipement technique, la finition et l'équipement et le mobilier amovibles; b) le coût final de construction du projet par type de travaux et par forme de soins; c) les factures ou états d'avancement transmis par l'entrepreneur; 3° un aperçu définitif des attributions, établi au vu d'un modèle mis à disposition par le Fonds; 4° une preuve du paiement de l'oeuvre d'art ou des oeuvres d'art en cas d'application de la réglementation relative à l'intégration d'oeuvres d'art dans les bâtiments des services publics et services y assimilés, et des établissements, associations et institutions subventionnés par l'autorité et relevant de la Communauté flamande; 5° un programme définitif d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux; 6° les documents suivants attestant qu'il s'agit d'une construction durable: a) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds; b) une lettre d'accord du demandeur que le programme d'exigences a été rempli, conformément aux exigences minimales du Ministre, et qu'il a suffisamment été tenu compte des exigences et avis; c) des études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB); 7° une évaluation du projet, établie au vu d'un modèle mis à disposition par le Fonds; 8° en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté: a) le dernier compte annuel approuvé du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; b) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du demandeur, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; c) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; d) une déclaration dont l'original est signé par l'entier conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, et par le demandeur d'autre part, qu'il n'existe pas de parenté illégitime entre le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur, tel que visé aux articles 2bis et 2ter du présent arrêté; 9°... Le demandeur tient les documents suivants à disposition: 1° les cahiers des charges; 2° le dossier d'attribution par adjudication, comprenant: a) le procès-verbal de l'ouverture des soumissions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur; 3° le procès-verbal de la réception provisoire ou définitive; 4° les données de consommation d'énergie et d'eau. Le Fonds établit une évaluation finale du dossier. Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.] Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, un supplément d'indice est accordé après l'évaluation finale positive visée à l'alinéa 5. Le supplément d'indice visé à l'alinéa 6 est calculé comme suit: [-5 (Image non reprise pour des raisons techniques, voir M.B. du 11-09-2024, p. 107330) IS = SLO x 50% x (indexAB + indexIGN/indexSLO -2) - IV, où: 1° IS: supplément d'indice; 2° SLO: la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention; 3° iIGN: l'indice de construction dans l'année de la mise en service; 4° iAB: l'indice de construction dans l'année de l'ordre de commencement. En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué; 5° iSLO: l'indice de construction dans l'année de la promesse de subvention; 6° IV: une modification de l'indice telle que visée à l'article 20, § 5. Pour les demandeurs qui ont donné un ordre de commencement avant le 1er janvier 2023, la somme du supplément d'indice et de la modification de l'indice, visée à l'article 20, § 5, correspond au minimum au montant calculé à l'aide de la formule suivante: SLO x 100 % x (iAB/iSLO -1). Pour l'infrastructure avec un ordre de commencement en 2021, l'indice de construction de 2022 est utilisé pour le calcul de ce minimum. Si le minimum précité n'est pas atteint, le supplément d'indice visé à l'alinéa 6 est ajusté. Le supplément d'indice visé à l'alinéa 6 peut ensuite également être adapté sur la base des factures soumises à titre de justification des tranches de paiement. Un supplément d'indice tel que visé à l'alinéa 6 qui est positif, est ajouté au solde de la subvention d'investissement. Un supplément d'indice tel que visé à l'alinéa 6 qui est négatif, est réglé avec le solde ou est récupéré.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p><p class=\"intro-text\">Au plus tôt un an après la mise en service de l'infrastructure en question<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et au plus tard six ans après l'ordre de démarrage des travaux\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2022050608#Art.10\" data-article-dossier-number=\"\">et au plus tard six ans après l'ordre de démarrage des travaux</span>, le demandeur peut demander auprès du Fonds le paiement de la cinquième tranche de la subvention d'investissement pour travaux. En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé: 1° par le Fonds, si ce délai est prolongé de deux ans maximum; 2° par le ministre, si ce délai est prolongé de plus de deux ans. Le demandeur transmet sa demande visée à l'alinéa premier, assortie des documents suivants: 1° un rapport ainsi qu'un aperçu de la manière dont le demandeur a donné suite aux remarques mentionnées dans la promesse de subvention, et de toutes les<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"modification\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.12\" data-article-dossier-number=\"\">modification</span>s ayant été apportées par rapport à la promesse de subvention, tant au niveau des aspects techniques et des aspects physiques de la construction qu'au niveau conceptuel et au niveau fonctionnel; 2° un décompte final, comportant: a) l'état final du projet, par parcelle et par partie. Les parties sont le gros oeuvre, l'équipement technique, la finition et l'équipement et le mobilier amovibles; b) le coût final de construction du projet par type de travaux et par forme de soins; c) les factures ou états d'avancement transmis par l'entrepreneur; 3° un aperçu définitif des attributions, établi au vu d'un modèle mis à disposition par le Fonds; 4° une preuve du paiement de l'oeuvre d'art ou des oeuvres d'art en cas d'application de la réglementation relative à l'intégration d'oeuvres d'art dans les bâtiments des services publics et services y assimilés, et des établissements, associations et institutions subventionnés par l'autorité et relevant de la Communauté flamande; 5° un programme définitif d'exigences en matière de confort et d'usage d'énergie, d'eau et de matériaux; 6° les documents suivants attestant qu'il s'agit d'une construction durable: a) une liste actualisée avec cases à cocher pour constructions durables, sur la base d'un modèle mis à disposition par le Fonds; b) une lettre d'accord du demandeur que le programme d'exigences a été rempli, conformément aux exigences minimales du Ministre, et qu'il a suffisamment été tenu compte des exigences et avis; c) des études ou avis à l'appui des critères indiqués pour constructions durables, dont un document attestant la réglementation en matière de performance énergétique (EPB); 7° une évaluation du projet, établie au vu d'un modèle mis à disposition par le Fonds; 8° en vue du contrôle sur la parenté, visée aux articles 2bis et 2ter, lorsque le demandeur n'est pas le propriétaire du terrain ou le détenteur du droit réel sur le terrain sur lequel le projet est envisagé, et sans préjudice de la possibilité du Fonds de demander des données complémentaires, conformément à l'article 2ter, alinéas 5 et 6 du présent arrêté: a) le dernier compte annuel approuvé du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; b) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du demandeur, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; c) le dernier compte annuel approuvé des administrateurs dotés de la personnalité juridique dans le conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain, lorsque celui-ci ne doit pas être déposé à la Banque nationale de Belgique; d) une déclaration dont l'original est signé par l'entier conseil d'administration du propriétaire du terrain ou du détenteur des droits réels sur le terrain d'une part, et par le demandeur d'autre part, qu'il n'existe pas de parenté illégitime entre le propriétaire du terrain ou le détenteur des droits réels sur le terrain et le demandeur, tel que visé aux articles 2bis et 2ter du présent arrêté; 9°<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.11\" data-article-dossier-number=\"\">...</span>Le demandeur tient les documents suivants à disposition: 1° les cahiers des charges; 2° le dossier d'attribution par adjudication, comprenant: a) le procès-verbal de l'ouverture des soumissions; b) toutes les offres; c) les rapports du contrôle des offres; d) le choix de l'entrepreneur ou du fournisseur, motivé par le demandeur; 3° le procès-verbal de la réception provisoire ou définitive; 4° les données de consommation d'énergie et d'eau. Le Fonds établit une évaluation finale du dossier.<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2023011305#Art.2\" data-article-dossier-number=\"\">Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.</span>] Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, un supplément d'indice est accordé après l'évaluation finale positive visée à l'alinéa 5. Le supplément d'indice visé à l'alinéa 6 est calculé comme suit: [-5 (Image non reprise pour des raisons techniques, voir M.B. du 11-09-2024, p. 107330) IS = SLO x 50% x (indexAB + indexIGN/indexSLO -2):</p><ul class=\"hyphenated-items\"><li class=\"hyphenated-item\"><span class=\"item-text\">IV, où: 1° IS: supplément d'indice; 2° SLO: la subvention calculée sur la base de l'indice de construction dans l'année de la promesse de subvention; 3° iIGN: l'indice de construction dans l'année de la mise en service; 4° iAB: l'indice de construction dans l'année de l'ordre de commencement.</span></li></ul><div class=\"closing-text\"><p>En cas d'un ordre de commencement des travaux en 2021, l'indice de construction de 2022 est appliqué; 5° iSLO: l'indice de construction dans l'année de la promesse de subvention; 6° IV: une modification de l'indice telle que visée à l'article 20, § 5. Pour les demandeurs qui ont donné un ordre de commencement avant le 1er janvier 2023, la somme du supplément d'indice et de la modification de l'indice, visée à l'article 20, § 5, correspond au minimum au montant calculé à l'aide de la formule suivante: SLO x 100 % x (iAB/iSLO -1). Pour l'infrastructure avec un ordre de commencement en 2021, l'indice de construction de 2022 est utilisé pour le calcul de ce minimum. Si le minimum précité n'est pas atteint, le supplément d'indice visé à l'alinéa 6 est ajusté. Le supplément d'indice visé à l'alinéa 6 peut ensuite également être adapté sur la base des factures soumises à titre de justification des tranches de paiement. Un supplément d'indice tel que visé à l'alinéa 6 qui est positif, est ajouté au solde de la subvention d'investissement. Un supplément d'indice tel que visé à l'alinéa 6 qui est négatif, est réglé avec le solde ou est récupéré.] Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.</p></div></div></div></article>",
                            "structured_content_metadata": {
                                "paragraph_count": 0,
                                "provision_count": 21,
                                "has_tables": False,
                                "generation_timestamp": "2025-08-19T14:05:18.323665"
                            }
                            }
                        },
                        "footnotes": [
                            {
                            "footnote_number": "1",
                            "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 17, 020; En vigueur : 20-03-2016>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2016-01-15/17",
                                "article_number": "art. 17",
                                "sequence_number": "020",
                                "full_reference": "AGF [2016-01-15/17]"
                            },
                            "effective_date": "20-03-2016",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.17"
                            },
                            {
                            "footnote_number": "2",
                            "footnote_content": "(2)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 11, 022; En vigueur : 11-10-2018>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2018-07-06/25",
                                "article_number": "art. 11",
                                "sequence_number": "022",
                                "full_reference": "AGF [2018-07-06/25]"
                            },
                            "effective_date": "11-10-2018",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.11"
                            },
                            {
                            "footnote_number": "3",
                            "footnote_content": "(3)<AGF [2022-05-06/08](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608), art. 10, 029; En vigueur : 12-08-2022>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2022-05-06/08",
                                "article_number": "art. 10",
                                "sequence_number": "029",
                                "full_reference": "AGF [2022-05-06/08]"
                            },
                            "effective_date": "12-08-2022",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2022050608#Art.10"
                            },
                            {
                            "footnote_number": "4",
                            "footnote_content": "(4)<AGF [2023-01-13/05](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023011305), art. 2, 030; En vigueur : 01-01-2023>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2023-01-13/05",
                                "article_number": "art. 2",
                                "sequence_number": "030",
                                "full_reference": "AGF [2023-01-13/05]"
                            },
                            "effective_date": "01-01-2023",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023011305",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2023011305#Art.2"
                            },
                            {
                            "footnote_number": "5",
                            "footnote_content": "(5)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 12, 034; En vigueur : 21-09-2024>",
                            "law_reference": {
                                "law_type": "AGF",
                                "date_reference": "2024-07-19/42",
                                "article_number": "art. 12",
                                "sequence_number": "034",
                                "full_reference": "AGF [2024-07-19/42]"
                            },
                            "effective_date": "21-09-2024",
                            "modification_type": "modification",
                            "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                            "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.12"
                            }
                        ],
                        "footnote_references": [
                            {
                            "reference_number": "3",
                            "text_position": 79,
                            "referenced_text": "et au plus tard six ans après l'ordre de démarrage des travaux",
                            "embedded_law_references": [],
                            "bracket_pattern": "[3 et au plus tard six ans après l'ordre de démarrage des travaux]3"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 279,
                            "referenced_text": "En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 En cas de force majeure, et sur requête motivée du demandeur, le délai précité peut être prolongé :  \n1° par le Fonds, si ce délai est prolongé de deux ans maximum ;  \n2° par le ministre, si ce délai est prolongé de plus de deux ans]5"
                            },
                            {
                            "reference_number": "2",
                            "text_position": 4025,
                            "referenced_text": "...",
                            "embedded_law_references": [],
                            "bracket_pattern": "[2 ...]2"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 4559,
                            "referenced_text": "Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 Après évaluation finale positive par le Fonds, 10%, à savoir le solde, de la subvention d'investissement est payé. En cas de transformation et dans tous les dossiers relevant de l'application de l'arrêté du Gouvernement flamand du 16 juillet 2010 fixant la subvention d'investissement et les normes techniques et physiques de la construction pour les établissements de soins, si nécessaire le solde est ajusté sur la base du décompte final. La subvention éventuellement perçue en trop est remboursée. La subvention insuffisamment perçue est ajoutée au solde.]4"
                            },
                            {
                            "reference_number": "4",
                            "text_position": 5128,
                            "referenced_text": "Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, un supplément d'indice est accordé après l'évaluation finale positive visée à l'alinéa 5.  \nLe supplément d'indice visé à l'alinéa 6 est calculé comme suit :  \n[-5 (Image non reprise pour des raisons techniques, voir M.B. du 11-09-2024, p. 107330)",
                            "embedded_law_references": [],
                            "bracket_pattern": "[4 Pour les travaux dont l'infrastructure a été mise en service à partir du 1er janvier 2022, un supplément d'indice est accordé après l'évaluation finale positive visée à l'alinéa 5.  \nLe supplément d'indice visé à l'alinéa 6 est calculé comme suit :  \n[-5 (Image non reprise pour des raisons techniques, voir M.B. du 11-09-2024, p. 107330)]4"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 6034,
                            "referenced_text": "modification",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 modification]5"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 6230,
                            "referenced_text": "modification",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 modification]5"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 6363,
                            "referenced_text": "SLO x 100 % x (iAB/iSLO -1)",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 SLO x 100 % x (iAB/iSLO -1)]5"
                            },
                            {
                            "reference_number": "5",
                            "text_position": 7029,
                            "referenced_text": "Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.",
                            "embedded_law_references": [],
                            "bracket_pattern": "[5 Les demandes de paiement d'une tranche introduites après le 15 décembre ne peuvent être déclarées recevables que pour paiement à partir du 1er janvier suivant.]5"
                            }
                        ]
                        }
                    ]
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE IV. [1 \\- Procédure spécifique pour projets avec autofinancement entier sans promesse de subvention préalable.]1",
            "metadata": {
                "title_type": "CHAPITRE IV.",
                "title_content": "[1 \\- Procédure spécifique pour projets avec autofinancement entier sans promesse de subvention préalable.]1",
                "rank": 2
            },
            "children": [
                {
                "type": "section",
                "label": "Section 1. ",
                "metadata": {
                    "title_type": "Section 1.",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 29",
                    "metadata": {
                        "article_range": "29",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "29",
                        "anchor_id": "art_29",
                        "content": {
                        "main_text_raw": "Sauf dans le cas des dérogations visées au présent article, les règles d'exécution du projet et de paiement de la subvention d'investissement visées au chapitre III du présent arrêté, s'appliquent également aux projets avec autofinancement entier sans promesse de subvention préalable tels que visés à l'article 8 du décret. Par dérogation à l'article 21, l'ordre de commencement des travaux peut déjà être donné, la commande peut déjà être passée ou l'acte authentique pour l'achat peut déjà être passé après que le Fonds..., a rendu un avis favorable en vue de l'obtention de la promesse de subvention, sans préjudice de l'application de la compétence de décision du Ministre. Le demandeur est informé de l'avis de la le Fonds. Après que le demandeur ait obtenu la promesse de subvention, il peut introduire une demande de paiement des subventions d'investissement conformément à la procédure reprise dans le chapitre III.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-29\"><header class=\"article-header\"><h2 class=\"article-number\">Article 29</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Sauf dans le cas des dérogations visées au présent article, les règles d'exécution du projet et de paiement de la subvention d'investissement visées au chapitre III du présent arrêté, s'appliquent également aux projets avec autofinancement entier sans promesse de subvention préalable tels que visés à l'article 8 du décret. Par dérogation à l'article 21, l'ordre de commencement des travaux peut déjà être donné, la commande peut déjà être passée ou l'acte authentique pour l'achat peut déjà être passé après que<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.13\" data-article-dossier-number=\"\">le Fonds</span><span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024071942#Art.13\" data-article-dossier-number=\"\">...</span>, a rendu un avis favorable en vue de l'obtention de la promesse de subvention, sans préjudice de l'application de la compétence de décision du Ministre. Le demandeur est informé de l'avis de la le Fonds. Après que le demandeur ait obtenu la promesse de subvention, il peut introduire une demande de paiement des subventions d'investissement conformément à la procédure reprise dans le chapitre III.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.323932"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur : 20-03-2016>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2016-01-15/17",
                            "article_number": "art. 18",
                            "sequence_number": "020",
                            "full_reference": "AGF [2016-01-15/17]"
                        },
                        "effective_date": "20-03-2016",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.18"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2024-07-19/42](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942), art. 13, 034; En vigueur : 21-09-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-07-19/42",
                            "article_number": "art. 13",
                            "sequence_number": "034",
                            "full_reference": "AGF [2024-07-19/42]"
                        },
                        "effective_date": "21-09-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024071942#Art.13"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 520,
                        "referenced_text": "le Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le Fonds]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 534,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 ...]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 737,
                        "referenced_text": "le Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le Fonds]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 30",
                    "metadata": {
                        "article_range": "30",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "30",
                        "anchor_id": "art_30",
                        "content": {
                        "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                        "numbered_provisions": [],
                        "abrogation_status": "abrogé",
                        "main_text": "<article class=\"legal-article\" id=\"art-30\"><header class=\"article-header\"><h2 class=\"article-number\">Article 30</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"18\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 18, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.324064"
                        },
                        "legal_citation": {
                            "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016",
                            "urls": [
                            "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                            ]
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "abrogation",
                            "law_type": "AGF",
                            "dossier_number": "2016-01-15/17",
                            "article_number": "18",
                            "sequence_number": "020",
                            "effective_date": "20-03-2016",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                            "prefix": "Abrogé par",
                            "raw_dossier": "2016-01-15/17",
                            "raw_article": "18",
                            "start_pos": 0,
                            "end_pos": 166,
                            "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>"
                            }
                        ]
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 31",
                    "metadata": {
                        "article_range": "31",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "31",
                        "anchor_id": "art_31",
                        "content": {
                        "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                        "numbered_provisions": [],
                        "abrogation_status": "abrogé",
                        "main_text": "<article class=\"legal-article\" id=\"art-31\"><header class=\"article-header\"><h2 class=\"article-number\">Article 31</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"18\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 18, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.324228"
                        },
                        "legal_citation": {
                            "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016",
                            "urls": [
                            "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                            ]
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "abrogation",
                            "law_type": "AGF",
                            "dossier_number": "2016-01-15/17",
                            "article_number": "18",
                            "sequence_number": "020",
                            "effective_date": "20-03-2016",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                            "prefix": "Abrogé par",
                            "raw_dossier": "2016-01-15/17",
                            "raw_article": "18",
                            "start_pos": 0,
                            "end_pos": 166,
                            "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>"
                            }
                        ]
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 2. ",
                "metadata": {
                    "title_type": "Section 2.",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 32",
                    "metadata": {
                        "article_range": "32",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "32",
                        "anchor_id": "art_32",
                        "content": {
                        "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                        "numbered_provisions": [],
                        "abrogation_status": "abrogé",
                        "main_text": "<article class=\"legal-article\" id=\"art-32\"><header class=\"article-header\"><h2 class=\"article-number\">Article 32</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"18\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 18, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.324349"
                        },
                        "legal_citation": {
                            "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016",
                            "urls": [
                            "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                            ]
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "abrogation",
                            "law_type": "AGF",
                            "dossier_number": "2016-01-15/17",
                            "article_number": "18",
                            "sequence_number": "020",
                            "effective_date": "20-03-2016",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                            "prefix": "Abrogé par",
                            "raw_dossier": "2016-01-15/17",
                            "raw_article": "18",
                            "start_pos": 0,
                            "end_pos": 166,
                            "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>"
                            }
                        ]
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 33",
                    "metadata": {
                        "article_range": "33",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "33",
                        "anchor_id": "art_33",
                        "content": {
                        "main_text_raw": "<Abrogé par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 30, 006; En vigueur: 03-10-2008>",
                        "numbered_provisions": [],
                        "abrogation_status": "abrogé",
                        "main_text": "<article class=\"legal-article\" id=\"art-33\"><header class=\"article-header\"><h2 class=\"article-number\">Article 33</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2008-05-30/39\" data-article-number=\"30\" data-law-type=\"AGF\" data-effective-date=\"03-10-2008\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008053039\">&lt;Abrogé par, AGF 2008-05-30/39, art. 30, 006; En vigueur : 03-10-2008&gt;</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.324451"
                        },
                        "legal_citation": {
                            "full_text": "Abrogé par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 30, 006; En vigueur: 03-10-2008",
                            "urls": [
                            "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039"
                            ]
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "abrogation",
                            "law_type": "AGF",
                            "dossier_number": "2008-05-30/39",
                            "article_number": "30",
                            "sequence_number": "006",
                            "effective_date": "03-10-2008",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                            "full_text": "<Abrogé par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 30, 006; En vigueur: 03-10-2008>",
                            "prefix": "Abrogé par",
                            "raw_dossier": "2008-05-30/39",
                            "raw_article": "30",
                            "start_pos": 0,
                            "end_pos": 166,
                            "matched_text": "<Abrogé par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 30, 006; En vigueur: 03-10-2008>"
                            }
                        ]
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 3. ",
                "metadata": {
                    "title_type": "Section 3.",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 34",
                    "metadata": {
                        "article_range": "34",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "34",
                        "anchor_id": "art_34",
                        "content": {
                        "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                        "numbered_provisions": [],
                        "abrogation_status": "abrogé",
                        "main_text": "<article class=\"legal-article\" id=\"art-34\"><header class=\"article-header\"><h2 class=\"article-number\">Article 34</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"18\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 18, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.324552"
                        },
                        "legal_citation": {
                            "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016",
                            "urls": [
                            "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                            ]
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "abrogation",
                            "law_type": "AGF",
                            "dossier_number": "2016-01-15/17",
                            "article_number": "18",
                            "sequence_number": "020",
                            "effective_date": "20-03-2016",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>",
                            "prefix": "Abrogé par",
                            "raw_dossier": "2016-01-15/17",
                            "raw_article": "18",
                            "start_pos": 0,
                            "end_pos": 166,
                            "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 18, 020; En vigueur: 20-03-2016>"
                            }
                        ]
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 35",
                    "metadata": {
                        "article_range": "35",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "35",
                        "anchor_id": "art_35",
                        "content": {
                        "main_text_raw": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 19, 020; En vigueur: 20-03-2016>",
                        "numbered_provisions": [],
                        "abrogation_status": "abrogé",
                        "main_text": "<article class=\"legal-article\" id=\"art-35\"><header class=\"article-header\"><h2 class=\"article-number\">Article 35</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"legal-citation legal-citation-abrogation\" data-citation-type=\"abrogation\" data-dossier-number=\"2016-01-15/17\" data-article-number=\"19\" data-law-type=\"AGF\" data-effective-date=\"20-03-2016\" data-citation-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2016011517\">&lt;Abrogé par, AGF 2016-01-15/17, art. 19, 020; En vigueur : 20-03-2016&gt;</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.324663"
                        },
                        "legal_citation": {
                            "full_text": "Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 19, 020; En vigueur: 20-03-2016",
                            "urls": [
                            "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517"
                            ]
                        },
                        "enhanced_citations": [
                            {
                            "citation_type": "abrogation",
                            "law_type": "AGF",
                            "dossier_number": "2016-01-15/17",
                            "article_number": "19",
                            "sequence_number": "020",
                            "effective_date": "20-03-2016",
                            "url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                            "full_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 19, 020; En vigueur: 20-03-2016>",
                            "prefix": "Abrogé par",
                            "raw_dossier": "2016-01-15/17",
                            "raw_article": "19",
                            "start_pos": 0,
                            "end_pos": 166,
                            "matched_text": "<Abrogé par AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 19, 020; En vigueur: 20-03-2016>"
                            }
                        ]
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE VI. Garantie d'investissement.",
            "metadata": {
                "title_type": "CHAPITRE VI.",
                "title_content": "Garantie d'investissement.",
                "rank": 2
            },
            "children": [
                {
                "type": "section",
                "label": "Section 1. L'importance.",
                "metadata": {
                    "title_type": "Section 1.",
                    "title_content": "L'importance.",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 36",
                    "metadata": {
                        "article_range": "36",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36",
                        "anchor_id": "art_36",
                        "content": {
                        "main_text_raw": "§ 1er. La garantie d'investissement ne peut être accordée que si le demandeur a obtenu une promesse de subvention. § 2. La garantie d'investissement s'élève au maximum à deux tiers de la subvention d'investissement. § 3. La garantie d'investissement ne porte que sur le solde en capital effectivement placé et les intérêts déchus à l'exception des intérêts moratoires et des intérêts intercalaires. En ce qui concerne le solde effectif de l'encours, n'entre en considération pour la garantie d'investissement que le solde effectif de l'encours qui ne dépasse pas le solde effectif de l'encours qui resterait en cas d'un emprunt à annuités à taux d'intérêt constants. § 4. Le taux d'intérêt applicable pour le calcul des intérêts garantis correspond au maximum au rendement d'obligations linéaires (OLO) sur dix ans, tel que calculé par le Fonds d'égalisation des intérêts et publié à la page Reuters SRF/OLOYIELD ou successeurs et dans le journal De Tijd à la date de la conclusion du contrat de financement, à majorer de quinze points de base. En cas de révision contractuelle du taux d'intérêt, la date de la conclusion du contrat de financement est remplacée par la date de la dernière révision contractuelle du taux d'intérêt. Si les dates précitées ne sont pas des jours ouvrables bancaires, la date du prochain jour ouvrable bancaire est retenue.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-36\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p>La garantie d'investissement ne peut être accordée que si<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.36\" data-article-dossier-number=\"\">le demandeur</span>a obtenu une<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"promesse de subvention\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.12\" data-article-dossier-number=\"\">promesse de subvention</span>.</p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>La garantie d'investissement s'élève au maximum à deux tiers de la subvention d'investissement.</p></div></section><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>La garantie d'investissement ne porte que sur le solde en capital effectivement placé et les intérêts déchus à l'exception des intérêts moratoires et des intérêts intercalaires. En ce qui concerne le solde effectif de l'encours, n'entre en considération pour la garantie d'investissement que le solde effectif de l'encours qui ne dépasse pas le solde effectif de l'encours qui resterait en cas d'un emprunt à annuités à taux d'intérêt constants.</p></div></section><section class=\"paragraph\" id=\"para-4\"><h3 class=\"paragraph-marker\">§ 4.</h3><div class=\"paragraph-content\"><p>Le taux d'intérêt applicable pour le calcul des intérêts garantis correspond au maximum au rendement d'obligations linéaires (OLO) sur dix ans, tel que calculé par le Fonds d'égalisation des intérêts et publié à la page Reuters SRF/OLOYIELD ou successeurs et dans le journal De Tijd à la date de la conclusion du contrat de financement, à majorer de quinze points de base. En cas de révision contractuelle du taux d'intérêt, la date de la conclusion du contrat de financement est remplacée par la date de la dernière révision contractuelle du taux d'intérêt. Si les dates précitées ne sont pas des jours ouvrables bancaires, la date du prochain jour ouvrable bancaire est retenue.</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 4,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.325096"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 32, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 32",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.32"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 36, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 36",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.36"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 12, 022; En vigueur : 11-10-2018>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2018-07-06/25",
                            "article_number": "art. 12",
                            "sequence_number": "022",
                            "full_reference": "AGF [2018-07-06/25]"
                        },
                        "effective_date": "11-10-2018",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.12"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 69,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 100,
                        "referenced_text": "promesse de subvention",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 promesse de subvention]3"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 1bis. [1 \\- Procédure]1",
                "metadata": {
                    "title_type": "Section 1bis.",
                    "title_content": "[1 \\- Procédure]1",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 36bis",
                    "metadata": {
                        "article_range": "36bis",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36bis",
                        "anchor_id": "art_36bis",
                        "content": {
                        "main_text_raw": "La demande d'obtention d'un accord de principe sur la garantie d'investissement peut être introduite par le demandeur au plus tôt au moment de la demande d'octroi d'une promesse de subvention. La demande est adressée au Fonds.... La demande d'obtention d'un accord de principe sur la garantie d'investissement contient les documents suivants: 1° le procès-verbal signé de la réunion des organes compétents du demandeur comprenant la décision de demander un accord de principe sur une garantie d'investissement; 2° le plan financier du projet démontrant que l'exploitation couvre au moins les dépenses et garantit une capacité de remboursement suffisante; 3°...; 4° une déclaration du demandeur marquant son accord de conclure, sur simple demande du Fonds, une hypothèque conventionnelle avec le Fonds, ou de donner au Fonds un mandat hypothécaire tel que visé à l'article 37, § 4; 5° les projets de contrat de financement portant sur le financement global du projet. Les projets de contrat de financement contiennent un calendrier de remboursement faisant la distinction entre le capital et les intérêts. Si le demandeur veut conclure, outre l'emprunt garanti par le Fonds, un emprunt sans garantie du Fonds, le demandeur présente un projet de contrat de financement pour un emprunt garanti par le Fonds, et un projet de contrat de financement séparé pour un emprunt sans garantie du Fonds.",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "le procès-verbal signé de la réunion des organes compétents [2 du demandeur",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "le plan financier du projet démontrant que l'exploitation couvre au moins les dépenses et garantit une capacité de remboursement suffisante",
                            "sub_items": []
                            },
                            {
                            "number": "3°",
                            "text": "[3...",
                            "sub_items": []
                            },
                            {
                            "number": "4°",
                            "text": "une déclaration [2 du demandeur",
                            "sub_items": []
                            },
                            {
                            "number": "5°",
                            "text": "les projets de contrat de financement portant sur le financement global du projet.",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-36bis\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36bis</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">La demande d'obtention d'un accord de principe sur la garantie d'investissement peut être introduite par<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.37\" data-article-dossier-number=\"\">le demandeur</span>au plus tôt au moment de la demande d'octroi d'une<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"promesse de subvention\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.13\" data-article-dossier-number=\"\">promesse de subvention</span>. La demande est adressée au Fonds<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.15\" data-article-dossier-number=\"\">...</span>. La demande d'obtention d'un accord de principe sur la garantie d'investissement contient les documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">le procès-verbal signé de la réunion des organes compétents [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.37\" data-article-dossier-number=\"\">du demandeur</span></span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">le plan financier du projet démontrant que l'exploitation couvre au moins les dépenses et garantit une capacité de remboursement suffisante</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">[3<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.15\" data-article-dossier-number=\"\">...</span></span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">une déclaration [2<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.37\" data-article-dossier-number=\"\">du demandeur</span></span></li><li class=\"provision\" data-number=\"5°\"><span class=\"provision-text\">les projets de contrat de financement portant sur le financement global du projet.</span></li></ol><p class=\"closing-text\">Les projets de contrat de financement contiennent un calendrier de remboursement faisant la distinction entre le capital et les intérêts. Si le demandeur veut conclure, outre l'emprunt garanti par le Fonds, un emprunt sans garantie du Fonds, le demandeur présente un projet de contrat de financement pour un emprunt garanti par le Fonds, et un projet de contrat de financement séparé pour un emprunt sans garantie du Fonds.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 5,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.325705"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<Inséré par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 33, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 33",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.33"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 37, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 37",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.37"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 15, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 15",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.15"
                        },
                        {
                        "footnote_number": "4",
                        "footnote_content": "(4)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 13, 022; En vigueur : 11-10-2018>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2018-07-06/25",
                            "article_number": "art. 13",
                            "sequence_number": "022",
                            "full_reference": "AGF [2018-07-06/25]"
                        },
                        "effective_date": "11-10-2018",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.13"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 109,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 178,
                        "referenced_text": "promesse de subvention",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 promesse de subvention]4"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 240,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 431,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 692,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 723,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1159,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1265,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 36ter",
                    "metadata": {
                        "article_range": "36ter",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36ter",
                        "anchor_id": "art_36ter",
                        "content": {
                        "main_text_raw": "Le Fonds examine si la demande, visée à l'article 36bis, répond aux dispositions de l'article 36bis. Dans les quatorze jours calendaires de la réception de la demande, le Fonds envoie un accusé de réception au demandeur, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La recevabilité implique que la demande remplit les exigences formelles visées à l'article 36bis. La date de recevabilité est la date de réception de la demande recevable. Dans les quatorze jours calendaires de la date de recevabilité, le Fonds prend l'avis d'un ou plusieurs fonctionnaires mis à la disposition du Fonds ou à un ou plusieurs experts externes, l'indemnité de ces experts externes étant à charge du budget du Fonds. Les fonctionnaires et les experts externes peuvent demander des renseignements complémentaires au demandeur. Ils remettent leur avis au Fonds dans les soixante jours calendaires de la réception de la demande d'avis.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-36ter\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36ter</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le Fonds examine si la demande, visée à l'article 36bis, répond aux dispositions de l'article 36bis. Dans les quatorze jours calendaires de la réception de la demande, le Fonds envoie un accusé de réception<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"au demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.38\" data-article-dossier-number=\"\">au demandeur</span>, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La recevabilité implique que la demande remplit les exigences formelles visées à l'article 36bis. La date de recevabilité est la date de réception de la demande recevable. Dans les quatorze jours calendaires de la date de recevabilité, le Fonds prend l'avis d'un ou plusieurs fonctionnaires mis à la disposition du Fonds ou à un ou plusieurs experts externes, l'indemnité de ces experts externes étant à charge du budget du Fonds. Les fonctionnaires et les experts externes peuvent demander des renseignements complémentaires au demandeur. Ils remettent leur avis au Fonds dans les soixante jours calendaires de la réception de la demande d'avis.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.325925"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<Inséré par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 33, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 33",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.33"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 38, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 38",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.38"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 211,
                        "referenced_text": "au demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 au demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 857,
                        "referenced_text": "au demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 au demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 36quater",
                    "metadata": {
                        "article_range": "36quater",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36quater",
                        "anchor_id": "art_36quater",
                        "content": {
                        "main_text_raw": "Le Fonds décide sur l'octroi d'un accord de principe concernant la garantie d'investissement. Le demandeur est notifié... de la décision du Fonds. Un accord de principe concernant la garantie d'investissement implique que le projet du demandeur est en principe éligible à une garantie d'investissement. Un accord de principe mentionne entre autres le projet auquel il se rapporte, des remarques éventuelles ainsi que sa date de début de validité. Un accord de principe concernant la garantie d'investissement échoit de droit à l'extinction de la subvention d'investissement.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-36quater\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36quater</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le Fonds décide sur l'octroi d'un accord de principe concernant la garantie d'investissement.<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.39\" data-article-dossier-number=\"\">Le demandeur</span>est notifié<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.16\" data-article-dossier-number=\"\">...</span>de la décision du Fonds. Un accord de principe concernant la garantie d'investissement implique que le projet<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.39\" data-article-dossier-number=\"\">du demandeur</span>est en principe éligible à une garantie d'investissement. Un accord de principe mentionne entre autres le projet auquel il se rapporte, des remarques éventuelles ainsi que sa date de début de validité. Un accord de principe concernant la garantie d'investissement échoit de droit à l'extinction de la subvention d'investissement.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.326116"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<Inséré par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 33, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 33",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.33"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 39, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 39",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.39"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 16, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 16",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.16"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 98,
                        "referenced_text": "Le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 Le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 128,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 249,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 36quinquies",
                    "metadata": {
                        "article_range": "36quinquies",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36quinquies",
                        "anchor_id": "art_36quinquies",
                        "content": {
                        "main_text_raw": "Après avoir reçu l'accord de principe concernant la garantie d'investissement, le demandeur peut introduire une demande d'octroi de la garantie d'investissement pour l'exécution de son projet. La demande d'octroi de la garantie d'investissement contient les documents suivants: 1°...; 2° pour les demandeurs qui ne déposent pas leurs comptes annuels auprès de la Banque nationale de Belgique: le dernier compte annuel approuvé, et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels; 3° un plan financier actualisé pour le projet...; 4° les projets des contrats de financement portant sur le financement global du projet. Les projets des contrats de financement contiennent un calendrier de remboursement faisant la distinction entre le capital et les intérêts. Si le demandeur veut conclure, outre l'emprunt garanti par le Fonds, un emprunt sans garantie du Fonds, le demandeur présente un projet de contrat de financement pour un emprunt garanti par le Fonds, et un projet de contrat de financement séparé pour un emprunt sans garantie du Fonds.",
                        "numbered_provisions": [
                            {
                            "number": "1°",
                            "text": "[3...",
                            "sub_items": []
                            },
                            {
                            "number": "2°",
                            "text": "[3 pour les demandeurs qui ne déposent pas leurs comptes annuels auprès de la Banque nationale de Belgique: le dernier compte annuel approuvé, et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels",
                            "sub_items": []
                            },
                            {
                            "number": "3°",
                            "text": "un plan financier actualisé pour le projet [3...",
                            "sub_items": []
                            },
                            {
                            "number": "4°",
                            "text": "les projets des contrats de financement portant sur le financement global du projet.",
                            "sub_items": []
                            }
                        ],
                        "main_text": "<article class=\"legal-article\" id=\"art-36quinquies\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36quinquies</h2></header><div class=\"article-content\"><div class=\"article-text\"><p class=\"intro-text\">Après avoir reçu l'accord de principe concernant la garantie d'investissement,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.40\" data-article-dossier-number=\"\">le demandeur</span>peut introduire une demande d'octroi de la garantie d'investissement pour l'exécution de son projet. La demande d'octroi de la garantie d'investissement contient les documents suivants:</p><ol class=\"numbered-provisions\"><li class=\"provision\" data-number=\"1°\"><span class=\"provision-text\">[3<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.17\" data-article-dossier-number=\"\">...</span></span></li><li class=\"provision\" data-number=\"2°\"><span class=\"provision-text\">[3 pour les demandeurs qui ne déposent pas leurs comptes annuels auprès de la Banque nationale de Belgique: le dernier compte annuel approuvé, et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels</span></li><li class=\"provision\" data-number=\"3°\"><span class=\"provision-text\">un plan financier actualisé pour le projet [3<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.17\" data-article-dossier-number=\"\">...</span></span></li><li class=\"provision\" data-number=\"4°\"><span class=\"provision-text\">les projets des contrats de financement portant sur le financement global du projet.</span></li></ol><p class=\"closing-text\">Les projets des contrats de financement contiennent un calendrier de remboursement faisant la distinction entre le capital et les intérêts. Si le demandeur veut conclure, outre l'emprunt garanti par le Fonds, un emprunt sans garantie du Fonds, le demandeur présente un projet de contrat de financement pour un emprunt garanti par le Fonds, et un projet de contrat de financement séparé pour un emprunt sans garantie du Fonds.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 4,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.326627"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<Inséré par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 33, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 33",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.33"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 40, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 40",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.40"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 17, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 17",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.17"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 83,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 295,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 310,
                        "referenced_text": "pour les demandeurs qui ne déposent pas leurs comptes annuels auprès de la Banque nationale de Belgique : le dernier compte annuel approuvé, et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels;",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 pour les demandeurs qui ne déposent pas leurs comptes annuels auprès de la Banque nationale de Belgique : le dernier compte annuel approuvé, et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels;]3"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 585,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 830,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 936,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 36sexies",
                    "metadata": {
                        "article_range": "36sexies",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36sexies",
                        "anchor_id": "art_36sexies",
                        "content": {
                        "main_text_raw": "Le Fonds examine si la demande, visée à l'article 36quinquies, répond aux dispositions de l'article 36quinquies. Dans les quatorze jours calendaires de la réception de la demande, le Fonds envoie un accusé de réception au demandeur, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La recevabilité implique que la demande remplit les exigences formelles visées à l'article 36quinquies. La date de recevabilité est la date de réception de la demande recevable. Dans les quatorze jours calendaires de la date de recevabilité de la demande, le Fonds prend l'avis d'un ou plusieurs fonctionnaires mis à la disposition du Fonds ou d'un ou plusieurs experts externes, l'indemnité de ces experts externes étant à charge du budget du Fonds. Les fonctionnaires et les experts externes peuvent demander des renseignements complémentaires au demandeur. Ils remettent leur avis au Fonds dans les trente jours calendaires de la réception de la demande d'avis.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-36sexies\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36sexies</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le Fonds examine si la demande, visée à l'article 36quinquies, répond aux dispositions de l'article 36quinquies. Dans les quatorze jours calendaires de la réception de la demande, le Fonds envoie un accusé de réception<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"au demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.41\" data-article-dossier-number=\"\">au demandeur</span>, indiquant si la demande est recevable ou non, et le cas échéant indiquant la date de recevabilité. La recevabilité implique que la demande remplit les exigences formelles visées à l'article 36quinquies. La date de recevabilité est la date de réception de la demande recevable. Dans les quatorze jours calendaires de la date de recevabilité de la demande, le Fonds prend l'avis d'un ou plusieurs fonctionnaires mis à la disposition du Fonds ou d'un ou plusieurs experts externes, l'indemnité de ces experts externes étant à charge du budget du Fonds. Les fonctionnaires et les experts externes peuvent demander des renseignements complémentaires au demandeur. Ils remettent leur avis au Fonds dans les trente jours calendaires de la réception de la demande d'avis.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.326851"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<Inséré par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 33, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 33",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.33"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 41, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 41",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.41"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 223,
                        "referenced_text": "au demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 au demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 889,
                        "referenced_text": "au demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 au demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 36septies",
                    "metadata": {
                        "article_range": "36septies",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "36septies",
                        "anchor_id": "art_36septies",
                        "content": {
                        "main_text_raw": "Le Fonds décide sur l'octroi de la garantie d'investissement. Le demandeur est notifié... de la décision du Fonds. Si la garantie d'investissement est octroyée, le demandeur doit remettre au Fonds le calendrier définitif de remboursements après l'achèvement du projet ou de la phase de projet.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-36septies\"><header class=\"article-header\"><h2 class=\"article-number\">Article 36septies</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le Fonds décide sur l'octroi de la garantie d'investissement.<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.42\" data-article-dossier-number=\"\">Le demandeur</span>est notifié<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.18\" data-article-dossier-number=\"\">...</span>de la décision du Fonds. Si la garantie d'investissement est octroyée,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.42\" data-article-dossier-number=\"\">le demandeur</span>doit remettre au Fonds le calendrier définitif de remboursements après l'achèvement du projet ou de la phase de projet.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.327009"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<Inséré par AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 33, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 33",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.33"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 42, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 42",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.42"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 18, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 18",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.18"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 66,
                        "referenced_text": "Le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 Le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 96,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 178,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        }
                    ]
                    }
                ]
                },
                {
                "type": "section",
                "label": "Section 2. Conditions.",
                "metadata": {
                    "title_type": "Section 2.",
                    "title_content": "Conditions.",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 37",
                    "metadata": {
                        "article_range": "37",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "37",
                        "anchor_id": "art_37",
                        "content": {
                        "main_text_raw": "§ 1er. La durée des emprunts garantis est déterminée en fonction de la durée de vie présumée des investissements auxquels ils se rapportent, sans toutefois dépasser trente ans. § 2. Les emprunts auxquels se rapporte la garantie d'investissement doivent être contractés par le demandeur auprès d'un financier. § 3. La garantie d'investissement ne peut être octroyée que s'il ressort de prévisions prudentes que les chances de succès financier du projet sont très réelles. § 4. La garantie ne peut être octroyée que si le demandeur se déclare d'accord de conclure, sur simple demande du Fonds, une hypothèque conventionnelle avec le Fonds, ou de donner au Fonds un mandat hypothécaire pour les biens immobiliers se rapportant au projet et le sol ou le terrain où se trouvent ces biens immobiliers. § 5. Le paiement de la garantie par le Fonds ne décharge pas le demandeur. Le Fonds dispose, par le paiement de la garantie, d'un droit de recours integral contre le demandeur. En payant la garantie, le Fonds est subrogé dans les droits du financier, mais ne peut faire appel aux sûretés qu'a le financier à l'égard du demandeur pour d'autres emprunts que ceux garantis par le Fonds, qu'après règlement de toutes les dettes du demandeur pour le projet autres que la dette garantie par le Fonds.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-37\"><header class=\"article-header\"><h2 class=\"article-number\">Article 37</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p>La durée des emprunts garantis est déterminée en fonction de la durée de vie présumée des investissements auxquels ils se rapportent, sans toutefois dépasser trente ans.</p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>Les emprunts auxquels se rapporte la garantie d'investissement doivent être contractés par<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.43\" data-article-dossier-number=\"\">le demandeur</span>auprès d'un financier.</p></div></section><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p>La garantie d'investissement ne peut être octroyée que s'il ressort de prévisions prudentes que les chances de succès financier du projet sont très réelles.</p></div></section><section class=\"paragraph\" id=\"para-4\"><h3 class=\"paragraph-marker\">§ 4.</h3><div class=\"paragraph-content\"><p>La garantie ne peut être octroyée que si<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.43\" data-article-dossier-number=\"\">le demandeur</span>se déclare d'accord de conclure, sur simple demande du Fonds, une hypothèque conventionnelle avec le Fonds, ou de donner au Fonds un mandat hypothécaire pour les biens immobiliers se rapportant au projet<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et le sol ou le terrain où se trouvent ces biens immobiliers\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.14\" data-article-dossier-number=\"\">et le sol ou le terrain où se trouvent ces biens immobiliers</span>.</p></div></section><section class=\"paragraph\" id=\"para-5\"><h3 class=\"paragraph-marker\">§ 5.</h3><div class=\"paragraph-content\"><p>Le paiement de la garantie par le Fonds ne décharge pas<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.43\" data-article-dossier-number=\"\">le demandeur</span>. Le Fonds dispose, par le paiement de la garantie, d'un droit de recours integral contre le demandeur. En payant la garantie, le Fonds est subrogé dans les droits du financier, mais ne peut faire appel aux sûretés qu'a le financier à l'égard<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.43\" data-article-dossier-number=\"\">du demandeur</span>pour d'autres emprunts que ceux garantis par le Fonds,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"qu'après règlement de toutes les dettes du demandeur pour le projet\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.14\" data-article-dossier-number=\"\">qu'après règlement de toutes les dettes du demandeur pour le projet</span>autres que la dette garantie par le Fonds.</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 5,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.327504"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 34, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 34",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.34"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 43, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 43",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.43"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 14, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 14",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.14"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 279,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 532,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 754,
                        "referenced_text": "et le sol ou le terrain où se trouvent ces biens immobiliers",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 et le sol ou le terrain où se trouvent ces biens immobiliers]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 884,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 991,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1149,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 1222,
                        "referenced_text": "qu'après règlement de toutes les dettes du demandeur pour le projet",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 qu'après règlement de toutes les dettes du demandeur pour le projet]3"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 38",
                    "metadata": {
                        "article_range": "38",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "38",
                        "anchor_id": "art_38",
                        "content": {
                        "main_text_raw": "Si la garantie d'investissement est accordée, le contrat de financement est contresigné par le Fonds avec mention de la clause suivante: \"Le Fonds s'engage à accorder sa garantie d'investissement aux conditions prescrites par l'arrêté du Gouvernement flamand du 6 juillet 1994 établissant les règles de procédure en matière d'infrastructure affectée aux matières personnalisables\". Pour la prolongation de la durée des emprunts garantis du contrat de financement, il suffit que le Fonds et le financier co-signent un document, qui est rédigé en concertation avec le Fonds. Ce document peut porter sur des contrats de financement de divers projets, demandeurs et financiers.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-38\"><header class=\"article-header\"><h2 class=\"article-number\">Article 38</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Si la garantie d'investissement est accordée, le contrat de financement est contresigné par le Fonds avec mention de la clause suivante: &quot;Le Fonds s'engage à accorder sa garantie d'investissement aux conditions prescrites par l'arrêté du Gouvernement flamand du 6 juillet 1994 établissant les règles de procédure en matière d'infrastructure affectée aux matières personnalisables&quot;.<span class=\"footnote-ref\" data-footnote-id=\"1\" data-referenced-text=\"Pour la prolongation de la durée des emprunts garantis du contrat de financement, il suffit que le Fonds et le financier co-signent un document, qui est rédigé en concertation avec le Fonds. Ce document peut porter sur des contrats de financement de divers projets, demandeurs et financiers.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2020050817#Art.74\" data-article-dossier-number=\"\">Pour la prolongation de la durée des emprunts garantis du contrat de financement, il suffit que le Fonds et le financier co-signent un document, qui est rédigé en concertation avec le Fonds. Ce document peut porter sur des contrats de financement de divers projets, demandeurs et financiers.</span></p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.327679"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2020-05-08/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2020050817), art. 74, 026; En vigueur : 20-03-2020>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2020-05-08/17",
                            "article_number": "art. 74",
                            "sequence_number": "026",
                            "full_reference": "AGF [2020-05-08/17]"
                        },
                        "effective_date": "20-03-2020",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2020050817",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2020050817#Art.74"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "1",
                        "text_position": 385,
                        "referenced_text": "Pour la prolongation de la durée des emprunts garantis du contrat de financement, il suffit que le Fonds et le financier co-signent un document, qui est rédigé en concertation avec le Fonds. Ce document peut porter sur des contrats de financement de divers projets, demandeurs et financiers.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[1 Pour la prolongation de la durée des emprunts garantis du contrat de financement, il suffit que le Fonds et le financier co-signent un document, qui est rédigé en concertation avec le Fonds. Ce document peut porter sur des contrats de financement de divers projets, demandeurs et financiers.]1"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 39",
                    "metadata": {
                        "article_range": "39",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "39",
                        "anchor_id": "art_39",
                        "content": {
                        "main_text_raw": "§ 1er. La garantie d'investissement ne produit ses effets qu'à partir de la date à laquelle le demandeur paie au Fonds une cotisation fixee à 0,35 pour cent du montant du crédit garanti, à majorer de 0,015 pour cent par année de durée du crédit. Aussitôt après le paiement, le Fonds informe le financier de la date de paiement..... Cette cotisation est versée dans les trente jours calendaires, à compter de la date de cosignature par le Fonds. Si la cotisation n'est pas versée dans ce délai, la garantie d'investissement du Fonds échoit. Sur demande motivée du demandeur, ou du financier, si celui-ci effectue le paiement pour le compte du demandeur, le Fonds peut déroger à titre exceptionnel aux échéances mentionnées. § 2. Si, à la demande du Fonds, il est constitué un mandat hypothécaire ou une hypothèque, ou si une hypothèque est souscrite, les frais et charges y afferents sont pris en charge par le Fonds, au maximum à raison du montant de la cotisation payée, telle que visée à l'article 1. Les frais et charges excédant ce montant sont à charge du demandeur. Si le demandeur se trouve dans l'impossibilité de payer ces frais et charges, le Fonds avancera le paiement. En ce cas, le Fonds se réserve le droit de recouvrer les montants avancés du demandeur. Le Fonds paie les montants en application de l'alinéa premier à charge du fonds de réserve du Fonds visé à l'article 14 du décret du 2 juin 2006 portant transformation du \" Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden \" en agence autonomisée interne dotée de la personnalité juridique, et modifiant le décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-39\"><header class=\"article-header\"><h2 class=\"article-number\">Article 39</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p>La garantie d'investissement ne produit ses effets qu'à partir de la date à laquelle<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.44\" data-article-dossier-number=\"\">le demandeur</span>paie au Fonds une cotisation fixee à 0,35 pour cent du montant du crédit garanti, à majorer de 0,015 pour cent par année de durée du crédit. Aussitôt après le paiement, le Fonds informe le financier de la date de paiement<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.20\" data-article-dossier-number=\"\">...</span>.. Cette cotisation est versée dans les trente jours calendaires, à compter de la date de cosignature par le Fonds. Si la cotisation n'est pas versée dans ce délai, la garantie d'investissement du Fonds échoit. Sur demande motivée<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.44\" data-article-dossier-number=\"\">du demandeur</span>,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"ou du financier, si celui-ci effectue le paiement pour le compte du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.20\" data-article-dossier-number=\"\">ou du financier, si celui-ci effectue le paiement pour le compte du demandeur</span>, le Fonds peut déroger à titre exceptionnel aux échéances mentionnées.</p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p>Si, à la demande du Fonds, il est constitué un mandat hypothécaire ou une hypothèque, ou si une hypothèque est souscrite, les frais et charges y afferents sont pris en charge par le Fonds, au maximum à raison du montant de la cotisation payée, telle que visée à l'article 1. Les frais et charges excédant ce montant sont à charge<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.44\" data-article-dossier-number=\"\">du demandeur</span>. Si<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.44\" data-article-dossier-number=\"\">le demandeur</span>se trouve dans l'impossibilité de payer ces frais et charges, le Fonds avancera le paiement. En ce cas, le Fonds se réserve le droit de recouvrer les montants avancés du demandeur. Le Fonds paie les montants en application de l'alinéa premier à charge du fonds de réserve du Fonds visé à l'article 14 du décret du 2 juin 2006 portant transformation du &quot; Vlaams Infrastructuurfonds voor Persoonsgebonden Aangelegenheden &quot; en agence autonomisée interne dotée de la personnalité juridique, et modifiant le décret du 23 février 1994 relatif à l'infrastructure affectée aux matières personnalisables.</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 2,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.328095"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 35, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 35",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.35"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 44, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 44",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.44"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 20, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 20",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.20"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "2",
                        "text_position": 96,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 337,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ...]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 577,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 596,
                        "referenced_text": "ou du financier, si celui-ci effectue le paiement pour le compte du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 ou du financier, si celui-ci effectue le paiement pour le compte du demandeur]3"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1087,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1109,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le demandeur]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1294,
                        "referenced_text": "du demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du demandeur]2"
                        }
                    ]
                    },
                    {
                    "type": "article",
                    "label": "Article 40",
                    "metadata": {
                        "article_range": "40",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "40",
                        "anchor_id": "art_40",
                        "content": {
                        "main_text_raw": "§ 1er. Le demandeur exécute son projet conformément à la promesse de subvention octroyées. Le demandeur qui ne dépose pas de comptes annuelles auprès de la Banque Nationale de Belgique, transmettra annuellement et pour la durée de l'emprunt garanti au Fonds, une copie des derniers comptes annuels approuvés et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels..... Le demandeur ne grèvera d'aucune manière d'une sûreté en faveur d'un tiers, le bien se rapportant au projet, ni la terre ou le terrain sur lequel il se trouve, sauf autorisation expresse et préalable du Ministre. Cette obligation s'applique à partir de la demande jusqu'à l'obtention d'un accord de principe relatif a la garantie d'investissement. La garantie d'investissement ne peut pas être octroyée si cette obligation n'est pas respectée. Si la garantie d'investissement a déjà été octroyée et cette obligation n'est pas respectée, la garantie d'investissement échoit. § 2. Le Fonds peut réclamer à tout moment du financier une attestation récente provenant du bureau des hypothèques compétent, dont il ressort si, oui ou non, il a été constitué une hypothèque sur les biens se rapportant au projet............. En ce qui concerne les biens immobiliers se rapportant au projet, le financier n'obtiendra pas de mandat hypothécaire, ni convertira tel mandat en inscription hypothécaire, ni prendra une inscription hypothécaire, ni procédera à l'éviction de son hypothèque, ni exigera le remboursement anticipé des crédits se rapportant au projet sans l'autorisation préalable du Fonds. Si, dans les cas susmentionnés, le Fonds ne réagit pas à une demande d'autorisation par le financier dans un délai de vingt jours ouvrables, prenant cours le jour de la réception de la demande adressée par le financier au Fonds par lettre recommandée avec récépissé, cette absence de réaction est assimilée à l'autorisation susmentionnée du Fonds. Le Fonds peut proroger d'au maximum vingt jours ouvrables ce délai de vingt jours ouvrables de vingt jours ouvrables au maximum, lorsque, à cause de circonstances exceptionnelles, il ne peut décider de la demande d'autorisation dans le délai original de vingt jours ouvrables. Dans ce cas, le Fonds notifie cette prorogation au financier dans le délai initial de vingt jours ouvrables. Si le demandeur ne respecte pas le calendrier de remboursement, le financier donnera son consentement, après l'accord du Fonds, à accorder un délai, à moins que le financier ne renonce à la garantie d'investissement octroyée. Si le financier est au courant que le demandeur, sans que celui-ci dispose de l'autorisation expresse et préalable du Ministre, procède au grèvement d'une sûreté en faveur d'un tiers, comme mentionné au § 1er, quatrième alinéa, ou...au grèvement d'un droit réel, comme mentionné à l'article 41, le financier est tenu d'en informer aussitôt le Fonds. En raison de ce fait, en ce qui concerne... un grèvement d'un droit réel tel que visé à l'art. 41, le Fonds peut exiger, à moins que le financier ne renonce à la garantie d'investissement octroyée, que celui-ci dénonce immédiatement le contrat de financement garanti et qu'il exige dès lors le paiement immédiat de tous les montants dus. La garantie d'investissement échoit si le financier ne manque à l'une de ses obligations....",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-40\"><header class=\"article-header\"><h2 class=\"article-number\">Article 40</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"Le demandeur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2011111007#Art.45\" data-article-dossier-number=\"\">Le demandeur</span>exécute son projet conformément<span class=\"footnote-ref\" data-footnote-id=\"5\" data-referenced-text=\"à la promesse de subvention\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2018070625#Art.14\" data-article-dossier-number=\"\">à la promesse de subvention</span>octroyées.<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"Le demandeur qui ne dépose pas de comptes annuelles auprès de la Banque Nationale de Belgique, transmettra annuellement et pour la durée de l'emprunt garanti au Fonds, une copie des derniers comptes annuels approuvés et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.21\" data-article-dossier-number=\"\">Le demandeur qui ne dépose pas de comptes annuelles auprès de la Banque Nationale de Belgique, transmettra annuellement et pour la durée de l'emprunt garanti au Fonds, une copie des derniers comptes annuels approuvés et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels.</span>.... Le demandeur ne grèvera d'aucune manière d'une sûreté en faveur d'un tiers, le bien se rapportant au projet, ni la terre ou le terrain sur lequel il se trouve, sauf autorisation expresse et préalable du Ministre. Cette obligation s'applique à partir de la demande jusqu'à l'obtention d'un accord de principe relatif a la garantie d'investissement. La garantie d'investissement ne peut pas être octroyée si cette obligation n'est pas respectée. Si la garantie d'investissement a déjà été octroyée et cette obligation n'est pas respectée, la garantie d'investissement échoit.</p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008071825#Art.18\" data-article-dossier-number=\"\">Le Fonds</span>peut réclamer à tout moment du financier une attestation récente provenant du bureau des hypothèques compétent, dont il ressort si, oui ou non, il a été constitué une hypothèque sur les biens se rapportant au projet<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.21\" data-article-dossier-number=\"\">...</span>.......... En ce qui concerne les biens immobiliers se rapportant au projet, le financier n'obtiendra pas de mandat hypothécaire, ni convertira tel mandat en inscription hypothécaire, ni prendra une inscription hypothécaire, ni procédera à l'éviction de son hypothèque, ni exigera le remboursement anticipé des crédits se rapportant au projet sans l'autorisation préalable<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"du Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008071825#Art.18\" data-article-dossier-number=\"\">du Fonds</span>. Si, dans les cas susmentionnés,<span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"le Fonds\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2008071825#Art.18\" data-article-dossier-number=\"\">le Fonds</span>ne réagit pas à une demande d'autorisation par le financier dans un délai de vingt jours ouvrables, prenant cours le jour de la réception de la demande adressée par le financier au Fonds par lettre recommandée avec récépissé, cette absence de réaction est assimilée à l'autorisation susmentionnée du Fonds. Le Fonds peut proroger d'au maximum vingt jours ouvrables ce délai de vingt jours ouvrables de vingt jours ouvrables au maximum, lorsque, à cause de circonstances exceptionnelles, il ne peut décider de la demande d'autorisation dans le délai original de vingt jours ouvrables. Dans ce cas, le Fonds notifie cette prorogation au financier dans le délai initial de vingt jours ouvrables.<span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"Si le demandeur ne respecte pas le calendrier de remboursement, le financier donnera son consentement, après l'accord du Fonds, à accorder un délai, à moins que le financier ne renonce à la garantie d'investissement octroyée.\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2014021426#Art.21\" data-article-dossier-number=\"\">Si le demandeur ne respecte pas le calendrier de remboursement, le financier donnera son consentement, après l'accord du Fonds, à accorder un délai, à moins que le financier ne renonce à la garantie d'investissement octroyée.</span>Si le financier est au courant que le demandeur, sans que celui-ci dispose de l'autorisation expresse et préalable du Ministre, procède au grèvement d'une sûreté en faveur d'un tiers, comme mentionné au § 1er, quatrième alinéa, ou...au grèvement d'un droit réel, comme mentionné à l'article 41, le financier est tenu d'en informer aussitôt le Fonds. En raison de ce fait, en ce qui concerne... un grèvement d'un droit réel tel que visé à l'art. 41, le Fonds peut exiger, à moins que le financier ne renonce à la garantie d'investissement octroyée, que celui-ci dénonce immédiatement le contrat de financement garanti et qu'il exige dès lors le paiement immédiat de tous les montants dus. La garantie d'investissement échoit si le financier ne manque à l'une de ses obligations....</p></div></section></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 2,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:05:18.328861"
                        }
                        }
                    },
                    "footnotes": [
                        {
                        "footnote_number": "1",
                        "footnote_content": "(1)<AGF [2008-05-30/39](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039), art. 36, 006; En vigueur : 03-10-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-05-30/39",
                            "article_number": "art. 36",
                            "sequence_number": "006",
                            "full_reference": "AGF [2008-05-30/39]"
                        },
                        "effective_date": "03-10-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008053039#Art.36"
                        },
                        {
                        "footnote_number": "2",
                        "footnote_content": "(2)<AGF [2008-07-18/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008071825), art. 18, 007; En vigueur : 09-11-2008>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2008-07-18/25",
                            "article_number": "art. 18",
                            "sequence_number": "007",
                            "full_reference": "AGF [2008-07-18/25]"
                        },
                        "effective_date": "09-11-2008",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008071825",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2008071825#Art.18"
                        },
                        {
                        "footnote_number": "3",
                        "footnote_content": "(3)<AGF [2011-11-10/07](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007), art. 45, 016; En vigueur : 19-12-2011>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2011-11-10/07",
                            "article_number": "art. 45",
                            "sequence_number": "016",
                            "full_reference": "AGF [2011-11-10/07]"
                        },
                        "effective_date": "19-12-2011",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2011111007#Art.45"
                        },
                        {
                        "footnote_number": "4",
                        "footnote_content": "(4)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 21, 017; En vigueur : 25-04-2014>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2014-02-14/26",
                            "article_number": "art. 21",
                            "sequence_number": "017",
                            "full_reference": "AGF [2014-02-14/26]"
                        },
                        "effective_date": "25-04-2014",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.21"
                        },
                        {
                        "footnote_number": "5",
                        "footnote_content": "(5)<AGF [2018-07-06/25](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625), art. 14, 022; En vigueur : 11-10-2018>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2018-07-06/25",
                            "article_number": "art. 14",
                            "sequence_number": "022",
                            "full_reference": "AGF [2018-07-06/25]"
                        },
                        "effective_date": "11-10-2018",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2018070625#Art.14"
                        },
                        {
                        "footnote_number": "6",
                        "footnote_content": "(6)<AGF [2024-05-31/16](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116), art. 10, 033; En vigueur : 01-08-2024>",
                        "law_reference": {
                            "law_type": "AGF",
                            "date_reference": "2024-05-31/16",
                            "article_number": "art. 10",
                            "sequence_number": "033",
                            "full_reference": "AGF [2024-05-31/16]"
                        },
                        "effective_date": "01-08-2024",
                        "modification_type": "modification",
                        "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116",
                        "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116#Art.10"
                        }
                    ],
                    "footnote_references": [
                        {
                        "reference_number": "3",
                        "text_position": 11,
                        "referenced_text": "Le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 Le demandeur]3"
                        },
                        {
                        "reference_number": "5",
                        "text_position": 61,
                        "referenced_text": "à la promesse de subvention",
                        "embedded_law_references": [],
                        "bracket_pattern": "[5 à la promesse de subvention]5"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 107,
                        "referenced_text": "Le demandeur qui ne dépose pas de comptes annuelles auprès de la Banque Nationale de Belgique, transmettra annuellement et pour la durée de l'emprunt garanti au Fonds, une copie des derniers comptes annuels approuvés et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 Le demandeur qui ne dépose pas de comptes annuelles auprès de la Banque Nationale de Belgique, transmettra annuellement et pour la durée de l'emprunt garanti au Fonds, une copie des derniers comptes annuels approuvés et, le cas échéant, le rapport du réviseur d'entreprise sur les comptes annuels.]4"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 412,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 ...]4"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 424,
                        "referenced_text": "Le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 Le demandeur]3"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 1238,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 ...]4"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 1250,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 ...]4"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 1262,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 ...]4"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1636,
                        "referenced_text": "du Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 du Fonds]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1683,
                        "referenced_text": "le Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le Fonds]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 1878,
                        "referenced_text": "Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 Fonds]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 2002,
                        "referenced_text": "Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 Fonds]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 2014,
                        "referenced_text": "Le Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 Le Fonds]2"
                        },
                        {
                        "reference_number": "2",
                        "text_position": 2309,
                        "referenced_text": "le Fonds",
                        "embedded_law_references": [],
                        "bracket_pattern": "[2 le Fonds]2"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 2412,
                        "referenced_text": "Si le demandeur ne respecte pas le calendrier de remboursement, le financier donnera son consentement, après l'accord du Fonds, à accorder un délai, à moins que le financier ne renonce à la garantie d'investissement octroyée.",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 Si le demandeur ne respecte pas le calendrier de remboursement, le financier donnera son consentement, après l'accord du Fonds, à accorder un délai, à moins que le financier ne renonce à la garantie d'investissement octroyée.]4"
                        },
                        {
                        "reference_number": "3",
                        "text_position": 2680,
                        "referenced_text": "le demandeur",
                        "embedded_law_references": [],
                        "bracket_pattern": "[3 le demandeur]3"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 2881,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 ...]6"
                        },
                        {
                        "reference_number": "6",
                        "text_position": 3047,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[6 ...]6"
                        },
                        {
                        "reference_number": "4",
                        "text_position": 3441,
                        "referenced_text": "...",
                        "embedded_law_references": [],
                        "bracket_pattern": "[4 ...]4"
                        }
                    ]
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE VII. Mesures de contrôle et disciplinaires.",
            "metadata": {
                "title_type": "CHAPITRE VII.",
                "title_content": "Mesures de contrôle et disciplinaires.",
                "rank": 2
            },
            "children": [
                {
                "type": "article",
                "label": "Article 41",
                "metadata": {
                    "article_range": "41",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "41",
                    "anchor_id": "art_41",
                    "content": {
                    "main_text_raw": "§ 1er. Les membres compétents de l'administration flamande, compétents pour le domaine politique dont relève le Fonds, exercent sur pièces ou sur place le contrôle du respect des obligations énoncées dans le présent arrêté. Le demandeur est obligé de transmettre tous les documents ayant trait au lien de parenté, visé aux articles 2bis et 2ter, au Fonds si ce dernier le demande. § 2.... § 3....",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-41\"><header class=\"article-header\"><h2 class=\"article-number\">Article 41</h2></header><div class=\"article-content\"><section class=\"paragraph\" id=\"para-1er\"><h3 class=\"paragraph-marker\">§ 1er.</h3><div class=\"paragraph-content\"><p>Les membres compétents de l'administration flamande, compétents pour le domaine politique dont relève le Fonds, exercent sur pièces ou sur place le contrôle du respect des obligations énoncées dans le présent arrêté. Le demandeur est obligé de transmettre tous les documents ayant trait au lien de parenté, visé aux articles 2bis et 2ter, au Fonds si ce dernier le demande.</p></div></section><section class=\"paragraph\" id=\"para-2\"><h3 class=\"paragraph-marker\">§ 2.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024053116#Art.11\" data-article-dossier-number=\"\">...</span></p></div></section><section class=\"paragraph\" id=\"para-3\"><h3 class=\"paragraph-marker\">§ 3.</h3><div class=\"paragraph-content\"><p><span class=\"footnote-ref\" data-footnote-id=\"4\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024053116#Art.11\" data-article-dossier-number=\"\">...</span></p></div></section></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 3,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.329119"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 22, 017; En vigueur : 25-04-2014>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2014-02-14/26",
                        "article_number": "art. 22",
                        "sequence_number": "017",
                        "full_reference": "AGF [2014-02-14/26]"
                    },
                    "effective_date": "25-04-2014",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.22"
                    },
                    {
                    "footnote_number": "2",
                    "footnote_content": "(2)<AGF [2015-10-30/22](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2015103022), art. 1, 019; En vigueur : 14-12-2015>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2015-10-30/22",
                        "article_number": "art. 1",
                        "sequence_number": "019",
                        "full_reference": "AGF [2015-10-30/22]"
                    },
                    "effective_date": "14-12-2015",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2015103022",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2015103022#Art.1"
                    },
                    {
                    "footnote_number": "3",
                    "footnote_content": "(3)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 20, 020; En vigueur : 20-03-2016>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2016-01-15/17",
                        "article_number": "art. 20",
                        "sequence_number": "020",
                        "full_reference": "AGF [2016-01-15/17]"
                    },
                    "effective_date": "20-03-2016",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.20"
                    },
                    {
                    "footnote_number": "4",
                    "footnote_content": "(4)<AGF [2024-05-31/16](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116), art. 11, 033; En vigueur : 01-08-2024>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2024-05-31/16",
                        "article_number": "art. 11",
                        "sequence_number": "033",
                        "full_reference": "AGF [2024-05-31/16]"
                    },
                    "effective_date": "01-08-2024",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116#Art.11"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "4",
                    "text_position": 394,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 ...]4"
                    },
                    {
                    "reference_number": "4",
                    "text_position": 410,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[4 ...]4"
                    }
                ]
                },
                {
                "type": "article",
                "label": "Article 42",
                "metadata": {
                    "article_range": "42",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "42",
                    "anchor_id": "art_42",
                    "content": {
                    "main_text_raw": "En cas d'infraction aux dispositions de l'article 40, § 1er, alinéa trois, et de l'article 41, § 1er et § 2, alinéa premier, ou si le demandeur dépose une déclaration inexacte relative aux conditions, visées aux articles 2bis et 2ter, les subventions d'investissement octroyées seront recouvrées, conformément à l'article 13 de la loi du 16 mai 2003 fixant les dispositions générales applicables aux budgets, au contrôle des subventions et à la comptabilité des communautés et des régions, ainsi qu'à l'organisation du contrôle de la Cour des comptes.......",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-42\"><header class=\"article-header\"><h2 class=\"article-number\">Article 42</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>En cas d'infraction aux dispositions de l'article 40, § 1er, alinéa trois,<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"et de l'article 41\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024053116#Art.12\" data-article-dossier-number=\"\">et de l'article 41</span>, § 1er et § 2, alinéa premier, ou si le demandeur dépose une déclaration inexacte relative aux conditions, visées aux articles 2bis et 2ter, les subventions d'investissement octroyées seront recouvrées, conformément à l'article 13 de la loi du 16 mai 2003 fixant les dispositions générales applicables aux budgets, au contrôle des subventions et à la comptabilité des communautés et des régions, ainsi qu'à l'organisation du contrôle de la Cour des comptes<span class=\"footnote-ref\" data-footnote-id=\"3\" data-referenced-text=\"...\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2024053116#Art.12\" data-article-dossier-number=\"\">...</span>....</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.329322"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<AGF [2014-02-14/26](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426), art. 23, 017; En vigueur : 25-04-2014>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2014-02-14/26",
                        "article_number": "art. 23",
                        "sequence_number": "017",
                        "full_reference": "AGF [2014-02-14/26]"
                    },
                    "effective_date": "25-04-2014",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2014021426#Art.23"
                    },
                    {
                    "footnote_number": "2",
                    "footnote_content": "(2)<AGF [2015-10-30/22](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2015103022), art. 2, 019; En vigueur : 14-12-2015>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2015-10-30/22",
                        "article_number": "art. 2",
                        "sequence_number": "019",
                        "full_reference": "AGF [2015-10-30/22]"
                    },
                    "effective_date": "14-12-2015",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2015103022",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2015103022#Art.2"
                    },
                    {
                    "footnote_number": "3",
                    "footnote_content": "(3)<AGF [2024-05-31/16](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116), art. 12, 033; En vigueur : 01-08-2024>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2024-05-31/16",
                        "article_number": "art. 12",
                        "sequence_number": "033",
                        "full_reference": "AGF [2024-05-31/16]"
                    },
                    "effective_date": "01-08-2024",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2024053116#Art.12"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "3",
                    "text_position": 79,
                    "referenced_text": "et de l'article 41",
                    "embedded_law_references": [],
                    "bracket_pattern": "[3 et de l'article 41]3"
                    },
                    {
                    "reference_number": "3",
                    "text_position": 563,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[3 ...]3"
                    },
                    {
                    "reference_number": "3",
                    "text_position": 574,
                    "referenced_text": "...",
                    "embedded_law_references": [],
                    "bracket_pattern": "[3 ...]3"
                    }
                ]
                },
                {
                "type": "article",
                "label": "Article 42bis",
                "metadata": {
                    "article_range": "42bis",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "42bis",
                    "anchor_id": "art_42bis",
                    "content": {
                    "main_text_raw": "Le demandeur, le financier ou l'investisseur transmet les documents, y compris les plans, par voie électronique au Fonds ou à l'administration fonctionnellement compétente. Les plans sont en outre transmis en double exemplaire sur papier.",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-42bis\"><header class=\"article-header\"><h2 class=\"article-number\">Article 42bis</h2></header><div class=\"article-content\"><div class=\"article-text\"><p><span class=\"footnote-ref\" data-footnote-id=\"2\" data-referenced-text=\"Le demandeur, le financier ou l'investisseur\" data-direct-article-url=\"https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&amp;lg_txt=f&amp;cn_search=2019051767#Art.5\" data-article-dossier-number=\"\">Le demandeur, le financier ou l'investisseur</span>transmet les documents, y compris les plans, par voie électronique au Fonds ou à l'administration fonctionnellement compétente. Les plans sont en outre transmis en double exemplaire sur papier.</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.329460"
                    }
                    }
                },
                "footnotes": [
                    {
                    "footnote_number": "1",
                    "footnote_content": "(1)<AGF [2016-01-15/17](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517), art. 21, 020; En vigueur : 20-03-2016>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2016-01-15/17",
                        "article_number": "art. 21",
                        "sequence_number": "020",
                        "full_reference": "AGF [2016-01-15/17]"
                    },
                    "effective_date": "20-03-2016",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2016011517#Art.21"
                    },
                    {
                    "footnote_number": "2",
                    "footnote_content": "(2)<AGF [2019-05-17/67](https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767), art. 5, 024; En vigueur : 19-09-2019>",
                    "law_reference": {
                        "law_type": "AGF",
                        "date_reference": "2019-05-17/67",
                        "article_number": "art. 5",
                        "sequence_number": "024",
                        "full_reference": "AGF [2019-05-17/67]"
                    },
                    "effective_date": "19-09-2019",
                    "modification_type": "modification",
                    "direct_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767",
                    "direct_article_url": "https://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&lg_txt=f&cn_search=2019051767#Art.5"
                    }
                ],
                "footnote_references": [
                    {
                    "reference_number": "2",
                    "text_position": 4,
                    "referenced_text": "Le demandeur, le financier ou l'investisseur",
                    "embedded_law_references": [],
                    "bracket_pattern": "[2 Le demandeur, le financier ou l'investisseur]2"
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE VIII. Dispositions finales.",
            "metadata": {
                "title_type": "CHAPITRE VIII.",
                "title_content": "Dispositions finales.",
                "rank": 2
            },
            "children": [
                {
                "type": "article",
                "label": "Article 43",
                "metadata": {
                    "article_range": "43",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "43",
                    "anchor_id": "art_43",
                    "content": {
                    "main_text_raw": "L'arrête du Gouvernement flamand du 6 juillet 1994 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables, modifié par les arrêtés du Gouvernement flamand des 30 novembre 1994, 5 avril 1995, 23 septembre 1997 et 10 mars 1998, est abrogé.",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-43\"><header class=\"article-header\"><h2 class=\"article-number\">Article 43</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>L'arrête du Gouvernement flamand du 6 juillet 1994 établissant les règles de procédure relatives à l'infrastructure affectée aux matières personnalisables, modifié par les arrêtés du Gouvernement flamand des 30 novembre 1994, 5 avril 1995, 23 septembre 1997 et 10 mars 1998, est abrogé.</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.329566"
                    }
                    }
                },
                "footnotes": [],
                "footnote_references": []
                },
                {
                "type": "article",
                "label": "Article 44",
                "metadata": {
                    "article_range": "44",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "44",
                    "anchor_id": "art_44",
                    "content": {
                    "main_text_raw": "Le Ministre flamand, ayant les investissements en faveur d'établissements de soins dans ses attributions, est chargé de l'exécution du présent arrêté.",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-44\"><header class=\"article-header\"><h2 class=\"article-number\">Article 44</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Le Ministre flamand, ayant les investissements en faveur d'établissements de soins dans ses attributions, est chargé de l'exécution du présent arrêté.</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:05:18.329673"
                    }
                    }
                },
                "footnotes": [],
                "footnote_references": []
                }
            ]
            }
        ],
        "references": {
            "modifies": [],
            "modified_by": [
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2024-09-11",
                "modified_articles": [
                "1",
                "15",
                "16",
                "19",
                "20",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2024/09/11_2.pdf#Page273",
                "full_title": "Arrêté gouvernement flamand du 19-07-2024 publié le 11-09-2024"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2024-08-07",
                "modified_articles": [
                "1",
                "4",
                "16"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2024/08/07_1.pdf#Page72",
                "full_title": "Arrêté gouvernement flamand du 21-06-2024 publié le 07-08-2024"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2024-07-31",
                "modified_articles": [
                "15",
                "40",
                "41",
                "42"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2024/07/31_1.pdf#Page207",
                "full_title": "Arrêté gouvernement flamand du 31-05-2024 publié le 31-07-2024"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2023-06-30",
                "modified_articles": [
                "1",
                "9"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2023/06/30_1.pdf#Page128",
                "full_title": "Arrêté gouvernement flamand du 12-05-2023 publié le 30-06-2023"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2023-03-10",
                "modified_articles": [
                "20",
                "28"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2023/03/10_1.pdf#Page331",
                "full_title": "Arrêté gouvernement flamand du 13-01-2023 publié le 10-03-2023"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2022-08-02",
                "modified_articles": [
                "4",
                "15",
                "19",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2022/08/02_1.pdf#Page146",
                "full_title": "Arrêté gouvernement flamand du 06-05-2022 publié le 02-08-2022"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2021-09-10",
                "modified_articles": [
                "1",
                "4",
                "5",
                "6",
                "9",
                "15",
                "16",
                "19"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2021/09/10_1.pdf#Page124",
                "full_title": "Arrêté gouvernement flamand du 16-07-2021 publié le 10-09-2021"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2021-06-25",
                "modified_articles": [
                "1",
                "5"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2021/06/25_2.pdf#Page105",
                "full_title": "Arrêté gouvernement flamand du 12-03-2021 publié le 25-06-2021"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2020-05-26",
                "modified_articles": [
                "38"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2020/05/26_1.pdf#Page108",
                "full_title": "Arrêté gouvernement flamand du 08-05-2020 publié le 26-05-2020"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2020-01-10",
                "modified_articles": [
                "1",
                "4",
                "15",
                "16"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2020/01/10_1.pdf#Page22",
                "full_title": "Arrêté gouvernement flamand du 13-12-2019 publié le 10-01-2020"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2019-09-09",
                "modified_articles": [
                "1",
                "15",
                "20",
                "21",
                "42bis"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2019/09/09_1.pdf#Page201",
                "full_title": "Arrêté gouvernement flamand du 17-05-2019 publié le 09-09-2019"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2018-12-28",
                "modified_articles": [
                "16"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2018/12/28_1.pdf#Page233",
                "full_title": "Arrêté gouvernement flamand du 23-11-2018 publié le 28-12-2018"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2018-10-01",
                "modified_articles": [
                "2bis",
                "2ter",
                "4",
                "6",
                "15",
                "16",
                "20",
                "22",
                "23",
                "24",
                "28",
                "36",
                "36bis",
                "40"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2018/10/01_1.pdf#Page44",
                "full_title": "Arrêté gouvernement flamand du 06-07-2018 publié le 01-10-2018"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2016-12-22",
                "modified_articles": [
                "4"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2016/12/22_1.pdf#Page70",
                "full_title": "Arrêté gouvernement flamand du 18-11-2016 publié le 22-12-2016"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2016-03-10",
                "modified_articles": [
                "1",
                "2bis",
                "4",
                "5",
                "6",
                "8",
                "9",
                "10",
                "13",
                "15",
                "16",
                "17",
                "18",
                "19",
                "20",
                "21",
                "22",
                "23",
                "24",
                "25",
                "26",
                "27",
                "28",
                "29",
                "30",
                "31",
                "32",
                "34",
                "35",
                "41",
                "42bis"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2016/03/10_1.pdf#Page48",
                "full_title": "Arrêté gouvernement flamand du 15-01-2016 publié le 10-03-2016"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2016-02-23",
                "modified_articles": [
                "22"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2016/02/23_1_6.pdf#Page91",
                "full_title": "Arrêté gouvernement flamand du 27-11-2015 publié le 23-02-2016"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2015-12-04",
                "modified_articles": [
                "41",
                "42"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2015/12/04_1.pdf#Page48",
                "full_title": "Arrêté gouvernement flamand du 30-10-2015 publié le 04-12-2015"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2014-11-03",
                "modified_articles": [
                "1",
                "4",
                "5",
                "8",
                "9",
                "15",
                "16",
                "18",
                "19"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2014/11/03_1.pdf#Page20",
                "full_title": "Arrêté gouvernement flamand du 05-09-2014 publié le 03-11-2014"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2014-04-15",
                "modified_articles": [
                "1",
                "4",
                "7",
                "11",
                "13",
                "17",
                "18",
                "20",
                "24",
                "25",
                "27",
                "34",
                "36bis",
                "36quater",
                "36quinquies",
                "36septies",
                "37",
                "39",
                "40",
                "41",
                "42",
                "42bis"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2014/04/15_1.pdf#Page92",
                "full_title": "Arrêté gouvernement flamand du 14-02-2014 publié le 15-04-2014"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2011-12-09",
                "modified_articles": [
                "1",
                "2",
                "2bis",
                "2ter",
                "3-9",
                "11",
                "13-23",
                "25-27",
                "29",
                "31",
                "32",
                "34-36",
                "36bis-36septies",
                "37",
                "39",
                "40-42",
                "42bis"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2011/12/09_2.pdf#Page18",
                "full_title": "Arrêté gouvernement flamand du 10-11-2011 publié le 09-12-2011"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2011-03-28",
                "modified_articles": [
                "15"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2011/12/09_2.pdf#Page18",
                "full_title": "Arrêté gouvernement flamand du 04-03-2011 publié le 28-03-2011"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2010-10-19",
                "modified_articles": [
                "15"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2010/10/19_1.pdf#Page30",
                "full_title": "Arrêté gouvernement flamand du 10-09-2010 publié le 19-10-2010"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2010-10-19",
                "modified_articles": [
                "15"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2010/10/19_1.pdf#Page23",
                "full_title": "Arrêté gouvernement flamand du 10-09-2010 publié le 19-10-2010"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2010-08-18",
                "modified_articles": [
                "15"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2010/08/18_2.pdf#Page100",
                "full_title": "Arrêté gouvernement flamand du 16-07-2010 publié le 18-08-2010"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2010-07-27",
                "modified_articles": [
                "15"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2010/07/27_1.pdf#Page35",
                "full_title": "Arrêté gouvernement flamand du 18-06-2010 publié le 27-07-2010"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2010-06-25",
                "modified_articles": [
                "1",
                "27"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2010/06/25_2.pdf#Page151",
                "full_title": "Arrêté gouvernement flamand du 04-06-2010 publié le 25-06-2010"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2009-12-17",
                "modified_articles": [
                "1",
                "4",
                "5",
                "8",
                "9",
                "15",
                "16",
                "19",
                "35"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2009/12/17_1.pdf#Page59",
                "full_title": "Arrêté gouvernement flamand du 24-07-2009 publié le 17-12-2009"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2009-09-03",
                "modified_articles": [
                "15"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2009/09/03_3.pdf#Page106",
                "full_title": "Arrêté gouvernement flamand du 19-06-2009 publié le 03-09-2009"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2008-10-30",
                "modified_articles": [
                "40"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2008/10/30_1.pdf#Page116",
                "full_title": "Arrêté gouvernement flamand du 18-07-2008 publié le 30-10-2008"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2008-09-23",
                "modified_articles": [
                "1",
                "3-13",
                "15-17",
                "19-22",
                "24-33",
                "35",
                "36"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2008/09/23_1.pdf#Page89",
                "full_title": "Arrêté gouvernement flamand du 30-05-2008 publié le 23-09-2008"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2006-05-31",
                "modified_articles": [
                "1",
                "6",
                "7",
                "9",
                "19",
                "35"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2006/05/31_2.pdf#Page262",
                "full_title": "Arrêté gouvernement flamand du 31-03-2006 publié le 31-05-2006"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2004-08-05",
                "modified_articles": [
                "22",
                "23"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2004/08/05_1.pdf#Page73",
                "full_title": "Arrêté gouvernement flamand du 23-04-2004 publié le 05-08-2004"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2002-07-02",
                "modified_articles": [
                "1",
                "4",
                "5",
                "7",
                "8",
                "9",
                "15",
                "16",
                "19"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2002/07/02_1.pdf#Page7",
                "full_title": "Arrêté gouvernement flamand du 19-04-2002 publié le 02-07-2002"
            },
            {
                "modification_type": "",
                "modification_date": "",
                "publication_date": "2001-04-24",
                "modified_articles": [
                "19"
                ],
                "source_url": "https://www.ejustice.just.fgov.be/mopdf/2001/04/24_1.pdf#Page19",
                "full_title": "Arrêté gouvernement flamand du 09-03-2001 publié le 24-04-2001"
            }
            ]
        },
        "external_links": {
            "official_links": [],
            "parliamentary_work": []
        },
        "extraction_metadata": {
            "extraction_date": "2025-08-19T14:05:18.330396",
            "source_file": "1999036088.md",
            "sections_included": [
            "document_metadata",
            "document_hierarchy",
            "references"
            ],
            "sections_excluded": [
            "articles",
            "legal_references",
            "modification_history"
            ],
            "completeness_flags": {
            "all_articles_extracted": True,
            "footnotes_linked": True,
            "hierarchical_structure_complete": True,
            "metadata_complete": True,
            "is_minimal_document": False,
            "preamble_extracted": True,
            "is_abrogated_document": False
            }
        }
    }


def get_json_2016A29166():
    """
    Return corrected JSON for document 2016A29166.
    This document has duplicate CHAPITRE 2 nodes that need to be merged.
    """
    # PASTE THE COMPLETE CORRECTED JSON HERE
    # You can load output/24/2016A29166.json, fix the duplicate CHAPITRE 2,
    # and paste the entire corrected structure here
    return {
        "document_metadata": {
            "document_number": "2016A29166",
            "title": "25 NOVEMBRE 2015. - Décision de la Commission paritaire de l'enseignement fondamental libre confessionnel du 25 novembre 2015 relative à la procédure électorale pour la mise en place ou le renouvellement des instances de concertation locales",
            "publication_date": "2016-04-18",
            "source": "Communauté française",
            "page_number": 26305,
            "dossier_number": "2015-11-25/24",
            "effective_date": "2015-11-25",
            "end_validity_date": "",
            "language": "fr",
            "document_type": "unknown",
            "status": "active",
            "version_info": {
            "archived_versions_count": 0,
            "archived_versions_url": "",
            "execution_orders_count": 0,
            "execution_orders_url": ""
            },
            "official_justel_url": "http://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&sum_date=&lg_txt=f&numac_search=2016A29166",
            "official_publication_pdf_url": "https://www.ejustice.just.fgov.be/mopdf/2016/04/18_1.pdf#Page193",
            "consolidated_pdf_url": ""
        },
        "preamble": "En sa séance du 25 novembre 2015, la Commission paritaire de l'enseignement fondamental libre confessionnel a adopté à l'unanimité la présente décision.\nCOMMISSION PARITAIRE DE L'ENSEIGNEMENT FONDAMENTAL LIBRE CONFESSIONNEL: PROCEDURE ELECTORALE POUR LA MISE EN PLACE OU LE RENOUVELLEMENT DES INSTANCES DE CONCERTATION LOCALES\nPréambule\n1. L'emploi dans la présente décision des noms masculins pour les différents titres et fonctions est épicène en vue d'assurer la lisibilité du texte nonobstant les dispositions du décret du 21 juin 1993 relatif à la féminisation des noms de métier.\n2. La procédure électorale décrite ci-dessous vise exclusivement à déterminer la représentativité des délégations syndicales au sein des I.C.L.\nElle ne concerne pas la désignation des représentants des membres du personnel au sein des sections fondamentales des C.E. et C.P.P.T.\n3. a) Les élections pour le renouvellement des représentants du personnel au sein des I.C.L. ou pour la désignation des représentants du personnel là où il n'y a pas d'I.C.L. auront lieu pendant la période prévue pour les élections sociales 2016 entre le 9 et le 22 mai 2016.\nb) Les I.C.L. à mettre en place ne doivent faire l'objet d'une élection que si une organisation syndicale en fait la demande par écrit auprès du P.O. avant le 15 février 2016.\n4. En fonction du calendrier scolaire 2015-2016, la commission paritaire recommande d'éviter de choisir comme date d'élection les dates suivantes : 10, 11, 17 et 18 mai.",
        "abrogation_info": {},
        "document_hierarchy": [
            {
            "type": "chapitre",
            "label": "CHAPITRE 1er. Procédure électorale avec calendrier commun",
            "metadata": {
                "title_type": "CHAPITRE 1er.",
                "title_content": "Procédure électorale avec calendrier commun",
                "rank": 2
            },
            "children": [
                {
                "type": "section",
                "label": "Première étape",
                "metadata": {
                    "title_type": "Première étape",
                    "title_content": "",
                    "rank": 3
                },
                "children": []
                },
                {
                "type": "section",
                "label": "Organisation du calendrier",
                "metadata": {
                    "title_type": "Organisation du calendrier",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 1er",
                    "metadata": {
                        "article_range": "1er",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "1er",
                        "anchor_id": "art_1er",
                        "content": {
                        "main_text_raw": "- 1. Les organisations syndicales sont tenues de déposer leur liste de candidats au plus tard le 14 mars 2016 par envoi recommandé ou par remise de la main à la main avec accusé de réception auprès du Président du P.O. ou de son délégué. La lettre recommandée produit ses effets le 3e jour ouvrable qui suit son envoi. 2. Au plus tard pour le 14 mars 2016, le P.O. fixe en concertation avec l'Instance de concertation locale en place ou à défaut, avec la délégation syndicale qui demande la mise en place d'une I.C.L.: a) la date des élections qui doit obligatoirement se situer entre le 9 et le 22 mai inclus ainsi que le calendrier de la procédure; b) la liste des électeurs par bureau de vote et par ordre alphabétique. Elle doit mentionner le nom, prénom, date de naissance et sexe des électeurs ainsi que leur(s) lieu(x) de travail; c) le nombre de mandats à pourvoir (en fonction de l'article 7 de la décision de la Commission Paritaire du 24 janvier 1996 portant création d'une I.C.L. - le nombre des membres du personnel étant celui calculé en référence au capital-périodes utilisé par le Pouvoir Organisateur divisé par 24 membres en primaire et en référence au nombre d'emplois en maternelle fixé selon la dernière dépêche ministérielle accordant les subventions-traitements reçues au jour des élections). Cette disposition modifie l'article 7, § 2 b, dernier alinéa de la décision du 24 janvier 1996 portant création des I.C.L. d) le nombre de bureaux de vote, leurs lieu et heures d'ouverture. Dans le cas où plusieurs bureaux de vote sont prévus, il sera procédé à la désignation d'un bureau principal chargé du dépouillement; en principe, un bureau de vote sera établi par établissement distant de plus de 300 m d'un autre établissement, sauf accord contraire des parties; e) la composition des bureaux de vote (un Président, un Secrétaire et au minimum un assesseur). Les candidats ne peuvent en être membres sauf si le nombre de membres du personnel ne permet pas de faire autrement. f) les lieux prévus pour l'affichage; Les élections ont lieu aux jour, heure et lieu habituels d'activités scolaires. 3. Pour le 18 mars 2016 au plus tard, le P.O. procède à l'affichage des décisions qu'il a prises suite à la concertation visée au point 2 ainsi qu'à l'affichage des listes de candidats. 4. Jusqu'au 22 mars 2016, toutes les parties concernées peuvent formuler toute réclamation qu'elles jugeront utiles, soit au sujet des décisions prises par le P.O. telles qu'affichées conformément au point 3, soit au sujet de la procédure électorale, soit au sujet des listes de candidats. Ces réclamations sont introduites comme suit: -les membres du personnel soumis au décret du 1er février 1993 et au décret du 2 juin 2006 et les organisations syndicales doivent introduire leurs réclamations au sujet des décisions prises par l'employeur telles qu'affichées conformément au point 3, au sujet de la procédure électorale ou des listes de candidats auprès de l'I.C.L. ou, à défaut, auprès du Président du P.O. ou de son délégué pour le 22 mars au plus tard. En cas de réclamation d'un ou de plusieurs membres du personnel auprès du Président du P.O. ou de son délégué, celui-ci transmet la réclamation aux organisations syndicales concernées le 1er jour ouvrable qui suit la réception de la réclamation. - le P.O. doit introduire ses réclamations au sujet des listes de candidats auprès de l'I.C.L. ou, à défaut, auprès des organisations syndicales concernées pour le 22 mars au plus tard. Le cas échéant, les délégués du personnel siégeant à l'I.C.L. transmettent la réclamation du P.O. à leur organisation syndicale. 5. Jusqu'au 25 mars 2016, les réclamations pourront être réglées de façon interne soit au sein de l'I.C.L., soit en concertation entre le P.O. et les organisations syndicales concernées. En cas de litige persistant, celui-ci sera soumis au bureau de conciliation de la Commission paritaire de l'Enseignement fondamental libre confessionnel qui se réunira le 15 avril 2016. Le litige sera transmis au Président de la Commission paritaire de l'Enseignement fondamental libre confessionnel au plus tard le 12 avril à l'adresse suivante: M. Benoît MPEYE BULA BULA, 2E 245 Pour M. Frédéric NOLLET, Président de la Commission paritaire de l'Enseignement fondamental libre confessionnel Boulevard Léopold II, 44 1080 Bruxelles (Tél. 02-413 21 58 - fax 02-413 40 48 - e-mail: benoit.mpeyebulabula@cfwb.be)",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-1er\"><header class=\"article-header\"><h2 class=\"article-number\">Article 1er</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- 1. Les organisations syndicales sont tenues de déposer leur liste de candidats au plus tard le 14 mars 2016 par envoi recommandé ou par remise de la main à la main avec accusé de réception auprès du Président du P.O. ou de son délégué. La lettre recommandée produit ses effets le 3e jour ouvrable qui suit son envoi. 2. Au plus tard pour le 14 mars 2016, le P.O. fixe en concertation avec l'Instance de concertation locale en place ou à défaut, avec la délégation syndicale qui demande la mise en place d'une I.C.L.: a) la date des élections qui doit obligatoirement se situer entre le 9 et le 22 mai inclus ainsi que le calendrier de la procédure; b) la liste des électeurs par bureau de vote et par ordre alphabétique. Elle doit mentionner le nom, prénom, date de naissance et sexe des électeurs ainsi que leur(s) lieu(x) de travail; c) le nombre de mandats à pourvoir (en fonction de l'article 7 de la décision de la Commission Paritaire du 24 janvier 1996 portant création d'une I.C.L. - le nombre des membres du personnel étant celui calculé en référence au capital-périodes utilisé par le Pouvoir Organisateur divisé par 24 membres en primaire et en référence au nombre d'emplois en maternelle fixé selon la dernière dépêche ministérielle accordant les subventions-traitements reçues au jour des élections). Cette disposition modifie l'article 7, § 2 b, dernier alinéa de la décision du 24 janvier 1996 portant création des I.C.L. d) le nombre de bureaux de vote, leurs lieu et heures d'ouverture. Dans le cas où plusieurs bureaux de vote sont prévus, il sera procédé à la désignation d'un bureau principal chargé du dépouillement; en principe, un bureau de vote sera établi par établissement distant de plus de 300 m d'un autre établissement, sauf accord contraire des parties; e) la composition des bureaux de vote (un Président, un Secrétaire et au minimum un assesseur). Les candidats ne peuvent en être membres sauf si le nombre de membres du personnel ne permet pas de faire autrement. f) les lieux prévus pour l'affichage; Les élections ont lieu aux jour, heure et lieu habituels d'activités scolaires. 3. Pour le 18 mars 2016 au plus tard, le P.O. procède à l'affichage des décisions qu'il a prises suite à la concertation visée au point 2 ainsi qu'à l'affichage des listes de candidats. 4. Jusqu'au 22 mars 2016, toutes les parties concernées peuvent formuler toute réclamation qu'elles jugeront utiles, soit au sujet des décisions prises par le P.O. telles qu'affichées conformément au point 3, soit au sujet de la procédure électorale, soit au sujet des listes de candidats. Ces réclamations sont introduites comme suit: -les membres du personnel soumis au décret du 1er février 1993 et au décret du 2 juin 2006 et les organisations syndicales doivent introduire leurs réclamations au sujet des décisions prises par l'employeur telles qu'affichées conformément au point 3, au sujet de la procédure électorale ou des listes de candidats auprès de l'I.C.L. ou, à défaut, auprès du Président du P.O. ou de son délégué pour le 22 mars au plus tard. En cas de réclamation d'un ou de plusieurs membres du personnel auprès du Président du P.O. ou de son délégué, celui-ci transmet la réclamation aux organisations syndicales concernées le 1er jour ouvrable qui suit la réception de la réclamation. - le P.O. doit introduire ses réclamations au sujet des listes de candidats auprès de l'I.C.L. ou, à défaut, auprès des organisations syndicales concernées pour le 22 mars au plus tard. Le cas échéant, les délégués du personnel siégeant à l'I.C.L. transmettent la réclamation du P.O. à leur organisation syndicale. 5. Jusqu'au 25 mars 2016, les réclamations pourront être réglées de façon interne soit au sein de l'I.C.L., soit en concertation entre le P.O. et les organisations syndicales concernées. En cas de litige persistant, celui-ci sera soumis au bureau de conciliation de la Commission paritaire de l'Enseignement fondamental libre confessionnel qui se réunira le 15 avril 2016. Le litige sera transmis au Président de la Commission paritaire de l'Enseignement fondamental libre confessionnel au plus tard le 12 avril à l'adresse suivante: M. Benoît MPEYE BULA BULA, 2E 245 Pour M. Frédéric NOLLET, Président de la Commission paritaire de l'Enseignement fondamental libre confessionnel Boulevard Léopold II, 44 1080 Bruxelles (Tél. 02-413 21 58 - fax 02-413 40 48 - e-mail: benoit.mpeyebulabula@cfwb.be)</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.009994"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                }
            ]
            },
            {
            "type": "chapitre",
            "label": "CHAPITRE 2. Procédure avec calendrier spécifique en fonction de la date fixée par le Pouvoir Organisateur pour l'élection de l'I.C.L.",
            "metadata": {
                "title_type": "CHAPITRE 2.",
                "title_content": "Procédure avec calendrier spécifique en fonction de la date fixée par le Pouvoir Organisateur pour l'élection de l'I.C.L.",
                "rank": 2
            },
            "children": [
                {
                "type": "section",
                "label": "Deuxième étape",
                "metadata": {
                    "title_type": "Deuxième étape",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 2",
                    "metadata": {
                        "article_range": "2",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "2",
                        "anchor_id": "art_2",
                        "content": {
                        "main_text_raw": "- 1. La date des élections, fixée en respect de l'article 1er, § 2 a, doit nécessairement se situer entre le 9 et le 22 mai inclus. 2. Dans le cas où une étape de la procédure se termine un samedi, un dimanche ou un jour de fermeture de l'établissement, il y a lieu de prendre en compte le dernier jour ouvrable qui précède immédiatement ce jour.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-2\"><header class=\"article-header\"><h2 class=\"article-number\">Article 2</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- 1. La date des élections, fixée en respect de l'article 1er, § 2 a, doit nécessairement se situer entre le 9 et le 22 mai inclus. 2. Dans le cas où une étape de la procédure se termine un samedi, un dimanche ou un jour de fermeture de l'établissement, il y a lieu de prendre en compte le dernier jour ouvrable qui précède immédiatement ce jour.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.010109"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Affichage des informations",
                "metadata": {
                    "title_type": "Affichage des informations",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 3",
                    "metadata": {
                        "article_range": "3",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "3",
                        "anchor_id": "art_3",
                        "content": {
                        "main_text_raw": "- 1. Jusqu'au 12e jour précédant les élections, les organisations syndicales qui ont présenté une liste pourront, après en avoir informé le P.O., remplacer un candidat qui figure sur les listes affichées, dans les cas suivants: - le décès d'un candidat; - la démission d'un candidat de son emploi; - la démission ou l'exclusion d'un candidat de l'organisation représentative des membres du personnel qui l'a présenté; - le retrait par un candidat de sa candidature. Le nouveau candidat figurera sur la liste, au choix de l'organisation qui a présenté sa candidature, soit à la même place que le candidat qu'il remplace, soit comme dernier candidat à la fin de la liste. Ces modifications seront affichées par le P.O., dès que le remplacement lui aura été signifié, aux lieux prévus. Le 11e jour avant la date fixée pour les élections, le P.O. procède à l'affichage des listes définitives d'électeurs et de candidats. Il procède également au toilettage des listes d'électeurs rayant les personnes qui ne sont plus membres du personnel à cette date.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-3\"><header class=\"article-header\"><h2 class=\"article-number\">Article 3</h2></header><div class=\"article-content\"><div class=\"article-text\"><ul class=\"hyphenated-items\"><li class=\"hyphenated-item\"><span class=\"item-text\">le décès d'un candidat</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">la démission d'un candidat de son emploi</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">la démission ou l'exclusion d'un candidat de l'organisation représentative des membres du personnel qui l'a présenté</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">le retrait par un candidat de sa candidature.</span></li></ul><div class=\"closing-text\"><p>Le nouveau candidat figurera sur la liste, au choix de l'organisation qui a présenté sa candidature, soit à la même place que le candidat qu'il remplace, soit comme dernier candidat à la fin de la liste. Ces modifications seront affichées par le P.O., dès que le remplacement lui aura été signifié, aux lieux prévus. Le 11e jour avant la date fixée pour les élections, le P.O. procède à l'affichage des listes définitives d'électeurs et de candidats. Il procède également au toilettage des listes d'électeurs rayant les personnes qui ne sont plus membres du personnel à cette date.</p></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.010318"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Dispense d'organiser les élections",
                "metadata": {
                    "title_type": "Dispense d'organiser les élections",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 4",
                    "metadata": {
                        "article_range": "4",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "4",
                        "anchor_id": "art_4",
                        "content": {
                        "main_text_raw": "- La procédure électorale est arrêtée 12 jours avant la date fixée pour l'élection lorsqu'une seule organisation syndicale est représentée et présente un nombre de candidats égal ou inférieur au nombre de mandats maximum par liste à attribuer. Dans ce cas, ces candidats sont élus d'office. Le bureau électoral doit néanmoins se réunir pour établir un procès-verbal où il indiquera qu'il n'y a pas eu de vote pour le motif énoncé ci-dessus. La décision d'arrêter la procédure et la composition de l'I.C.L. sont communiquées aux membres du personnel par voie d'affichage.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-4\"><header class=\"article-header\"><h2 class=\"article-number\">Article 4</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- La procédure électorale est arrêtée 12 jours avant la date fixée pour l'élection lorsqu'une seule organisation syndicale est représentée et présente un nombre de candidats égal ou inférieur au nombre de mandats maximum par liste à attribuer. Dans ce cas, ces candidats sont élus d'office. Le bureau électoral doit néanmoins se réunir pour établir un procès-verbal où il indiquera qu'il n'y a pas eu de vote pour le motif énoncé ci-dessus. La décision d'arrêter la procédure et la composition de l'I.C.L. sont communiquées aux membres du personnel par voie d'affichage.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.010446"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Convocations",
                "metadata": {
                    "title_type": "Convocations",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 5",
                    "metadata": {
                        "article_range": "5",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "5",
                        "anchor_id": "art_5",
                        "content": {
                        "main_text_raw": "- 1. Au plus tard 10 jours avant la date fixée pour l'élection, le P.O. informe les électeurs que les convocations sont mises à leur disposition au bureau de la direction et, ce, jusqu'au jour fixé pour l'élection. Chaque électeur en accusera réception au moment où il recevra sa convocation. Cette convocation reprend la date, l'heure et le lieu du bureau de vote choisi pour les élections. 2. Au plus tard 10 jours avant la date fixée pour l'élection, le P.O. notifie une convocation à tous les membres du personnel temporairement éloignés du service et dont la durée d'éloignement couvre au minimum la période du 11 avril jusqu'à la date fixée pour les élections. Cette notification se fait soit par lettre recommandée, soit par remise de la main à la main contre accusé de réception en y joignant la liste des candidats.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-5\"><header class=\"article-header\"><h2 class=\"article-number\">Article 5</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- 1. Au plus tard 10 jours avant la date fixée pour l'élection, le P.O. informe les électeurs que les convocations sont mises à leur disposition au bureau de la direction et, ce, jusqu'au jour fixé pour l'élection. Chaque électeur en accusera réception au moment où il recevra sa convocation. Cette convocation reprend la date, l'heure et le lieu du bureau de vote choisi pour les élections. 2. Au plus tard 10 jours avant la date fixée pour l'élection, le P.O. notifie une convocation à tous les membres du personnel temporairement éloignés du service et dont la durée d'éloignement couvre au minimum la période du 11 avril jusqu'à la date fixée pour les élections. Cette notification se fait soit par lettre recommandée, soit par remise de la main à la main contre accusé de réception en y joignant la liste des candidats.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.010598"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Qualité d'électeur",
                "metadata": {
                    "title_type": "Qualité d'électeur",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 6",
                    "metadata": {
                        "article_range": "6",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "6",
                        "anchor_id": "art_6",
                        "content": {
                        "main_text_raw": "- En conformité avec la décision du 24 janvier 1996 portant création des I.C.L., a la qualité d'électeur tout membre du personnel en activité de service (ou en maladie ou en congé assimilé à une activité de service) au sein du Pouvoir Organisateur et quel que soit l'horaire dont il dispose pour autant qu'il dispose d'une ancienneté de service au sein du P.O. d'au moins 15 semaines au moment des élections. Cette disposition modifie l'article 9 b in fine, de la décision du 24 janvier 1996 portant création des I.C.L. Tout membre du personnel mis en disponibilité par défaut d'emploi conserve la qualité d'électeur tant qu'il n'est pas entièrement réaffecté dans un établissement relevant d'un autre Pouvoir Organisateur. En outre, ont également la qualité d'électeurs, les puériculteurs engagés à titre définitif conformément aux dispositions du décret du 2 juin 2006 relatif au cadre organique et au statut des puériculteurs des établissements d'enseignement maternel ordinaire organisés et subventionnés par la Communauté française.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-6\"><header class=\"article-header\"><h2 class=\"article-number\">Article 6</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- En conformité avec la décision du 24 janvier 1996 portant création des I.C.L., a la qualité d'électeur tout membre du personnel en activité de service (ou en maladie ou en congé assimilé à une activité de service) au sein du Pouvoir Organisateur et quel que soit l'horaire dont il dispose pour autant qu'il dispose d'une ancienneté de service au sein du P.O. d'au moins 15 semaines au moment des élections. Cette disposition modifie l'article 9 b in fine, de la décision du 24 janvier 1996 portant création des I.C.L. Tout membre du personnel mis en disponibilité par défaut d'emploi conserve la qualité d'électeur tant qu'il n'est pas entièrement réaffecté dans un établissement relevant d'un autre Pouvoir Organisateur. En outre, ont également la qualité d'électeurs, les puériculteurs engagés à titre définitif conformément aux dispositions du décret du 2 juin 2006 relatif au cadre organique et au statut des puériculteurs des établissements d'enseignement maternel ordinaire organisés et subventionnés par la Communauté française.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.010768"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Conditions d'éligibilité",
                "metadata": {
                    "title_type": "Conditions d'éligibilité",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 7",
                    "metadata": {
                        "article_range": "7",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "7",
                        "anchor_id": "art_7",
                        "content": {
                        "main_text_raw": "- Sont éligibles les membres du personnel qui, à la date des élections, sont engagés à titre définitif à concurrence d'un 1/4 temps au moins par le Pouvoir Organisateur concerné et sont soumis aux dispositions du décret du 1er février 1993 fixant le statut des membres du personnel subsidiés de l'enseignement libre subventionné et aux dispositions du décret du 2 juin 2006 précité pour ce qui concerne les puériculteurs engagés à titre définitif, en activité de service ou en congé de maladie ou en congé assimilé à de l'activité de service. Tout membre du personnel mis en disponibilité par défaut d'emploi reste éligible tant qu'il n'est pas entièrement réaffecté dans un établissement relevant d'un autre Pouvoir Organisateur. Nul ne peut être membre de plus d'une I.C.L.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-7\"><header class=\"article-header\"><h2 class=\"article-number\">Article 7</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- Sont éligibles les membres du personnel qui, à la date des élections, sont engagés à titre définitif à concurrence d'un 1/4 temps au moins par le Pouvoir Organisateur concerné et sont soumis aux dispositions du décret du 1er février 1993 fixant le statut des membres du personnel subsidiés de l'enseignement libre subventionné et aux dispositions du décret du 2 juin 2006 précité pour ce qui concerne les puériculteurs engagés à titre définitif, en activité de service ou en congé de maladie ou en congé assimilé à de l'activité de service. Tout membre du personnel mis en disponibilité par défaut d'emploi reste éligible tant qu'il n'est pas entièrement réaffecté dans un établissement relevant d'un autre Pouvoir Organisateur. Nul ne peut être membre de plus d'une I.C.L.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.010913"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Bulletins de vote",
                "metadata": {
                    "title_type": "Bulletins de vote",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 8",
                    "metadata": {
                        "article_range": "8",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "8",
                        "anchor_id": "art_8",
                        "content": {
                        "main_text_raw": "- Les bulletins de vote, établis par le Pouvoir Organisateur, reprennent les listes déposées par les organisations syndicales sous les titres suivants: A.P.P.E.L., C.S.C.-Enseignement., S.E.L./SETCa.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-8\"><header class=\"article-header\"><h2 class=\"article-number\">Article 8</h2></header><div class=\"article-content\"><div class=\"article-text\"><ul class=\"hyphenated-items\"><li class=\"hyphenated-item\"><span class=\"item-text\">Les bulletins de vote, établis par le Pouvoir Organisateur, reprennent les listes déposées par les organisations syndicales sous les titres suivants: A.P.P.E.L., C.S.C.-Enseignement., S.E.L./SETCa.</span></li></ul></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.011007"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Le vote",
                "metadata": {
                    "title_type": "Le vote",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 9",
                    "metadata": {
                        "article_range": "9",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "9",
                        "anchor_id": "art_9",
                        "content": {
                        "main_text_raw": "- 1. Le vote n'est pas obligatoire. Toutefois, le P.O. encourage les membres du personnel à y participer de manière à assurer au mieux leur représentativité. 2. Le vote est à bulletin secret. L'électeur vote de manière nominative sur une même liste ou en tête de liste. 3. En cas de vote nominatif, le nombre maximum de votes émis ne peut dépasser le nombre de mandats à pourvoir. 4. En cas de vote en tête de liste assorti d'un vote nominatif sur une même liste, seul le vote nominatif sera pris en considération. 5. Est réputé nul, tout vote exprimé sur différentes listes ou tout bulletin qui ne respecterait pas les prescriptions décrites supra (points 2 et 3) ou tout vote qui porterait atteinte au secret du scrutin. 6. Le vote par procuration n'est autorisé qu'en cas de maladie ou incapacité de travail et sur production d'un certificat médical ou en cas de travail dans un autre établissement scolaire dépendant d'un autre P.O. ou auprès d'un autre employeur le jour des élections. Un membre du personnel ne peut être porteur que d'une seule procuration. La procuration datée et signée par le mandant et portant nom, prénom et date de naissance de la personne mandatée sera remise au Président du bureau électoral, lequel s'assurera de la conformité du document et signalera le fait au procès-verbal des élections. La procuration y sera annexée. 7. Un témoin par organisation syndicale pourra être présent dans le bureau de vote pour autant qu'il détienne un document probant de l'organisation syndicale.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-9\"><header class=\"article-header\"><h2 class=\"article-number\">Article 9</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- 1. Le vote n'est pas obligatoire. Toutefois, le P.O. encourage les membres du personnel à y participer de manière à assurer au mieux leur représentativité. 2. Le vote est à bulletin secret. L'électeur vote de manière nominative sur une même liste ou en tête de liste. 3. En cas de vote nominatif, le nombre maximum de votes émis ne peut dépasser le nombre de mandats à pourvoir. 4. En cas de vote en tête de liste assorti d'un vote nominatif sur une même liste, seul le vote nominatif sera pris en considération. 5. Est réputé nul, tout vote exprimé sur différentes listes ou tout bulletin qui ne respecterait pas les prescriptions décrites supra (points 2 et 3) ou tout vote qui porterait atteinte au secret du scrutin. 6. Le vote par procuration n'est autorisé qu'en cas de maladie ou incapacité de travail et sur production d'un certificat médical ou en cas de travail dans un autre établissement scolaire dépendant d'un autre P.O. ou auprès d'un autre employeur le jour des élections. Un membre du personnel ne peut être porteur que d'une seule procuration. La procuration datée et signée par le mandant et portant nom, prénom et date de naissance de la personne mandatée sera remise au Président du bureau électoral, lequel s'assurera de la conformité du document et signalera le fait au procès-verbal des élections. La procuration y sera annexée. 7. Un témoin par organisation syndicale pourra être présent dans le bureau de vote pour autant qu'il détienne un document probant de l'organisation syndicale.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.011229"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Le dépouillement",
                "metadata": {
                    "title_type": "Le dépouillement",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 10",
                    "metadata": {
                        "article_range": "10",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "10",
                        "anchor_id": "art_10",
                        "content": {
                        "main_text_raw": "- 1. Lorsque plusieurs bureaux de vote ont été constitués, les urnes contenant les bulletins de vote sont amenées sous scellés au bureau de vote désigné pour le dépouillement. Les témoins peuvent assister au transfert des urnes. 2. Le bureau de dépouillement dont le Président est le Président du Pouvoir Organisateur ou un membre délégué du Pouvoir Organisateur, est composé paritairement de représentants du Pouvoir Organisateur et de membres du personnel non candidats (temporaires ou définitifs). Il comporte au moins 2 membres du P.O., dont 1 assume la présidence, et 2 membres non candidats du personnel, dont l'un assume le secrétariat. Un membre candidat peut toutefois siéger dans le bureau électoral si le nombre de membres du personnel ne permet pas de faire autrement. Les témoins peuvent assister au dépouillement.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-10\"><header class=\"article-header\"><h2 class=\"article-number\">Article 10</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- 1. Lorsque plusieurs bureaux de vote ont été constitués, les urnes contenant les bulletins de vote sont amenées sous scellés au bureau de vote désigné pour le dépouillement. Les témoins peuvent assister au transfert des urnes. 2. Le bureau de dépouillement dont le Président est le Président du Pouvoir Organisateur ou un membre délégué du Pouvoir Organisateur, est composé paritairement de représentants du Pouvoir Organisateur et de membres du personnel non candidats (temporaires ou définitifs). Il comporte au moins 2 membres du P.O., dont 1 assume la présidence, et 2 membres non candidats du personnel, dont l'un assume le secrétariat. Un membre candidat peut toutefois siéger dans le bureau électoral si le nombre de membres du personnel ne permet pas de faire autrement. Les témoins peuvent assister au dépouillement.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.011378"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Dévolution des sièges",
                "metadata": {
                    "title_type": "Dévolution des sièges",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 11",
                    "metadata": {
                        "article_range": "11",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "11",
                        "anchor_id": "art_11",
                        "content": {
                        "main_text_raw": "- L'attribution des sièges entre organisations syndicales et la désignation des candidats élus à l'intérieur de chaque liste s'opère de la manière suivante: 1. Attribution de sièges entre organisations syndicales 1.1. Un siège est attribué par liste. 1.2. La dévolution des sièges supplémentaires éventuels s'établit comme suit: a) le nombre de voix obtenu par chaque organisation est divisé successivement par 2, 3, 4. On obtient ainsi des quotients électoraux qui déterminent l'attribution des sièges supplémentaires; b) en cas d'égalité du quotient électoral en a), c'est la liste qui a obtenu le plus de voix qui bénéficie du mandat supplémentaire. 2. Désignation des candidats à l'intérieur de chaque liste 2.1. Lorsque le nombre de candidats d'une liste est égal ou inférieur à celui de sièges revenant à cette liste, ces candidats sont tous élus. 2.2. Lorsque ce nombre est supérieur, les sièges sont confiés aux candidats qui atteignent le chiffre spécial d'éligibilité dans l'ordre de leur présentation. S'il reste des mandats à conférer, ils le sont aux candidats qui ont obtenu le plus grand nombre de voix. En cas de parité, l'ordre de présentation prévaut. 2.3 Préalablement à la désignation des élus, le bureau principal procède à l'attribution individuelle aux candidats des votes de liste favorables à l'ordre de présentation. 2.4. Le nombre de ces votes de liste est établi en multipliant le nombre de bulletins marqués tête de liste par le nombre de sièges obtenus par cette liste. L'attribution des votes de tête de liste se fait d'après un mode dévolutif: les votes de tête de liste sont ajoutés aux suffrages nominatifs obtenus par le premier candidat de la liste à concurrence de ce qui est nécessaire pour parfaire le chiffre d'éligibilité spécial à la liste. L'excédent, s'il y en a, est attribué dans une mesure semblable au deuxième candidat et ainsi de suite jusqu'à ce que tous les votes de listes aient été attribués. 2.5. Le chiffre d'éligibilité spécial à chaque liste s'obtient en divisant par le nombre plus un de sièges attribués à la liste l'ensemble des suffrages utiles. Lorsqu'il comprend une décimale, il est arrondi au chiffre inférieur pour une décimale de un à quatre, au chiffre supérieur pour une décimale de 5 à neuf. 2.6. L'ensemble des suffrages utiles est établi en multipliant le nombre de bulletins contenant un vote valable en tête de liste additionné du nombre de bulletins contenant des suffrages en faveur d'un ou de plusieurs candidats de la liste par le nombre de sièges obtenus par la liste.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-11\"><header class=\"article-header\"><h2 class=\"article-number\">Article 11</h2></header><div class=\"article-content\"><div class=\"article-text\"><ul class=\"hyphenated-items\"><li class=\"hyphenated-item\"><span class=\"item-text\">L'attribution des sièges entre organisations syndicales et la désignation des candidats élus à l'intérieur de chaque liste s'opère de la manière suivante: 1.</span></li></ul><div class=\"closing-text\"><p>Attribution de sièges entre organisations syndicales 1.1. Un siège est attribué par liste. 1.2. La dévolution des sièges supplémentaires éventuels s'établit comme suit: a) le nombre de voix obtenu par chaque organisation est divisé successivement par 2, 3, 4. On obtient ainsi des quotients électoraux qui déterminent l'attribution des sièges supplémentaires; b) en cas d'égalité du quotient électoral en a), c'est la liste qui a obtenu le plus de voix qui bénéficie du mandat supplémentaire. 2. Désignation des candidats à l'intérieur de chaque liste 2.1. Lorsque le nombre de candidats d'une liste est égal ou inférieur à celui de sièges revenant à cette liste, ces candidats sont tous élus. 2.2. Lorsque ce nombre est supérieur, les sièges sont confiés aux candidats qui atteignent le chiffre spécial d'éligibilité dans l'ordre de leur présentation. S'il reste des mandats à conférer, ils le sont aux candidats qui ont obtenu le plus grand nombre de voix. En cas de parité, l'ordre de présentation prévaut. 2.3 Préalablement à la désignation des élus, le bureau principal procède à l'attribution individuelle aux candidats des votes de liste favorables à l'ordre de présentation. 2.4. Le nombre de ces votes de liste est établi en multipliant le nombre de bulletins marqués tête de liste par le nombre de sièges obtenus par cette liste. L'attribution des votes de tête de liste se fait d'après un mode dévolutif: les votes de tête de liste sont ajoutés aux suffrages nominatifs obtenus par le premier candidat de la liste à concurrence de ce qui est nécessaire pour parfaire le chiffre d'éligibilité spécial à la liste. L'excédent, s'il y en a, est attribué dans une mesure semblable au deuxième candidat et ainsi de suite jusqu'à ce que tous les votes de listes aient été attribués. 2.5. Le chiffre d'éligibilité spécial à chaque liste s'obtient en divisant par le nombre plus un de sièges attribués à la liste l'ensemble des suffrages utiles. Lorsqu'il comprend une décimale, il est arrondi au chiffre inférieur pour une décimale de un à quatre, au chiffre supérieur pour une décimale de 5 à neuf. 2.6. L'ensemble des suffrages utiles est établi en multipliant le nombre de bulletins contenant un vote valable en tête de liste additionné du nombre de bulletins contenant des suffrages en faveur d'un ou de plusieurs candidats de la liste par le nombre de sièges obtenus par la liste.</p></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.011733"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Le procès-verbal",
                "metadata": {
                    "title_type": "Le procès-verbal",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 12",
                    "metadata": {
                        "article_range": "12",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "12",
                        "anchor_id": "art_12",
                        "content": {
                        "main_text_raw": "- A l'issue du dépouillement, le bureau de dépouillement établit un procès-verbal mentionnant le nombre de votes valables, les voix obtenues par chacun des candidats, les voix exprimées en tête de liste ainsi que la représentativité des organisations syndicales. Les témoins pourront faire des remarques éventuelles sur le procès-verbal. Le procès-verbal de dépouillement est signé et certifié par le représentant du Pouvoir Organisateur et par les membres du personnel qui ont procédé au dépouillement et, ce, sur l'honneur ainsi que par les témoins éventuels visés à l'article 10 de la présente décision. Le Pouvoir Organisateur en adresse copie par envoi recommandé aux organisations syndicales ayant déposé une liste dans les 5 jours ouvrables qui suivent la date des élections. A sa demande, le Président de la Commission paritaire peut également en obtenir copie.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-12\"><header class=\"article-header\"><h2 class=\"article-number\">Article 12</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- A l'issue du dépouillement, le bureau de dépouillement établit un procès-verbal mentionnant le nombre de votes valables, les voix obtenues par chacun des candidats, les voix exprimées en tête de liste ainsi que la représentativité des organisations syndicales. Les témoins pourront faire des remarques éventuelles sur le procès-verbal. Le procès-verbal de dépouillement est signé et certifié par le représentant du Pouvoir Organisateur et par les membres du personnel qui ont procédé au dépouillement et, ce, sur l'honneur ainsi que par les témoins éventuels visés à l'article 10 de la présente décision. Le Pouvoir Organisateur en adresse copie par envoi recommandé aux organisations syndicales ayant déposé une liste dans les 5 jours ouvrables qui suivent la date des élections. A sa demande, le Président de la Commission paritaire peut également en obtenir copie.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.011882"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 13",
                    "metadata": {
                        "article_range": "13",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "13",
                        "anchor_id": "art_13",
                        "content": {
                        "main_text_raw": "- Le Pouvoir Organisateur conserve les bulletins ainsi que l'original du procès-verbal de dépouillement jusqu'à l'expiration du délai de recours visé à l'article 14.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-13\"><header class=\"article-header\"><h2 class=\"article-number\">Article 13</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- Le Pouvoir Organisateur conserve les bulletins ainsi que l'original du procès-verbal de dépouillement jusqu'à l'expiration du délai de recours visé à l'article 14.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.011959"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                },
                {
                "type": "section",
                "label": "Recours",
                "metadata": {
                    "title_type": "Recours",
                    "title_content": "",
                    "rank": 3
                },
                "children": [
                    {
                    "type": "article",
                    "label": "Article 14",
                    "metadata": {
                        "article_range": "14",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "14",
                        "anchor_id": "art_14",
                        "content": {
                        "main_text_raw": "- En cas de contestation relative à la procédure électorale, toute partie intéressée peut saisir le bureau de conciliation institué auprès de la Commission paritaire de l'Enseignement fondamental libre confessionnel dans les 15 jours de la notification du procès-verbal. La saisine du bureau de conciliation est suspensive.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-14\"><header class=\"article-header\"><h2 class=\"article-number\">Article 14</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- En cas de contestation relative à la procédure électorale, toute partie intéressée peut saisir le bureau de conciliation institué auprès de la Commission paritaire de l'Enseignement fondamental libre confessionnel dans les 15 jours de la notification du procès-verbal. La saisine du bureau de conciliation est suspensive.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.012050"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 15",
                    "metadata": {
                        "article_range": "15",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "15",
                        "anchor_id": "art_15",
                        "content": {
                        "main_text_raw": "- Dès réception du procès-verbal de dépouillement, les organisations syndicales accusent réception et confirment le mandat attribué à leurs délégués. Lorsqu'un représentant du personnel ne peut plus exercer son mandat pour un des motifs suivants: - décès; - démission; - retrait de l'accréditation par l'organisation syndicale; - démission de l'organisation syndicale, l'organisation syndicale concernée désigne un remplaçant, le cas échéant, d'abord parmi les membres non élus de la liste qu'elle avait présentée et en informe le P.O. Dans ce cas, le membre du personnel remplaçant continue l'exercice du mandat jusqu'aux prochaines élections.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-15\"><header class=\"article-header\"><h2 class=\"article-number\">Article 15</h2></header><div class=\"article-content\"><div class=\"article-text\"><ul class=\"hyphenated-items\"><li class=\"hyphenated-item\"><span class=\"item-text\">Dès réception du procès-verbal de dépouillement, les organisations syndicales accusent réception et confirment le mandat attribué à leurs délégués.</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">démission</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">retrait de l'accréditation par l'organisation syndicale</span></li><li class=\"hyphenated-item\"><span class=\"item-text\">démission de l'organisation syndicale, l'organisation syndicale concernée désigne un remplaçant, le cas échéant, d'abord parmi les membres non élus de la liste qu'elle avait présentée et en informe le P.O.</span></li></ul><div class=\"closing-text\"><p>Dans ce cas, le membre du personnel remplaçant continue l'exercice du mandat jusqu'aux prochaines élections.</p></div></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.012204"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 16",
                    "metadata": {
                        "article_range": "16",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "16",
                        "anchor_id": "art_16",
                        "content": {
                        "main_text_raw": "- Les mandats des nouveaux élus prennent leurs effets au 1er juillet 2016. Les I.C.L. en place gardent leurs prérogatives jusqu'à cette date.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-16\"><header class=\"article-header\"><h2 class=\"article-number\">Article 16</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- Les mandats des nouveaux élus prennent leurs effets au 1er juillet 2016. Les I.C.L. en place gardent leurs prérogatives jusqu'à cette date.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.012282"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 17",
                    "metadata": {
                        "article_range": "17",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "17",
                        "anchor_id": "art_17",
                        "content": {
                        "main_text_raw": "- Les organisations syndicales procéderont à la désignation des mandataires aux OrCE dans le respect de l'article 6, § 2 de l'A.G.C.F. du 1er octobre 1998, appliquant l'article 25 du décret du 13 juillet 1998 portant organisation de l'enseignement maternel et primaire ordinaire et modifiant la réglementation de l'enseignement, pour le 1er juillet 2016.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-17\"><header class=\"article-header\"><h2 class=\"article-number\">Article 17</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- Les organisations syndicales procéderont à la désignation des mandataires aux OrCE dans le respect de l'article 6, § 2 de l'A.G.C.F. du 1er octobre 1998, appliquant l'article 25 du décret du 13 juillet 1998 portant organisation de l'enseignement maternel et primaire ordinaire et modifiant la réglementation de l'enseignement, pour le 1er juillet 2016.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.012378"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 18",
                    "metadata": {
                        "article_range": "18",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "18",
                        "anchor_id": "art_18",
                        "content": {
                        "main_text_raw": "- La présente décision prend effet le 25 novembre 2015 et prend fin le 30 juin de l'année scolaire précédant les élections sociales suivantes. Les parties s'engagent à renégocier les termes de la présente décision pour les élections sociales suivantes.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-18\"><header class=\"article-header\"><h2 class=\"article-number\">Article 18</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- La présente décision prend effet le 25 novembre 2015 et prend fin le 30 juin de l'année scolaire précédant les élections sociales suivantes. Les parties s'engagent à renégocier les termes de la présente décision pour les élections sociales suivantes.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.012466"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    },
                    {
                    "type": "article",
                    "label": "Article 19",
                    "metadata": {
                        "article_range": "19",
                        "rank": 5
                    },
                    "article_content": {
                        "article_number": "19",
                        "anchor_id": "art_19",
                        "content": {
                        "main_text_raw": "- Les parties signataires demandent au Gouvernement de la Communauté française de rendre obligatoire cette décision conformément aux dispositions du décret du 1er février 1993 fixant le statut des membres du personnel subsidié de l'Enseignement libre subventionné.",
                        "numbered_provisions": [],
                        "main_text": "<article class=\"legal-article\" id=\"art-19\"><header class=\"article-header\"><h2 class=\"article-number\">Article 19</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>- Les parties signataires demandent au Gouvernement de la Communauté française de rendre obligatoire cette décision conformément aux dispositions du décret du 1er février 1993 fixant le statut des membres du personnel subsidié de l'Enseignement libre subventionné.</p></div></div></article>",
                        "structured_content_metadata": {
                            "paragraph_count": 0,
                            "provision_count": 0,
                            "has_tables": False,
                            "generation_timestamp": "2025-08-19T14:40:42.012551"
                        }
                        }
                    },
                    "footnotes": [],
                    "footnote_references": []
                    }
                ]
                }
            ]
            },
            {
            "type": "annexe",
            "label": "ANNEXE.",
            "metadata": {
                "title_type": "ANNEXE.",
                "title_content": "",
                "rank": 1
            },
            "children": [
                {
                "type": "article",
                "label": "Article N",
                "metadata": {
                    "article_range": "N",
                    "rank": 5
                },
                "article_content": {
                    "article_number": "N",
                    "anchor_id": "art_N",
                    "content": {
                    "main_text_raw": "Instance de Concertation Locale - I.C.L. - Elections mai 2016 (Annexe non reprise pour des raisons techniques, voir M.B. du 18-04-2016, p. 26309)",
                    "numbered_provisions": [],
                    "main_text": "<article class=\"legal-article\" id=\"art-N\"><header class=\"article-header\"><h2 class=\"article-number\">Article N</h2></header><div class=\"article-content\"><div class=\"article-text\"><p>Instance de Concertation Locale - I.C.L. - Elections mai 2016 (Annexe non reprise pour des raisons techniques, voir M.B. du 18-04-2016, p. 26309)</p></div></div></article>",
                    "structured_content_metadata": {
                        "paragraph_count": 0,
                        "provision_count": 0,
                        "has_tables": False,
                        "generation_timestamp": "2025-08-19T14:40:42.012631"
                    }
                    }
                },
                "footnotes": [],
                "footnote_references": []
                }
            ]
            }
        ],
        "references": {
            "modifies": [],
            "modified_by": []
        },
        "external_links": {
            "official_links": [
            "http://www.ejustice.just.fgov.be/cgi_loi/article.pl?language=fr&sum_date=&lg_txt=f&numac_search=2016A29166"
            ],
            "parliamentary_work": [
            "http://reflex.raadvst-consetat.be/reflex/?page=chrono&c=detail_get&d=detail&docid=133161&tab=chrono&lang=fr"
            ]
        },
        "extraction_metadata": {
            "extraction_date": "2025-08-19T14:40:42.013007",
            "source_file": "2016A29166.md",
            "sections_included": [
            "document_metadata",
            "document_hierarchy",
            "references"
            ],
            "sections_excluded": [
            "articles",
            "legal_references",
            "modification_history"
            ],
            "completeness_flags": {
            "all_articles_extracted": True,
            "footnotes_linked": True,
            "hierarchical_structure_complete": True,
            "metadata_complete": True,
            "is_minimal_document": False,
            "preamble_extracted": True,
            "is_abrogated_document": False
            }
        }
    }