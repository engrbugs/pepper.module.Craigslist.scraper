import requests
import webReader
import pandas as pd

import FileIni
import emailmod
from threading import Timer,Thread,Event

import time
import sys
import os
lastseenUrls = []

#LOAD SETTINGS INI FILE

lastseenUrls = FileIni.readini()
print('List of Seen Items:')
print(*lastseenUrls, sep="\n")
counter = 0


##########DATA HERE################
version = '1.01'

webpageToScrape = "https://vancouver.craigslist.ca/search/rch/apa?max_price=2000&availabilityMode=0&laundry=1&sale_date=all+dates"
#I think with HTTPS:// please

refreshRate = 60 #seconds
recipients = ['USER1@gmail.com', 'USER2@gmail.com']

##########DATA END###############

def checkCoverifNew():
    print('-------------------------------------------')
    webReader.Read_Cover(webpageToScrape)
    print(webReader.totalcount)

    

    global lastseenUrls
    for url in lastseenUrls:
        if webReader.houseitems['Url'].str.contains(url).any():
            print('seen the last seen!')
            myseries = webReader.houseitems['Url']
            ind = myseries[myseries == url].index[0] 
            if (ind != 0):
                print(webReader.houseitems[:ind])
                if (emailmod.sendSingleEmailOnePage(recipients, 
                                            webReader.houseitems[:ind],
                                            webpageToScrape,
                                            version,
                                            webReader.houseitems,
                                            webReader.totalcount
                                            ) == True):
                    #emailmod.changeLastseenEmail(url, webReader.houseitems['Url'][0])
                    lastseenUrls = []
                    for i in range(5):
                        lastseenUrls.append(webReader.houseitems['Url'][i])
            break
    print('List of Seen Items:')
    print(*lastseenUrls, sep="\n")
    ###############print('I did not found the Last Seen!')<---- Where should I put this


    FileIni.WriteIni(lastseenUrls)
    global counter
    counter += 1
    print('counter: ' + str(counter))
    print('time: ' + time.strftime('%H:%M'))
    print('location: Richmond')
    #print('lastseen: ' + lastseenUrl)
    print('List of Seen Items:')
    print(*lastseenUrls, sep="\n")
    print('-----------------**END**-------------------')

    



class perpetualTimer():
    #this can be stopped by t.cancel()

    def __init__(self,t,hFunction):
        self.t=t
        self.hFunction = hFunction
        self.thread = Timer(self.t,self.handle_function)
      
    def handle_function(self):
        self.hFunction()
        self.thread = Timer(self.t,self.handle_function)
        self.thread.start()

    def start(self):
        self.thread.start()

    def cancel(self):
        self.thread.cancel()

t = perpetualTimer(refreshRate,checkCoverifNew)
checkCoverifNew()
t.start()




