import pyautogui
from detector import detectarbase
from detector import detectar
from esperarf import esperar
import hotkey
import time
import random

pyautogui.PAUSE = 0

# Função para segurar teclas por um determinado tempo
def segurar_teclas(teclas, duracao):
    for tecla in teclas:
        pyautogui.keyDown(tecla)

    esperar(duracao)

    for tecla in teclas:
        pyautogui.keyUp(tecla)


# Função para spam de teclas
def spam_teclas(tecla, vezes):
    for i in range(vezes):
        segurar_teclas([tecla],0.1)
        esperar(0.2)
    hotkey.log("Spam de teclas concluído")


# Função para pressionar teclas até detectar uma imagem
def press_detec(teclas, caminhos_referencia):
    achou, _ = detectar(caminhos_referencia)
    for tecla in teclas:    
        pyautogui.keyDown(tecla)
    
    while not achou:
        achou, _ = detectar(caminhos_referencia)
        esperar(0.03)

    for tecla in teclas:    
            pyautogui.keyUp(tecla)
    hotkey.log("Imagem detectada")


# Função para esperar até detectar uma imagem
def espe_detec(caminhos_referencia):
    achou, _ = detectar(caminhos_referencia)

    while not achou:
        achou, _ = detectar(caminhos_referencia)
        esperar(0.1)
    
    hotkey.log("Imagem detectada")


# Função de esperar morrer
def esperar_morrer(caminho_referencia):
    achou, _ = detectarbase(caminho_referencia)
    
    while not achou:
        direcao = random.choice([['w','a'], ['w','d'], ['s','a'], ['s','d'], ['w'], ['a'], ['s'], ['d']])
        segurar_teclas(direcao, 0.5)
        achou, _ = detectarbase(caminho_referencia)
        
        # ao invés de sleep(5) de uma vez, fatia em pedacinhos de 0.2s,
        # verificando a cada pedaço
        tempo_esperado = 0
        while tempo_esperado < 5 and not achou:
            esperar(0.2)
            tempo_esperado += 0.2
            achou, _ = detectarbase(caminho_referencia)
