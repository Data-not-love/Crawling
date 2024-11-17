import requests
from bs4 import BeautifulSoup

url  = "https://daotao.vku.udn.vn/sv/lienheGV"
url_1 = 'https://interactives.ap.org/election-results/customers/layouts/organization-layouts/published/49221/23238.html'
u ="https://www.270towin.com/2024-election-results-live/president/"
response = requests.get(u)
content = response.text
print (response)
print (content)

print ("----------------------------------------------------------------------------------------")
soup = BeautifulSoup(content,'html.parser')
print(soup.prettify())