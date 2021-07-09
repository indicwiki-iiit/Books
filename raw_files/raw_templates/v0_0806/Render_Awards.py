# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
    if row['goodreads_awards'] != "":
        data['awards_list'] = ast.literal_eval(row['goodreads_awards'])
    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('Awards.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
