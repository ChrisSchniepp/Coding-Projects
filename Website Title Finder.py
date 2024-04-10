import requests
from bs4 import BeautifulSoup
import re

# NY Times
ny = requests.get("https://www.nytimes.com/")
ny_html = ny.text

soup = BeautifulSoup(ny_html,'html.parser')
Article = soup.find_all('p','indicate-hover')

# NBC
nbc = requests.get("https://www.nbcnews.com/")
nbc_html = nbc.text

soup2 = BeautifulSoup(nbc_html,'html.parser')
Article2 = soup2.find_all('a')


def make_string(names): # takes a soup list
    s = []
    for i in range(0,len(names)):
        s.append(names[i].string)

    return s

def look_for_title(longlist):
    shortlist = []
    for i in range(0,len(longlist)):
        string_length = str(longlist[i]).split()
        if len(string_length)>=5:
            shortlist.append(longlist[i])
    return shortlist        

def duplicates(x):
    y = []
    for i in x:
        iii = 0
        for ii in x:
            if i == ii:
                iii+=1
        if iii>=2 and i not in y:
            y.append(i)            
    return y

title = duplicates(look_for_title(make_string(Article2)))

print(title)




