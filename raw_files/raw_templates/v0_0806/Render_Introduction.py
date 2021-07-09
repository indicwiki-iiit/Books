# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
    if row['book_title'] != "":
        data['book_title'] = row['book_title']
        
    if row['subtitle'] != "":
        data['subtitle'] = row['subtitle']
        
    if row['published_date'] != "":
        data['published_date'] = row['published_date']
        
    if row['authors'] != "":
        data['authors'] = ast.literal_eval(row['authors'])
        
    if row['publisher'] != "":
        data['publisher'] = row['publisher']
        
    if row['language'] != "":
        data['language'] = row['language']
        
    if row['categories'] != "":
        data['categories'] = row['categories']
        
    if row['description'] != "":
        data['description'] = row['description']
        
    if row['maturity_rating'] != "":
        data['maturity_rating'] = row['maturity_rating']

    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Introduction.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
