import pandas as pd
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import math
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import GridSearchCV
import joblib
from pathlib import Path
import os
path = Path(os.getcwd()).parent;
movie_data = pd.read_csv(str(path)+'/csv_files/red_movie_data.csv')
cols = movie_data.columns.values

#column names start-----------
one_hot = pd.get_dummies(movie_data)

#column names start-----------
one_hot_months = pd.get_dummies(movie_data["Release date"]).columns.values
one_hot_genre = pd.get_dummies(movie_data["Genere"]).columns.values
one_hot_language = pd.get_dummies(movie_data["Language"]).columns.values
one_hot_procuder = pd.get_dummies(movie_data["Produced by"]).columns.values
one_hot_writer = pd.get_dummies(movie_data["Written by"]).columns.values
one_hot_hero = pd.get_dummies(movie_data["Hero"]).columns.values
one_hot_heroine = pd.get_dummies(movie_data["Heroine"]).columns.values
one_hot_musician = pd.get_dummies(movie_data["Music by"]).columns.values
one_hot_cinematographer = pd.get_dummies(movie_data["Cinematography"]).columns.values
one_hot_editor  = pd.get_dummies(movie_data["Edited by"]).columns.values
one_hot_company  = pd.get_dummies(movie_data["company"]).columns.values

	# for x in cols:
		# y = str("one_hot_"+x+" = one_hot_"+x+".sort()")
		# print(y)
		
one_hot_Genere = one_hot_Genere.sort()
one_hot_Imdb_rating = one_hot_Imdb_rating.sort()
one_hot_User_rating = one_hot_User_rating.sort()
one_hot_Directed_by = one_hot_Directed_by.sort()
one_hot_Produced_by = one_hot_Produced_by.sort()
one_hot_Written_by = one_hot_Written_by.sort()
one_hot_Hero = one_hot_Hero.sort()
one_hot_Heroine = one_hot_Heroine.sort()
one_hot_Music_by = one_hot_Music by.sort()
one_hot_Cinematography = one_hot_Cinematography.sort()
one_hot_Edited_by = one_hot_Edited by.sort()
one_hot_company = one_hot_company.sort()
one_hot_Release_date = one_hot_Release_date.sort()
one_hot_Language = one_hot_Language.sort()

#drop Others columns 
drop_list = ["company_Others","Genere_Others","Directed by_Others","Produced by_Others","Written by_Others","Hero_Others","Heroine_Others","Music by_Others","Cinematography_Others","Edited by_Others","Language_Others"]
one_hot = one_hot.drop(drop_list,axis=1)
one_hot.columns.values[:5]

#column names end-----------

#making predictions
x = one_hot.values[:,3:]		#use these to predict
y = one_hot.values[:,1:3]		#predict these values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=0)

#Not needed in this.......
# classifier = SVR()
# parameters = {'C':[1,10,100,1000],'gamma':[1,0.1,0.01,0.001,0.0001]}
# clf = GridSearchCV(classifier,parameters,cv=20)
# clf.fit(x_train,y_train)
# print(clf.best_params_)

classifier = MultiOutputRegressor(SVR(kernel='rbf', C=100000, gamma=0.001))


#--->with normalization
# C=1000, gamma=0.0001  ==>58%
# C=10000, gamma=0.0001  ==>164%
# C=100000, gamma=0.0001  ==>361%

#---->withour normalization
# C =100000 gamma = 0.001

#data normalization
scaler = StandardScaler().fit(x)
x_trans = scaler.transform(x)

scaler = StandardScaler().fit(x_train)
x_train_trans = scaler.transform(x_train)

x_test_trans  = scaler.transform(x_test)
classifier.fit(x_train_trans,y_train)
print(classifier.score(x_test_trans,y_test))

model_name = str(path)+'/csv_files/predict_user_nulls'
joblib.dump(classifier,model_name)

y_rbf = classifier.predict(x_test_trans)

predict_imdb = joblib.load("predict_imdb")
result = predict_imdb.predict(y_rbf)
print(result)

lw = 20
plt.scatter(x_test_trans, y_test, color='darkorange', label='data')
plt.plot(x_test, y_rbf, color='navy', lw=lw)
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()




