from jinja2 import Environment, FileSystemLoader
import pandas as pd 
import numpy as np
import pickle
import ast
from render import getInfo
from deeptranslit import DeepTranslit
translit = DeepTranslit('telugu').transliterate
from googletrans import Translator
translator = Translator(service_urls=['translate.googleapis.com'])

d_author1_nationality = {
    'Australia': 'ఆస్ట్రేలియా', 
    'Ireland': 'ఐర్లాండ్', 
    'Switzerland': 'స్విట్జర్లాండ్', 
    'Roman Empire': 'రోమన్ ఎంపైర్', 
    'Belize': 'బెలిజ్', 
    'Belgium': 'బెల్జియం', 
    'Lithuania': 'లిథుయేనియా', 
    'Colombia': 'కొలంబియా', 
    'Uruguay': 'ఉరుగువే', 
    'Africa': 'ఆఫ్రికా', 
    'Siberia': 'సిబేరియా', 
    'Barbados': 'బర్బడోస్', 
    'Belarus': 'బెలరస్', 
    'Turkey': 'టర్కీ', 
    'Israel': 'ఇజ్రాయెల్', 
    'Italy': 'ఇటలీ', 
    'Malta': 'మాల్టా', 
    'Sri Lanka': 'శ్రీ లంక', 
    'South Africa': 'సౌత్ ఆఫ్రికా', 
    'Chile': 'చిలే', 
    'Czechoslovakia': 'జెకోస్లోవేకియా', 
    'India': 'భారతదేశం', 
    'Albania': 'అల్బేనియా', 
    'Lebanon': 'లెబనన్', 
    'Bolivia': 'బొలివియా', 
    'Algeria': 'అల్జీరియా', 
    'Romania': 'రొమేనియా', 
    'Guatemala': 'గువాటెమాల', 
    'Panama': 'పనామా', 
    'Canada': 'కెనడా', 
    'Dominican Republic': 'డామినికాన్ రిపబ్లిక్', 
    'Nepal': 'నేపాల్', 
    'Russia': 'రష్యా', 
    'Spain': 'స్పైన్', 
    'Argentina': 'అర్జెంటిన', 
    'Scotland': 'స్కోట్లండ్', 
    'Britain': 'బ్రిటైన్', 
    'Croatia': 'క్రోయేటియా', 
    'Bangladesh': 'బంగ్లాదేశ్', 
    'Nigeria': 'నైజీరియా', 
    'Greece': 'గ్రీస్', 
    'Egypt': 'ఈజిప్ట్', 
    'Trinidad and Tobago': 'ట్రినిడాడ్ అండ్ టోబాగో', 
    'Ghana': 'ఘన', 
    'Zambia': 'జాంబియా', 
    'Puerto Rico': 'పూర్తో రికో', 
    'Japan': 'జపాన్', 
    'France': 'ఫ్రాన్స్', 
    'Pakistan': 'పాకిస్తాన్', 
    'Netherlands': 'నెథర్లాండ్స్', 
    'Northern Ireland': 'నార్దర్న్ ఐర్లాండ్', 
    'Sweden': 'స్వీడన్', 
    'Jamaica': 'జామైక', 
    'United States of America': 'యునిటెడ్ స్టేట్స్ ఆఫ్ అమెరికా', 
    'Tibet': 'టిబెట్', 
    'Wales': 'వేల్స్', 
    'Norway': 'నార్వే', 
    'Portugal': 'పోర్టుగల్', 
    'Poland': 'పోలాండ్', 
    'Cambodia': 'కంబోడియా', 
    'Slovenia': 'స్లోవేనియా', 
    'China': 'చైనా', 
    'Luxembourg': 'లక్సెంబర్గ్', 
    'Iran': 'ఇరాన్', 
    'Iceland': 'ఐస్లాండ్', 
    'Yugoslavia': 'యుగోస్లవియా', 
    'Peru': 'పెరు', 
    'Palestine': 'పాలెస్టిన్', 
    'Cuba': 'క్యూబా', 
    'Germany': 'జర్మనీ', 
    'Brazil': 'బ్రెజిల్', 
    'Mexico': 'మెక్సికో', 
    'Philippines': 'ఫిలిప్పైన్స్', 
    'Austria': 'ఆస్ట్రియా', 
    'Afghanistan': 'ఆఫ్ఘనిస్తాన్', 
    'New Zealand': 'న్యూ జీలాండ్', 
    'Denmark': 'డెన్మార్క్'
}

d_categories = {
    'History': 'చరిత్ర', 
    'Poetry': 'కవిత్వం', 
    'Health and Fitness': 'ఆరోగ్యం మరియు ఫిట్నెస్', 
    'Drama': 'నాటకం', 
    'Social Commentary': 'సామాజిక వ్యాఖ్యానం', 
    'Mythology': 'పురాణం', 
    'Psychology': 'సైకాలజీ', 
    'Fiction': 'ఫిక్షన్', 
    'Biography': 'జీవిత చరిత్ర', 
    'Literature': 'సాహిత్యం', 
    'Contemporary': 'సమకాలీనం', 
    'Crime/Thriller': 'క్రైమ్ / థ్రిల్లర్', 
    'Religion': 'ధర్మం/మతం'
}

d_language = {
    'Latin': 'లాటిన్', 
    'Spanish': 'స్పానిష్', 
    'French': 'ఫ్రెంచ్', 
    'Danish': 'డానిష్', 
    'Russian': 'రష్యన్', 
    'Italian': 'ఇటాలియన్', 
    'English': 'ఆంగ్ల', 
    'Korean': 'కొరియన్'
}

d_maturity_rating = {
    'Mature': 'మెచ్యూర్', 
    'Not Mature':'నాన్ మెచ్యూర్'
}  

def getData(row):
    
    data = getInfo(row)
    # print(data)
    #######################################################################################################################
    # THE FOLLOWING SECTION IS FOR TRANSLITERATING/TRANSLATING ATTRIBUTES WITH FEW DISTINCT VALUES
    # Dictionaries have been made for four attributes : 'author1_nationality', 'maturity_rating', 'categories', 'language'
    #########################################################################################################################

    ###########################################################################################################
    # FROM THIS POINT, START ADDING TRANSLITERATION OR TRANSLATION FUNCTIONS
    # Example below

    # trans = DeepTranslit('telugu')

    # res = trans.transliterate(data['publisher'])[0]['pred']
    # data['publisher'] = res

    # res = trans.transliterate(data['book_title'])[0]['pred']
    # data['book_title'] = res
    ##########################################################################################################

    telugu_data_dict = dict()
    
    """ 
        ['google_books_id', 'info_link', 'canonical_volume_link', 'etag',
       'goodreads_link', 'librarything_url', 'librarything_members',
       'librarything_avg_rating', 'librarything_reviews',
       'librarything_popularity', 'librarything_conversations',
       'librarything_mentions', 'librarything_characters',
       'librarything_book_summary', 'worldcat_url', 'worldcat_oclc_number',
       'worldcat_author_more_works', 'amazon_formats_and_links',
       'amazon_book_specifications', 'isbn_13', 'isbn_10', 'book_title',
       'authors', 'publisher', 'published_date', 'page_count', 'language',
       'maturity_rating', 'categories', 'subtitle', 'description',
       'small_thumbnail_link', 'large_thumbnail_link', 'preview_link',
       'self_link', 'univ_link', 'ebook_availability_on_google_books',
       'epub_availability_on_google_books', 'pdf_availability_on_google_books',
       'book_editions', 'book_series', 'publisher_collection', 'author1_name',
       'author1_image', 'author1_nationality', 'author1_education',
       'author1_awards_received', 'author1_notable_works', 'author1_genre',
       'author1_stats', 'author1_library_holdings', 'author1_wiki',
       'more_by_author', 'average_rating', 'ratings_count', 'goodreads_rating',
       'goodreads_ratings_count', 'goodreads_awards']

       ['authors', 'book_title', 'language', 'categories', 'publisher', 'published_date', 'page_count', 'isbn_13', 'isbn_10', 'worldcat_oclc_number', 'Dimensions', 'infobox_attrs', 'book_editions', 'book_series', 'ebook_availability_on_google_books', 'epub_availability_on_google_books', 'pdf_availability_on_google_books', 'preview_link', 'formats_and_links', 'worldcat_url', 'univ_link', 'publisher_collection', 'formats_in_telugu', 'google_books_id', 'ratings_count', 'average_rating', 'goodreads_ratings_count', 'goodreads_rating', 'librarything_reviews', 'librarything_avg_rating', 'author1_name', 'author1_nationality', 'author1_stats', 'author1_library_holdings', 'small_thumbnail_link', 'subtitle', 'description', 'maturity_rating', 'librarything_characters', 'librarything_book_summary', 'goodreads_awards', 'author1_education', 'author1_image', 'author1_genre', 'author1_notable_works', 'author1_awards_received', 'bestseller_rank', 'amazon_ratings_count', 'amazon_rating', 'REF_GR', 'REF_LT', 'REF_GG', 'REF_AM', 'REF_WC', 'REF_AU', 'CATEGORY_YEAR', 'CATEGORY_GENRE']
    """

    # authors
    if 'authors' in data and data['authors'] != "":
        telugu_data_dict['authors'] = list()
        for i in data['authors']:
            author = translit(i)[0]['pred']
            telugu_data_dict['authors'].append(author)
    else:
        telugu_data_dict['authors'] = ""
    
    # book_title
    if 'book_title' in data and data['book_title'] != "":
        book_title = translit(data['book_title'])[0]['pred']
        telugu_data_dict['book_title'] = book_title
    else:
        telugu_data_dict['book_title'] = ""
    
    # language
    if 'language' in data and data['language'] != "":
        language = d_language[data['language']]
        telugu_data_dict['language'] = language
    else:
        telugu_data_dict['language'] = ""

    # categories
    if 'categories' in data and data['categories'] != "":
        telugu_data_dict['categories'] = d_categories[data['categories']]
    else:
        telugu_data_dict['categories'] = ""
    
    # publisher
    if 'publisher' in data and data['publisher'] != "":
        publisher = translit(data['publisher'])[0]['pred']
        telugu_data_dict['publisher'] = publisher
    else:
        telugu_data_dict['publisher'] = ""

    # published_date
    if 'published_date' in data and data['published_date'] != "":
        published_date = data['published_date']
        telugu_data_dict['published_date'] = translator.translate(published_date, src="en", dest="te").text
    else:
        telugu_data_dict['published_date'] = ""

    # page_count
    if 'page_count' in data and data['page_count'] != "":
        page_count = data['page_count']
        telugu_data_dict['page_count'] = page_count
    else:
        telugu_data_dict['page_count'] = ""

    # isbn_13
    if 'isbn_13' in data and data['isbn_13'] != "":
        isbn_13 = data['isbn_13']
        telugu_data_dict['isbn_13'] = isbn_13
    else:
        telugu_data_dict['isbn_13'] = ""

    # isbn_10
    if 'isbn_10' in data and data['isbn_10'] != "":
        isbn_10 = data['isbn_10']
        telugu_data_dict['isbn_10'] = isbn_10
    else:
        telugu_data_dict['isbn_10'] = ""

    # worldcat_oclc_number
    if 'worldcat_oclc_number' in data and data['worldcat_oclc_number'] != "":
        worldcat_oclc_number = data['worldcat_oclc_number']
        telugu_data_dict['worldcat_oclc_number'] = worldcat_oclc_number
    else:
        telugu_data_dict['worldcat_oclc_number'] = ""

    # ebook_availability_on_google_books
    if 'ebook_availability_on_google_books' in data and data['ebook_availability_on_google_books'] != "":
        ebook_availability_on_google_books = data['ebook_availability_on_google_books']
        telugu_data_dict['ebook_availability_on_google_books'] = ebook_availability_on_google_books
    else:
        telugu_data_dict['ebook_availability_on_google_books'] = ""
    
    # epub_availability_on_google_books
    if 'epub_availability_on_google_books' in data and data['epub_availability_on_google_books'] != "":
        epub_availability_on_google_books = data['epub_availability_on_google_books']
        telugu_data_dict['epub_availability_on_google_books'] = epub_availability_on_google_books
    else:
        telugu_data_dict['epub_availability_on_google_books'] = ""

    # pdf_availability_on_google_books
    if 'pdf_availability_on_google_books' in data and data['pdf_availability_on_google_books'] != "":
        pdf_availability_on_google_books = data['pdf_availability_on_google_books']
        telugu_data_dict['pdf_availability_on_google_books'] = pdf_availability_on_google_books
    else:
        telugu_data_dict['pdf_availability_on_google_books'] = ""

    # preview_link
    if 'preview_link' in data and data['preview_link'] != "":
        preview_link = data['preview_link']
        telugu_data_dict['preview_link'] = preview_link
    else:
        telugu_data_dict['preview_link'] = ""

    # formats_and_links
    if 'formats_and_links' in data and data['formats_and_links'] != "":
        telugu_data_dict['formats_and_links'] = data['formats_and_links']
    else:
        telugu_data_dict['formats_and_links'] = ""
    
    # worldcat_url
    if 'worldcat_url' in data and data['worldcat_url'] != "":
        worldcat_url = data['worldcat_url']
        telugu_data_dict['worldcat_url'] = worldcat_url
    else:
        telugu_data_dict['worldcat_url'] = ""
    
    # univ_link
    if 'univ_link' in data and data['univ_link'] != "":
        univ_link = data['univ_link']
        telugu_data_dict['univ_link'] = univ_link
    else:
        telugu_data_dict['univ_link'] = ""

    # formats_in_telugu
    if 'formats_in_telugu' in data:
        telugu_data_dict['formats_in_telugu'] = data['formats_in_telugu']

    # google_books_id
    if 'google_books_id' in data and data['google_books_id'] != "":
        google_books_id = data['google_books_id']
        telugu_data_dict['google_books_id'] = google_books_id
    else:
        telugu_data_dict['google_books_id'] = ""

    # ratings_count
    if 'ratings_count' in data and data['ratings_count'] != "":
        ratings_count = str(data['ratings_count'])
        telugu_data_dict['ratings_count'] = ratings_count
    else:
        telugu_data_dict['ratings_count'] = ""

    # average_rating
    if 'average_rating' in data and data['average_rating'] != "":
        average_rating = str(data['average_rating'])
        telugu_data_dict['average_rating'] = average_rating
    else:
        telugu_data_dict['avergae_rating'] = ""

    # goodreads_ratings_count (It's datatype is of float, so we are converting it to int and then to str)
    if 'goodreads_ratings_count' in data and data['goodreads_ratings_count'] != "":
        goodreads_ratings_count = str(int(data['goodreads_ratings_count']))
        telugu_data_dict['goodreads_ratings_count'] = goodreads_ratings_count
    
    # goodreads_rating (It's datatype is of float, and then to str)
    if 'goodreads_rating' in data and data['goodreads_rating'] != "":
        goodreads_rating = str(data['goodreads_rating'])
        telugu_data_dict['goodreads_rating'] = goodreads_rating
    else:
        telugu_data_dict['goodreads_rating'] = ""
    
    # librarything_reviews (It's datatype is str, hence not converting it)
    if 'librarything_reviews' in data and data['librarything_reviews'] != "":
        librarything_reviews = data['librarything_reviews']
        telugu_data_dict['librarything_reviews'] = librarything_reviews
    else:
        telugu_data_dict['librarything_reviews'] = ""
    
    # librarything_avg_rating (It's datatype is str but there are parantheses around the value. We need to remove them)
    if 'librarything_avg_rating' in data and data['librarything_avg_rating'] != "":
        librarything_avg_rating = data['librarything_avg_rating'][1:-1]
        telugu_data_dict['librarything_avg_rating'] = librarything_avg_rating
    else:
        telugu_data_dict['librarything_avg_rating'] = ""

    # amazon_ratings_count
    if 'amazon_ratings_count' in data and data['amazon_ratings_count'] != "":
        amazon_ratings_count = data['amazon_ratings_count']
        telugu_data_dict['amazon_ratings_count'] = amazon_ratings_count
    else:
        telugu_data_dict['amazon_ratings_count'] = ""
    
    # amazon_rating
    if 'amazon_rating' in data and data['amazon_rating'] != "":
        amazon_rating = data['amazon_rating']
        telugu_data_dict['amazon_rating'] = amazon_rating
    else:
        telugu_data_dict['amazon_rating'] = ""

    # Dimensions
    if 'Dimensions' in data and data['Dimensions'] != "":
        temp = list()
        for i in data['Dimensions'].split(' x '):
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['Dimensions'] = ' x '.join(temp)
    else:
        telugu_data_dict['Dimensions'] = ""

    # book_editions
    # This is a list of lists. Each list is of below format
    # [isbn, book format, publisher, date/year, page count]
    if 'book_editions' in data and data['book_editions'] != "":
        telugu_data_dict['book_editions'] = list()
        for edition in data['book_editions']:
            temp = list()
            book_isbn = edition[0] # No transla/literation required
            temp.append(book_isbn)
            book_format = edition[1] # book_format in telugu is available inside formats_in_telugu dict
            temp.append(book_format)
            book_publisher = edition[2]
            temp.append(translit(book_publisher)[0]['pred'])
            book_published_date_or_year = edition[3]
            temp.append(book_published_date_or_year)
            book_page_count = edition[4]
            temp.append(book_page_count)
            telugu_data_dict['book_editions'].append(temp)
    else:
        telugu_data_dict['book_editions'] = ""

    # book_series
    if 'book_series' in data and data['book_series'] != "":
        temp = list()
        for i in data['book_series']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['book_series'] = temp
    else:
        telugu_data_dict['book_series'] = ""

    # publisher_collection
    if 'publisher_collection' in data and data['publisher_collection'] != "":
        temp = list()
        for i in data['publisher_collection']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['publisher_collection'] = temp
    else:
        telugu_data_dict['publisher_collection'] = ""

    # author1_name
    if 'author1_name' in data and data['author1_name'] != "":
        author1_name = data['author1_name']
        telugu_data_dict['author1_name'] = translit(author1_name)[0]['pred']
    else:
        telugu_data_dict['author1_name'] = ""
    
    # author1_nationality
    if 'author1_nationality' in data and data['author1_nationality'] != "":
        author1_nationality = data['author1_nationality']
        telugu_data_dict['author1_nationality'] = d_author1_nationality[author1_nationality]
    else:
        telugu_data_dict['author1_nationality'] = ""

    # author1_stats
    if 'author1_stats' in data and data['author1_stats'] != "":
        author1_stats = data['author1_stats']
        telugu_data_dict['author1_stats'] = translator.translate(author1_stats, src="en", dest="te").text
    else:
        telugu_data_dict['author1_stats'] = ""

    # author1_library_holdings
    if 'author1_library_holdings' in data and data['author1_library_holdings'] != "":
        author1_library_holdings = data['author1_library_holdings']
        telugu_data_dict['author1_library_holdings'] = translator.translate(author1_library_holdings, src="en", dest="te").text
    else:
        telugu_data_dict['author1_library_holdings'] = ""

    # small_thumbnail_link
    if 'small_thumbnail_link' in data and data['small_thumbnail_link'] != "":
        small_thumbnail_link = data['small_thumbnail_link']
        telugu_data_dict['small_thumbnail_link'] = small_thumbnail_link
    else:
        telugu_data_dict['small_thumbnail_link'] = ""

    # subtitle
    if 'subtitle' in data and data['subtitle'] != "":
        subtitle = data['subtitle']
        telugu_data_dict['subtitle'] = translit(subtitle)[0]['pred']
    else:
        telugu_data_dict['subtitle'] = ""

    # description
    if 'description' in data and data['description'] != "":
        telugu_data_dict['description'] = translator.translate(data['description'], src="en", dest="te").text
    else:
        telugu_data_dict['description'] = ""

    # maturity_rating
    if 'maturity_rating' in data and data['maturity_rating'] != "":
        telugu_data_dict['maturity_rating'] = d_maturity_rating[data['maturity_rating']]
    else:
        telugu_data_dict['maturity_rating'] = ""
    
    # librarything_characters
    if 'librarything_characters' in data and data['librarything_characters'] != "":
        temp = list()
        for i in data['librarything_characters']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['librarything_characters'] = temp
    else:
        telugu_data_dict['librarything_characters'] = ""
    
    # librarything_book_summary
    if 'librarything_book_summary' in data and data['librarything_book_summary'] != "":
        book_summary = data['librarything_book_summary']
        if book_summary[-4:] == 'more':
            book_summary = book_summary[:-4]
        telugu_data_dict['librarything_book_summary'] = translator.translate(book_summary, src="en", dest="te").text
    else:
        telugu_data_dict['librarything_book_summary'] = ""
    
    # goodreads_awards
    if 'goodreads_awards' in data and data['goodreads_awards'] != "":
        temp = list()
        for i in data['goodreads_awards']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['goodreads_awards'] = temp
    else:
        telugu_data_dict['goodreads_awards'] = ""

    # author1_education
    if 'author1_education' in data and data['author1_education'] != "":
        telugu_data_dict['author1_education'] = translit(data['author1_education'])[0]['pred']
    else:
        telugu_data_dict['author1_education'] = ""
    
    # author1_image
    if 'author1_image' in data and data['author1_image'] != "":
        telugu_data_dict['author1_image'] = data['author1_image']
    else:
        telugu_data_dict['author1_image'] = ""

    # author1_genre
    if 'author1_genre' in data and data['author1_genre'] != "":
        temp = list()
        for i in data['author1_genre']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['author1_genre'] = temp
    else:
        telugu_data_dict['author1_genre'] = ""

    # author1_notable_works
    if 'author1_notable_works' in data and data['author1_notable_works'] != "":
        temp = list()
        for i in data['author1_notable_works']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['author1_notable_works'] = temp
    else:
        telugu_data_dict['author1_notable_works'] = ""

    # author1_awards_received
    if 'author1_awards_received' in data and data['author1_awards_received']:
        temp = list()
        for i in data['author1_awards_received']:
            temp.append(translit(i)[0]['pred'])
        telugu_data_dict['author1_awards_received'] = temp
    else:
        telugu_data_dict['author1_awards_received'] = ""

    # bestseller_rank
    if 'bestseller_rank' in data and data['bestseller_rank'] != "":
        telugu_data_dict['bestseller_rank'] = data['bestseller_rank']
    else:
        telugu_data_dict['bestseller_rank'] != ""

    # ref tags
    if 'book_title' in data and data['book_title'] != "":
        book_title = translit(data['book_title'])[0]['pred']
        if 'GR' in data:
            GR_WIKI_LINK = "<ref name='gr-link'>{{{{cite web |url={} |title={} - గుడ్ రీడ్స్}}}}</ref>".format(data['GR'], book_title)
            telugu_data_dict['REF_GR'] = GR_WIKI_LINK
        if 'LT' in data:
            LT_WIKI_LINK = "<ref name='lt-link'>{{{{cite web |url={} |title={} - లైబ్రరీ థింగ్}}}}</ref>".format(data['LT'], book_title)
            telugu_data_dict['REF_LT'] = LT_WIKI_LINK
        if 'GG' in data:
            GG_WIKI_LINK = "<ref name='gg-link'>{{{{cite web |url={} |title={} - గూగుల్ బుక్స్}}}}</ref>".format(data['GG'], book_title)
            telugu_data_dict['REF_GG'] = GG_WIKI_LINK
        if 'AM' in data:
            AM_WIKI_LINK = "<ref name='am-link'>{{{{cite web |url={} |title={} - అమెజాన్}}}}</ref>".format(data['AM'], book_title)
            telugu_data_dict['REF_AM'] = AM_WIKI_LINK
        if 'WC' in data:
            WC_WIKI_LINK = "<ref name='wc-link'>{{{{cite web |url={} |title={} - వరల్డ్ కాట్}}}}</ref>".format(data['WC'], book_title)
            telugu_data_dict['REF_WC'] = WC_WIKI_LINK
    if 'author1_name' in data and data['author1_name'] != "":
        author1_name = translit(data['author1_name'])[0]['pred']
        if 'AU' in data:
            AU_WIKI_LINK = "<ref name='au-link'>{{{{cite web |url={} |title={} - వికీపీడియా}}}}</ref>".format(data['AU'], author1_name)
            telugu_data_dict['REF_AU'] = AU_WIKI_LINK

    # Categories at end CATEGORY_YEAR, CATEGORY_GENRE
    # CATEGORY_YEAR
    if 'CATEGORY_YEAR' in data:
        telugu_data_dict['CATEGORY_YEAR'] = data['CATEGORY_YEAR']

    # CATEGORY_GENRE
    if 'categories' in data:
        category = d_categories[data['categories']]
        telugu_data_dict['CATEGORY_GENRE'] = '[[వర్గం: ' + category + ' రచనాశైలిలో రచింపబడిన పుస్తకాలు'+']]'
    
    return telugu_data_dict

file_loader = FileSystemLoader('')
env = Environment(loader= file_loader)
template = env.get_template("template.jinja")

p = pickle.load(open('merged_pickle_v3.pkl','rb'))
row = p.loc[0]
data = getData(row)
text = template.render(data)

f = open("output_final.txt","w",encoding="utf-8")
f.write(text)
print("Done")
