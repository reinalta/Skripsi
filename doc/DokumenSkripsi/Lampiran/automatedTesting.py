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
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import * 
from tkinter import messagebox
import os


os.environ["PATH"] = os.getcwd()
print(os.environ["PATH"])

driver = webdriver.Chrome(ChromeDriverManager().install())


parser = ConfigParser()
parser.read('database.ini')

i = 1
while (i <= i):
    x = parser.get('database_config',str(i)).split()
    if  x[0] == "open" :
        driver.get(x[1]) 
        i += 1    
    elif x[0] == "click":
        try:
            elemen = WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, x[1])))
            if elemen.is_displayed() and elemen.is_enabled() :
                elemen.click()
        except TimeoutException:
                driver.quit()
                root = Tk()
                root.withdraw()
                a = "Absensi Gagal, Elemen tidak ditemukan:", x[1] 
                messagebox.showwarning("Warning", a)  
                break
        i+=1        
    elif x[0] == "sendkeys":
        inpt =  WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,x[1])))
        inpt.send_keys(x[2])        
        i += 1 
    elif x[0] =="or":
        try:
            elemen1 = driver.find_element(By.CSS_SELECTOR, x[1]) #jadwal
            elemen2 = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR,x[2]))) #notif
            if elemen2.is_displayed() and elemen2.is_enabled() :   
                elemen2.click()
                elemen1.click()         
        except TimeoutException:
                elemen1.click()
        i +=1
    elif x[0] == "quit":
        driver.wait(3)
        driver.quit()
        root = Tk()
        root.withdraw()
        messagebox.showinfo("Information", "Absen Berhasil")  
        break
         
