#predicts imdb based on user rating only

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import joblib
from pathlib import Path
import os
from sklearn.linear_model import BayesianRidge, LinearRegression
import matplotlib.pyplot as plt

path = Path(os.getcwd()).parent;
movie_data = pd.read_csv(str(path)+'/csv_files/red_movie_data.csv')
ratings_nulls = movie_data[["Imdb_rating","User_rating","num_nulls"]]
x = ratings_nulls.values[:,1]
x = x.reshape(-1,1)
y = ratings_nulls.values[:,0]

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)

# classifier = SVR()
# parameters = {'C':[1,10,100,1000],'gamma':[0.1,0.01,0.001]}
# clf = GridSearchCV(classifier,parameters,cv=8)
# clf.fit(x_train,y_train)
# print(clf.best_params_)


#C=100000 gamma=0.005    => 11.636%   =>13.2seconds		^reasonable
#C=1000000 gamma=0.001    => 58.334%   =>13.2seconds
#C=1000000 gamma=0.005    => 18.068%   =>13.2seconds	
#C=1000000 gamma=0.09    => 39.604%   =>13.2seconds	

classifier = SVR(kernel='rbf', C=1000000, gamma=0.005)
classifier.fit(x_train,y_train)
classifier.score(x_test,y_test)

model_name = str(path)+'/models/predict_imdb'
joblib.dump(classifier,model_name)

plt.scatter(x_train,y_train)
plt.xlabel("user_ rating")
plt.ylabel("imdb rating")

plt.scatter(x_test,classifier.predict(x_test))
plt.xlabel("$userRating_i$")
plt.ylabel("$\hat{ImdbRating}_i$")
plt.title("$userRating_i$ vs $\hat{ImdbRating}_i$")

plt.show()

model_name = str(path)+'\models\predict_imdb'
loaded_model = joblib.load(model_name)
result = loaded_model.score(x_test, y_test)
print(result)

classifier.predict([[96]])