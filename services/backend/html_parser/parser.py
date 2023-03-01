from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
import csv

# Using Chrome to access web
url='https://www.englishprofile.org/american-english'
driver = webdriver.Chrome()
# Open the website
driver.get(url)

#driver.find_element('id','filter_custom_Level2').click()
wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="adminForm"]/div[1]/div[2]/div/fieldset/div/label[3]'))).click()
button = driver.find_element('xpath','//*[@id="adminForm"]/div[1]/div[3]/button')
button.click()
drop_down = Select(driver.find_element('id','limit'))
drop_down.select_by_value('0')

html_content = requests.get(driver.current_url).text
 
# Parsing the HTML
soup = BeautifulSoup(html_content, 'html.parser')
# Find the table element by its ID
table = soup.find('table', {'id':'reportList'})
# Open a new CSV file for writing
tbody=soup.find('tbody')
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Find all the rows in the table
    rows = tbody.find_all('tr')
    
    # Loop through the rows and extract the first cell
    for row in rows:
        cells = row.find_all('td')
        first_cell = cells[0].text.strip()

        # Write the data to the CSV file
        writer.writerow([first_cell])
    
        