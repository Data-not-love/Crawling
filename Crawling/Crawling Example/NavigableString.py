from bs4 import BeautifulSoup


with open ('index.html','r',encoding='utf-8') as file:
    content = file.read()

soup = BeautifulSoup(content,'html.parser')

a_items = soup.find_all('a')
for tag in a_items:
    print(tag.string)
    print(tag.prettify())

p_items = soup.find_all('p')

for tag in p_items:
    print(tag.string)