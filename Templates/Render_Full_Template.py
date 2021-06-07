# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
    
    # Book editions sub section data
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
    
    # Data for Summary section
    if row['librarything_characters'] != "":
        data['librarything_characters'] = row['librarything_characters']
        
    if row['librarything_book_summary'] != "":
        data['librarything_book_summary'] = row['librarything_book_summary']
        
    # Data for Infobox
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
    if 'Publication date' in row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]:
        data['published_date'] = row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]['Publication date']
    
    # Data for Introduction section
    if row['description'] != "":
        data['description'] = row['description']
        
    if row['maturity_rating'] != "":
        data['maturity_rating'] = row['maturity_rating']
    # Reamining data is already been fetched(through infobox)
    
    # Data for awards section
    if row['goodreads_awards'] != "":
        data['awards_list'] = ast.literal_eval(row['goodreads_awards'])
        
    # Data for About the author section
    if row['author1_name'] != "":
        data['author1_name'] = row['author1_name']
        
    if row['author1_nationality'] != "":
        data['author1_nationality'] = row['author1_nationality']
        
    if row['author1_education'] != "":
        data['author1_education'] = ast.literal_eval(row['author1_education'])
    
    if row['author1_stats'] != "":
        data['author1_stats'] = row['author1_stats']
      
    if row['author1_library_holdings'] != "":
        data['author1_library_holdings'] = row['author1_library_holdings']
      
    if row['author1_genre'] != "":
        data['author1_genre'] = ast.literal_eval(row['author1_genre'])
        
    if row['author1_notable_works'] != "":
        data['author1_notable_works'] = ast.literal_eval(row['author1_notable_works'])
      
    if row['author1_awards_received'] != "":
        data['author1_awards_received'] = ast.literal_eval(row['author1_awards_received'])
    
    # Data for Ratings section
    if 'Best Sellers rank' in row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]:
        data['Best_Sellers_rank'] = row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]['Best Sellers rank'].split('\n')
        
    if 'Rating' in row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]:
        data['amazon_rating'] = row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]['Rating']
    
    if 'Ratings count' in row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]:
        data['amazon_ratings_count'] = row['amazon_book_specifications'][list(row['amazon_book_specifications'].keys())[0]]['Ratings count']
    
    if row['ratings_count'] != "":
        data['ratings_count'] = row['ratings_count']
    
    if row['average_rating'] != "":
        data['average_rating'] = row['average_rating']
    
    if row['goodreads_ratings_count'] != "":
        data['goodreads_ratings_count'] = row['goodreads_ratings_count']
        
    if row['goodreads_rating'] != "":
        data['goodreads_rating'] = row['goodreads_rating']
    
    if row['librarything_reviews'] != "":
        data['librarything_reviews'] = row['librarything_reviews']
    
    if row['librarything_avg_rating'] != "":
        data['librarything_avg_rating'] = row['librarything_avg_rating']

    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Full_Template.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
