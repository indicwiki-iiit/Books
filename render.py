import pandas as pd 
import numpy as np
import pickle
from ast import literal_eval
from jinja2 import Environment, FileSystemLoader
from genXML import addPage, tewiki

def getData(data):
    """
    This function takes a row from the csv file as an argument which is stored inside 'data' variable
    Finally return a dictionary which contains all the data required for the Jinja template to render
    """
    template_data = dict()
    if(not pd.isnull(data['WIKIPEDIA_TITLE_TELUGU'])):
        temp = data['WIKIPEDIA_TITLE_TELUGU']
        temp = temp.replace("'స్", "స్")
        temp = temp.replace("&", "&amp;")
        temp = temp.replace("<", "&lt;")
        temp = temp.replace(">", "&gt;")
        temp = temp.replace("'", "&apos;")
        temp = temp.replace('"', "&quot;")
        template_data['WIKIPEDIA_TITLE'] = temp

    else:
        template_data['WIKIPEDIA_TITLE_TELUGU'] = ""

    if(not pd.isnull(data['BOOK_TITLE_TELUGU'])):
        template_data['BOOK_TITLE'] = data['BOOK_TITLE_TELUGU']
        template_data['BOOK_TITLE_ENGLISH'] = data['BOOK_TITLE_ENGLISH']
    else:
        template_data['BOOK_TITLE'] = ""
        template_data['BOOK_TITLE_ENGLISH'] = ""

    if(not pd.isnull(data['SUBTITLE_TELUGU'])):
        template_data['SUBTITLE'] = data['SUBTITLE_TELUGU']
    else:
        template_data['SUBTITLE'] = ""

    if(not pd.isnull(data['LANGUAGE_TELUGU'])):
        template_data['LANGUAGE'] = data['LANGUAGE_TELUGU']
    else:
        template_data['LANGUAGE'] = ""
    
    if(not pd.isnull(data['AUTHORS_TELUGU'])):
        template_data['AUTHORS'] = literal_eval(data['AUTHORS_TELUGU'])
        template_data['AUTHORS_ENGLISH'] = literal_eval(data['AUTHORS_ENGLISH'])
        temp = list()
        for i, j in zip(template_data['AUTHORS'], template_data['AUTHORS_ENGLISH']):
            temp.append("{} ({})".format(i, j))
        template_data['AUTHORS_INTRO'] = temp
    else:
        template_data['AUTHORS'] = ""
        template_data['AUTHORS_ENGLISH'] = ""

    if(not pd.isnull(data['PUBLISHED_YEAR'])):
        template_data['PUBLISHED_YEAR'] = data['PUBLISHED_YEAR']
    else:
        template_data['PUBLISHED_YEAR'] = ''

    if(not pd.isnull(data['GENRE_TELUGU'])):
        template_data['GENRE'] = data['GENRE_TELUGU']
    else:
        template_data['GENRE'] = ''

    if(not pd.isnull(data['PAGE_COUNT'])):
        template_data['PAGE_COUNT'] = data['PAGE_COUNT']
    else:
        template_data['PAGE_COUNT'] = ""

    if(not pd.isnull(data['ISBN13'])):
        template_data['ISBN13'] = str((data['ISBN13']))
    else:
        template_data['ISBN13'] = ""

    if(not pd.isnull(data['ISBN10'])):
        template_data['ISBN10'] = str((data['ISBN10']))
    else:
        template_data['ISBN10'] = ""

    if(not pd.isnull(data['OCLC'])):
        template_data['OCLC'] = str((data['OCLC'])).replace(".0", "")
    else:
        template_data['OCLC'] = ""

    if(not pd.isnull(data['BOOK_IMAGE'])):
        template_data['BOOK_IMAGE'] = data['BOOK_IMAGE']
    else:
        template_data['BOOK_IMAGE'] = ""

    if(not pd.isnull(data['AUTHOR_NAME_TELUGU'])):
        template_data['AUTHOR_NAME'] = data['AUTHOR_NAME_TELUGU']
        template_data['AUTHOR_NAME_ENGLISH'] = data['AUTHOR_NAME_ENGLISH']
    else:
        template_data['AUTHOR_NAME'] = ""
        template_data['AUTHOR_NAME_ENGLISH'] = ""

    if(not pd.isnull(data['AUTHOR_NATIONALITY_TELUGU'])):
        template_data['AUTHOR_NATIONALITY'] = data['AUTHOR_NATIONALITY_TELUGU']
    else:
        template_data['AUTHOR_NATIONALITY'] = ""
    
    if(not pd.isnull(data['AUTHOR_EDUCATION_TELUGU'])):
        template_data['AUTHOR_EDUCATION'] = data['AUTHOR_EDUCATION_TELUGU']
    else:
        template_data['AUTHOR_EDUCATION'] = ""

    if(not pd.isnull(data['AUTHOR_STATS_TELUGU'])):
        template_data['AUTHOR_STATS'] = data['AUTHOR_STATS_TELUGU']
    else:
        template_data['AUTHOR_STATS'] = ""

    if(not pd.isnull(data['AUTHOR_LIBRARY_HOLDINGS'])):
        template_data['AUTHOR_LIBRARY_HOLDINGS'] = data['AUTHOR_LIBRARY_HOLDINGS']
    else:
        template_data['AUTHOR_LIBRARY_HOLDINGS'] = ""

    if(not pd.isnull(data['AUTHOR_GENRE_TELUGU'])):
        template_data['AUTHOR_GENRE'] = literal_eval(data['AUTHOR_GENRE_TELUGU'])
    else:
        template_data['AUTHOR_GENRE'] = ""

    if(not pd.isnull(data['AUTHOR_NOTABLE_WORKS_TELUGU'])):
        template_data['AUTHOR_NOTABLE_WORKS'] = list(set(literal_eval(data['AUTHOR_NOTABLE_WORKS_TELUGU'])))
    else:
        template_data['AUTHOR_NOTABLE_WORKS'] = ""

    if(not pd.isnull(data['AUTHOR_OTHER_WORKS_TELUGU'])):
        template_data['AUTHOR_OTHER_WORKS'] = list(set(literal_eval(data['AUTHOR_OTHER_WORKS_TELUGU'])))
    else:
        template_data['AUTHOR_OTHER_WORKS'] = ""

    if(not pd.isnull(data['AUTHOR_AWARDS_TELUGU'])):
        template_data['AUTHOR_AWARDS'] = list(set(literal_eval(data['AUTHOR_AWARDS_TELUGU'])))
    else:
        template_data['AUTHOR_AWARDS'] = ""    
    
    if(not pd.isnull(data['PUBLISHER_TELUGU'])):
        template_data['PUBLISHER'] = data['PUBLISHER_TELUGU']
        template_data['PUBLISHER_ENGLISH'] = data['PUBLISHER_ENGLISH']
    else:
        template_data['PUBLISHER'] = ""
        template_data['PUBLISHER_ENGLISH'] = ""

    if(not pd.isnull(data['CHARACTERS_TELUGU'])):
        template_data['CHARACTERS'] = list(set(literal_eval(data['CHARACTERS_TELUGU'])))
    else:
        template_data['CHARACTERS'] = ""

    if(not pd.isnull(data['BOOK_SUMMARY_TELUGU'])):
        template_data['BOOK_SUMMARY'] = data['BOOK_SUMMARY_TELUGU']
    else:
        template_data['BOOK_SUMMARY'] = ""

    if(not pd.isnull(data['AUTHOR_IMAGE'])):
        try:
            template_data['AUTHOR_IMAGE'] = literal_eval(data['AUTHOR_IMAGE'])[0]
        except:
            template_data['AUTHOR_IMAGE'] = data['AUTHOR_IMAGE']
    else:
        template_data['AUTHOR_IMAGE'] = ""

    if(not pd.isnull(data['BOOK_SERIES_TELUGU'])):
        template_data['BOOK_SERIES'] = list(set(literal_eval(data['BOOK_SERIES_TELUGU'])))
    else:
        template_data['BOOK_SERIES'] = ""

    if(not pd.isnull(data['BOOK_EDITIONS_TELUGU'])):
        template_data['BOOK_EDITIONS'] = literal_eval(data['BOOK_EDITIONS_TELUGU'])
    else:
        template_data['BOOK_EDITIONS'] = ""

    if(not pd.isnull(data['EBOOK_AVAILABILITY_ON_GOOGLE_BOOKS'])):
        template_data['EBOOK_AVAILABILITY_ON_GOOGLE_BOOKS'] = data['EBOOK_AVAILABILITY_ON_GOOGLE_BOOKS']
    else:
        template_data['EBOOK_AVAILABILITY_ON_GOOGLE_BOOKS'] = ""

    if(not pd.isnull(data['EPUB_AVAILABILITY_ON_GOOGLE_BOOKS'])):
        template_data['EPUB_AVAILABILITY_ON_GOOGLE_BOOKS'] = data['EPUB_AVAILABILITY_ON_GOOGLE_BOOKS']
    else:
        template_data['EPUB_AVAILABILITY_ON_GOOGLE_BOOKS'] = ""

    if(not pd.isnull(data['PDF_AVAILABILITY_ON_GOOGLE_BOOKS'])):
        template_data['PDF_AVAILABILITY_ON_GOOGLE_BOOKS'] = data['PDF_AVAILABILITY_ON_GOOGLE_BOOKS']
    else:
        template_data['PDF_AVAILABILITY_ON_GOOGLE_BOOKS'] = ""

    if(not pd.isnull(data['FORMATS_AND_LINKS_TELUGU'])):
        template_data['FORMATS_AND_LINKS'] = literal_eval(data['FORMATS_AND_LINKS_TELUGU'])
    else:
        template_data['FORMATS_AND_LINKS'] = ""

    if(not pd.isnull(data['PUBLISHER_COLLECTION_TELUGU'])):
        template_data['PUBLISHER_COLLECTION'] = list(set(literal_eval(data['PUBLISHER_COLLECTION_TELUGU'])))
    else:
        template_data['PUBLISHER_COLLECTION'] = ""
        
    if(not pd.isnull(data['PREVIEW_LINK'])):
        template_data['PREVIEW_LINK'] = data['PREVIEW_LINK']
    else:
        template_data['PREVIEW_LINK'] = ""

    if(not pd.isnull(data['UNIV_LINK'])):
        template_data['UNIV_LINK'] = data['UNIV_LINK']
    else:
        template_data['UNIV_LINK'] = ""

    if(not pd.isnull(data['BOOK_AWARDS_TELUGU'])):
        temp = list()
        template_data['BOOK_AWARDS'] = literal_eval(data['BOOK_AWARDS_TELUGU'])
        for i, j in zip(literal_eval(data['BOOK_AWARDS_TELUGU']), literal_eval(data['BOOK_AWARDS_ENGLISH'])):
            temp.append("{} ({})".format(i, j))
        template_data['BOOKS_AWARDS_SECTION'] = temp
    else:
        template_data['BOOK_AWARDS'] = ""
        template_data['BOOKS_AWARDS_SECTION'] = ""

    if((not pd.isnull(data['AMAZON_RATING'])) and (not pd.isnull(data['AMAZON_RATINGS_COUNT']))):
        template_data['AMAZON_RATING'] = data['AMAZON_RATING']
        template_data['AMAZON_RATINGS_COUNT'] = str(data['AMAZON_RATINGS_COUNT'])
    else:
        template_data['AMAZON_RATING'] = ""
        template_data['AMAZON_RATINGS_COUNT'] = ""

    if((not pd.isnull(data['GOODREADS_RATING'])) and (not pd.isnull(data['GOODREADS_RATINGS_COUNT']))):
        template_data['GOODREADS_RATING'] = data['GOODREADS_RATING']
        template_data['GOODREADS_RATINGS_COUNT'] = str(int(data['GOODREADS_RATINGS_COUNT']))
    else:
        template_data['GOODREADS_RATING'] = ""
        template_data['GOODREADS_RATINGS_COUNT'] = ""

    if((not pd.isnull(data['GOOGLE_BOOKS_RATING'])) and (not pd.isnull(data['GOOGLE_BOOKS_RATINGS_COUNT']))):
        template_data['GOOGLE_BOOKS_RATING'] = data['GOOGLE_BOOKS_RATING']
        template_data['GOOGLE_BOOKS_RATINGS_COUNT'] = str(data['GOOGLE_BOOKS_RATINGS_COUNT'])
    else:
        template_data['GOOGLE_BOOKS_RATING'] = ""
        template_data['GOOGLE_BOOKS_RATINGS_COUNT'] = ""

    if((not pd.isnull(data['LIBRARYTHING_RATING'])) and (not pd.isnull(data['LIBRARYTHING_REVIEWS_COUNT']))):
        template_data['LIBRARYTHING_RATING'] = data['LIBRARYTHING_RATING']
        template_data['LIBRARYTHING_REVIEWS_COUNT'] = str(int(data['LIBRARYTHING_REVIEWS_COUNT']))
    else:
        template_data['LIBRARYTHING_RATING'] = ""
        template_data['LIBRARYTHING_REVIEWS_COUNT'] = ""

    if(not pd.isnull(data['WORLDCAT_URL'])):
        template_data['WORLDCAT_URL'] = data['WORLDCAT_URL']
    else:
        template_data['WORLDCAT_URL'] = ""

    REF_GOOGLE_BOOKS = ""
    if(not pd.isnull(data['GOOGLE_BOOKS_URL'])):
        REF_GOOGLE_BOOKS = "<ref name='googlebooks'>{{{{cite web |url={} |title={} - గూగుల్ బుక్స్}}}}</ref>".format(data['GOOGLE_BOOKS_URL'], template_data['BOOK_TITLE'])
    template_data['REF_GOOGLE_BOOKS'] = REF_GOOGLE_BOOKS

    REF_WORLDCAT = ""
    if(not pd.isnull(data['WORLDCAT_URL'])):
        REF_WORLDCAT = "<ref name='worldcat'>{{{{cite web |url={} |title={} - వరల్డ్ కాట్}}}}</ref>".format(data['WORLDCAT_URL'], template_data['BOOK_TITLE'])
    template_data['REF_WORLDCAT'] = REF_WORLDCAT

    REF_LIBRARYTHING = ""
    if(not pd.isnull(data['LIBRARYTHING_URL'])):
        REF_LIBRARYTHING = "<ref name='librarything'>{{{{cite web |url={} |title={} - లైబ్రరీ థింగ్}}}}</ref>".format(data['LIBRARYTHING_URL'], template_data['BOOK_TITLE'])
    template_data['REF_LIBRARYTHING'] = REF_LIBRARYTHING

    REF_GOODREADS = ""
    if(not pd.isnull(data['GOODREADS_URL'])):
        REF_GOODREADS = "<ref name='goodreads'>{{{{cite web |url={} |title={} - గుడ్ రీడ్స్}}}}</ref>".format(data['GOODREADS_URL'], template_data['BOOK_TITLE'])
    template_data['REF_GOODREADS'] = REF_GOODREADS

    REF_AMAZON = ""
    if(not pd.isnull(data['AMAZON_URL'])):
        REF_AMAZON = "<ref name='amazon'>{{{{cite web |url={} |title={} - అమెజాన్}}}}</ref>".format(data['AMAZON_URL'], template_data['BOOK_TITLE'])
    template_data['REF_AMAZON'] = REF_AMAZON

    REF_AUTHOR_WIKI = ""
    if(not pd.isnull(data['AUTHOR_WIKI'])):
        REF_AUTHOR_WIKI = "<ref name='authorwiki'>{{{{cite web |url={} |title={} - వికీపీడియా}}}}</ref>".format(data['AMAZON_URL'], template_data['AUTHOR_NAME'])
    template_data['REF_AUTHOR_WIKI'] = REF_AUTHOR_WIKI

    CATEGORIES = list()
    if(not pd.isnull(data['LANGUAGE_TELUGU'])):
        CATEGORIES.append('[[Category:{} పుస్తకాలు]]'.format(data['LANGUAGE_TELUGU']))
    
    if(not pd.isnull(data['PUBLISHED_YEAR'])):
        CATEGORIES.append('[[Category:{} పుస్తకాలు]]'.format(data['PUBLISHED_YEAR']))

    if(not pd.isnull(data['GENRE_TELUGU'])):
        CATEGORIES.append('[[Category:{} పుస్తకాలు]]'.format(data['GENRE_TELUGU']))

    if(not pd.isnull(data['AUTHOR_NAME_TELUGU'])):
        CATEGORIES.append("[[Category:{} రచనలు]]".format(data['AUTHOR_NAME_TELUGU']))

    if(not pd.isnull(data['PUBLISHER_TELUGU'])):
        CATEGORIES.append("[[Category:{} ప్రచురించిన పుస్తకాలు]]".format(data['PUBLISHER_TELUGU']))

    if(not pd.isnull(data['AWARDS_AS_CATEGORY'])):
        temp = literal_eval(data['AWARDS_AS_CATEGORY'])
        for i in temp:
            CATEGORIES.append("[[Category:{} పొందిన పుస్తకాలు]]".format(i))

    CATEGORIES.append("[[Category:తెవికీ పుస్తకాలు]]")

    if CATEGORIES == list():
        template_data['CATEGORIES'] = ''
    else:
        template_data['CATEGORIES'] = CATEGORIES

    return template_data

def generate_xml(d):
    """
    This is the function that generates the final XML file for all the records in the CSV file with the help of addPage() function in the genXML.py file
    """

    # The username, user_id are unique for a tewiki account. These values can be found by exporting a sample article from tewiki special pages --> export pages
    username = "Booksindicwiki"
    user_id = "18103"
    page_id = 5000001
    # page_id must be unique for every page element in the xml file. Hence we kept on incrementing the page_id in the below for loop

    xml = tewiki
    for i in range(len(d)):

        # The articles corresponding to the index values in the below set are not included in the xml because the data is incorrect for these rows
        if i in (1090, 1974, 2529, 3077, 3147, 4298, 4368, 4966, 5321, 5436):
            continue
        data = getData(d.loc[i])
        wikitext = template.render(data)

        # Special case
        wikitext = wikitext.replace("'స్", "స్")

        # XML 5 pre-defined entity references
        wikitext = wikitext.replace("&", "&amp;")
        wikitext = wikitext.replace("<", "&lt;")
        wikitext = wikitext.replace(">", "&gt;")
        wikitext = wikitext.replace("'", "&apos;")
        wikitext = wikitext.replace('"', "&quot;")

        # Send the wikitext and other required parameters to the addPage() function
        page = addPage(data['WIKIPEDIA_TITLE'], page_id, username, user_id, wikitext)
        xml = xml + page
        page_id += 1

    # Append the closing tag </mediawiki>
    xml = xml + '</mediawiki>'

    # Saving xml text to a file called 'AUTOXML.xml'
    f = open("AUTOXML.xml", "w")
    f.write(xml)
    f.close()

if __name__ == "__main__":

    # Below three statements are for loading the jinja template
    file_loader = FileSystemLoader('template/')
    env = Environment(loader=file_loader)
    template = env.get_template("template.j2")

    # Read csv file
    d = pd.read_csv("data/FINAL-KB.csv")

    # Generating an article for a row from the FINAL-KB.csv
    data = getData(d.loc[0]) # 0 is the row index here
    wikitext = template.render(data)
    # Writing the wikipedia article source code to a file called "ARTICLE.txt"
    f = open("ARTICLE.txt", "w")
    f.write(wikitext)
    f.close()

    # Finally generate XML for all records
    generate_xml(d)