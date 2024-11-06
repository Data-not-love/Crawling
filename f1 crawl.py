import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.formula1.com/en/results.html/2024/fastest-laps.html'
url_1 = 'https://www.formula1.com/en/results.html/2024/drivers.html'
url_2 = 'https://www.formula1.com/en/results.html/2024/team.html'
urls = [url,url_1,url_2]
def crawl_data (url_path):
    response = requests.get(url_path)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')


    table_items = soup.find_all('table')

    for tag in table_items:
        cols_values = tag.find_all('th') # container các giá trị

    columns = []
    for col_value in cols_values:
        attribute = col_value.get_text(strip=True)
        columns.append(attribute)
    print(columns)


    values = []
    for tag in table_items:
        rows_values = tag.find_all('p')

    for rows_value in rows_values:
        value = rows_value.get_text(strip=True,separator=' ')
        if value not in columns:
            values.append(value)
    print(values)



    to_dataframe = []
    for i in range(0, len(values), len(columns)):
        data = values[i:i + len(columns)]
        to_dataframe.append(data)

    df = pd.DataFrame(to_dataframe, columns=columns)

    print(df.to_string(index=False))


for each_url in urls:
    crawl_data(each_url)
    print ("-------------------------------------------------------------------")