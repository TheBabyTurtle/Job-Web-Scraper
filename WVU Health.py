import requests
from bs4 import BeautifulSoup

URL = "http://health.wvu.edu/healthaffairs/careers/"
page = requests.get(URL)
counter = 0
soup = BeautifulSoup(page.content, "html.parser")
pieces = []
piece = []
results = soup.find(id="content")
target = results.find(class_="page-primary rich-text")
for child in target.children:
    if(child.name == "h4"):
        piece.append(child.text.strip())
        while(True):
            child = child.nextSibling
            if(child.name == "h4" or child.name == "h3"):
                pieces += piece
                counter += 1
                piece.clear()
                break
            elif(child.name == "p"):
                piece.append(child.text.strip())
for bit in pieces:
    print(bit)