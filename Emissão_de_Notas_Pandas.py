"""
---- PASSO A PASSO: ----

1. Fazer login no site (Selenium)
2. Pegar todos XPATH e criar várival
3. Abrir a planilha (Pandas)
4. Separar as informações e percorrer cada uma dela
5. Preencher cada campo com as informações da planilha
6. Emitir a nota
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# Configurando para caso tenha notificação de manter download ou descartar
# Linhas de códigos para permitir
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
  "download.default_directory": r"C:\Users\Alan\Downloads",
  "download.prompt_for_download": False,
  "download.directory_upgrade": True,
  "safebrowsing.enabled": True
})

navegador = webdriver.Chrome(options=options)
navegador.get(r'C:\Users\Alan\Downloads\Arquivos-20220419T044739Z-001\Arquivos\login.html')

# Pegando informações dos campos:
login = navegador.find_element(By.XPATH, '/html/body/div/form/input[1]')
login.send_keys('corporativo@gmail.com')
sleep(0.5)

senha = navegador.find_element(By.XPATH, '/html/body/div/form/input[2]')
senha.send_keys('senha123')
sleep(0.5)

botao_login = navegador.find_element(By.XPATH, '/html/body/div/form/button')
botao_login.click()
sleep(0.5)


tabela = pd.read_excel('NotasEmitir.xlsx') # Abrindo planilha

for linha in tabela.index: # Percorrendo o indice, que é linha da tabela
    # Usando o loc[], identificando a linha e pegando os valores da coluna
    navegador.find_element(By.XPATH,'//*[@id="nome"]').send_keys(tabela.loc[linha, 'Cliente'])
    navegador.find_element(By.XPATH, '//input[@name="endereco"]').send_keys(tabela.loc[linha, 'Endereço'])
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[3]').send_keys(tabela.loc[linha, 'Bairro'])
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[4]').send_keys(tabela.loc[linha, 'Municipio'])
    navegador.find_element(By.XPATH,'//*[@id="formulario"]/input[5]').send_keys(str(tabela.loc[linha, 'CEP']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/select').send_keys(tabela.loc[linha, 'UF'])
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[6]').send_keys(str(tabela.loc[linha, 'CPF/CNPJ']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[7]').send_keys(str(tabela.loc[linha, 'Inscricao Estadual']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[8]').send_keys(tabela.loc[linha, 'Descrição'])
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[9]').send_keys(str(tabela.loc[linha, 'Quantidade']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[10]').send_keys(str(tabela.loc[linha, 'Valor Unitario']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/input[11]').send_keys(str(tabela.loc[linha, 'Valor Total']))
    navegador.find_element(By.XPATH, '//*[@id="formulario"]/button').click()
    sleep(1)
    navegador.refresh() # Atualizar a página

navegador.quit()
sleep(30)
