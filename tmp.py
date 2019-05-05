from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import time
from bs4 import BeautifulSoup

IP='140.113.216.91'

chrome_options = Options()
chrome_options.add_argument('window-size=1920x3000') 
chrome_options.add_argument('--disable-gpu') 
chrome_options.add_argument('--hide-scrollbars') 
chrome_options.add_argument('blink-settings=imagesEnabled=false') 
chrome_options.add_argument('--headless') 
chrome_options.add_argument("--log-level=3")  

driver=webdriver.Chrome(chrome_options=chrome_options)           
driver.get("https://talosintelligence.com/reputation_center/lookup?search="+IP)       
time.sleep(10)                            

html=driver.page_source
soup = BeautifulSoup(html, 'html.parser')
REPUTATION = soup.find_all("span", class_=re.compile('details-rep-*'),limit=1)#details-rep-Good | Neutral
print(IP)
for REPUTATION_span in REPUTATION:
	print(REPUTATION_span.text)

driver.quit()