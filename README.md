# BookSearch

Simple web based app to search books using Google Books API made in Python using Flask

# How to Use

  - Install flask,flask-wtf and wtforms (and Google API library)
  - Run bookmain.py
  - Enter queries in the search bar and get results

# booksearch.py

Function which sends requests to the API or checks whether the query results are already present in the cache.

# bookmain.py

Routes to the different pages, constructs the list of recent results, takes requests and records time for each requst

# forms.py

Form for the search page

# HTML pages

 - layout.html
    Basic template (from bootstrap) inherited by all the pages
 - search.html
   Main search page
 - results.html
   redirect page after a query
 -recent.html
  redirect page after clicking on recent searches
 -about.html
  About page

