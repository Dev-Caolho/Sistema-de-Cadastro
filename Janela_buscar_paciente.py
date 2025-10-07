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

def janela_de_busca(pacientes):
    janela3 = tk.Toplevel()
    janela3.title("Buscar pacientes")
    janela3.config(bg="light steel blue")
    janela3.iconbitmap(resource_path('OIP-3805769249 (1).ico'))

    janela3.grab_set()
    janela3.focus_force()

    centralizar_janela(janela3, 300, 250)
    janela3.minsize(300, 250)

    # Ver se tem o paciente cadastrado.
    tk.Label(janela3, text="Buscar paciente pelo nome", bg="light steel blue").pack(pady=(50, 5))
    entry_busca = tk.Entry(janela3)
    entry_busca.pack()
    entry_busca.focus_set()


    #Função que busca todos os pacientes cadastrados que tenham o nome que o usuário tenha digitado.
    def buscar_pacientes():
        nome_busca = entry_busca.get().strip().lower()
        #Caso nenhum nome tenha sido digitado exibe mensagem de erro.
        if not nome_busca:
            messagebox.showerror("Erro", "Digite um nome para buscar.", parent=janela3)
            return

        #Lista que guarda os pacientes que o sistema achou com base no que foi digitado no campo de busca de pacientes.
        resultados = [
            paciente for paciente in pacientes
            if nome_busca in paciente["nome"].lower()
        ]

        #Faz a verificação se há algo dentro da lista dos resultados e exibe o que aparecer.
        if resultados:
            lista = "\n\n".join(f"Nome: {p['nome']}\nIdade: {p['idade']}\nTelefone: {p['telefone']}\nNúmero de emergência: {p['telefone_emergencia']}" for p in resultados)
            messagebox.showinfo("Pacientes encontrados", lista, parent=janela3)

        #Caso não tenha nada exibe um aviso.
        else:
            messagebox.showwarning("Paciente não encontrado", f"Nenhum paciente com o nome {nome_busca} foi encontrado. Verifique se o nome está certo", parent=janela3)

    tk.Button(janela3, text="Procurar", command=buscar_pacientes, font=("TkDefaultFont", 12, "bold")).pack(pady=(30, 5))

    # Botão de saída da janela
    tk.Button(janela3, text="Voltar", command=janela3.destroy, bg="red", fg="white", font=("Arial", 10)).pack(pady=(10, 5))

#Função para o programa abrir no centro da tela.
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
