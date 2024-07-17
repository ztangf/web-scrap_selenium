import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


#Initialzation of Chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options= options, service=service)

url = "https://contratos.sistema.gov.br/transparencia/arp-item?palavra_chave=equipo&status=todos"
driver.get(url)

#tag = table;  class="table table-striped table-bordered dataTable no-footer"

r = driver.find_elements(By.CLASS_NAME, "dataTables_wrapper")
print(r)