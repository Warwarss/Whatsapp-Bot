import time
import config
import csv
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# http://api.whatsapp.com/send?phone=xxxxxxxxxx yabancı numaralarla konuşabilmek için bunu kullan

global driver
global wait5

class Person:
    def __init__(self,name):
        self.name=name
    status=False
    online_time=""

def open_chat (name):    
        chat_value=f'//span[@title="{name}"]'
        wait5.until(EC.presence_of_element_located((By.XPATH,'//div[@contenteditable="true"][@data-tab="3"]'))).click
        search_box=driver.find_element(by=By.XPATH, value='//div[@contenteditable="true"][@data-tab="3"]')
        search_box.clear()
        search_box.click()
        search_box.send_keys(name)       
        wait5.until(EC.presence_of_element_located((By.XPATH,chat_value)))
        chat=driver.find_element(by=By.XPATH, value=chat_value)
        chat.click()
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        try:
            driver.find_element(by=By.XPATH, value='//span[@title="çevrimiçi"]')
        except:
            print(f"{name} is not online", current_time )
            if (d[name].status==True):
                d[name].status=False
                print(f"{name} went offline at", current_time,d[name].status)
                write_csv(name,current_time,d[name].online_time,d[name].status)

        else:
            print(f"{name} is online", current_time )
            if (d[name].status==False):
                d[name].status=True
                d[name].online_time=current_time
                print(f"{name} came online at", current_time)

def write_csv(name,current_time,online_time,status):
    with open(f'{name}.csv', mode='a',newline="") as _file:
        writer = csv.writer(_file, delimiter=',')
        writer.writerow([name,online_time,current_time])

PATH="C:\Program Files (x86)\Chromedriver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\Users\ACER\AppData\Local\Google\Chrome\User Data")
options.add_argument(r"--profile--directory=C:\Users\ACER\AppData\Local\Google\Chrome\User Data\Profile 1")
driver = webdriver.Chrome(PATH,chrome_options=options)
wait5=WebDriverWait(driver, 5)
driver.get("https://web.whatsapp.com")
time.sleep(10)
Array=config.Array
d={}
for name in Array:
   d[name]=Person(name)

while(1):
    for name in Array:
        open_chat(name)
