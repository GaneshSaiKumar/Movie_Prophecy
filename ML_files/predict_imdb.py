#predics imdb rating based on user rating and nulls present 

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import joblib
from pathlib import Path
import os
path = Path(os.getcwd()).parent;
movie_data = pd.read_csv(str(path)+'/csv_files/red_movie_data.csv')
ratings_nulls = movie_data[["Imdb_rating","User_rating","num_nulls"]]
x = ratings_nulls.values[:,1:]
y = ratings_nulls.values[:,0]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

scaler = StandardScaler().fit(x)
x_trans = scaler.transform(x)
scaler = StandardScaler().fit(x_train)
x_train_trans = scaler.transform(x_train)
x_test_trans  = scaler.transform(x_test)

classifier = SVR()
parameters = {'C':[1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
clf = GridSearchCV(classifier,parameters,cv=20)
clf.fit(x_train,y_train)
print(clf.best_params_)

classifier = SVR(kernel='rbf', C=1, gamma=0.1)
classifier.fit(x_train,y_train)
classifier.score(x_test,y_test)

model_name = str(path)+'/models/predict_imdb'
joblib.dump(classifier,model_name)

loaded_model = joblib.load(model_name)
result = loaded_model.score(x_test, y_test)
print(result)

predict(classifier.predict([[84,6]]))
