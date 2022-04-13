import os
import time
import datetime
import sys
reload(sys) 
sys.setdefaultencoding("utf-8")
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# http://api.whatsapp.com/send?phone=xxxxxxxxxx yabancı numaralarla konuşabilmek için bunu kullan

global driver
global wait5
def send_message_to (name,message):    
        chat_value=f'//span[@title="{name}"]'
        search_box=wait5.until(EC.presence_of_element_located((By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]')))
        search_box.clear()
        search_box.click()
        search_box.send_keys(name)
        time.sleep(3)
        chat=driver.find_element(by=By.XPATH, value=chat_value)
        time.sleep(1)
        chat.click()
        chat_box='//div[@title="Schreib eine Nachricht"]'
        for i in range(25):
            chat_box.click()
            chat_box.send_keys(message)
            chat_box.send_keys(Keys.RETURN)

PATH="C:\Program Files (x86)\Chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\ACER\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile--directory=C:\Users\ACER\AppData\Local\Google\Chrome\User Data\Profile 1")
driver = webdriver.Chrome(PATH,chrome_options=options)
wait5=WebDriverWait(driver, 5)
driver.get("https://web.whatsapp.com")
send_message_to("kızılbaş" .encode("unicode"),"Allah")
search_box=wait5.until(EC.presence_of_element_located((By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]')))
search_box.clear()
search_box.click()
search_box.send_keys(Contact)
time.sleep(5)
chat=driver.find_element(by=By.XPATH, value='//span[@title="illegal ama kutsal"]')
time.sleep(1)
chat.click()
time.sleep(1)
chat_box=driver.find_element(by=By.XPATH, value='//div[@title="Schreib eine Nachricht"]')
for i in range(25):
    chat_box.click()
    chat_box.send_keys("Allah")
    chat_box.send_keys(Keys.RETURN)

time.sleep(10)
