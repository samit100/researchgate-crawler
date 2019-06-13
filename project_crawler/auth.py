import requests
import sys
import os
sys.path.append(os.path.abspath("./docs/"))
from conf import *
from bs4 import BeautifulSoup
#class to create authentication
class Authentication:
    
    def RequestAuth():
        session = requests.Session()
        loginpage = session.get(urls['login'])
        request_token = BeautifulSoup(loginpage.text,"lxml").form.find("input",{"name":"request_token"}).attrs["value"]
        params = {"request_token":request_token,
                "invalidPasswordCount":0,
                'login': configData['email'], 
                'password': configData['password'],
                "setLoginCookie":configData['setLoginCookie']
                }
        session.post(urls['login'], data = params)
        s = session.get(urls['search'])
        pageBody = BeautifulSoup(s.text,"lxml").body
        
        return pageBody

    def checkAuth():
        s = session.get(urls['search'])
        pageBody = BeautifulSoup(s.text,"lxml").body
        isLoggedIn = pageBody.find_all(Authentication.match_class(["header-logged-in__logo"]))
        print(isLoggedIn)


    def withoutAuth(pageNumber):
        s = requests.get(urls['search']+str(pageNumber))
        print(urls['search']+str(pageNumber))
        pageBody = BeautifulSoup(s.text,"lxml").body
        
        return pageBody    

    def match_class(target):                                                        
        def do_match(tag):                                                          
            classes = tag.get('class', [])                                          
            return all(c in classes for c in target)                                
        return do_match

    def writeFacultyUrls(pageBody):
        allUrls = pageBody.find_all(Authentication.match_class(["display-name"]))
        file1 = open(files['facultyURL'],"a") 

        for m in allUrls:
            file1.write (urls['mainUrl']+str(m.attrs['href']))
            file1.write ("\n")
        file1.close()


if __name__ == "__main__":
    
    #start basic execution
    for pageNumber in range(1,3):          
        afterAuth = Authentication.withoutAuth(pageNumber)
        #Authentication.getfaculltyUrls()
        Authentication.writeFacultyUrls(afterAuth)
       