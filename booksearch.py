import os
import requests
import json
import settings

class gbooks():

    #main function which sends request to API and returns the json file
    def search(self, value, cache):
        # converted to lowercase so that queries differing in case aren't sent to the API again
        value = value.lower()
        # try-catch block to check whether a particular key exists within the cache
        try:
            val = cache[value]
            print ('from cache')
            return val
        except KeyError:
            parms = {"q":value, 'key':settings.googleapikey}
            r = requests.get(url="https://www.googleapis.com/books/v1/volumes", params=parms)
            #print (r.url)
            rj  = r.json()
            cache[value] = rj
            return rj
