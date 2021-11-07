from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #Esperar a que carguen los elementos
from selenium.webdriver.support import expected_conditions #
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# TODO 3: start de web driver
options = webdriver.ChromeOptions()
options.add_argument('--disable-infobars')
options.add_experimental_option('useAutomationExtension',False)
options.add_experimental_option('excludeSwitches',['enable-automation'])
#options.add_argument('--kiosk')
prefs = {"credentials_enable_service":False,"profile.password_manager_enable":False}
options.add_experimental_option("prefs",prefs)

driver_path = 'C:\ivan\python\chromedriver.exe'
driver = webdriver.Chrome(driver_path,chrome_options=options)

#Inicializar driver
url = 'http://localhost:8100/'
driver.get(url)

#SEDE
PASSWORD_SEDE = "1502,1"

#scraping
def sede():
    location_code = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH,"//*[contains(@aria-labelledby,'ion-input-2-lbl')]")))
    location_code.click()
    location_code.clear()
    location_code.send_keys(PASSWORD_SEDE)
    
def is_login():    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="outputMessage"]')))
    message = driver.find_element_by_xpath('//*[@id="outputMessage"]')
    text = message.text
    if text == 'login':
        sede()
        print(text)
        sleep(1)
    elif text == 'login_true':
        sede()
        print('login_true')
        sleep(1)
    else:
        print(text)

i=1
while i == 1:
    sleep(1)
    is_login()