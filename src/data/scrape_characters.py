import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#set up chrome options for selenium web driver
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')

#create service
webdriver_service =Service(ChromeDriverManager().install())

#create driver
driver = webdriver.Chrome(service = webdriver_service, options=chrome_options)

#go to url with characters
page_url = 'https://www.hp-lexicon.org/character/?letter=A'
driver.get(page_url)

#get list of pages and their links
pagination=driver.find_element(By.XPATH, "//ul[@class='pagination']")
page_elements = pagination.find_elements(By.TAG_NAME,'a')

pages = []
for page in page_elements:
    page_url = page.get_attribute('href')
    page_name = page.text
    pages.append({'page_name': page_name, 'url':page_url})
    
character_list=[]

#for each page in the pagination
for page in pages:
    #go to the page url
    driver.get(page['url'])
    #get the elements with the names of the characters
    character_elements = driver.find_elements(By.XPATH, '//span[@itemprop="headline"]')
    #for each character, add their name and the page they were found to the list
    for character in character_elements:
        letter = page['page_name']
        character = character.text
        character_list.append({'letter': letter, 'character':character})


characters_df=pd.DataFrame(character_list)
characters_df.head()

path=r'C:\Users\Sherrif\Desktop\Everything\Projects\Code\Network analysis\harry_potter_network\data\interim\ '
characters_df.to_csv(path +'characters1.csv')
