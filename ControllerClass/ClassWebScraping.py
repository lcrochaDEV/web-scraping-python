from selenium import webdriver;
from selenium.webdriver.common.by import By;
from datetime import datetime
import time as time
import re

class ControllerAPI:
	def __init__(self, site, url, caminho):
		self.site = site
		self.url = url
		self.caminho = caminho

	def varrerDados(self):
		try:
			#options = webdriver.ChromeOptions()
			#options.add_argument("--headless=new")
			#driver = webdriver.Chrome(options=options)
			driver = webdriver.Firefox()
			driver.get(f"{self.url}")
			driver.maximize_window() #ABRE COM A JENALA FULL
			driver.implicitly_wait(5) 
			#BARRA LATERAL AUTO SCROLL
			scroll = driver.execute_script('return document.body.scrollHeight')
			for contador in range(200):
				driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')
				time.sleep(2)
				new_scroll = driver.execute_script('return document.body.scrollHeight')
				if new_scroll == scroll:
					break
				scroll = new_scroll

			data_e_hora_atuais = datetime.now()
			data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y')
			print(f'{self.site} {data_e_hora_em_texto}')
			meuip = driver.find_element(By.XPATH, self.caminho)
			print(meuip.text)

		except:
			print(f'Sem acesso ao Site {self.site}')