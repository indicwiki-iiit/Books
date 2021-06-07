# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
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
    data['infobox_attrs'] = ['authors', 'book_title', 'subtitle', 'language', 'categories', 'publisher', 'published_date', 'page_count', 'Dimensions', 'isbn_13', 'isbn_10', 'worldcat_oclc_number']

    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Infobox.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
