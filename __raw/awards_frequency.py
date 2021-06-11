###########################################################
# For the output, please visit awards_frequency.txt
###########################################################
import pickle 
import pandas as pd
import ast 

d = {}
df = pickle.load(open('merged_pickle_v32.pkl','rb'))
for i in range(0,6500):
    if df.iloc[i]['goodreads_awards']!='':
        x = ast.literal_eval(df.iloc[i]['goodreads_awards'])
        for i in x:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

l = list(d.items())
l = sorted(l,key = lambda x: x[1],reverse=True)
d = {}
for i in l:
    d[i[0]] = i[1]

for i in d.items():
    print(i)
