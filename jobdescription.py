import re
from nltk.corpus import stopwords
from goose3 import Goose
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import time
import requests
import random
import pandas as pd
import matplotlib.pyplot as plt
import csv


base_url = "http://www.indeed.com"    
#change the start_url can scrape different cities.
start_url = "http://www.indeed.com/jobs?q=data+scientist&l=San+Francisco%2C+CA"

#creating a response object called resp
resp = requests.get(start_url)

#You can find out what encoding Requests is using, and change it, using the r.encoding property
#print(resp.encoding)

# Running the url link through BeautifulSoup give us a BeautifulSoup object, which represents the document as a nested data structure.
start_soup = BeautifulSoup(resp.content)
urls = start_soup.findAll('a',{'rel':'nofollow','target':'_blank'}) #this are the links of the job posts

#To store all url links to a list called links.
links=[]
for link in urls:
    links.append(link.get('href'))
#print(links[0:2])

#urls = [link['href'] for link in urls] 
#print(urls[0:2])

# prevent the driver stopping due to the unexpectedAlertBehaviour.
webdriver.DesiredCapabilities.FIREFOX["unexpectedAlertBehaviour"] = "accept"
get_info = True

DRIVER_EXE = r"C:\Users\Andrew Yan\Documents\GitHub\data_skills\geckodriver.exe"
#the instance of Firefox WebDriver is created.
driver=webdriver.Firefox(executable_path=DRIVER_EXE)

# set a page load time limit so that don't have to wait forever if the links are broken.
driver.set_page_load_timeout(15)
for i in range(len(urls)):
    get_info = True
    try:
        driver.get(base_url+links[i]) #The driver.get method will navigate to a page given by the URL.
    except TimeoutException:
        get_info = False
        continue
    j = random.randint(1000,2200)/1000.0
    time.sleep(j) #waits for a random time so that the website don't consider you as a bot
    if get_info:
        soup=BeautifulSoup(driver.page_source)

        print (driver.current_url)
        
driver.quit()
    