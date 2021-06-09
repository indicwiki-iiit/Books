from jinja2 import Environment, FileSystemLoader
import pandas as pd 
import numpy as np
import pickle
import ast
from render import getInfo


d_author1_nationality = {
    'Australia': 'ఆస్ట్రేలియా', 'Ireland': 'ఐర్లాండ్', 'Switzerland': 'స్విట్జర్లాండ్', 'Roman Empire': 'రోమన్ ఎంపైర్', 'Belize': 'బెలిజ్', 'Belgium': 'బెల్జియం', 'Lithuania': 'లిథుయేనియా', 
    'Colombia': 'కొలంబియా', 'Uruguay': 'ఉరుగువే', 'Africa': 'ఆఫ్రికా', 'Siberia': 'సిబేరియా', 'Barbados': 'బర్బడోస్', 'Belarus': 'బెలరస్', 'Turkey': 'టర్కీ', 'Israel': 'ఇజ్రాయెల్', 
    'Italy': 'ఇటలీ', 'Malta': 'మాల్టా', 'Sri Lanka': 'శ్రీ లంక', 'South Africa': 'సౌత్ ఆఫ్రికా', 'Chile': 'చిలే', 'Czechoslovakia': 'జెకోస్లోవేకియా', 'India': 'భారతదేశం', 
    'Albania': 'అల్బేనియా', 'Lebanon': 'లెబనన్', 'Bolivia': 'బొలివియా', 'Algeria': 'అల్జీరియా', 'Romania': 'రొమేనియా', 'Guatemala': 'గువాటెమాల', 'Panama': 'పనామా', 'Canada': 'కెనడా', 
    'Dominican Republic': 'డామినికాన్ రిపబ్లిక్', 'Nepal': 'నేపాల్', 'Russia': 'రష్యా', 'Spain': 'స్పైన్', 'Argentina': 'అర్జెంటిన', 'Scotland': 'స్కోట్లండ్', 'Britain': 'బ్రిటైన్', 'Croatia': 'క్రోయేటియా', 
    'Bangladesh': 'బంగ్లాదేశ్', 'Nigeria': 'నైజీరియా', 'Greece': 'గ్రీస్', 'Egypt': 'ఈజిప్ట్', 'Trinidad and Tobago': 'ట్రినిడాడ్ అండ్ టోబాగో', 'Ghana': 'ఘన', 'Zambia': 'జాంబియా', 'Puerto Rico': 'పూర్తో రికో', 
    'Japan': 'జపాన్', 'France': 'ఫ్రాన్స్', 'Pakistan': 'పాకిస్తాన్', 'Netherlands': 'నెథర్లాండ్స్', 'Northern Ireland': 'నార్దర్న్ ఐర్లాండ్', 'Sweden': 'స్వీడన్', 'Jamaica': 'జామైక', 
    'United States of America': 'యునిటెడ్ స్టేట్స్ ఆఫ్ అమెరికా', 'Tibet': 'టిబెట్', 'Wales': 'వేల్స్', 'Norway': 'నార్వే', 'Portugal': 'పోర్టుగల్', 'Poland': 'పోలాండ్', 'Cambodia': 'కంబోడియా', 
    'Slovenia': 'స్లోవేనియా', 'China': 'చైనా', 'Luxembourg': 'లక్సెంబర్గ్', 'Iran': 'ఇరాన్', 'Iceland': 'ఐస్లాండ్', 'Yugoslavia': 'యుగోస్లవియా', 'Peru': 'పెరు', 'Palestine': 'పాలెస్టిన్', 'Cuba': 'క్యూబా', 
    'Germany': 'జర్మనీ', 'Brazil': 'బ్రెజిల్', 'Mexico': 'మెక్సికో', 'Philippines': 'ఫిలిప్పైన్స్', 'Austria': 'ఆస్ట్రియా', 'Afghanistan': 'ఆఫ్ఘనిస్తాన్', 'New Zealand': 'న్యూ జీలాండ్', 'Denmark': 'డెన్మార్క్'}

d_categories = {'History': 'చరిత్ర', 'Poetry': 'కవిత్వం', 'Health and Fitness': 'ఆరోగ్యం మరియు ఫిట్నెస్', 'Drama': 'నాటకం', 'Social Commentary': 'సామాజిక వ్యాఖ్యానం', 
    'Mythology': 'పురాణం', 'Psychology': 'సైకాలజీ', 'Fiction': 'ఫిక్షన్', 'Biography': 'జీవిత చరిత్ర', 'Literature': 'సాహిత్యం', 'Contemporary': 'సమకాలీనం', 'Crime/Thriller': 'క్రైమ్ / థ్రిల్లర్', 
    'Religion': 'ధర్మం/మతం'}

d_language = {'Latin': 'లాటిన్', 'Spanish': 'స్పానిష్', 'French': 'ఫ్రెంచ్', 'Danish': 'డానిష్', 'Russian': 'రష్యన్', 'Italian': 'ఇటాలియన్', 
    'English': 'ఆంగ్ల', 'Korean': 'కొరియన్'}

d_maturity_rating = {'Mature': 'మెచ్యూర్', 'Not Mature':'నాన్ మెచ్యూర్'}        




def getData(row):
    
    data = getInfo(row)
    
    #######################################################################################################################
    # THE FOLLOWING SECTION IS FOR TRANSLITERATING/TRANSLATING ATTRIBUTES WITH FEW DISTINCT VALUES
    # Dictionaries have been made for four attributes : 'author1_nationality', 'maturity_rating', 'categories', 'language'
    #########################################################################################################################

    data['language']            = d_language[data['language']]
    data['maturity_rating']     = d_maturity_rating[data['maturity_rating']]
    data['categories']          = d_categories[data['categories']]
    data['author1_nationality'] = d_author1_nationality[data['author1_nationality']]

    
    ###########################################################################################################
    # FROM THIS POINT, START ADDING TRANSLITERATION OR TRANSLATION FUNCTIONS
    # Example below

    # trans = DeepTranslit('telugu')

    # res = trans.transliterate(data['publisher'])[0]['pred']
    # data['publisher'] = res

    # res = trans.transliterate(data['book_title'])[0]['pred']
    # data['book_title'] = res
    ##########################################################################################################

    
    
    
    
    
    return data




file_loader = FileSystemLoader('')
env = Environment(loader= file_loader)
template = env.get_template("template.j2")

p = pickle.load(open('merged_pickle_v2.pkl','rb'))
row = p.loc[1345]
data = getData(row)
for i in data.items():
    print(i)
text = template.render(data)


f = open("output_final.txt","w",encoding="utf-8")
f.write(text)
print("Done")
