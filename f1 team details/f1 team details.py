import requests
from bs4 import BeautifulSoup
from f1_team_links_craw import href_links
import json


contents = []
for team_url in href_links:
    response = requests.get(team_url)
    content = response.text
    contents.append(content)


all_data = []
for content in contents:
    soup = BeautifulSoup(content,'html.parser')
    tags = soup.find_all(['dd','dt'])

    extracted_values = {}
    current_key = None

    # Duyệt qua các thẻ `dd` và `dt`
    for tag in tags:
        stripped_text = tag.get_text(strip=True, separator=' ')

        if tag.name == 'dt':
            current_key = stripped_text
        elif tag.name == 'dd' and current_key:
            extracted_values[current_key] = stripped_text


    all_data.append(extracted_values)

json_output = json.dumps(all_data, ensure_ascii=False, indent=4)
print(json_output)


