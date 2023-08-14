import time
import selenium
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager

s = Service('C:\\Python311\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("http://checkip.dyndns.org/")

driver.maximize_window()
#time.sleep(5000)
ip_message = driver.find_element("xpath", "/html/body").text
print(ip_message.strip('Current IP Address: '))

try:
    file = open("C:\\Python311\\_external_IP_.txt", "w")
except:
    file = open("C:\\Python311\\_external_IP_.txt", "w+")

file.write(ip_message.strip('Current IP Address: '))


#time.sleep(5000)


