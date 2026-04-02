import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/Users/tbf216/Downloads/chromedriver.exe')

driver.get('https://www.nba.com/news')
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element_1 in soup.findAll(attrs="ArticleTile_tile__y70gI"):
    name = element_1.find('h3')
    if name not in results:
        results.append(name.text)

for element_2 in soup.findAll(attrs="ArticleTile_tileTimestamp__xz7Ky"):
    if element_2 not in results:
       other_results.append(element_2.text)

df = pd.DataFrame({'Latest News': results, 'Dates': other_results})
df.to_csv('latest_news.csv', index=False, encoding='utf-8')