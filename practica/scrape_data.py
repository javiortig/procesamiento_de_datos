from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
import csv
import json


driver = webdriver.Firefox()
driver.get("https://www.everyonesinvited.uk/read")

# Scrollear para abajo
for i in range(10):
    try:
        # Find the button element by its classes
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.font-surt.bg-DemonicYellow.rounded-full")))

        # Click the button
        button.click()

        # Wait for 8 seconds before clicking the button again
        # time.sleep(2)

    except NoSuchElementException:
        # If the button is not found, break out of the loop
        break

# Extraer los datos basados en un selector css
wait = WebDriverWait(driver, 30)

text_body = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.text-left.font-surt")))
text_date_location = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.font-surt.text-xs")))



# Extraer cada texto
data_body = [element.text for element in text_body]
data_date_location = [element.text for element in text_date_location]

data = [
    {
        "body": body.text, 
        "date": (date_location.text.split(',')[0] + date_location.text.split(',')[1]) if  date_location.text != '' else '',
        "location": date_location.text.split(',')[2].replace(" ", "", 1) if  date_location.text != '' else ''
    } 
    for body, date_location in zip(text_body, text_date_location)]

# Guardamos en el json
with open("data.json", "w") as f:
    json.dump(data, f)

# Guardamos en un csv donde las keys son los nombres de las columnas
with open('data.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())

    #Escribimos el header
    writer.writeheader()

    # guardamos linea por linea
    for obj in data:
        writer.writerow(obj)

driver.close()


# Guardarlo en un csv
# with open('data.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Data'])
#     for item in data_body:
#         writer.writerow([item])

