from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os
import zipfile
import requests
import time

ANEXOS = r"C:\Users\guilh\OneDrive\Documents\Teste IntuitiveCare\Anexos"

def baixar_arquivos():
    if not os.path.exists(ANEXOS):
        os.makedirs(ANEXOS)
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    try:
        driver.get("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos")
        time.sleep(5)  

        linksInfo = []
        for link in driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf')]"):
            nomeArquivoPagina = link.text
            url = link.get_attribute('href')
            if "Anexo I" in nomeArquivoPagina or "Anexo II" in nomeArquivoPagina:
                linksInfo.append((nomeArquivoPagina, url))
        
        for nomeArquivoPagina, url in linksInfo:
            if url:
                response = requests.get(url)
                if response.status_code == 200:
                    nomeArquivoSalvo = url.split('/')[-1]
                    with open(os.path.join(ANEXOS, nomeArquivoSalvo), 'wb') as f:
                        f.write(response.content)
    finally:
        driver.quit()

def compactar_arquivos():
    with zipfile.ZipFile(os.path.join(ANEXOS, "Anexos.zip"), 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arquivo in os.listdir(ANEXOS):
            if arquivo.endswith(".pdf"):
                zipf.write(os.path.join(ANEXOS, arquivo), arquivo)

if __name__ == "__main__":
    baixar_arquivos()
    compactar_arquivos()