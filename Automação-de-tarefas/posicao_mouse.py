#para pegar a posição dos campos no seu cumputador, rode esse programa no vs e coloque em cima do 
#local de email , esse programa pegará a coordenada do mause depois de 5 segundos então pegue as coordenadas no terminal. faça o mesmo para as outras coordenadas no código.
import time
import pyautogui

time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(200)


