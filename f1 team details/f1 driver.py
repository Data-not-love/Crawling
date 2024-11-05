import requests
from bs4 import BeautifulSoup
from f1_team_links_craw import href_links


contents = []
for driver_url in href_links:
    response = requests.get(driver_url)
    content = response.text
    contents.append(content)


for content in contents:
    soup = BeautifulSoup(content,'html.parser')
    tags = soup.find_all(['div'], class_='flex flex-col align-center px-normal py-xl laptop:px-xl')

    extracted_values = []
    extracted_attributes = []

    for value_tag in tags:
        stripped_text = value_tag.get_text(strip=True, separator=' ')  # strip=True sẽ loại bỏ khoảng trắng
        if stripped_text not in extracted_attributes:
            extracted_values.append(stripped_text)

    print(extracted_values)