What's new - 

1. Category names of genre and year have been edited as per the existing categories in te.wikipedia.org. Category names have been added for 'language' and 'award' attributes. Significant awards have been transliterated and hard coded into a list of tuples listed in the raw directory. On the basis of these tuples, a new attribute "awards_as_category" has been added to the existing pickle file to make "merged_pickle_v3.pkl". While rendering, instead of transliterating awards from the 'goodreads_awards' attribute and then putting them into a category, we can directly access data from the "awards_as_category" attribute from this pickle file and print the list ( note : this is an actual list, unlike the other attributes which were lists enclosed in strings and needed ast.literal_eval() )

2. Many edge cases went missing in the previous editions of the template's "render.py" file, so changes have been made accordingly, to attributes such as amazon_book_specifications. There were other edge cases like not including the book title of the current book in the attributes "author1_notable_works", "publisher_collection" and changes have been made accordingly.

3. Some grammatical corrections, and modifications to some lines in the template have been made, as suggested in the review meet on 11/06.
