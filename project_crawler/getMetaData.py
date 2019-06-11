import requests
import sys
import os
sys.path.append(os.path.abspath("./docs/"))
from auth import *
from bs4 import BeautifulSoup
#class to create authentication

class Metadata:

    def visitUrl():
        try:
            readUrl = open(files['facultyURL'], 'r')
            lines = readUrl.readlines()
            print(lines)
        finally:    
            readUrl.close()
            
Metadata.visitUrl()


