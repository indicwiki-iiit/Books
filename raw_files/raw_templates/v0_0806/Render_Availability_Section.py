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
    
    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Availability_Section.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
