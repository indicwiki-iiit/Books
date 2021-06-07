# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

# Function that returns data dictionary
def getData(row):
    data = dict()
    if row['book_series'] != "":
        data['book_series'] = ast.literal_eval(row['book_series'])
    return data

# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Franchise_Series.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
