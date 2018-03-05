import pandas as pd
import re
from string import digits
from pathlib import Path
import os
path = Path(os.getcwd()).parent;
movie_data = pd.read_csv(str(path)+'\csv_files\processed_movie_ratings_data.csv')

movie_data = movie_data.drop(["Year","Movie","Screenplay by","Running time"],axis=1)

movie_obj = movie_data.select_dtypes(['object'])
movie_data[movie_obj.columns] = movie_obj.apply(lambda x:x.str.strip())

# movie_data = movie_data[movie_data["Release date"].notnull()]
movie_data.fillna("Others",inplace=True)

rel_data = movie_data["Release date"]
 
# for i in range(len(rel_data)):
    # index = [m.start() for m in re.finditer('-',rel_data[i])]
    # if len(index) == 2:
        # rel_data[i] = rel_data[i][index[0]+1:index[1]]

for i in range(len(rel_data)):
    rel_data[i] = "".join(re.findall("[a-zA-Z]{3,9}", rel_data[i]))
    # rel_data[i] = "".join(re.findall("[a-zA-Z]+", rel_data[i]))


for i in range(len(rel_data)):
        # print(str(i)+"---"+rel_data[i])
        if(rel_data[i] == ""):
            rel_data[i] = "Others"
            print(i)
        if(rel_data[i] == "Feb"):
            rel_data[i] = "February"
            print(i)

movie_data = movie_data[movie_data["Release date"] != "Others"]
rel_data = movie_data["Release date"]
print(rel_data.value_counts())
movie_data.to_csv(str(path)+'/csv_files/processed_movie_release_data.csv',sep=',',index=False)