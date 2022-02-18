from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
navegador = webdriver.Chrome(chrome_options=chrome_options)

# Accessing the website
navegador.get('https://www.google.com'),
time.sleep(10),
# Writing Search Term
navegador.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('SEARCH TERM'),
time.sleep(2),
# Click Search
navegador.find_element(By.XPATH, '/ html / body / div[1] / div[3] / form / div[1] / div[1] / div[3] / center / input[1]').click(),
time.sleep(10),
webdriver.Chrome.quit(navegador)
