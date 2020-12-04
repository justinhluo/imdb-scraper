from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
my_url = 'https://www.imdb.com/search/title/?count=100&groups=top_1000&sort=user_rating'
nextURL = 'https://www.imdb.com/search/title/?groups=top_1000&sort=user_rating,desc&count=100&start=' 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

filename = "top1000.csv"
f = open(filename, "w")

headers = "ID, IMDB_rating, Title, Rated, Runtime, Genre, Votes, Gross, Metascore\n"
f.write(headers)


containers = page_soup.findAll("div",{"class":"lister-item-content"})
for container in containers:
	id_ = container.h3.a['href'].split('/')[2].strip()
	name = container.h3.a.text.strip()
	name = name.replace(',','')
	
	imdb = container.div.div["data-value"]
	metascore = container.findAll("div",{"class":"inline-block ratings-metascore"})
	if metascore:
        
		metascore_ = metascore[0].text.strip()
		
		metascore_ = metascore_.replace('Metascore', '')

	rating = container.findAll("span",{"class":"certificate"})
	if rating:
		rating_ = rating[0].text.strip()

	runtime = container.findAll("span", {"class":"runtime"})
	if runtime:
		runtime_ = runtime[0].text.strip()
	genre = container.findAll("span", {"class":"genre"})
	if genre:
		genre_ = genre[0].text.strip()
		genre_ = genre_.replace(',', ' ')
	votes = container.findAll("span", {"name": "nv"})
	if votes:
		votes_ = votes[0].text
		votes_ = votes_.replace(',','')
		if len(votes) > 1:
			gross = votes[1].text
			gross = gross.replace(',','NaN')
		else: gross = ''
	print(votes_)
	print(gross)
	print("id: " + id_)
	print("title: " + name)
	print("rated: " + rating_)
	print("time: " + runtime_)
	print("genre: " + genre_)
	print("rating: " + imdb)
	print("metascore: " + metascore_)

	f.write(id_ + ',' + imdb + ',' + name + ',' +  rating_ + ',' + runtime_ + ',' +genre_ + ',' + votes_ + ',' + gross + ',' + metascore_)


for i in range(9):
    i = i + 1
    nextURL = nextURL + str(i) + '01&ref_=adv_nxt'
    uClient = uReq(nextURL)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")

    containers = page_soup.findAll("div",{"class":"lister-item-content"})
    for container in containers:
	    id_ = container.h3.a['href'].split('/')[2].strip()
	    name = container.h3.a.text.strip()
	    name = name.replace(',','')
		
	    imdb = container.div.div["data-value"]
	    metascore = container.findAll("div",{"class":"inline-block ratings-metascore"})
	    if metascore:
	        
		    metascore_ = metascore[0].text.strip()
			
		    metascore_ = metascore_.replace('Metascore', '')

	    rating = container.findAll("span",{"class":"certificate"})
	    if rating:

		    rating_ = rating[0].text.strip()

	    runtime = container.findAll("span", {"class":"runtime"})
	    if runtime:
		    runtime_ = runtime[0].text.strip()

	    genre = container.findAll("span", {"class":"genre"})
	    if genre:
	    	genre_ = genre[0].text.strip()
	    	genre_ = genre_.replace(',', ' ')
	    votes = container.findAll("span", {"name": "nv"})
	    if votes:
	    	votes_ = votes[0].text
	    	votes_ = votes_.replace(',','')
	    	if len(votes) > 1:
	    		gross = votes[1].text
	    		gross = gross.replace(',','NaN')
	    	else: gross = ''

	    print(votes_)
	    print(gross)
	    print("id: " + id_)
	    print("title: " + name)
	    print("rated: " + rating_)
	    print("time: " + runtime_)
	    print("genre: " + genre_)
	    print("rating: " + imdb)
	    print("metascore: " + metascore_)

	    f.write( id_ + ',' + imdb + ',' + name + ',' + rating_ + ',' + runtime_ + ',' +genre_ + ',' + votes_ + ',' + gross + ',' +metascore_) 

f.close()
