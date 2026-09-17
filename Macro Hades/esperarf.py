import time
import hotkey
import keyboard
import time

# Função de esperar e verificar
def esperar(duracao):
    tempo_passado = 0
    while tempo_passado < duracao and hotkey.macro_ligado:
        if keyboard.is_pressed('f8'):
            hotkey.macro_ligado = False

            duracao_segundos = time.time() - hotkey.tempo_inicio
            duracao_formatada = time.strftime('%H:%M:%S', time.gmtime(duracao_segundos))
            hotkey.log(f"Macro Finalizado! Rodou {hotkey.total_ciclos} vezes em {duracao_formatada}.", cor="green")

        time.sleep(0.1)
        tempo_passado += 0.1