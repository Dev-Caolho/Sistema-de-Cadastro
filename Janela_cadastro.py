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


#Função que abre a janela de cadastro.
def janela_cadastro(pacientes):
    #Abre a janela acima da principal
    janela2 = tk.Toplevel()
    janela2.title("Cadastrar Paciente")
    janela2.config(bg="light steel blue")
    janela2.iconbitmap(resource_path('OIP-3805769249 (1).ico'))
    janela2.grab_set()
    janela2.focus_force()

    centralizar_janela(janela2, 400, 300)
    janela2.minsize(400, 300)

    # Função que guarda na lista as informações digitadas nos campos.
    def cadastrar():
        # Variáveis que armazenam as informações das caixas de texto.
        nome = entry_nome.get()
        idade = entry_idade.get()
        telefone = entry_telefone.get()
        telefone_emergencia = entry_telefone_emergencia.get()

        # Verifica se todas as caixas foram preenchidas corretamente. Caso foram, cria um dicionário e adiciona na lista.
        if nome and idade.isdigit() and telefone.isdigit() and len(
                telefone) == 11 and telefone_emergencia.isdigit() and len(telefone_emergencia) == 11:
            pacientes.append({"nome": nome.title().strip(), "idade": idade, "telefone": telefone,
                              "telefone_emergencia": telefone_emergencia})
            messagebox.showinfo("Sucesso", f"Paciente {nome.title().strip()} cadastrado!", parent=janela2)

            # Limpa as caixas quando o cadastro é realizado.
            entry_nome.delete(0, tk.END)
            entry_idade.delete(0, tk.END)
            entry_telefone.delete(0, tk.END)
            entry_telefone_emergencia.delete(0, tk.END)

        # Caso não, apresenta uma mensagem de erro.
        else:
            messagebox.showerror("Erro","Preencha os campos com informações válidas.\nNão deixe espaços ao preencher os números de telefone.\nExemplo: 81912345678", parent=janela2)

    # Cria uma label chamada Nome e uma caixa para digitar as informações.
    tk.Label(janela2, text="Nome", bg="light steel blue").pack(pady=(10, 2))
    entry_nome = tk.Entry(janela2)
    entry_nome.pack()
    entry_nome.focus_set()

    # A mesma coisa para a idade.
    tk.Label(janela2, text="Idade", bg="light steel blue").pack()
    entry_idade = tk.Entry(janela2)
    entry_idade.pack()

    # Mesma coisa.
    tk.Label(janela2, text="Telefone", bg="light steel blue").pack()
    entry_telefone = tk.Entry(janela2)
    entry_telefone.pack()

    # Mesma coisa.
    tk.Label(janela2, text="Telefone de emergência\n (Pode ser de algum familiar próximo.\nCaso não tenha, repita o número colocado acima)", bg="light steel blue").pack(pady=(5, 5))
    entry_telefone_emergencia = tk.Entry(janela2)
    entry_telefone_emergencia.pack()

    #Botão que efetua o cadastro
    tk.Button(janela2, text="Cadastrar", command=cadastrar, font=("TkDefaultFont", 12, "bold")).pack(pady=(10, 0))

    # Botão de saída da janela
    tk.Button(janela2, text="Voltar", command=janela2.destroy, bg="red", fg="white", font=("Arial", 10)).pack(pady=(5, 5))


#Função para o programa abrir no centro da tela.
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
