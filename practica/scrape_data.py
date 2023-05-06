from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

import time
import csv
import json
from itertools import zip_longest

MAX_SCROLL_ITERATIONS = 200
WAIT_TIME_SERVER_LOAD_DATA = 60
URL_TESTIMONIES = "https://www.everyonesinvited.uk/read"
RUN_HEADLESS = True

# Iniciamos el driver headless para ir más rapido
driver_options = Options()
if RUN_HEADLESS: 
    driver_options.add_argument('-headless')

driver = webdriver.Firefox(options=driver_options)

#Entramos en la URL
driver.get(URL_TESTIMONIES)

# Scrollear para abajo
for i in range(MAX_SCROLL_ITERATIONS):
    try:
        # imprime una barra de progreso
        percent = int((i / MAX_SCROLL_ITERATIONS) * 100)
        print(f"[{'=' * percent}{' ' * (100 - percent)}] {percent}% complete", end='\r')

        # Encontramos el boton por sus clases y lo pulsamos
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.font-surt.bg-DemonicYellow.rounded-full")))
        button.click()

        time.sleep(2) if (i%6 == 0) else time.sleep(0.3)
        

    except Exception as e:
        #Si no encontramos el boton, hemos terminado el scroll
        break

print('\nExtracting data...')

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
        "body": body.text , 
        "date": (date_location.text.split(',')[0] + date_location.text.split(',')[1]) if  ((date_location != None) and (date_location.text != '') and (date_location.text != None)) else '',
        "location": date_location.text.split(',')[2].replace(" ", "", 1) if  ((date_location != None) and (date_location.text != '') and (date_location.text != None)) else ''
    } 
    for body, date_location in zip_longest(text_body, text_date_location)]


print('Saving...')

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

driver.close()

print('Job done!')