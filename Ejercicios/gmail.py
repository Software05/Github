#pip install selenium
#importing modules
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#Abrimos el navegador
driver = webdriver.Chrome()

#Maximizamos la pantalla
driver.maximize_window()

#Borramos las cookies
dirver.delete_all_cookies()

#Navegamos a la URL
driver.get("https://www.gmail.com/")

#Identificacion el usuario del correo
driver.find_element_by_id("identifierID").send_keys("andreslalo28@gmail.com")
time.sleep(2)

#Click en el boton continuar
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]').click()

#Identificacion de la clave
driver.find_element_by_name("password").send_keys("simonandres")
time.sleep(3)

#Click en continuar
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]').click()
time.sleep(3)

#Cerrar el navegador
driver.close()
print("Se a logueado correctamente")
