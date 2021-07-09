## Raw Code 

This folder is a collection of all Python scripts used to scrape data or obtain data from sources like APIs, preprocess data, and a lot more. Each folder contains a python notebook designated for a specific purpose, as described below - 

### 📁 [amazon_dot_com](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/amazon_dot_com)
Python script used to scrape details of the book when queried with ISBN as displayed on the Amazon page, such as dimensions, edition, year of publication, etc.

### 📁 [analysis_of_stats](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/analysis_of_stats)
Python script used to estimate the number of words corresponding to each record in each section. To see the final stats file, visit [this](https://github.com/indicwiki-iiit/Books/blob/new/data/Data%20-%20Byte%20Count%20Stats.xlsx) link.

### 📁 [attributes_preprocessing](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/attributes_preprocessing)
Python script used for attribute preprocessing, removing null values, normalizing values, eliminating foreign characters, grouping, merging, etc.

### 📁 [awards_as_category](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/awards_as_category)
Python script used to eliminate non-significant awards and words from the list of awards and designing an attribute that can be directly rendered as a category in the article.

### 📁 [final_preprocessing](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/final_preprocessing)
Python script used in the final stages of the project to perform preprocessing for one final time, involving corrections associated with list based attributes and foreign characters.

### 📁 [googlebooks_data_extraction](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/googlebooks_data_extraction)
Python script used to scrape 20-30 attributes associated with a book from [Google Books](https://www.books.google.com) such as ISBN13, ISBN10, Authors, Publisher, Published Date, Language, Categories, Book Series, Book Editions, Availability in different formats, etc. 

### 📁 [librarything_dot_com](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/librarything_dot_com)
Python script used to scrape details of the book from [LibraryThing](https://www.librarything.org), such as Book Summary, Character, Ranking, Ratings, Number of Ratings using **Selenium** and **BeautifulSoup**.

### 📁 [wikidata_authors_data](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/wikidata_authors_data)
Python script used to scrape Wikidata to obtain details of authors ( education, nationality, notable works, etc ) using both **Selenium** and the python module **wptools**.

### 📁 [wikidata_wikimedia_images](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/wikidata_wikimedia_images)
Python script used to scrape WikiData and Wikipedia Articles of the book of other languages to obtain images of the book from Wikimedia Commons, using **Selenium**.

### 📁 [worldcat_dot_org](https://github.com/indicwiki-iiit/Books/tree/new/raw_files/raw_code/worldcat_dot_org)
Python script used to scrape details of books from [WorldCat](https://www.worldcat.org) such as OCLC Number, Genres and Awards Received by the Book, Authors' Genres, Stats and Library Holdings, using **Selenium**.
