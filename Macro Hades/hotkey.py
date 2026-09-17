import keyboard
import time

macro_ligado = False
total_ciclos = 0
tempo_inicio = None

def alternar_macro():
    global macro_ligado, tempo_inicio
    macro_ligado = not macro_ligado

    if macro_ligado:
        tempo_inicio = time.time()
        log("Macro Iniciado!")
    else:
        duracao_segundos = time.time() - tempo_inicio
        duracao_formatada = time.strftime("%H:%M:%S", time.gmtime(duracao_segundos))
        log(f"Macro Finalizado! Rodou {total_ciclos} vezes em {duracao_formatada}.", cor="green")

keyboard.add_hotkey('f8', alternar_macro)

mensagens_pendentes = []

def log(mensagem, cor="white"):
    mensagens_pendentes.append((mensagem, cor))