# Import statements
import pandas as pd
import pickle
from jinja2 import Environment, FileSystemLoader
import ast

def getData(row):
    data = dict()
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
template = env.get_template('Ratings.jinja')

p = pickle.load(open("../merged_pickle_v2.pkl", "rb"))
row = p.loc[0]
data = getData(row)
text = template.render(data)
print(text)
