from appium import webdriver  # Importa diretamente do appium
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from PIL import Image
import time

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
options.no_reset = True
options.full_reset = False

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)


# Aguarda o app carregar
time.sleep(4)
Wait = WebDriverWait(driver, 200)

pointer = PointerInput("touch", "finger")
Actions = ActionBuilder(driver,mouse=pointer)

screenshot_path = "pixel.png"

Coords = {
"Start": (977, 2050),
"Select": (825, 2050),
"A": (950, 2300),
"B" : (750, 2300),
"Max_Pokebola_Coord": (540, 380),
"Max_Pokebola_Pixel": (140, 190, 140, 255),
"Gary_Pokebola_Coord": (470, 380),
"Gary_Pokebola_Pixel": (140, 190, 140, 255),
"Up": (230, 2050),
"Down": (230, 2315),
"Right": (350, 2200),
"Left": (75, 2050),
"Charmander_Coord": (323, 340),
"Charmander_Pixel": (255, 146, 66, 255),
"Reset_label": (188, 1725),
"Menu": (540, 1770),
"Dialog_Coord": (1025, 715),
"Dialog_Pixel": (0,0,0,0)
}



def click(Coordenadas):
    # Realizar o toque
    Actions.pointer_action.move_to_location(Coordenadas[0], Coordenadas[1])
    Actions.pointer_action.pointer_down()
    Actions.pointer_action.pause(0.1)
    Actions.pointer_action.pointer_up()
    Actions.perform()
    #print(f"Click Efetuado na Coordenada ({Coordenadas[0]}, {Coordenadas[1]})")


def click_hold(Coordenadas):
    Actions.pointer_action.move_to_location(Coordenadas[0], Coordenadas[1])
    Actions.pointer_action.pointer_down()
    Actions.pointer_action.pause(1.50)
    Actions.pointer_action.pointer_up()
    Actions.perform()
    #print(f"Click Efetuado na Coordenada ({Coordenadas[0]}, {Coordenadas[1]})")


def make_reset():
    click(Coords["Menu"])
    click(Coords["Reset_label"])


def open_image(screenshot_path):
    image = Image.open(screenshot_path)
    return image
   
    
    

def verify_pixel(coordenadas, cor_esperada):
  
    driver.save_screenshot(screenshot_path)

    image = open_image(screenshot_path)

    rgb = image.getpixel(coordenadas)

    if(cor_esperada != rgb):
        return False

    return True

    

    

