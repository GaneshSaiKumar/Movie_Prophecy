from http.cookiejar import CookieJar
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as BeautifulSoup
import re
import sys
import urllib.error


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
Titles = "Year,Movie,Genere,Imbd_rating,User_rating,Directed by,Produced by,Written by,Screenplay by,Hero,Heroine,Music by,Cinematography,Edited by,company,Distributed by,Release date,Running time,Country,Language,Budget,Box office\n"
rup = u"\u20B9"

base_filename = "D:/Movie datasets/"
counter = 0

def scrape_wiki(wiki_url):
    wiki_page = urlopen(wiki_url)
    wiki_html = BeautifulSoup(wiki_page.read(),'html.parser')

    wiki_table = wiki_html.find('table',{'class':'infobox'}  )
    if(wiki_table is None):
        return '0'
    wiki_data = wiki_table.text.replace('\n',' , ')
    # print(wiki_data)
    # print("---------------------------------------------")
    l=[]
    for row in wiki_data.split(','):
        if row != "  " and row != " ":
            l.append(row)
    wiki_data = ",".join(l)
    print(wiki_data)
    # print("---------------------------------------------")
    bef, at, aft = wiki_data.partition("Directed by")
    if aft != "": 
        Director  = aft.split(',')[1]
        # print("Directed by  ")
        # print(Director)
        # print("---------------------------------------------")
    else:
        Director="null"
        # print(Director)
    bef, at, aft = wiki_data.partition("Produced by")
    if aft != "": 
        Producer  = aft.split(',')[1]
        # print("Produced by  ")
        # print(Producer)
        # print("---------------------------------------------")
    else:
        Producer="null"
        # print(Producer)
    bef, at, aft = wiki_data.partition("Written by")
    if aft != "": 
        Writer  = aft.split(',')[1]
        # print("Written by  ")
        # print(Writer)
        # print("---------------------------------------------")
    else:
        Writer="null"
        # print(Writer)
    bef, at, aft = wiki_data.partition("Screenplay by")
    if aft != "":
        Screenplay  = aft.split(',')[1]
        # print("Screenplay by  ")
        # print(Screenplay)
        # print("---------------------------------------------")
    else:
        Screenplay="null"
        # print(Screenplay)
    bef, at, aft = wiki_data.partition("Starring")
    if aft != "":
        Starring  = aft.split(',')[1:3]
        Starring = ','.join(Starring)
        # print("Starring  ")
        # print(Starring)
        # print("---------------------------------------------")
    else:
        Starring="null"
        # print(Starring)
    bef, at, aft = wiki_data.partition("Music by")
    if aft != "": 
        Music  = aft.split(',')[1]
        # print("Music by  ")
        # print(Music)
        # print("---------------------------------------------")
    else:
        Music="null"
        # print(Music)
    bef, at, aft = wiki_data.partition("Cinematography")
    if aft != "": 
        Cinematography  = aft.split(',')[1]
        # print("Cinematography  \r")
        # print(Cinematography)
        # print("---------------------------------------------")
    else:
        Cinematography="null"
        # print(Cinematography)
    bef, at, aft = wiki_data.partition("Edited by")
    if aft != "": 
        Editor  = aft.split(',')[1]
        # print("Edited by  ")
        # print(Editor)
        # print("---------------------------------------------")
    else:
        Editor="null"
        # print(Editor)
    bef, at, aft = wiki_data.partition("company")
    if aft != "": 
        Production  = aft.split(',')[1]
        # print("Production company  ")
        # print(Production)
        # print("---------------------------------------------")
    else:
        Production="null"
        # print(Production)
    bef, at, aft = wiki_data.partition("Distributed by")
    if aft != "": 
        Distributor  = aft.split(',')[1]
        # print("Distributed by  ")
        # print(Distributor)
        # print("---------------------------------------------")
    else:
        Distributor="null"
        # print(Distributor)
    bef, at, aft = wiki_data.partition("Release date")
    if aft != "":
        Release  = aft.split(',')[1].strip()
        # print(Release)
        Release = Release.replace(' ',' ')
        Release = Release.split(' ')[:3]
        Release = '-'.join(Release)
        '''
        # print(Release+'\n')
        date = re.findall(r'\([^()]*\)',Release)[0][1:-1]
        # print(date)
        b,p,a = date.split('-')
        if(int(b)>=40):
            Release = a+'-'+p+'-'+b
         '''
        # print("Release date  ")
        # print(Release)
        # print("---------------------------------------------")
    else:
        Release="null"
        # print(Release)
    bef, at, aft = wiki_data.partition("Running time")
    if aft != "": 
        Time  = aft.split(',')[1]
        # print("Running time  ")
        # print(Time)
        # print("---------------------------------------------")
    else:
        Time="null"
        # print(Time)
    bef, at, aft = wiki_data.partition("Country")
    if aft != "": 
        Country  = aft.split(',')[1]
        # print("Country  ")
        # print(Country)
        # print("---------------------------------------------")
    else:
        Country="null"
        # print(Country)
    bef, at, aft = wiki_data.partition("Language")
    if aft != "": 
        Language  = aft.split(',')[1]
        # print("Language  ")
        # print(Language)
        # print("---------------------------------------------")
    else:
        Language="null"
        # print(Language)
    bef, at, aft = wiki_data.partition("Budget")
    if aft != "": 
        Budget  = aft.split(',')[1].replace('–','-')
        st_index = Budget.find('(')
        Budget = Budget[:st_index]
        # print("Budget  ")
        # print(Budget)
        # print("---------------------------------------------")
    else:
        Budget="null"
        # print(Budget)
    bef, at, aft = wiki_data.partition("Box office")
    if aft != "": 
        BO = aft.split(',')[1]
        st_index = Budget.find('(')
        Budget = Budget[:st_index]
        # print("Box office  :")
        # print(BO)
        # print(":---------------------------------------------")
    else:
        BO="null"
        # print(BO)


    str = Director,Producer,Writer,Screenplay,Starring,Music,Cinematography,Editor,Production,Distributor,Release,Time,Country,Language,Budget,BO

    # print('\n--->\n')
    string = ','.join(str)
    string = string.replace('₹','')
    string = string.replace('–','-')
    # print("return one:  \n")
    # print(string)

    return string+"\n"

# wiki_url of movies are generated here
def scrape_movie(url):
    req = Request(url, headers=hdr)
    try:
        page = urlopen(req)
    except:
        print("url Error")
    # except urllib.error.URLError as e:
        # print(e.fp.read())

    content = page.read()
    page_soup = BeautifulSoup(content,"html.parser")
    
    imdb_rating = page_soup.find('span',{'class':'_tvg'})
    if(imdb_rating != None):
        imdb_rating = imdb_rating.text[:3]
    else:
        imdb_rating = "null"
    # print(imdb_rating)
    
    user_rating = page_soup.find('div',{'class':'_cNr _hhs'})
    # print("user rating = "+str(user_rating))
    if user_rating!= None:
        user_rating = user_rating.text[:3]
    else:
        user_rating = "null"
    # print('\n'+user_rating+'\n')
    
    movieurl = page_soup.find("h3",{"class":"r"})
    wiki_url = movieurl.find('a')['href']
    print("-->\n"+wiki_url+'\n')
    if(wiki_url.find('wikipedia') != -1 ):
        wiki_data = scrape_wiki(wiki_url)
        if wiki_data != '0':
            wiki_data= str(imdb_rating)+','+str(user_rating)+','+wiki_data
            return wiki_data
    # print("return one:  \n")
    # print(wiki_data)
    return 0;


#Generating Movie_page from google

def movies_per_year(site,filename,year):
    global counter
    req = Request(site, headers=hdr)
    try:
        page = urlopen(req)
    except:
        print("url Error")
        sys.exit()
    # except (urllib.request.HTTPError, e):
        # print(e.fp.read())

    content = page.read()
    page_soup = BeautifulSoup(content,"html.parser")
    g_scrolling_carousel = page_soup.find("g-scrolling-carousel")
    containers = g_scrolling_carousel.findAll("div",{'style':"height:260px;width:120px;margin-right:8px"})

    print("no of carousels : "+str(len(containers)))

    for container in containers:
        counter += 1
        print(str(counter)+"-------------------------------------------")
        movie = container.find("a")['aria-label']
        url = container.find("a")['href']
        genere = container.find("div",{"class":"ellip klmeta"})
        url = "https://www.google.co.in"+url
        # print(' \n container-url: \n'+url+'\n')
        if(genere):
            genere = genere.text
        else:
            genere = "Not Defined"
        # print(movie+","+genere+",\n"+url+"\n---")
        url = scrape_movie(url)
        if (url == 0):
            counter -=1
            continue
        # print(str(url))
        f = open(filename,'a')
        Final_movie_data = year+','+movie+","+genere+","+url
        print(Final_movie_data)
        f.write(Final_movie_data)
        f.close()

def main():
    # year = sys.argv[1]
	for year in range(1995,2000):
		year = str(year)
		site= "https://www.google.co.in/search?rlz=1C1CHBF_enIN724IN724&biw=785&bih=735&ei=bf46WvyRGon1vASUwJDABg&q=telugu+movies+"+year+"&oq=telugu+movies+"+year+"&gs_l=psy-ab.3..0l2j0i20i263k1j0l7.19418.21746.0.22455.8.8.0.0.0.0.315.1220.2-4j1.5.0....0...1c.1.64.psy-ab..3.5.1218...35i39k1j0i67k1.0.m0FbC69BHIw"
		fyear = year[:3]+'0'
		filename = base_filename+"data_"+fyear+".csv"
		f = open(filename,"a+")
		# f.write(Titles)
		f.close()
		movies_per_year(site,filename,year)

if __name__ == "__main__":
    main()
    
    
    