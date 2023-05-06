from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import csv
import json

MAX_SCROLL_ITERATIONS = 50
URL_TESTIMONIES = "https://www.everyonesinvited.uk/read"
WAIT_TIME_SERVER_LOAD_DATA = 60

driver = webdriver.Firefox()
driver.get(URL_TESTIMONIES)

# Scrollear para abajo
for i in range(MAX_SCROLL_ITERATIONS):
    try:
        # Encontramos el boton por sus clases y lo pulsamos
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.font-surt.bg-DemonicYellow.rounded-full")))
        button.click()

        time.sleep(0.3)

    except Exception as e:
        #Si no encontramos el boton, hemos terminado el scroll
        break

# Extraer los datos basados en un selector css
wait = WebDriverWait(driver, 60)
wait2 = WebDriverWait(driver, 60)

text_body = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.text-left.font-surt")))
text_date_location = wait2.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.font-surt.text-xs")))


# Extraer cada texto
data_body = [element.text for element in text_body]
data_date_location = [element.text for element in text_date_location]

# Creamos un array de objetos y limpiamos los datos
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

    # Escribimos el header
    writer.writeheader()

    # Guardamos linea por linea
    for obj in data:
        writer.writerow(obj)

#driver.close()
