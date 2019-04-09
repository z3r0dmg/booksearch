from flask import Flask, render_template, url_for, request
from forms import SearchForm
from booksearch import gbooks
import json
import time
from cachetools import TTLCache

app = Flask(__name__)

app.config['SECRET_KEY'] = '6a5c6dc14729082181c6266a6adeabd0'

#initialising TTL cache to store query results for 10 minutes
cache = TTLCache(maxsize=1024, ttl=600)

#list to store history of queries
recents = []

#function to store results in the recents list
def storeRecent(results):
	temp_list = []
	for result in results["items"]:
		store = {}
		try:
			store['author'] = result["volumeInfo"]["authors"][0]
		except:
			store['author'] = 'No author'

		try:
			store['publishedDate'] = result["volumeInfo"]["publishedDate"]
		except:
			store['publishedDate'] = 'Unknown'

		try:
			store['title'] = result["volumeInfo"]["title"]
		except:
			store['title'] = 'Unknown'
		
		try:
			store['description'] = result["volumeInfo"]["description"]
		except:
			store['description'] = 'No description'

		temp_list.append(store)
	temp_list = temp_list[::-1]
	return temp_list

#Main page
@app.route("/", methods=['GET', 'POST'])
def home():
	form = SearchForm(request.form)

	#get query string from form
	if request.method == 'POST' and form.validate():
		query = form.query.data

		#get results and measure the time
		a=time.time()
		results = gbooks().search(str(query), cache)
		recents.append(str(query))
		b=time.time()
		time_taken = b-a
		time_taken = round(time_taken,2)

		#if no items are returned from a query print message to indicate it
		if results["totalItems"]==0:
			return render_template('search.html',form=form,res=False)
			
		#add results to reccents list
		for i in storeRecent(results):
			recents.append(i)
			
		return render_template('results.html',results=results, query=query, time_taken=time_taken)

	return render_template('search.html',form=form,res=True)

#Recent Searches page
@app.route("/recent")
def recent():
	return render_template('recent.html',recents = recents[::-1])

#About Page
@app.route("/about")
def about():
	return render_template('about.html')


if __name__ == '__main__':
	app.run()