from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import xlsxwriter
from tkinter import messagebox
import os
import time 


class Valores():
    def __init__(self):
        self.app = webdriver.Chrome()
        self.dolar:str
        self.euro:str
        self.euro_pega()
        
    def dolar_get(self):
        self.app.get('https://www.google.com')

        pesquisa = self.app.find_element(By.NAME, 'q')
        pesquisa.send_keys('dolar hoje')
        pesquisa.send_keys(Keys.ENTER)
        time.sleep(1)
        self.dolar = self.app.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
        print(self.dolar)
        


    def euro_pega(self):
        self.app.get('https://www.google.com')
        
        pesquisa = self.app.find_element(By.NAME, 'q')
        pesquisa.send_keys('euro hoje')
        pesquisa.send_keys(Keys.ENTER)
        time.sleep(1)
        self.euro = self.app.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text
        print(self.euro)
        
        time.sleep(2)
        self.dolar_get()
        #aqui cria o excel e salva os dados que foi pego no google
        workbook = xlsxwriter.Workbook('cotação.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Euro')
        worksheet.write('B1', 'Dolar')
        worksheet.write(1, 0, self.euro)
        worksheet.write(1, 1, self.dolar)
        workbook.close()
        messagebox.showinfo("Finalizado ","Cotação com sucesso")
     
        self.app.quit()

Valores()


