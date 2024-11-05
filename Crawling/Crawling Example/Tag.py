from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'html.parser')
tag = soup.b
print(type(tag))
# in tên thẻ
print (tag.name)


with open ('index.html','r',encoding='utf-8') as file :
    content = file.read()
print (content)
soup = BeautifulSoup(content,'html.parser')

# attrs chỉ in thuộc tính thẻ gốc ko in thuộc tính thẻ trong đ

div = soup.find('a')
print(div.attrs)

div_resultset = soup.find_all('a')
print(type(div_resultset))

for div in div_resultset:
    print(div.attrs)
    print(div.prettify())