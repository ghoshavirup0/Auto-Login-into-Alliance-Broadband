import time
import requests
import sys
import getpass
from bs4 import BeautifulSoup
import os
import random

################################################################### EDIT USERNAME AND PASSWORD ###################################################################
username='EXAMPLE_USERNAME'
password='EXAMPLE_PASSWORD'
##################################################################################################################################################################

url='http://10.254.254.20/0/up/'




def login(url, username, password):
    print("Attempting to login..")
    payload = {'user': username,
               'pass': password,
               'login': 'Login'}
    try:
        requests.post(url, data=payload)
        print("Logged In")
    except:
        print("Could not connect to alliance server")


websites=[
"https://www.youtube.com/",
"https://www.google.co.in",
"https://www.twitter.com/?lang=en",
"https://www.facebook.com/",
"https://www.wikipedia.org/",
"https://in.yahoo.com/",
"https://www.amazon.co.in/"
]


def is_connected():
    
    try:
        website=random.choice(websites)
        print('Fetching: '+website.split('.')[1].upper())
        response = requests.get(website)
    
        if response.status_code is 200:
            print('Internet is connected')
            return True
        else:
            print('Internet is disconnected')
            return False
    except:
        print('Internet is disconnected')
        return False

def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')
   
def get_service_status(url):
    try:
        r = requests.get(url).text
        soup = BeautifulSoup(r, "lxml")

        soup = soup.find('table', attrs={'id': 'thesmalltable'})
        rows = soup.find_all('tr')
        # show only name, client id, package and expiry date
        
        name = rows[0].find_all('td')[1].text
        print("NAME: ", name)
        client_id = rows[2].find_all('td')[1].text
        print("CLIENT ID: ", client_id)
        package = rows[3].find_all('td')[1].text
        print("PACKAGE: ", package)
        expiry = rows[4].find_all('td')[1].text
        print("EXPIRY: ", expiry)
    except:
        return

while(True):
    if is_connected():
        get_service_status(url)
        time.sleep(60)
        screen_clear()
    else:
        login(url, username,password)
        time.sleep(5)
        screen_clear()



