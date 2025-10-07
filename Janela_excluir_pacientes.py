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

#Função que cria a janela.
def janela_de_excluir(pacientes):
    #Informações da janela.
    janela4 = tk.Toplevel()
    janela4.title("Excluir paciente do sistema")
    janela4.config(bg="light steel blue")
    janela4.iconbitmap(resource_path('OIP-3805769249 (1).ico'))
    centralizar_janela(janela4, 300, 250)
    janela4.minsize(300, 250)
    janela4.grab_set()
    janela4.focus_force()

    #Mostra que o usuário deve escrever o nome do paciente que deseja excluir do sistema.
    tk.Label(janela4, text="Digite o nome do paciente que deseja excluir", bg="light steel blue").pack(pady=(25, 5))
    entry_nome = tk.Entry(janela4)
    entry_nome.pack()
    entry_nome.focus_set()

    #Espaço usado pra exibir as caixas de marcação posteriormente.
    caixas_resultados = tk.Frame(janela4, bg="light steel blue")
    caixas_resultados.pack(pady=10, fill="both",)

    #Lista com todas as caixas criadas, com cada uma tendo as informações de um paciente que foi encontrado no sistema.
    caixas_criadas = []

    #Função que faz a busca dos pacientes na lista de cadastros.
    def buscar():
        #Dá acesso a lista pra poder adicionar itens nela.
        nonlocal caixas_criadas

        #Deleta todos os widgets que estavam anteriormente caso haja algum.
        for widget in caixas_resultados.winfo_children():
            widget.destroy()

        #Zera a lista de caixas criadas para poder adicionar informações novas sem embaralhar dados.
        caixas_criadas = []

        # Guarda o que foi digitado na caixa de entrada
        nome_busca = entry_nome.get().strip().lower()

        # Verifica se algo foi escrito. Se não, a função retorna uma mensagem de erro.
        if not nome_busca:
            messagebox.showerror("Erro", "Digite um nome para buscar.", parent=janela4)
            return

        # Procura na lista de pacientes todos os pacientes que tenham as palavras que foram escritas na caixa.
        resultados = [p for p in pacientes if nome_busca in p["nome"].lower()]

        #Caso tenha encontrado algo, cria caixas de seleção e as adiciona na lista e no frame.
        if resultados:
            tk.Label(caixas_resultados, text="Selecione os pacientes que deseja excluir:", bg="light steel blue").pack(anchor="w")

            #Para cada paciente encontrado cria uma variável booleana ligada à caixa de seleção.
            # Adiciona na lista o par de informações, a caixa de seleção e sua variável booleana indicando se ela é verdadeira (marcada) ou falsa (desmarcada).
            for idx, p in enumerate(resultados):
                var = tk.BooleanVar()
                caixas_criadas.append((var, p))

                #Junta as informações encontradas da lista de pacientes numa linha de texto só e mostra uma caixa de seleção com essas informações.
                info = f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}"
                tk.Checkbutton(caixas_resultados, text=info, variable=var, bg="light steel blue", anchor="w", justify="left").pack(fill="x", padx=5, pady=2)

        #Caso nada seja encontrado, mostra uma label avisando.
        else:
            tk.Label(caixas_resultados, text="Nenhum paciente encontrado.", bg="light steel blue").pack()

        #Ajusta a janela pro tamanho das caixas sem distorcer os componentes.
        janela4.geometry("")


    #Função que executa a exclusão do paciente noo sistema.
    def excluir():

        #Pega todos os pacientes da lista caixas_criadas que estão marcados (var.get()==True)
        selecionados = [p for var, p in caixas_criadas if var.get()]

        #Se nenhuma caixa foi selecionada exibe um aviso indicando que ao menos uma deve ser marcada.
        if not selecionados:
            messagebox.showwarning("Aviso", "Selecione ao menos um paciente para excluir.", parent=janela4)
            return

        #Reúne as informações dos pacientes das caixas marcadas para exclusão.
        lista_selecionados = "\n\n".join(f"Nome: {p['nome']}\nIdade: {p['idade']}" for p in selecionados)

        #Abre uma janela de confirmação como forma de evitar exclusões acidentais.
        confirmar = messagebox.askyesno("Confirmar exclusão",f"Tem certeza que deseja excluir os seguintes pacientes?\n\n{lista_selecionados}", parent=janela4)

        #Se foi confirmado apaga os pacientes selecionados da lista de pacientes e mostra uma mensagem dizendo que a ação foi concluída com sucesso.
        if confirmar:

            for p in selecionados:
                pacientes.remove(p)

            messagebox.showinfo("Sucesso", "Paciente(s) excluído(s) com sucesso!", parent=janela4)

            #Limpa a caixa de texto e o frame retorna pro estado original, vazio, e ajusta o tamanho da janela.
            entry_nome.delete(0, tk.END)
            for widget in caixas_resultados.winfo_children():
                widget.destroy()
            centralizar_janela(janela4, 300, 300)

    #Botões e suas respectivas funções.
    tk.Button(janela4, text="Buscar", command=buscar, font=("TkDefaultFont", 10,"bold")).pack(pady=(5, 5))
    tk.Button(janela4, text="Excluir", command=excluir, font=("TkDefaultFont", 10, "bold")).pack(pady=(5,5))
    tk.Button(janela4, text="Voltar", command=janela4.destroy, bg="red", fg="White").pack(pady=(5, 50))


#Função para o programa abrir no centro da tela.
def centralizar_janela(janela, largura, altura):
    janela.update_idletasks()
    x = (janela.winfo_screenwidth() // 2) - (largura // 2)
    y = (janela.winfo_screenheight() // 2) - (altura // 2)
    janela.geometry(f"{largura}x{altura}+{x}+{y}")
