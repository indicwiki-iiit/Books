# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
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
    
    return data
    
# Main code
file_loader = FileSystemLoader('../Templates')
env = Environment(loader=file_loader)
template = env.get_template('About_the_Author.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
