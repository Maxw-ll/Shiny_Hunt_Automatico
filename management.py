from appium import webdriver  # Importa diretamente do appium
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from PIL import Image
import time
import os


senha="Coloque_sua_senha_aqui"
cpf="coloque_seu_cpf como string"

def formatar_cpf(cpf: str) -> str:
    """Formata um CPF de uma sequência numérica para o padrão XXX.XXX.XXX-XX"""
    cpf = cpf.zfill(11)  # Garante que tenha 11 dígitos
    return f"{cpf[:3]},{cpf[3:6]},{cpf[6:9]}-{cpf[9:]}"

# Configuração do Appium para Android 14 no dispostivo física RedmiNote13
options = UiAutomator2Options()
options.platform_name = "Android"
options.device_name = "31444565"
options.app = "M:\\Shiny_Hunt_Automatico\\MyBoy.apk"
options.automation_name = "UiAutomator2"

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Aguarda o app carregar
time.sleep(5)
Wait = WebDriverWait(driver, 200)

pointer = PointerInput("touch", "finger")
Actions = ActionBuilder(driver,mouse=pointer)



def connect_button(Xpath: str):
    return Wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, Xpath)))


def cores_sao_semelhantes(rgb1, rgb2, tolerancia=10):
    return all(abs(c1 - c2) <= tolerancia for c1, c2 in zip(rgb1, rgb2))


def click(x, y):
    # Realizar o toque
    Actions.pointer_action.move_to_location(x, y)
    Actions.pointer_action.pointer_down()
    Actions.pointer_action.pause(0.1)
    Actions.pointer_action.pointer_up()
    Actions.perform()
    print(f"Click Efetuado na Coordenada ({x}, {y})")

def delete_card(x, y):
    
    click(x, y)
    time.sleep(4)
    #Botão de Excluir
    click(115, 2010)
    time.sleep(4)
    #Botão de Sim (Confirmar)
    click(820, 1440)
    time.sleep(4)


def verify_error():

    time.sleep(5)
    screenshot_path = "screenshot.png"
    driver.save_screenshot(screenshot_path)
    time.sleep(1)
    image = Image.open(screenshot_path)
    
    #Coordenadas de onde o primeiro card é adicionada nas abas de Pressão, Glicemia e IMC
    x, y = 725, 1035  

    # Pega a cor do pixel (RGB)
    rgb = image.getpixel((x, y))
    branco = (255,255,255)

    if(not(cores_sao_semelhantes(rgb, branco))):
        delete_card(x, y)
        os.remove(screenshot_path)
        time.sleep(1)
        return False
    else:
        os.remove(screenshot_path)
        time.sleep(1)
        return True

    
    

def navegar_meu_diario():

    #Sair das Mensagens Iniciais
    time.sleep(2)
    click(540, 420)
    time.sleep(2)
    click(540, 420)
    time.sleep(2)

    #CLicar em "Ver Tudo"
    click(500, 1380)
    time.sleep(2)
    #Clique em Diário de Saúde
    click(868, 1228)
    time.sleep(8)



def selecionar_IMC():
    time.sleep(2)
    click(950, 445)
    time.sleep(2)

def selecionar_pressao():
    time.sleep(2)
    click(420,445)
    time.sleep(2)

def selecionar_glicose():
    time.sleep(2)
    click(700, 445)
    time.sleep(2)

def cadastrar_click():
    click(260, 980)
    time.sleep(2)


Botoes_Numeros = {
    
    '1': (130, 1770),
    '2': (400, 1770),
    '3': (650, 1770),
    '4': (130, 1900),
    '5': (400, 1900),
    '6': (650, 1900),
    '7': (130, 2050),
    '8': (400, 2050),
    '9': (650, 2050),
    '0': (400, 2200),
}


def escrever_valor(valor: str):
    

    for k in valor:
        time.sleep(0.5)
        click(Botoes_Numeros[k][0], Botoes_Numeros[k][1]) #Clicar em cada Numero
        time.sleep(0.5)
    
    time.sleep(1)
    click(755, 1555)#Clicar em Confirmar
    time.sleep(1)


def cadastrar_pressao(pressao_max, pressao_min, data):
    cadastrar_click()
    click(175,1410)  # Pressão Maxima
    time.sleep(1)
    escrever_valor(pressao_max)
    time.sleep(1)
    
    click(175,1650) 
    time.sleep(1)
    escrever_valor(pressao_min)
    time.sleep(1)# Pressão Mínima

    click(175, 1900)
    time.sleep(1)
    click(175, 1100) #Clicar no campo de Data para digitar
    escrever_valor(data)
    time.sleep(1) # Data

    time.sleep(1)
    click(700, 2250)
    time.sleep(5)

    if(verify_error() == False):
        print()
        print("✅ Pressão Cadastrada com Sucesso!")
        print()
    else:
        print()
        print("❌ Erro! Pressão Não Cadastrada!")
        print()
    
    time.sleep(2)

    


def formatar_cpf(cpf: str) -> str:
    """Formata um CPF de uma sequência numérica para o padrão XXX.XXX.XXX-XX"""
    cpf = cpf.zfill(11)  # Garante que tenha 11 dígitos
    return f"{cpf[:3]},{cpf[3:6]},{cpf[6:9]}-{cpf[9:]}"

def cadastrar_glicose(glicose, data):
    cadastrar_click()
    time.sleep(1)
    click(175, 1470) # Click digitar glicose
    time.sleep(1)
    escrever_valor(glicose)
    time.sleep(1)
    
    click(175, 1700)
    time.sleep(1)
    click(175, 1100) #Clicar no campo de Data para digitar
    escrever_valor(data)
    time.sleep(1) 

    time.sleep(1)
    click(700, 2250)
    time.sleep(5)

    if(verify_error() == False):
        print("✅ Glicose Cadastrada com Sucesso!")
    else:
        print("❌ Erro! Glicose Não Cadastrada!")
    
    time.sleep(2)