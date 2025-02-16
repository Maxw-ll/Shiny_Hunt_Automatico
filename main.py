from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time
from management import *

driver.implicitly_wait(10)

time.sleep(1)

not_shiny = True


Resets = 0

arquivo = 'Resets_Charmander.txt'

arq = open(arquivo, 'r')
Resets = int(arq.read())
arq.close()

while not_shiny:


    while verify_pixel(Coords["Max_Pokebola_Coord"], Coords["Max_Pokebola_Pixel"]) == False:

        click(Coords["A"])
        click_hold(Coords["A"])
    

    while verify_pixel(Coords["Gary_Pokebola_Coord"], Coords["Gary_Pokebola_Pixel"]) == False:

        click(Coords["B"])
        click_hold(Coords["B"])

    time.sleep(4.75)

    click(Coords["Start"])
    time.sleep(0.75)
    click(Coords["A"])
    time.sleep(0.75)
    click(Coords["A"])
    time.sleep(0.75)
    click(Coords["A"])
    time.sleep(2)

    if verify_pixel(Coords["Charmander_Coord"], Coords["Charmander_Pixel"]):
        make_reset()
        Resets += 1

        arq = open(arquivo, 'w')
        arq.write(f"{Resets}")
        arq.close()

    else:
        not_shiny = False
    
    print(f"Resets = {Resets}")

arq  = open(arquivo, 'w')
arq.write(f"Shiny  encontrado com {Resets} Resets")
print(f"Shiny Encontrado! Com {Resets} resets")
arq.close()



