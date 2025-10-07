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

#Importações da biblioteca tkinter
import tkinter as tk
from tkinter import ttk

#As janelas foram colocadas em scripts separados para melhor visualização do código.
from Janela_cadastro import janela_cadastro
from Janela_buscar_paciente import janela_de_busca
from Janela_excluir_pacientes import janela_de_excluir
from Janela_listar_pacientes import janela_lista
from Janela_verificacao_atendimento import janela_verificacao

#Lista que armazena os dados dos pacientes.
pacientes = []

#Função para o programa abrir no centro da tela.
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")

#Cria a janela
root = tk.Tk()
centralizar_janela(root, 650, 500)

#Título da janela
root.title("Sistema de Cadastro Clínica Vida+")

#Define o tamanho mínimo da janela
root.minsize(650, 500)

#Ícone da janela
root.iconbitmap(resource_path('OIP-3805769249 (1).ico'))


#Cor de fundo
root.config(bg="light blue")

#Label inicial para situar o usuário.
ttk.Label(
    root,
    text= "Clínica Saúde Vida+",
    background= "light blue",
    foreground= "white",
    font=("Verdana", 22, "bold"),
    borderwidth=10,
    relief="solid",
    anchor="center"
).pack(pady=(35,0))

#Os botões com suas respectivas funções.
tk.Button(root, text="Cadastrar paciente", command=lambda: janela_cadastro(pacientes), font=("Arial", 16), width=15).pack(pady=(65, 5))
tk.Button(root, text="Buscar pacientes", command=lambda: janela_de_busca(pacientes), font=("Arial", 16), width=15).pack(pady=5)
tk.Button(root, text="Excluir pacientes", command=lambda: janela_de_excluir(pacientes), font=("Arial", 16), width=15).pack(pady=5)
tk.Button(root, text="Listar pacientes", command=lambda: janela_lista(pacientes), font=("Arial", 16), width=15).pack(pady=5)
tk.Button(root, text="Verificar atendimento", command=lambda: janela_verificacao(), font=("Arial", 14), width=18).pack(pady=5)

#Botão de saída.
tk.Button(root, text="Sair", command=root.quit, bg="red", fg="white", font=("Arial", 11), width=10).pack(pady=5)

#Roda a aplicação em loop.
root.mainloop()