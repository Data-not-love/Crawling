import requests
from bs4 import BeautifulSoup
# cào dữ liệu từ F1 và in ra csv, json
url = 'https://www.formula1.com/en/results.html/2024/drivers.html'

response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, 'html.parser')

# ko gọi trưc tiêp ở resultset
table_items = soup.find_all('table')



for tag in table_items:
    rows = tag.find_all('tr')


values = []
for row in rows:
    value = row.get_text(strip=False,separator=' ')
    values.append(value)
print(values)
# Hướng 1 tạo list extracted_values = []
# Thead tìm các thuộc tính
