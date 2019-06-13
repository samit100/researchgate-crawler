import requests
import sys
import os
sys.path.append(os.path.abspath("./docs/"))
from auth import *
from bs4 import BeautifulSoup

#class to get metadata

class Metadata:

    def visitUrl():
        try:
            readUrl = open(files['facultyURL'], 'r')
            lines = readUrl.readlines()
            print(lines)
        finally:    
            readUrl.close()

    def createDirectories(dir):
        if not os.path.exists(dir):
            os.makedirs(dir)
        
    def getMetaData():
        session = requests.Session()
        loginpage = session.get(urls['login'])
        request_token = BeautifulSoup(loginpage.text,"lxml").form.find("input",{"name":"request_token"}).attrs["value"]
        params = {"request_token":request_token,
                "invalidPasswordCount":0,
                'login': configData['email'], 
                'password': configData['password'],
                "setLoginCookie":configData['setLoginCookie'],
                "x-requested-with": "XMLHttpRequest",
                "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
                }
        session.post(urls['login'], data = params)
        s = session.get("https://www.researchgate.net/publication/331074067_Classical_Greek_Models_of_the_Gospels_and_Acts_Studies_in_Mimesis_Criticism")
        pageBody = BeautifulSoup(s.text,"lxml").body

        #getData = requests.get(urls['mark'])
        getData = BeautifulSoup(pageBody.text,"lxml").body
        print(getData);        
            
Metadata.getMetaData()
Metadata.createDirectories("./downloads/Mark_Bilby")
Metadata.createDirectories("./downloads/Mark_Bilby/pdfs")
Metadata.createDirectories("./downloads/Mark_Bilby/metadata")
Metadata.createDirectories("./downloads/Mark_Bilby/metadata/")

putMetaData = open("./downloads/Mark_Bilby/metadata/metadata.txt","a")
putMetaData.write ("Publisher: Claremont PressEditor: Mark G. BilbyISBN: 978-1946230188")

