import pandas as pd
import sys
from collections import Counter
from pathlib import Path
import os
path = Path(os.getcwd()).parent;
movie_data = pd.read_csv(str(path)+'\csv_files\21century_data.csv')
# movie_data = pd.read_csv(sys.argv[1])
print(movie_data.isnull().sum())
# removing unnecessary rows from data1
num_nulls_row = movie_data.isnull().sum(axis=1).tolist()
movie_data["num_nulls"] = movie_data.isnull().sum(axis=1).tolist()
freq_count = Counter(num_nulls_row)
myset = set(freq_count)
myset_list = list(myset)

print("total rows = "+str(len(num_nulls_row))+"\n"+"null_count of rach row :\n"+str(freq_count))
max_nulls = int(input("Enter maximum nulls allowed in each row is :- ")) + 1
for i in range(len(myset_list)):
    if myset_list[i] >= max_nulls:
        break

sel_null_count = myset_list[max_nulls:len(myset_list)]

columns = movie_data.columns.values
refine_movie_data = pd.DataFrame(columns=columns)

i=0
for index,row in movie_data.iterrows():
    if( row["num_nulls"] not in sel_null_count ):
        refine_movie_data[i] = row
        i+=1

refine_movie_data.reset_index()
refine_movie_data = refine_movie_data.T
refine_movie_data = refine_movie_data[19:]

#filling missing user ratings
ratings = refine_movie_data[["Imdb_rating","User_rating"]]
null_count = ratings["Imdb_rating"].isnull().sum()
ratings["Imdb_rating"].fillna('0',inplace=True)
imdb = ratings["Imdb_rating"]
print(imdb[22:25])

a = []
print("************Phase 0************")
for x in imdb:
    if x.find('/') != -1:
        x = x.replace('/','.')
    if x.find('%') != -1:
        x = x.replace('%','.')
        x=float(x)/10
    a.append(round(float(x),1))

print("************Phase 1************")
for i in range(len(imdb)):
    imdb[i] = a[i]

imdb_mean = imdb.sum()/(len(imdb)-null_count)
ratings = refine_movie_data[["Imdb_rating","User_rating"]]
ratings["Imdb_rating"].fillna(str(imdb_mean),inplace=True)
imdb = ratings["Imdb_rating"]
a = []
for x in imdb:
    if x.find('/') != -1:
        x = x.replace('/','.')
    if x.find('%') != -1:
        x = x.replace('%','.')
        x=float(x)/10
    a.append(round(float(x),1))

for i in range(len(imdb)):
    imdb[i] = a[i]

ratings["Imdb_rating"] = imdb

user = ratings["User_rating"]
null_count = user.isnull().sum()
user.fillna("000",inplace=True)

for i in range(len(user)):
    user[i] = float(user[i][:2])

user_mean = user.sum()/(len(user)-null_count)

for i in range(len(user)):
    if user[i] == float(0) :
        user[i] = round(user_mean)

refine_movie_data[["Imdb_rating","User_rating"]] = ratings

refine_movie_data.to_csv(str(path)+'/csv_files/processed_movie_ratings_data.csv',sep=',',index=False)