import customtkinter as ctk
import hotkey
import time
from PIL import Image
from resourcepath import resource_path

def criar_interface():
    app = ctk.CTk()
    app.title("Macro Hades")
    app.geometry("600x500")

    titulo_frame = ctk.CTkFrame(app, fg_color="transparent")
    titulo_frame.pack(pady=(0,20))

    macro_label = ctk.CTkLabel(titulo_frame, text="Macro ", font=("Bahnschrift SemiBold", 60), text_color="white")
    macro_label.pack(side="left", padx=0)

    logo_imagem = Image.open(resource_path("Logo hades\Logo Hades.png"))
    logo_ctk = ctk.CTkImage(light_image=logo_imagem, dark_image=logo_imagem, size=(300, 100))

    logo_label = ctk.CTkLabel(titulo_frame, image=logo_ctk, text="")
    logo_label.pack(side="left", pady=(30,0), padx=0)

    instrucao_label = ctk.CTkLabel(app, text="Aperte F8 para ligar/desligar o macro...", font=("Bahnschrift", 18), text_color="Green")
    instrucao_label.pack(pady=(5,20))

    status_label = ctk.CTkLabel(app, text="Desligado", font=("Bahnschrift", 24), text_color="red")
    status_label.pack(pady=5)

    ciclos_label = ctk.CTkLabel(app, text="Ciclos: 0", font=("Bahnschrift", 16))
    ciclos_label.pack(pady=2)

    tempo_label = ctk.CTkLabel(app, text="Tempo: 00:00:00", font=("Bahnschrift", 16))
    tempo_label.pack(pady=2)

    log_textbox = ctk.CTkTextbox(app, width=550, height=200)
    log_textbox.pack(pady=10)

    log_textbox.tag_config("green", foreground="#00FF00")
    log_textbox.tag_config("white", foreground="#FFFFFF")

    def adicionar_log(mensagem):
        log_textbox.insert("end", mensagem + "\n")
        log_textbox.see("end")

    def atualizar_tela():
        if hotkey.macro_ligado:
            status_label.configure(text="Ligado", text_color="green")
            duracao = time.time() - hotkey.tempo_inicio
        else:
            status_label.configure(text="Desligado", text_color="red")
            duracao = 0

        ciclos_label.configure(text=f"Ciclos: {hotkey.total_ciclos}")
        duracao_formatada = time.strftime('%H:%M:%S', time.gmtime(duracao))
        tempo_label.configure(text=f"Tempo: {duracao_formatada}")

        while hotkey.mensagens_pendentes:
            mensagem, cor = hotkey.mensagens_pendentes.pop(0)
            log_textbox.insert("end", mensagem + "\n", cor)
            log_textbox.see("end")

        app.after(500, atualizar_tela)

    atualizar_tela()
    app.mainloop()