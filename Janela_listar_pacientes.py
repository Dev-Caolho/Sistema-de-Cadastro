import sys, os

def resource_path(relative_path):
    """Retorna o caminho correto do recurso, tanto no .exe quanto no .py"""
    try:
        # Quando estiver empacotado pelo PyInstaller
        base_path = sys._MEIPASS
    except Exception:
        # Quando rodar no modo normal (Python)
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext


def janela_lista(pacientes):
    #Abre a janela acima da principal
    janela5 = tk.Toplevel()
    janela5.title("Lista de pacientes")
    janela5.config(bg="light steel blue")
    janela5.iconbitmap(resource_path('OIP-3805769249 (1).ico'))
    janela5.grab_set()
    janela5.focus_force()

    #Função que centraliza a janela e determina seu tamanho mínimo
    centralizar_janela(janela5, 400, 300)
    janela5.minsize(400, 300)


    #Função de listar todos os pacientes cadastrados
    #Verifica se existem pacientes cadastrados, e se houver, abre uma janela listando o que foi encontrado, com uma scrollbar para evitar que o texto vaze para fora da janela.
    if not pacientes:
        messagebox.showinfo("Lista", "Nenhum paciente cadastrado.")
        return janela5.destroy()

    lista = "\n\n".join(
        f"Nome: {p.get('nome', '')}\nIdade: {p.get('idade', '')} anos\nTelefone: {p.get('telefone', '')}\nTelefone emergência: {p.get('telefone_emergencia', '')}"
        for p in pacientes)

    st = scrolledtext.ScrolledText(janela5, wrap='word')
    st.insert('1.0', lista)
    st.configure(state='disabled')  # só leitura
    st.pack(fill='both', expand=True, padx=10, pady=10)
    st.config(bg="light steel blue")



#Função para o programa abrir no centro da tela.
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
