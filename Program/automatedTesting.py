# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 11:35:40 2022

@author: user
"""
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path='D:\Kuliah\Skripsi\Prasyarat\python\chromedriver.exe')
parser = ConfigParser()
parser.read('database.config')

i = 1
while (i <= i):
    x = parser.get('database_config',str(i)).split()
    if  x[0] == "open" :
        driver.get(x[1]) 
    elif x[0] == "click":
        driver.find_element(By.CSS_SELECTOR, x[1]).click()
    elif x[0] == "sendkeys":
        inpt =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,x[1])))
        inpt.send_keys(x[2])           
    i += 1        

