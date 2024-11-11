import requests
from bs4 import BeautifulSoup


url = 'https://interactives.ap.org/election-results/customers/layouts/organization-layouts/published/49221/23238.html'
from selenium import webdriver
driver = webdriver.Chrome()  # hoặc Firefox, Edge
driver.get(url)
html_content = driver.page_source
with open("page.html", "w", encoding="utf-8") as file:
    file.write(html_content)
driver.quit()
