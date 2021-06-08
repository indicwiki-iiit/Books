# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
    if row['librarything_characters'] != "":
        data['librarything_characters'] = row['librarything_characters']
        
    if row['librarything_book_summary'] != "":
        data['librarything_book_summary'] = row['librarything_book_summary']

    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Summary.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
