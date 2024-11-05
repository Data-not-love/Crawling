import requests
from bs4 import BeautifulSoup

url = 'https://www.formula1.com/en/teams.html'
response = requests.get(url)
print (response)
content = response.text

soup = BeautifulSoup(content, 'html.parser')


tag_links = soup.find_all('a')
# lấy link cào

href_links = []
base_url = 'https://www.formula1.com'
for tag_link in tag_links:
    href = tag_link.get('href')  # Lấy giá trị của thuộc tính href
    if href and href.startswith('/en/teams/'):
        href_links.append(f'{base_url}'+href+'.html')
print(href_links)



