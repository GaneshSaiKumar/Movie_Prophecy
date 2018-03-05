import pandas as pd
from pathlib import Path
import os
path = Path(os.getcwd()).parent;
movie_data = pd.read_csv(str(path)+'\csv_files\processed_movie_release_data.csv')

unique_months = movie_data["Release date"].value_counts()

#Cleaning Genere
unique_genre = movie_data["Genere"].value_counts()
others_list = []
for k,v in unique_genre.items():
    if(v<8):
        others_list.append(k)

for i in range(len(movie_data["Genere"])):
    if movie_data["Genere"][i] in others_list:
        movie_data["Genere"][i] = "Others"

#Cleaning Language
unique_language = movie_data["Language"].value_counts()
others_list = []
for k,v in unique_language.items():
    if(v<3):
        others_list.append(k)

for i in range(len(movie_data["Language"])):
    if movie_data["Language"][i] in others_list:
        movie_data["Language"][i] = "Others"

#Cleaning Director
unique_director = movie_data["Directed by"].value_counts()
others_list = []
for k,v in unique_director.items():
    if(v<5):
        others_list.append(k)

for i in range(len(movie_data["Directed by"])):
    if movie_data["Directed by"][i] in others_list:
        movie_data["Directed by"][i] = "Others"

#Cleaning producer
unique_producer = movie_data["Produced by"].value_counts()
others_list = []
for k,v in unique_producer.items():
    if(v<3):
        others_list.append(k)

for i in range(len(movie_data["Produced by"])):
    if movie_data["Produced by"][i] in others_list:
        movie_data["Produced by"][i] = "Others"

#Cleaning writers
unique_writer = movie_data["Written by"].value_counts()
others_list = []
for k,v in unique_writer.items():
    if(v<3):
        others_list.append(k)

for i in range(len(movie_data["Written by"])):
    if movie_data["Written by"][i] in others_list:
        movie_data["Written by"][i] = "Others"

#Cleaning Heros
unique_hero = movie_data["Hero"].value_counts()
others_list = []
for k,v in unique_hero.items():
    if(v<6):
        others_list.append(k)

for i in range(len(movie_data["Hero"])):
    if movie_data["Hero"][i] in others_list:
        movie_data["Hero"][i] = "Others"

#Cleaning Heroines
unique_heroine = movie_data["Heroine"].value_counts()
others_list = []
for k,v in unique_heroine.items():
    if(v<6):
        others_list.append(k)

for i in range(len(movie_data["Heroine"])):
    if movie_data["Heroine"][i] in others_list:
        movie_data["Heroine"][i] = "Others"

#Cleaning Music
unique_musician = movie_data["Music by"].value_counts()
others_list = []
for k,v in unique_musician.items():
    if(v<6):
        others_list.append(k)

for i in range(len(movie_data["Music by"])):
    if movie_data["Music by"][i] in others_list:
        movie_data["Music by"][i] = "Others"

#Cleaning Cinematography
unique_cinematographer = movie_data["Cinematography"].value_counts()
others_list = []
for k,v in unique_cinematographer.items():
    if(v<6):
        others_list.append(k)

for i in range(len(movie_data["Cinematography"])):
    if movie_data["Cinematography"][i] in others_list:
        movie_data["Cinematography"][i] = "Others"

#Cleaning Edited
unique_editor  = movie_data["Edited by"].value_counts()
others_list = []
for k,v in unique_editor.items():
    if(v<6):
        others_list.append(k)

for i in range(len(movie_data["Edited by"])):
    if movie_data["Edited by"][i] in others_list:
        movie_data["Edited by"][i] = "Others"

#Cleaning company
unique_company  = movie_data["company"].value_counts()
others_list = []
for k,v in unique_company.items():
    if(v<5):
        others_list.append(k)

for i in range(len(movie_data["company"])):
    if movie_data["company"][i] in others_list:
        movie_data["company"][i] = "Others"


movie_data.to_csv(str(path)+'/csv_files/red_movie_data.csv',sep=',',index=False)