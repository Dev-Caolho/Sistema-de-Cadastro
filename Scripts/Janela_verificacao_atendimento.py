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

#Função que cria a janela e toda a lógica de verificação do estado do atendimento do paciente
def janela_verificacao():
    # Abre a janela acima da principal
    janela6 = tk.Toplevel()
    janela6.title("Lista de pacientes")
    janela6.config(bg="light steel blue")
    janela6.iconbitmap(resource_path('OIP-3805769249 (1).ico'))
    janela6.grab_set()
    janela6.focus_force()

    #Função que centraliza a janela e determina seu tamanho mínimo
    centralizar_janela(janela6, 400, 300)
    janela6.minsize(400, 300)

    #Funções de avaliação

    #A consulta normal só acontece se: O paciente tem agendamento E tem os documentos em dia E tem médico disponível, OU se o paciente tem os documentos, tem médico disponível e os pagamentos estão em dias
    def consulta_normal(A, B, C, D):
        return (A and B and C) or (B and C and D)

    #Em casos de emergência o atendimeto ocorre quando se tem médico disponível E o paciente tem os documentos OU os pagamentos estão em dia
    def emergencia(A, B, C, D):
        return C and (B or D)

    #Função principal ao clicar no botão

    #Verifica as caixas que foram marcadas e as que não foram, e mostra as formas do paciente ser atendido, tanto numa consulta normal quanto numa emergência
    def verificar():
        #Pega os dados obtidos das checkboxes que foram, ou não,, marcadas
        agendamento = varA.get()
        documentos = varB.get()
        medico = varC.get()
        pagamentos = varD.get()

        #Preenche as funções com os dados obtidos e mostra os resultados em uma caixa de mensagem na tela
        res_normal = consulta_normal(agendamento, documentos, medico, pagamentos)
        res_emerg = emergencia(agendamento, documentos, medico, pagamentos)

        msg = ""
        msg += f"Para consulta Normal: {'Pode ser atendido' if res_normal else 'Não pode ser atendido'}\n"
        msg += f"Para emergências: {'Pode ser atendido' if res_emerg else 'Não pode ser atendido'}"

        messagebox.showinfo("Resultado", msg)

    #Variáveis dos checkboxes
    varA = tk.IntVar()
    varB = tk.IntVar()
    varC = tk.IntVar()
    varD = tk.IntVar()

    #Criação das checkboxes
    label = tk.Label(janela6, text="Preencha as condições do paciente:", font=("TkDefaultFont", 12), bg="light steel blue")
    label.pack(pady=(15, 10))

    tk.Checkbutton(janela6, text="Tem agendamento", variable=varA, bg="light steel blue").pack(anchor="w", pady=(20, 3))
    tk.Checkbutton(janela6, text="Documentos estão OK", variable=varB, bg="light steel blue").pack(anchor="w", pady=3)
    tk.Checkbutton(janela6, text="O médico está disponível", variable=varC, bg="light steel blue").pack(anchor="w", pady=3)
    tk.Checkbutton(janela6, text="Os pagamentos estão em dia", variable=varD, bg="light steel blue").pack(anchor="w", pady=3)

    # Botão verificar
    btn = tk.Button(janela6, text="Verificar Atendimento", command=verificar, bg="lightblue")
    btn.pack(pady=(20, 10))

    tk.Button(janela6, text="Voltar", command=janela6.destroy, bg="red", fg="white", font=("Arial", 11), width=8).pack()

#Função para o programa abrir no centro da tela.
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
