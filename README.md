This application scrapes the metservice.com website every half an hour for the
current temperature with and without windchill, before storing it in an SQL
database.

To run this you will need python2.7, sqlite3 and scrapy:

http://doc.scrapy.org/en/latest/intro/install.html#intro-install

Run.py is executed, it uses multiprocessing to start a process which sleeps 
for half an hour at a time before executing the scrapy shell with a spider 
targeting the metservice website. This is to save on processing power but also 
allow user input to quit the application or see how much time is left until 
the next scrape.

Much more information can be gathered, just modify the wget_spider.py script
and the weather_data.db to store the required data. If you want it to point to
another location you will have to look for it using your web browsers developer
tools while loading the correct metserivce page (it will be named similiarly to 
metservice.com/publicdata/localObs_porirua). If you're into web scraping at all
this won't be hard for you.

The scrapy script recieves a json module in response to GET query and just 
parses it for the temperature data, and then enters it into the sql data base 
called weather_data.db.

It's very lightweight, designed to run on a small webserver so that the data
from the sql database could be displayed dynamically via a webpage.
