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

#drop Others columns 
drop_list = ["company_Others","Genere_Others","Directed by_Others","Produced by_Others","Written by_Others","Hero_Others","Heroine_Others","Music by_Others","Cinematography_Others","Edited by_Others","Language_Others"]
one_hot = one_hot.drop(drop_list,axis=1)
one_hot.columns.values[:5]

#making predictions
x = one_hot.values[:,3:]		#use these to predict
y = one_hot.values[:,1]		#predict these values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=0)

#Not needed in this.......
classifier = SVR()
parameters = {'C':[100,1000,10000],'gamma':[0.001,0.0001,0.00001]}
clf = GridSearchCV(classifier,parameters,cv=20)
clf.fit(x_train,y_train)
print(clf.best_params_)


#C=10000 gamma=0.001 with others  => 1.0666
#C=10000 gamma=0.0005 with others  => 79.450
#C=10000 gamma=0.0006 with others  => 93.792

classifier = SVR(kernel='rbf',C=10000,gamma=0.0006)
classifier.fit(x_train,y_train)
classifier.score(x_test,y_test)


model_name = str(path)+'/models/predict_user_rating'
joblib.dump(classifier,model_name)

y_rbf = classifier.predict(x_test)

model_name= str(path)+'\models\predict_user_rating'
predict_user_rating = joblib.load(model_name)
result = predict_user_rating.predict(y_rbf)
print(result)

lw = 2
# plt.scatter(x_test_trans, y_test, color='darkorange', label='data')
plt.plot(x_test, y_rbf, color='navy', lw=lw)
plt.xlabel('data')
plt.ylabel('target')
plt.title('Support Vector Regression')
plt.legend()
plt.show()

