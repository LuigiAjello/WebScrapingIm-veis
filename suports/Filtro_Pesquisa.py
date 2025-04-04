from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd

'''' @NOTE

Só foi possivel escrever assim pois o código seguia um padrão 
    Por exemplo o = "select2-search__field" que estava em todos os filtros de -> add_filtro_digitavel_e_selecionavel

'''
class Filtro_pesquisa:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def add_filtro_digitavel_e_selecionavel(self, xpath , key_selecionada):
        try:
            element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            element.click()
            element = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "select2-search__field")))
            element.send_keys(key_selecionada)
            element.send_keys(Keys.ENTER)
            sleep(1)
        except Exception as e:
            print(f"Erro ao aplicar filtro: {e}")


    def add_filtro_somente_selecionavel(self, xpath , key_selecionada):
        
        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()  
        sleep(1)       
        quartos = self.wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "select2-results__option")))


        for item in quartos:
            texto = item.text.strip()  # Obter o texto do elemento

            # Se a opção já está selecionada, sair do loop
            if key_selecionada == "Todos os quartos" and texto == "Todos os quartos":
                print("Já está selecionado, continuando...")
                break

            # Caso seja um número válido, converte para inteiro e compara
            elif texto.isdigit() and int(texto) == key_selecionada:
                print(f"Selecionando {key_selecionada} quartos")
                item.click()
                break  # Sai do loop após a seleção

            # Caso seja "5 ou +" ou "5 OU MAIS"
            elif key_selecionada == "5 ou +" and ("5" in texto or "5 OU MAIS" in texto):
                print(f"Selecionando a opção '{texto}'")
                item.click()
                break

    def add_filtro_somente_digitavel(self, xpath , key_selecionada):

        element = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.send_keys(key_selecionada)
        '''@NOTE 

        Se apertar enter apos o endereco ele da enter em todos os filtros

        #element.send_keys(Keys.ENTER)

        '''
        sleep(1)
    
    
    



