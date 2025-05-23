#Teste 03
# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 🚀 Inicializa o navegador (Chrome)
driver = webdriver.Chrome()  # Certifique-se de que o chromedriver está no PATH

# 🌐 Acessa o site do Google
driver.get("https://www.google.com")

# 💤 Aguarda alguns segundos para garantir o carregamento da página
time.sleep(2)

# 🔍 Encontra a barra de pesquisa pelo nome do elemento
barra_pesquisa = driver.find_element(By.NAME, "q")

# ⌨️ Digita o termo de busca e envia
barra_pesquisa.send_keys("Quality Assurance")
barra_pesquisa.send_keys(Keys.RETURN)

# 💤 Aguarda os resultados carregarem
time.sleep(3)

# 📋 Pega o título da primeira página de resultados
print("Título da página:", driver.title)

# ❌ Fecha o navegador
driver.quit()
