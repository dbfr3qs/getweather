# run the python script that scrapes the metserivce website for porirua's data and writes it to the weather_data.db SQLite database
# Because sleep.time is used to save on processing power between scrapes, I have used multiprocessing in order to allow for user input
# to restart the process or quit. 

import os
import time
import multiprocessing

def getSleepTime(): # work out how many seconds to wait until next hour or half hour is reached
    t = time.localtime()
    mn = t.tm_min
    sc = t.tm_sec    
    
    tmm = 60 - mn
    scs = 60 - sc
    
    if tmm > 30:
        tmm-=30
    
    return ((tmm*60) + scs)

def exe_script(): # executes the scrapy script, as a seperate process
    print str(getSleepTime())+" seconds to wait."
    time.sleep(getSleepTime())
        
    os.system("scrapy crawl metservice -s LOG_ENABLED=0")    
    
if __name__ == '__main__':
    p = multiprocessing.Process(target=exe_script)
    while True: # check every half an hour
        
        if not p.is_alive(): 
            try:
                p.start()
                
            except:
                print "There was an error starting the exe_script process."
            
        c = raw_input('r to reset, t for time left or q to quit\n');
        
        if (c == 'r'):
            p.terminate();
            time.sleep(0.1)
            p.join
            p = multiprocessing.Process(target=exe_script)
            
        if (c == 'q'):
            p.terminate();
            time.sleep(0.1)
            p.join
            break
        
        if (c == 't'):
            print str(getSleepTime())+" seconds to wait."
            time.sleep(0.1)
            
          