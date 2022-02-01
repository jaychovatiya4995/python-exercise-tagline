# Scrape any Website, then find all anchor tags and Store them in 
# the JSON file where the key is URL and the value is anchor text.

import requests
from bs4 import BeautifulSoup
import json

website_url = input("Enter a websie link for Scrape: ")

urls = website_url
grab = requests.get(urls)
soup = BeautifulSoup(grab.text, 'html.parser')

all_urls = []
for link in soup.find_all('a'):    
    data = link.get('href')
    all_urls.append(data)
    
# write_data = json.dumps({urls : all_urls})
write_data = json.dumps({'urls' : all_urls})
with open('url_program6.json', 'w') as file:
    file.write(write_data)

# with open('url_program6.json', 'r+') as file:
#        file_data = json.load(file)
#        file_data["urls"].append({urls : all_urls})
#        json.dump(file_data, file)

