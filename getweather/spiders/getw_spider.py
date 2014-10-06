# this script scrapes the metservice website for porirua's current data
# it queries with a GET and receives a json node in response, which is parsed for the location, temperature etc
# writes it into weather_data.db, an SQL database in the format: <datetime> <temp> <windchill>

import scrapy
import json
import sqlite3 as lite
import time

class MetSpider(scrapy.Spider):
    global con
    con = None
    con = lite.connect('weather_data.db')
    global localtime
    localtime = (time.asctime( time.localtime(time.time()) ))
    print "Local current time :", localtime    
    
    name = "metservice"
    allowed_domains = ["metservice.com"]
    start_urls = [
        "http://www.metservice.com/publicData/localObs_porirua"
        ]
    
    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        
        print "Current location: " + jsonresponse["location"]
        print "Current temperature: " + jsonresponse["threeHour"][u'temp']
        print "Current temperature minus windchill: " + jsonresponse["threeHour"][u'windChill']
        
        temp = (jsonresponse["threeHour"][u'temp'])
        wind_chill = (jsonresponse["threeHour"][u'windChill'])
        message = 'INSERT INTO weather(time, temp, wchill) VALUES("'+str(localtime)+'", "'+str(temp)+'", "'+str(wind_chill)+'")'
        #print message
        with con:
            cur = con.cursor()
            cur.execute(message) 
