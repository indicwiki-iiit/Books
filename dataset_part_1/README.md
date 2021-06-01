The following files contain preprocessed values of attributes collected from the "Google Books API", Author Details and others, and Ratings/Reviews/Book Awards collected from "Goodreads" and "Amazon".

Visit the SWEETVIZ_REPORT.html for insights on missing values.

Further description on the attributes is as follows :

**'isbn_13'** : ISBN 13 of the book\n
**'isbn_10'** : ISBN 10 of the book
**'book_title'** 
**'authors'**    : 'list' containing names of authors of the book
**'publisher'** 
**'published_date'**
**'page_count'** 
**'language'** 
**'maturity_rating'** : 'Mature' or 'Not Mature' Rating
**'categories'** : Genre of the Book
**'subtitle'**
**'description'**
**'small_thumbnail_link'**
**'large_thumbnail_link'**
**'preview_link'** : Link needed to preview the book on Google Books
**'self_link'** : Link pointing to itself on Google Books ( this can be used in the references section of the article )
**'univ_link'** : Link redirecting to the book's page on "openlibrary.org" to show free audio/ebook alternatives to the book
**'ebook_availability_on_google_books'**
**'epub_availability_on_google_books'**
**'pdf_availability_on_google_books'**
**'book_editions'** : 'list' of 'list's in which each list is an edition, and is of the format ['isbn','format','publisher','published_date','page_count']
**'book_series'** : 'list' containing names of books belonging to the same series
**'publisher_collection'** : 'list' containing names of books published by the same publisher. While printing, the current book has to be excluded from the list.
**'author1_name'** : Name of the **first** author, added just for better accessibility to directly print in the author's section of the article
**'author1_image'** : 'string' (or) 'list' of 'strings' in which each string can directly be used in the template to get a photo with that name from Wikimedia Commons
**'author1_nationality'** : Country the author belongs to
**'author1_education'** : Last place of study of the author
**'author1_awards_received'** : 'list' of strings in which each string is an award received by the author
**'author1_notable_works'** : 'list' of strings in which each string is a notable work of the author
**'author1_genre'** : 'list' of strings in which each string is a genre the author has worked on
**'author1_stats'** : a string of this format : 120,616 writings in 383,830 publications in 95 languages
**'author1_library_holdings'** : a string of this format : 6,127,240 library holdings
**'author1_wiki'** : **external** Wikipedia link, leading to the author's profile
**'more_by_author'** : 'list' of strings in which each string is a book written by the author
**'average_rating'** : Rating as collected from Google Books
**'ratings_count'** : Number of people who rated the book on Google Books
**'goodreads_rating'** : Rating as collected from Goodreads
**'goodreads_ratings_count'** : Number of people who rated the book on Goodreads
**'goodreads_awards'** : List of awards received by each work, created after merging awards obtained from Goodreads with those obtained from LibraryThing
