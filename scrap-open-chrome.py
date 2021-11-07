from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #Esperar a que carguen los elementos
from selenium.webdriver.support import expected_conditions #
from selenium.webdriver.common.by import By
import time
import pandas as pd

#Opciones de navegacion

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

driver_path = 'C:\ivan\python\chromedriver.exe'
driver = webdriver.Chrome(driver_path,chrome_options=options)

#Inicializar driver

driver.get('https://ivansantander.com')
