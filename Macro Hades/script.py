from acoes import segurar_teclas
from acoes import spam_teclas
from acoes import press_detec
from acoes import espe_detec
from detector import detectarbase
from acoes import esperar_morrer
from esperarf import esperar
import pyautogui
import hotkey
import time

pyautogui.PAUSE = 0

def statemachine():
    # Respawn e falar com o Hipnos
    espe_detec([r"Prints Jogo\Print 2 - piscina de estige.png", r"Prints Jogo\Print 2 - texto a casa de hades.png"])
    esperar(0.1)
    if not hotkey.macro_ligado:
        return
    hotkey.log("Indo até o Hipnos...")

    segurar_teclas(['w', 'd'], 2.20)
    esperar(0.1)
    if not hotkey.macro_ligado:
            return
    tem_missao, _ = detectarbase(r"Prints Jogo\Print 3 - Icone de missao.png")

    if tem_missao:
        duracao_segundos = time.time() - hotkey.tempo_inicio
        duracao_formatada = time.strftime('%H:%M:%S', time.gmtime(duracao_segundos))
        hotkey.log(f"🎉 DIÁLOGO DE MISSÃO LIBERADO! Macro rodou {hotkey.total_ciclos} vezes em {duracao_formatada}.", cor="green")
        hotkey.macro_ligado = False   # para o macro
  
    segurar_teclas(['q'], 0.1)
    esperar(1)
    if not hotkey.macro_ligado:
            return
    spam_teclas('enter', 10)

    hotkey.log("Dialogo concluido, indo até a sala de armas")

    # Indo até a sala de armas
    esperar(1)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['w', 'd'], 1.4)
    esperar(1)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['s', 'd'], 3.4)
    esperar(1)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['w', 'd'], 6)
    esperar(4)
    if not hotkey.macro_ligado:
            return
    hotkey.log("Indo para o pacto...")

    #Iniciando run
    segurar_teclas(['w', 'd'], 0.5)
    esperar(1)
    if not hotkey.macro_ligado:
            return
    press_detec(['s', 'd'], [r"Prints Jogo\Print 4 - Icone de preparar-se.png"])
    esperar(0.1)
    if not hotkey.macro_ligado:
            return

    hotkey.log("Iniciando run...")
    segurar_teclas(['q'], 0.1)
    esperar(1.5)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['enter'], 0.1)

    # Escolher a benção
    hotkey.log("Esperando a run iniciar...")
    espe_detec([r"Prints Jogo\Print 5 - Porta Hades.png", r"Prints Jogo\Print 5 - Estatua sala 1.png"])
    esperar(0.1)
    if not hotkey.macro_ligado:
            return
    hotkey.log("Run iniciada, indo escolher a benção...")

    segurar_teclas(['s', 'd'], 1.45)
    esperar(1)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['w', 'd'], 0.55)
    esperar(1)
    if not hotkey.macro_ligado:
            return

    eh_martelo, _ = detectarbase(r"Prints Jogo\Print 6 - Icone de aprimorar.png")

    if eh_martelo:
        hotkey.log("Martelo detectado, escolhendo aprimoramento...")
        segurar_teclas(['q'], 0.1)
        esperar(2)
        if not hotkey.macro_ligado:
                return
        pyautogui.moveTo(960, 540)
        esperar(0.1)
        if not hotkey.macro_ligado:
                return
        segurar_teclas(['space'], 0.1)
        hotkey.log("Escolha de aprimoramento concluido, preparando pra se matar")

    else:
        hotkey.log("Benção detectada, escolhendo benção...")
        segurar_teclas(['q'], 0.1)
        esperar(3)
        if not hotkey.macro_ligado:
                return
        segurar_teclas(['space'], 0.1)
        esperar(2)
        if not hotkey.macro_ligado:
                return
        pyautogui.moveTo(960, 540)
        esperar(0.1)
        if not hotkey.macro_ligado:
                return
        segurar_teclas(['space'], 0.1)
        hotkey.log("Escolha de benção concluida, preparando pra se matar")


    # Se matar e renascer
    esperar(1.5)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['w', 'a'], 0.50)
    esperar(0.1)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['w', 'd'], 2.70)
    esperar(0.1)
    if not hotkey.macro_ligado:
            return
    segurar_teclas(['s', 'd'], 0.40)

    hotkey.log("Esperando se matar...")
    esperar(5)
    if not hotkey.macro_ligado:
            return
    esperar_morrer(r"Prints Jogo\Print 1 - Nao ha escapatoria.png")
    hotkey.log("Morte detectada, renascendo...")

    hotkey.total_ciclos += 1
    hotkey.log(f"Ciclo completo ({hotkey.total_ciclos})", cor="green")


