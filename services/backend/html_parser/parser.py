import requests
from bs4 import BeautifulSoup
import csv

# Make request 
html=requests.get("https://www.englishprofile.org/wordlists/evp?filter_search=&filter_custom_Level%5B%5D=1&filter_custom_Level%5B%5D=2&filter_custom_Level%5B%5D=3&filter_custom_Level%5B%5D=4&filter_custom_Level%5B%5D=5&filter_custom_Level%5B%5D=6&filter_custom_Topic=&filter_custom_Parts=&filter_custom_Category=1&filter_custom_Grammar=&filter_custom_Usage=&filter_custom_Prefix=&filter_custom_Suffix=&limit=0&directionTable=asc&sortTable=base&task=&boxchecked=0&filter_order=pos_rank&filter_order_Dir=asc&c536d88c2638e9654405bcaa8620fed2=1")

# Parsing the HTML
soup = BeautifulSoup(html.content, 'html.parser')
# Find the table element by its ID
table = soup.find('table', {'id':'reportList'})
# Open a new CSV file for writing
tbody=soup.find('tbody')
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Find all the rows in the table
    rows = tbody.find_all('tr')
    # Write column names
    writer.writerow(["en_word", "word_level", "uk_word"])
    # Create word list to avoid duplicates of words
    word_list=[]
    # Loop through the rows and extract the cells
    for row in rows:
        cells = row.find_all('td')
        word_cell = cells[0].text.strip()
        level_cell = cells[2].text.strip()       
        # Write the data to the CSV file
        if word_cell not in word_list:
            word_list.append(word_cell)
            writer.writerow([word_cell,level_cell])
    
        
        