from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

navegador = webdriver.Chrome()
navegador.get(r'file:///C:/Users/Alan/Downloads/Arquivos-20220419T045228Z-001/Arquivos/formulario.html')

# Botão Padrão (Clicar em botão)
navegador.find_element(By.XPATH, '/html/body/form/input[1]').click()
# Clicar aceitar ou recusar popup de alerta
alerta = navegador.switch_to.alert # Mudar para Alerta
alerta.accept() # Aceitar caixinhas de Pop-up

# Dica: Atento ao atributo "value" dos inputs, pode ajudar

navegador.find_element(By.XPATH, '/html/body/form/input[2]').click()
# is_select -> Responder se a caixinha ou opção está selecionada
selecionado = navegador.find_element(By.XPATH, '/html/body/form/input[2]').is_selected()
print(selecionado)

# Preenchendo a coluna de cor
navegador.find_element(By.XPATH, '/html/body/form/input[4]').send_keys("#9289B8")
# Pegando valor da caixinha de cor
caixa_cor = navegador.find_element(By.XPATH ,'/html/body/form/input[4]').get_attribute('value')

# Preenchendo campo cor:
navegador.find_element(By.XPATH, '/html/body/form/input[5]').send_keys("#2143E8")

# Preenchendo campo data:
navegador.find_element(By.XPATH, '/html/body/form/input[6]').send_keys('11/11/2002')

# Preenchendo a coluna de data e horas, usando a função Keys do teclado para dar TAB e depois preencher as horas
navegador.find_element(By.XPATH, '/html/body/form/input[7]').send_keys('11/11/2002', Keys.TAB, '10:30')

# Anexando arquivo
navegador.find_element(By.XPATH, '/html/body/form/input[8]').send_keys(r'C:\Users\Alan\Downloads\Material Completo de Fundamentos de Redes.pdf')

# Preenchendo campo Mês e Ano:
navegador.find_element(By.XPATH, '/html/body/form/input[9]').send_keys('11', Keys.TAB, '2002')

# Preenchendo campo numéricos:
navegador.find_element(By.XPATH, '/html/body/form/input[10]').send_keys('19')

# Preenchendo campo senha:
navegador.find_element(By.XPATH, '/html/body/form/input[11]').send_keys('alan123')

# Preenchendo campo radio buttons:
navegador.find_element(By.XPATH, '/html/body/form/input[13]').click()

# Preenchendo campo time:
navegador.find_element(By.XPATH, '/html/body/form/input[16]').send_keys('Barcelona')

# Preenchendo campo horas:
navegador.find_element(By.XPATH, '/html/body/form/input[17]').send_keys('21:18')

# Preenchendo campo semana e horas:
navegador.find_element(By.XPATH, '/html/body/form/input[18]').send_keys('1','2120')

# Preenchendo o campo texto e usando clear depois
navegador.find_element(By.XPATH, '//*[@id="story"]').send_keys('Olá seres humanos!', Keys.ENTER, 'Alan quem vós fala...', Keys.ENTER, 'Hehehehe')
sleep(2)
navegador.find_element(By.XPATH, '//*[@id="story"]').clear()

# Preenchendo campo de arrastar
# Pegando o valor que está
valor = navegador.find_element(By.XPATH, '/html/body/form/input[15]').get_attribute('value')
print(valor)

#Limpando o valor
elemento = navegador.find_element(By.XPATH, '/html/body/form/input[15]')
elemento.clear()

# Colocando o valor desejado com o for e setinha do teclado
for i in range(70-50):
    elemento.send_keys(Keys.ARROW_RIGHT)

# Coluna clicando para selecionar:
# 1. Opção: Enivando o valor da coluna no send_keys
navegador.find_element(By.XPATH,"/html/body/form/select[1]").send_keys('C')


# 2. Opção: Clicando na coluna e clicando na opção de escolha (B)
navegador.find_element(By.XPATH,"/html/body/form/select[1]").click()
sleep(0.5)

navegador.find_element(By.XPATH, '/html/body/form/select[1]/option[2]').click()
sleep(1)

# Selecionar com Select
elemento2 = navegador.find_element(By.TAG_NAME, 'select')
elemento2_select = Select(elemento2)
elemento2_select.select_by_visible_text('C') # Selecionando o valor C pelo texto visivel
# elemento2_select.select_by_value('c') Selecionando pelo valor do html

# Formas de desselecionar elemento:

# elemento2_select.deselect_all() # Desselecionar todos elementos  
# elemento2_select.deselect_by_index('0')  Desselecionar pelo indice
# elemento2_select.deselect_by_visible_text('C') Pelo texto que está visivel
# elemento2_select.deselect_by_value('c') Pelo valor do html

# Verificar se é elemento multiplo, selecionar varias opções
print(elemento2_select.is_multiple)

# Ler o item selecionado:
item = elemento2_select.first_selected_option # Pegando a primeira opção para seleção

lista_itens = elemento2_select.all_selected_options # Pegando uma lista com várias opções de seleção
print(lista_itens[0].get_attribute('value')) # Vendo o primeiro elemento da lista de elementos
print(lista_itens[0].text) # Pegando apenas o texto



sleep(30)
