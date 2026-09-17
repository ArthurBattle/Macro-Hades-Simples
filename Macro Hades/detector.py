import pyautogui
import cv2
import numpy as np
from resourcepath import resource_path

pyautogui.PAUSE = 0

def detectarbase(caminho_referencia, confianca=0.8):
    tela = pyautogui.screenshot()
    tela = cv2.cvtColor(np.array(tela), cv2.COLOR_RGB2BGR)

    referencia = cv2.imdecode(np.fromfile(resource_path(caminho_referencia), dtype=np.uint8), cv2.IMREAD_COLOR)

    resultado = cv2.matchTemplate(tela, referencia, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= confianca:
        return True, max_loc
    return False, None


def detectar(caminhos_referencia, confianca=0.8):
    for caminho in caminhos_referencia:
        achou, posicao = detectarbase(caminho, confianca)
        if achou:
            return True, posicao
    return False, None
    
