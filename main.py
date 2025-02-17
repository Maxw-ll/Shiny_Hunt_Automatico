from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

import time
from management import *

driver.implicitly_wait(10)

time.sleep(1)

not_shiny = True


Resets = 0
Total_time = 0

arquivo = 'Resets_Charmander.txt'

arq = open(arquivo, 'r')
linhas = arq.readlines()
Resets = int(linhas[0])
Total_time = float(linhas[1])
arq.close()

while not_shiny:
    start = time.time()


    while verify_pixel_fast(Coords["Max_Pokebola_Coord"], Coords["Max_Pokebola_Pixel"]) == False:

        click(Coords["A"])
        #click_hold(Coords["A"])
    

    while verify_pixel_fast(Coords["Gary_Pokebola_Coord"], Coords["Gary_Pokebola_Pixel"]) == False:

        click(Coords["B"])
        #click_hold(Coords["B"])

    time.sleep(2.5)

    click(Coords["Start"])
    time.sleep(0.60)
    click(Coords["A"])
    time.sleep(0.60)
    click(Coords["A"])
    time.sleep(0.60)
    click(Coords["A"])
    time.sleep(2.5)

    if verify_pixel(Coords["Charmander_Coord"], Coords["Charmander_Pixel"]):
        make_reset()
        Resets += 1

    else:
        not_shiny = False
    
    print(f"Resets = {Resets}")

    print(f"Tempo Reset: {time.time() - start}")

    Total_time += time.time() - start

    arq = open(arquivo, 'w')
    arq.write(f"{Resets}\n")
    arq.write(f"{Total_time}")
    arq.close()


print(f"Shiny Encontrado! Com {Resets} Resets  e Tempo Total: {Total_time}")




