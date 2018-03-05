#!/usr/bin/env python
from flask import Flask, flash, redirect, render_template,request,url_for
import pandas as pd
import sys
import joblib
from sklearn.multioutput import MultiOutputRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVR
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from sklearn.model_selection import GridSearchCV
from pathlib import Path
import os
path = Path(os.getcwd())
movie_data = pd.read_csv(str(path)+'/csv_files/red_movie_data.csv')

one_hot = pd.get_dummies(movie_data)
columns = one_hot.columns.values
new_df = pd.DataFrame(columns=columns)
drop_list = ["Imdb_rating","User_rating","num_nulls","company_Others","Genere_Others","Directed by_Others","Produced by_Others","Written by_Others","Hero_Others","Heroine_Others","Music by_Others","Cinematography_Others","Edited by_Others","Language_Others"]
new_df = new_df.drop(drop_list,axis=1)
columns = new_df.columns.values
new_df.loc[0]=[0 for n in range(len(columns))]


#Generes
genere_list = pd.unique(movie_data["Genere"])
genere = []
for i in range(len(genere_list)):
    temp = {"genere":genere_list[i]}
    genere.append(temp)

print("genere = ")
print(len(genere))

#Directors
directors_list = pd.unique(movie_data["Directed by"])
directors = []
for i in range(len(directors_list)):
    temp = {"directors_list":directors_list[i]}
    directors.append(temp)

print("Directors : ")
print(len(directors))

#Producers
producers_list = pd.unique(movie_data["Produced by"])
producers = []
for i in range(len(producers_list)):
    temp = {"producers_list":producers_list[i]}
    producers.append(temp)

print("producers = ")
print(len(producers))

#writers
writers_list = pd.unique(movie_data["Written by"])
writers = []
for i in range(len(writers_list)):
    temp = {"writers_list":writers_list[i]}
    writers.append(temp)

print("writers : ")
print(len(writers))

#Hero
hero_list = pd.unique(movie_data["Hero"])
Hero = []
for i in range(len(hero_list)):
    temp = {"hero_list":hero_list[i]}
    Hero.append(temp)

print("Hero : ")
print(len(Hero))

#Heroine
heroine_list = pd.unique(movie_data["Heroine"])
Heroine = []
for i in range(len(heroine_list)):
    temp = {"heroine_list":heroine_list[i]}
    Heroine.append(temp)

print("Heroine : ")
print(len(Heroine))

#Music
music_list = pd.unique(movie_data["Music by"])
Music = []
for i in range(len(music_list)):
    temp = {"music_list":music_list[i]}
    Music.append(temp)

print("Music : ")
print(len(Music))

#Cinematography
Cinematography_list = pd.unique(movie_data["Cinematography"])
Cinematography = []
for i in range(len(Cinematography_list)):
    temp = {"Cinematography_list":Cinematography_list[i]}
    Cinematography.append(temp)

print("Cinematography : ")
print(len(Cinematography))

#Edited
Edited_list = pd.unique(movie_data["Edited by"])
Edited = []
for i in range(len(Edited_list)):
    temp = {"Edited_list":Edited_list[i]}
    Edited.append(temp)

print("Edited : ")
print(len(Edited))

#company
company_list = pd.unique(movie_data["company"])
company = []
for i in range(len(company_list)):
    temp = {"company_list":company_list[i]}
    company.append(temp)

print("company : ")
print(len(company))

#Language
Language_list = pd.unique(movie_data["Language"])
Language = []
for i in range(len(Language_list)):
    temp = {"Language_list":Language_list[i]}
    Language.append(temp)

print("Language : ")
print(len(Language))

#Release Months
rel_months = pd.unique(movie_data["Release date"])
months = []
for i in range(len(rel_months)):
    temp = {"rel_months":rel_months[i]}
    months.append(temp)

print("months: - ")
print(len(months))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'movie_prophecy.html'
	)
        #data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}]
		# data = [genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,company,months,Language]
		# )

@app.route("/latest")
def latest():
    return render_template(
        'latest_happenings.html',
        #data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}]
		data = [genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,company,months,Language])

@app.route("/contact")
def contact():
    return render_template(
        'contact.html',
        #data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}]
		data = [genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,company,months,Language])

@app.route("/services")
def services():
    return render_template(
        'services.html',
        #data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}]
		data = [genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,company,months,Language])

@app.route("/predict")
def predict():
    return render_template(
        'predict.html',
        #data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}]
		data = [genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,company,months,Language])


@app.route("/result" , methods=['GET', 'POST'])
def result():
#[genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,
#company,months,Language])
	genere_select = request.form.get('genere_select')
	directors_select = request.form.get('directors_select')
	producers_select = request.form.get('produders_select')
	writers_select = request.form.get('writers_select')
	Hero_select = request.form.get('Hero_select')
	Heroine_select = request.form.get('Heroine_select')
	Music_select = request.form.get('Music_select')
	Cinematography_select = request.form.get('Cinematography_select')
	Edited_select = request.form.get('Edited_select')
	company_select = request.form.get('company_select')
	Language_select = request.form.get('Language_select')
	month_select = request.form.get('month_select')
	
	selections = [genere_select,directors_select,producers_select,writers_select,
	Hero_select,Heroine_select,Music_select,Cinematography_select,Edited_select,
	company_select,Language_select,month_select]
	
	nulls = selections.count("Others")
	
	genere_col = "Genere_"+genere_select
	directors_col = "Directed by_"+directors_select
	producers_col = "Produced by_"+producers_select
	writers_col = "Written by_"+writers_select
	Hero_col = "Hero_"+Hero_select
	Heroine_col = "Heroine_"+Heroine_select
	Music_col = "Music by_"+Music_select
	Cinematography_col = "Cinematography_"+Cinematography_select
	Edited_col = "Edited by_"+Edited_select
	company_col = "company_"+company_select
	Language_col = "Language_"+Language_select
	month_col = "Release date_"+month_select
	
	selected_cols = [genere_col,directors_col,producers_col,writers_col,
	Hero_col,Heroine_col,Music_col,Cinematography_col,Edited_col,
	company_col,Language_col,month_col]
	
	for i in range(20):
		print("***************************************"+str(nulls),file=sys.stderr)
	
	# print(columns,file=sys.stderr)
	
	for i in range(5):
		print("***************************************"+str(nulls),file=sys.stderr)
	for x in range(len(selected_cols)):
		if( selected_cols[x] in columns):
			print(str(selected_cols[x]),file=sys.stderr)
			new_df[selected_cols[x]][0] = 1
	
	user_selection = new_df
	
	print(user_selection,file=sys.stderr)
	
	# scaler = StandardScaler().fit(user_selection)
	# user_selection_trans = scaler.transform(user_selection)
	# user_selection_test_trans  = scaler.transform(user_selection_trans)
	
	
	model_name= str(path)+'\models\predict_user_rating'
	predict_user_rating = joblib.load(model_name)

	user_rating = predict_user_rating.predict(user_selection)
	
	print("******+++++++User rating++++++++*******",file=sys.stderr)
	print(user_rating,file=sys.stderr)
	
	model_name = str(path)+'\models\predict_imdb'
	predict_imdb = joblib.load(model_name)

	Imdb = predict_imdb.predict([user_rating])
	
	print("******+++++++Imdb rating++++++++*******",file=sys.stderr)
	print(Imdb,file=sys.stderr)
	
	print("+++++++++++++++nulls: "+str(nulls),file=sys.stderr)
	
	new_df.loc[0]=[0 for n in range(len(columns))]
	
	print(str(Language_col),file=sys.stderr)
	print("*************nulls: "+str(nulls),file=sys.stderr)
	
	# return ("<h1> Movie prophecy</h1><hr>"+str(user_nulls));
	
	# return render_template(
        # 'result.html',
        # data=[{'name':'red'}, {'name':'green'}, {'name':'blue'}]
		# data = [genere,directors,producers,writers,Hero,Heroine,Music,Cinematography,Edited,company,months,Language])
	
	user_rating = round(user_rating[0],2);
	Imdb = round(Imdb[0],1);
	return render_template(
        'result.html',
        data=[{'user_rating':user_rating}, {'Imdb_rating':Imdb}]
		)

@app.route("/sendmail" , methods=['GET', 'POST'])
def sendmail():
	name = request.form.get('username')
	emailid = request.form.get('emailid')
	message = request.form.get('message')
	
	msg = MIMEMultipart('alternative')
	html = """\
	<!DOCTYPE html PUBLIC " -//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
	<html xmlns="http://www.w3.org/1999/xhtml">
	  <head>                                                               
		<title>
		</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width">
		<style type="text/css">    body, html {
		  width: 100% !important;
		  margin: 0;
		  padding: 0;
		  -webkit-font-smoothing: antialiased;
		  -webkit-text-size-adjust: none;
		  -ms-text-size-adjust:100%;
		}
		  table td, table {
			mso-table-lspace: 0pt;
			mso-table-rspace: 0pt;
		  }
		  #outlook a {
			padding: 0;
		  }
		  .ExternalClass, .ExternalClass p, .ExternalClass span, .ExternalClass font, .ExternalClass td, .ExternalClass div {
			line-height: 100%;
		  }
		  .ExternalClass {
			width: 100%;
		  }
		  @media only screen and (max-width: 480px) {
			table, table tr td, table td {
			  width: 100% !important;
			}
			img {
			  width: inherit;
			}
			.layer_2 {
			  max-width: 100% !important;
			}
		  }
		</style>
		<!--[if gte mso 9]><style type="text/css">    table td, table {        border-collapse: collapse;    }</style><![endif]-->
	  </head>
	  <body style="padding:0; margin: 0;">                                                    
		<table align="center" style="width: 100%; height: 100%; background-color: #efefef;">        
		  <tbody>            
			<tr>                
			  <td valign="top" id="dbody" data-version="2.29" style="padding-top: 30px; padding-bottom: 30px; width: 100%; background-color: #efefef;">
				<!--[if (gte mso 9)|(IE)]><table align="center" style="max-width:600px" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td valign="top"><![endif]-->                    
				<table class="layer_1" align="center" border="0" cellpadding="0" cellspacing="0" style="max-width: 600px; width: 100%; box-sizing: border-box; margin: 0px auto;">                        
				  <tbody>                            
					<tr>
					  <td class="drow" valign="top" align="center" style="background-color: #2fe4e9; box-sizing: border-box; font-size: 0px;">
						<!--[if (gte mso 9)|(IE)]><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td valign="top"><![endif]-->
						<div class="layer_2" style="max-width: 600px; width: 100%; display: inline-block; vertical-align: top; margin: 0px auto;">
						  <table border="0" cellspacing="0" class="edcontent" style="border-collapse: collapse;width:100%">
							<tbody>
							  <tr>
								<td valign="top" class="edtext" style="padding: 20px; color: #5f5f5f; font-size: 12px; font-family: Helvetica, Arial, sans-serif; text-align: left; direction: ltr; box-sizing: border-box;">
								  <p class="text-center" style="text-align: center; margin: 0px; padding: 0px;">
									<span style="font-size: 24px; color: #d93838;">Movie-Prophecy
									</span>
								  </p>
								</td>
							  </tr>
							</tbody>
						  </table>
						</div>
						<!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]-->
					  </td>
					</tr>
					<tr>
					  <td class="drow" valign="top" align="center" style="box-sizing: border-box; font-size: 0px; background-color: #ffffff;">
						<!--[if (gte mso 9)|(IE)]><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td valign="top"><![endif]-->
						<div class="layer_2" style="display: inline-block; vertical-align: top; width: 100%; max-width: 600px; margin: 0px auto;">
						  <table border="0" cellspacing="0" cellpadding="0" class="edcontent" style="border-collapse: collapse;width:100%">
							<tbody>
							  <tr>
								<td valign="top" class="edimg" style="text-align: center; padding: 0px; box-sizing: border-box;">
								  <img src="https://api.elasticemail.com/userfile/9c8f10a9-4f1b-4eed-8311-f55ef6878a0b/Movie-making4.jpg" alt="Image" width="584" style="border-width: 8px; border-style: solid; max-width: 584px; width: 100%; border-color: #2fe4e9;">
								</td>
							  </tr>
							</tbody>
						  </table>
						</div>
						<!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]-->
					  </td>
					</tr>                                                        
					<tr>                                
					  <td class="drow" valign="top" align="center" style="background-color: #92b9bb; box-sizing: border-box; font-size: 0px;">                                    
						<!--[if (gte mso 9)|(IE)]><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td valign="top"><![endif]-->
						<div class="layer_2" style="max-width: 600px; width: 100%; display: inline-block; vertical-align: top; margin: 0px auto;">
						  <table class="edcontent" style="border-collapse: collapse; width: 100%;" border="0" cellpadding="0" cellspacing="0">                                                        
							<tbody>                                                            
							  <tr>                                                                
								<td class="edtext" valign="top" style="padding: 20px; color: #5f5f5f; font-size: 12px; font-family: Helvetica, Arial, sans-serif; text-align: left; direction: ltr; box-sizing: border-box;">                                                                    
								  <div class="style2 text-center" style="text-align: center; color: #ffffff; font-size: 32px; font-family: &quot;Trebuchet MS&quot;, Helvetica, sans-serif;">                                                                            Movie Prophecy
									<br>
								  </div>
								  <div>
									<br>We provie predictions for various cast and crew combinations of your favourite actors, directors, producers, writers and so on...
								  </div>
								  <p style="margin: 0px; padding: 0px;">Happy to see you here and hope you had a great time with in our website making out good predictions of your favourite cast and crew.
									<br>
								  </p>                                         
								</td>                                     
							  </tr>                                 
							</tbody>                             
						  </table>
						</div>
						<!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]-->         
					  </td>     
					</tr>                                                        
					<tr>                                
					  <td class="drow" valign="top" align="center" style="box-sizing: border-box; font-size: 0px; background-color: #ffffff;">                                    
						<!--[if (gte mso 9)|(IE)]><table width="100%" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td valign="top"><![endif]-->
						<div class="layer_2" style="max-width: 191px; width: 100%; display: inline-block; vertical-align: top; margin: 0px auto;">
						  <table class="edcontent" style="border-collapse: collapse;width:100%" border="0" cellpadding="0" cellspacing="0">                                                        
							<tbody>                                                            
							  <tr>                                                                
								<td class="edimg" valign="bottom" style="padding: 54px; box-sizing: border-box; text-align: center;">                                                                                                                                            
								  <img style="border-width: 28px; border-style: none; max-width: 83px; width: 100%;" alt="Image" src="https://api.elasticemail.com/userfile/a18de9fc-4724-42f2-b203-4992ceddc1de/adventuretime_map.png" width="83">                                                                                        
								</td>                                     
							  </tr>                                 
							</tbody>                             
						  </table>
						</div>                                    
						<!--[if (gte mso 9)|(IE)]></td><td valign="top"><![endif]-->
						<div class="layer_2" style="max-width: 409px; width: 100%; display: inline-block; vertical-align: top; margin: 0px auto;">
						  <table class="edcontent" style="border-collapse: collapse;width:100%" border="0" cellpadding="0" cellspacing="0">                                                        
							<tbody>                                                            
							  <tr>                                                                
								<td class="edtext" valign="middle" style="padding: 20px; color: #5f5f5f; font-size: 12px; font-family: Helvetica, Arial, sans-serif; text-align: left; direction: ltr; box-sizing: border-box;">
								  <div class="style1" style="text-align: justify; color: #000000; font-size: 28px; font-family: Tahoma, Geneva, sans-serif;">
									<span style="color: #000000;">Start
									</span>
									<br>
								  </div>
								  <br>
								  <div>                                                                            
								  </div>
								  <p style="margin: 0px; padding: 0px;">Where ever you may start at. But for sure your destiny of choosing Movie-Prophecy as your choice to predict the success rate of your favourite cast and crew's combination is a good one to start.
								  </p>
								  <p style="margin: 0px; padding: 0px;">
									<br>
								  </p>
								  <p style="margin: 0px; padding: 0px;">Thank You.
								  </p>
								  <p style="margin: 0px; padding: 0px;">
									<br>
								  </p>
								  <p style="margin: 0px; padding: 0px;">Awaiting Your visit and have a great day.
								  </p>
								  <p style="margin: 0px; padding: 0px;">
									<br>
								  </p>
								  <p style="margin: 0px; padding: 0px;">Team Movie-Prophecy.
								  </p>
								  <div>
								  </div>
								</td>                                     
							  </tr>                                 
							</tbody>                             
						  </table>
						</div>
						<!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]-->         
					  </td>     
					</tr>
				  </tbody>
				</table>
				<!--[if (gte mso 9)|(IE)]></td></tr></table><![endif]-->
			  </td>
			</tr>
		  </tbody>
		</table>
	  </body>
	</html>

	"""
		
	# Record the MIME types of both parts - text/plain and text/html.
	
	msg['Subject'] = "Get in touch with Movie-Prophecy "
	part = MIMEText(html, 'html')

	msg.attach(part)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login("movieprophecymail@gmail.com", "makeprediction")

	try:
		server.sendmail("movieprophecymail@gmail.com", emailid, msg.as_string())
		print("Successfully sent email")
	except smtplib.SMTPException:
		print("Error: unable to send email")

	server.quit()

	return render_template(
        'movie_prophecy.html'
	)
	




if __name__=='__main__':
    app.run(debug=True)



