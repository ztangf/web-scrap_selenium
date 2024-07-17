import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialzation of Chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=service)

url = "https://contratos.sistema.gov.br/transparencia/arp-item?palavra_chave=equipo&status=todos"
driver.get(url)

# Wait for the table to load
table = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "dataTables_wrapper"))
)

# Get the HTML of the page
html = driver.page_source