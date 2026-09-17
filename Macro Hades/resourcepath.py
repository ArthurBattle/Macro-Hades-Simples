import sys
import os

def resource_path(caminho_relativo):
    """Retorna o caminho absoluto do recurso, funcionando tanto
    rodando via script quanto empacotado pelo PyInstaller."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, caminho_relativo)