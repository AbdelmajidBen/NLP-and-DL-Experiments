This repository contains code and resources related to a lab project focusing on Natural Language Processing (NLP) techniques applied to Arabic web data. Here's an overview of the key components:

Scraping: The code utilizes libraries like Scrapy and Beautiful Soup to scrape data from Arabic web sources within a specific domain. It retrieves relevant textual information for further processing.

Storage: The raw scraped data is stored in a NoSQL database, MongoDB. This ensures efficient storage and retrieval of the collected data for analysis.

NLP Pipeline: The project establishes an NLP pipeline consisting of text cleaning, tokenization, stop words removal, discretization, and normalization. These steps prepare the text data for further analysis and modeling.

Stemming and Lemmatization: Stemming and lemmatization techniques are applied to reduce words to their root forms, facilitating better text analysis and understanding.

Parts of Speech (POS) Tagging: Both rule-based and machine learning approaches are used to perform Parts of Speech tagging on the text data. This helps in identifying the grammatical structure and understanding the relationships between words.

Named Entity Recognition (NER): NER methods are employed to identify and classify entities such as names, organizations, and locations within the text. This adds another layer of semantic understanding to the analysis.
