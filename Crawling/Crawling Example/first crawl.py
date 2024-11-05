from bs4 import BeautifulSoup


# ko đưa trực tiếp file HTML, đọc file HTML trc
with open ('index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
soup = BeautifulSoup( html_content,'html.parser')

print (soup.prettify())

# in cấu trúc thẻ
print(soup.title)

# in loại thẻ
print(soup.title.name)

# in string trong thẻ title
print(soup.title.string)

# in thành phần đâu tiên trong thẻ p
print (soup.p)

# in all thành phần trong thẻ p
print(soup.find_all('p'))

#
print(soup.p['class'])

# thành phần đấu tiên trong thẻ a
print(soup.a)


# tìm theo id
print(soup.find(id="link3"))

# lấy all text
print (soup.get_text())