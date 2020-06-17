import requests
import bs4

result= requests.get("https://en.wikipedia.org/wiki/Shah_Rukh_Khan")
soup = bs4.BeautifulSoup(result.text,'lxml')

comp = soup.select('img')[0]
print(comp['src'])

image_link = requests.get("https://upload.wikimedia.org/wikipedia/en/thumb/e/e7/Cscr-featured.svg/20px-Cscr-featured.svg.png")

