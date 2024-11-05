from bs4 import BeautifulSoup

with open ('F:/3.5 Years/First Year/Python/Web Scarping/Crawling/Crawling Example/index.html','r', encoding='utf-8') as file :
    content = file.read()


soup = BeautifulSoup(content,'html.parser')

print (soup.find('head'))


a_items = soup.find_all('a')
for a_item in a_items:
    print(a_item.prettify())