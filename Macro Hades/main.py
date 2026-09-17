import hotkey
import time
import threading
from script import statemachine
from interface import criar_interface

def rodar_macro():
    while True:
        if hotkey.macro_ligado:
            statemachine()
        time.sleep(0.1)

thread_macro = threading.Thread(target=rodar_macro, daemon=True)
thread_macro.start()

criar_interface()