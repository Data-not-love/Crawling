from fi_driver_details_links import href_links
from bs4 import BeautifulSoup
import requests
import json
p = 'f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-normal non-italic f1-heading__body font-formulaOne f1-utils-inline-image--loose text-greyDark'
h1 = 'f1-heading tracking-normal text-fs-24px tablet:text-fs-42px leading-tight normal-case font-bold non-italic f1-heading__body font-formulaOne'
dd = 'f1-heading tracking-normal text-fs-14px leading-tight normal-case font-bold non-italic f1-heading__body font-formulaOne'
dt = 'f1-text font-titillium tracking-normal font-normal non-italic normal-case leading-snug f1-text__body text-fs-17px max-laptop:mb-normal'
contents = []
for driver_url in href_links:
    response = requests.get(driver_url)
    content = response.text
    contents.append(content)

all_data = []
for content in contents:
    soup = BeautifulSoup(content,'html.parser')
    #class_ strip thông tin cụ thể
    tags = soup.find_all(['p','h1','dd','dt'], class_ = [p,h1,dd,dt])

    # Duyệt qua các thẻ `dd` và `dt`
    extracted_values = {}
    current_key = None

    # Duyệt qua các thẻ `dd` và `dt`
    for tag in tags:

        stripped_text = tag.get_text(strip=True, separator=' ')

        if tag.name == 'dt' :
            current_key = stripped_text
        if tag.name == 'dd' or tag.name == 'h1' or tag.name == 'p' and current_key :
            extracted_values[current_key] = stripped_text
            # reset key = 0 để ko thêm list roongx
            current_key = None

    if extracted_values:
        # Tạo dictionary mới với "Driver's Name" ở đầu
        if None in extracted_values:
            driver_name = extracted_values.pop(None)

        elif "null" in extracted_values:
            driver_name = extracted_values.pop("null")

        # Tạo dictionary mới với tên tài xế ở đầu
        ordered_dict = {
            "Driver's Name": driver_name,
            **extracted_values  # spread operator để thêm các key-value pairs còn lại
        }

        all_data.append(ordered_dict)

json_output = json.dumps(all_data, ensure_ascii=False, indent=4)
print(json_output)


