import requests
import bs4

result= requests.get("https://en.wikipedia.org/wiki/Web_scraping")
soup = bs4.BeautifulSoup(result.text,'lxml')
for i in range(len(soup.select('.toctext'))):   #grab a class from bs4 library
    print(soup.select('.toctext')[i].getText())


