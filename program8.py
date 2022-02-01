# Fetch all images from this site: http://rizzyhome.com/Images/Full_Img/ 
# and put them into a text file as well as JSON File.

# 	Note:- Put only the image file name in the text file.
# 	           Full path put into the JSON file.

import requests
from bs4 import BeautifulSoup
import json


grab = requests.get('http://rizzyhome.com/Images/Full_Img/')
soup = BeautifulSoup(grab.text, 'html.parser')

image_full_path = []
image_name = []

for link in soup.find_all('a'):    
    data = link.get('href')
    image_name.append(link.get_text())
    image_full_path.append(data)

write_image_full_path = json.dumps(image_full_path)
with open('image_fullpath_program8.json', 'w') as file:    
    file.write(write_image_full_path)

with open('image_filename_program8.txt', 'w') as textfile:    
    for name in image_name:
        textfile.write(name + "\n")
        
print("Scraping Done.")