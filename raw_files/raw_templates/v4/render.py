import pandas as pd 
import numpy as np
import pickle
import ast

###################################################################
# THE FOLLOWING FUNCTIONS ARE REQUIRED FOR SOME PREPROCESSING
# BECAUSE OF THE STRING-LIST DISCREPANCY
###################################################################

def moderator(inp):
    if inp=='':
        return ''
    elif inp=='None':
        return ''
    else:
        if type(inp)==str:
            if inp[0]=='[':
                return ast.literal_eval(inp)
            else:
                return inp
        else:
            return inp


        
def pro_moderator(inp,mode='unknown'):
    if inp=='':
        return inp
    else:
        if mode=='author1_image' or mode=='author1_education':
            if inp[0]=='[':
                return ast.literal_eval(inp)[0]
            else:
                inp = '[\''+inp+'\']'
                return ast.literal_eval(inp)[0]

        else:
            if inp[0]=='[':
                return ast.literal_eval(inp)
            else:
                inp = '[\''+inp+'\']'
                return ast.literal_eval(inp)

def conversion(sample):
	res = ast.literal_eval(sample)
	return(res)

def clean1(sample):
	bad = ["'","[","]","'"]
	for i in bad:
		sample = sample.replace(i,'')	
	return(str(sample))


###################################################################
# PREPROCESSING FUNCTIONS END HERE
# THE getInfo() METHOD AND THE MAIN CODE ARE BELOW THIS LINE
###################################################################

def getInfo(row): 
    data = dict()

    # CODE TO ADD ATTRIBUTES AND THEIR VALUES FROM OTHER PARTS OF THE TEMPLATE CAN BE ADDED HERE 

    infobox_list = ['authors', 'book_title', 'subtitle', 'language', 'categories', 'publisher', 'published_date', 'page_count', 'isbn_13', 'isbn_10', 'worldcat_oclc_number']
    for i in infobox_list:
        if i == 'authors' and row[i] != "":
            data[i] = ast.literal_eval(row[i])
        elif row[i] != "":
            data[i] = row[i]    
    
    # Dimensions
    if 'Dimensions' in row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]:
        data['Dimensions'] = row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]['Dimensions']
    
    # Publication date    
    
   
    
    data['infobox_attrs'] = ['authors', 'book_title', 'subtitle', 'language', 'categories', 'publisher', 'published_date', 'page_count', 'Dimensions', 'isbn_13', 'isbn_10', 'worldcat_oclc_number']


    if row['book_editions'] != "":
        data['book_editions'] = list()
        for i in ast.literal_eval(row['book_editions']):
            data['book_editions'].append(i)
            
    # Franchise/Series sub section data
    if row['book_series'] != "":
        data['book_series'] = ast.literal_eval(row['book_series'])
    
    # Availability on sites sub section data
    data['ebook_availability_on_google_books'] = row['ebook_availability_on_google_books']
    data['epub_availability_on_google_books'] = row['epub_availability_on_google_books']
    data['pdf_availability_on_google_books'] = row['pdf_availability_on_google_books']
    data['preview_link'] = row['preview_link']
    data['formats_and_links'] = row['amazon_formats_and_links']
    data['worldcat_url'] = row['worldcat_url']
    data['univ_link'] = row['univ_link']
    data['isbn_13'] = row['isbn_13']
    
    #data['author1_notable_works'] =  conversion(row['author1_notable_works'])
    data['publisher'] =  (row['publisher'])
    data['publisher_collection'] =  conversion(row['publisher_collection'])
    
    # Common data for book editions and availability on sites subsections
    data['formats_in_telugu'] = {
        'Preloaded Digital Audio Player': 'ప్రీలోడెడ్ డిజిటల్ ఆడియో ప్లేయర్', 
        'Bonded Leather': 'బాండెడ్ లెదర్', 
        'Textbook Binding': 'టెక్స్ట్ బుక్ బైండింగ్', 
        'Library Binding': 'లైబ్రరీ బైండింగ్', 
        'Audio CD': 'ఆడియో సిడి', 
        'DVD-ROM': 'డివిడి-రామ్', 
        'Print on Demand (Paperback)': 'ప్రింట్ ఆన్ డిమాండ్ (పేపర్‌బ్యాక్)', 
        'Paperback Bunko': 'పేపర్‌బ్యాక్ బంకో', 
        'Hardcover-spiral': 'హార్డ్ కవర్- స్పైరల్ ', 
        'Hardcover': 'హార్డ్ కవర్', 
        'Digital': 'డిజిటల్', 
        'Journal': 'జర్నల్', 
        'Calendar': 'క్యాలెండర్', 
        'Stationery': 'స్టేషనరీ', 
        'Wall Chart': 'వాల్ చార్ట్', 
        'Mass Market Paperback': 'మాస్ మార్కెట్ పేపర్‌బ్యాక్',
        'Workbook': 'వర్క్‌బుక్', 
        'Kindle & comiXology': 'కిండెల్ & కామిక్సాలజీ', 
        'Imitation Leather': 'ఇమిటేషన్ లెదర్', 
        'Kindle Edition': 'కిండెల్ ఎడిషన్', 
        'Book Supplement': 'బుక్ సప్లిమెంట్', 
        'Pop-Up': 'పాప్-అప్', 
        'Leather Bound': 'లెదర్ బౌండ్', 
        'Turtleback': 'టర్టిల్ బ్యాక్', 
        'Print on Demand (Hardcover)': 'ప్రింట్ ఆన్ డిమాండ్ (హార్డ్ కవర్)', 
        'Flexibound': 'ఫ్లెక్సిబౌండ్', 
        'Sheet music': 'షీట్ మ్యూజిక్', 
        'Kindle': 'కిండెల్', 
        'Kindle Edition with Audio/Video': 'కిండెల్ ఎడిషన్ విత్ ఆడియో / వీడియో', 
        'Audible Audiobook': 'ఆడిబుల్ ఆడియోబుక్', 
        'Board book': 'బోర్డ్ బుక్', 
        'MP3 CD': 'ఎమ్‌పి 3 సిడి', 
        'Comics': 'కామిక్స్', 
        'Unbound': 'అన్‌బౌండ్', 
        'Audio CD Library Binding': 'ఆడియో సిడి లైబ్రరీ బైండింగ్', 
        'Perfect Paperback': 'పర్ఫెక్ట్ పేపర్‌బ్యాక్', 
        'Digital Audiobook': 'డిజిటల్ ఆడియోబుక్', 
        'Diary': 'డైరీ', 
        'Single Issue Magazine': 'సింగిల్ ఇష్యూ మ్యాగజైన్', 
        'Pamphlet': 'పాంప్లెట్', 
        'Spiral-bound': 'స్పైరల్-బౌండ్', 
        'Printed Access Code': 'ప్రింటెడ్ యాక్సెస్ కోడ్', 
        'Bath Book': 'బాత్ బుక్', 
        'Loose Leaf': 'లూస్ లీఫ్', 
        'School & Library Binding': 'స్కూల్ & లైబ్రరీ బైండింగ్', 
        'Rag Book': 'రాగ్ బుక్', 
        'Cards': 'కార్డులు', 
        'Paperback': 'పేపర్‌బ్యాక్', 
        'Unknown Binding': 'తెలియని బైండింగ్', 
        'MP3 CD Library Binding': 'ఎమ్‌పి 3 సిడి లైబ్రరీ బైండింగ్', 
        'Vinyl Bound': 'వినైల్ బౌండ్', 
        'Audio, Cassette': 'ఆడియో, క్యాసెట్', 
        'Pocket Book': 'పాకెట్ బుక్', 
        'Accessory with book': 'యాక్సెసరీ విత్ బుక్', 
        'Multimedia CD': 'మల్టీమీడియా సిడి', 
        'eTextbook': 'ఇటెక్స్ట్‌బుక్',
        'Audiobook': 'ఆడియోబుక్',
        '—': '—',
        'Ebook': 'ఈబుక్',
        'Trade paperback': 'ట్రేడ్ పేపర్‌బ్యాక్',
        '[': '—',
        'Library binding': 'లైబ్రరీ బైండింగ్',
        'Microform': 'మైక్రోఫార్మ్',
        'Mass market paperback': 'మాస్ మార్కెట్ పేపర్‌బ్యాక్',
    }
    data['google_books_id'] = row['google_books_id']

    moderated_attributes = [ 
    'ratings_count', 
    'average_rating', 
    'goodreads_ratings_count', 
    'goodreads_rating',
    'librarything_reviews', 
    'librarything_avg_rating',
    'author1_name',
    'author1_nationality',
    'author1_stats',
    'author1_library_holdings',
    'book_title',
    'published_date',
    'small_thumbnail_link',
    'subtitle',
    'authors',
    'publisher',
    'language',
    'categories',
    'description',
    'maturity_rating',
    'librarything_characters',
    'librarything_book_summary' 
    ]

    pro_moderated_attributes = [
        'goodreads_awards',
        'author1_education', 
        'author1_image',
        'author1_genre',
        'author1_notable_works',
        'author1_awards_received'
    ]

    for i in moderated_attributes:
        x = moderator(row[i])
        data.update({i:x})

    for i in pro_moderated_attributes:
        if i=='author1_image':
            x = pro_moderator(row[i],'author1_image')
        elif i=='author1_education':
            x = pro_moderator(row[i],'author1_education')
        else:
            x = pro_moderator(row[i])
        data.update({i:x})


    tempdic = row['amazon_book_specifications']
    if tempdic=='':
        data.update({'bestseller_rank':''})
        data.update({'amazon_ratings_count':''})
        data.update({'amazon_rating':''})

    else:
        tempdic_key = list(tempdic.keys())[0] #HardCover, Paperback, etc
        
        try:
            bestseller_rank      = tempdic[tempdic_key]['Best Sellers rank'].split(' ')[0][1:]
            data.update({'bestseller_rank':bestseller_rank})
        except:
            data.update({'bestseller_rank':''})

        try:
            amazon_ratings_count = tempdic[tempdic_key]['Ratings count'].split(' ')[0]
            data.update({'amazon_ratings_count':amazon_ratings_count})
        except:
            data.update({'amazon_ratings_count':''})

        try:
            amazon_rating        = tempdic[tempdic_key]['Rating'].split(' ')[0]
            data.update({'amazon_rating':amazon_rating})
        except:
            data.update({'amazon_rating':''})
        
    ##########################################
    # REFERENCES (Coded ref tags inside trans-render.py)
    ##########################################

    #GR - Goodreads, #LT - LibraryThing, #GG - Google, #AM - Amazon, #WC - WorldCat, #AU - Author Wikipedia Link
    if row['goodreads_link'] != "":
        GR = row['goodreads_link']
        data['GR'] = GR
    if row['librarything_url'] != "":
        LT = row['librarything_url']
        data['LT'] = LT
    if row['google_books_id'] != "":
        GG = "https://www.google.co.in/books/edition/_/{}".format(row['google_books_id'])
        data['GG'] = GG
    if row['isbn_13'] != "":
        AM = "https://www.amazon.com/s?i=stripbooks&rh=p_66%3A{}&s=relevanceexprank".format(row['isbn_13'])
        data['AM'] = AM
    if row['worldcat_url'] != "":
        WC = row['worldcat_url']
        data['WC'] = WC
    if row['author1_wiki'] != "":
        AU = row['author1_wiki']
        data['AU'] = AU

    ######################################
    # CATEGORIES
    ######################################

    cat_y  = data['published_date']
    cat_g = data['categories']

    data['CATEGORY_YEAR']  = '[[Category: ' + cat_y + ' సంవత్సరంలో ప్రచురించబడిన పుస్తకాలు'+']]'
    data['CATEGORY_GENRE'] = '[[Category: ' + cat_g + ' రచనాశైలిలో రచింపబడిన పుస్తకాలు'+']]'

    return data