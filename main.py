from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time
from management import *






botao_skip = connect_button("//android.widget.Button[@resource-id='android:id/button2']")
botao_select_folder = connect_button("//android.widget.Button[@resource-id='android:id/button3']")
botao_skip.click()



selecionar_pokemon = connect_button("//android.widget.TextView[@resource-id='android:id/text1']")










### APLICATIVO MEU SUS DIGITAL
'''

permission_button = connect_button("//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']")
permission_button.click()

botao_entrar    =  connect_button("//android.widget.Button[@text='Entrar com o Gov.br']")
botao_entrar.click()

ui_cpf= connect_button("//android.widget.EditText")

ui_cpf.clear()
ui_cpf.send_keys(formatar_cpf(cpf))
# Tempo máximo de espera
timeout = 20
start_time = time.time()

while time.time() - start_time < timeout:
cpf_value = ui_cpf.get_attribute("text")
if cpf_value == formatar_cpf(cpf):  # Confirma se o texto foi inserido corretamente
print("✅ CPF inserido com sucesso!")
break

time.sleep(0.5)  # Pequena espera antes de tentar de novo

if(ui_cpf.get_attribute("text") == formatar_cpf(cpf) ):

botao_continuar = connect_button("//android.widget.Button[@text='Continuar']")
botao_continuar.click()


start_time = time.time()
time.sleep(5)

ui_senha = connect_button('//android.widget.EditText')
ui_senha.send_keys(senha)

botao_entrar = connect_button("//android.widget.Button[@text='Botão Entrar. Aperte a tecla enter para entrar.']")
botao_entrar.click()

time.sleep(10)

#Colocar aqui os proximos passos aqui
#Cada clique e com sua coordenada


navegar_meu_diario()

print("Testando Pressão - CT05_03")
selecionar_pressao()
cadastrar_pressao("1000", "8", "02022025")

print("Testando Pressão - CT05_06")
selecionar_pressao()
cadastrar_pressao("12", "8", "02022025")

print("Testando Glicose - CT06_01")
selecionar_glicose()
cadastrar_glicose("1000", "20052025")

print("Testando Glicose - CT06_04")
selecionar_glicose()
cadastrar_glicose("70", "02022025")
'''