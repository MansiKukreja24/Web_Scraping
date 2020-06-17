import requests
import bs4

result = requests.get("http://www.example.com")  #using only request library
print("")
print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")  #using bs4 library
print(soup)


print(soup.select('title')[0].getText())    #grabbing title from the source code
