from time import sleep

# Lista para guardar os pacientes
pacientes = []

#Cria um loop que fica sendo executado até que o usuário decida sair.
while True:
    print("====== Menu de Opções ======")
    print("1 - Cadastrar novo Paciente")
    print("2 - Ver lista de pacientes cadastrados no sistema")
    print("3 - Estatísticas dos pacientes")
    print("4 - Procurar paciente pelo nome")
    print("5 - Sair do sistema")
    print("============================")
    print("")

    #Faz uma verificação para saber se o que foi digitado foi algum número (forma de prevenção de erros),
    #Se sim, o loop segue normalmente. Se não, mostra uma mensagem de erro e o loop reinicia.
    try:
        opcao = int(input("Digite a ação desejada: "))
    except:
        print("Digite apenas números!")
        sleep(2)
        continue

    print("")

    #Aqui é a parte que determina o que cada opção digitada anteriormente faz.

    # 1 - Cadastro de paciente
    #Exibe um input para que se coloque os dados do paciente. Nome, Idade e Telefone.
    if opcao == 1:

        nome = input("Nome do paciente: ")

        #Aqui se faz uma verificação para saber se foi uma idade válida (números).
        #Se está válido, continua, se não, cacela o cadastro e retorna para o início para evitar erros.
        try:
            idade = int(input("Idade do paciente: "))
        except:
            print("Idade inválida! Cadastro cancelado.")
            sleep(2)
            continue

        #Mesma verificação igual a da idade.
        try:
            telefone = int(input("Telefone do paciente: "))
        except:
            print("Digite somente números! Cadastro cancelado.")
            sleep(2)
            continue

        #Adiciona as informações escritas na lista pacientes para serem usadas mais tarde se necessário.
        paciente = {"nome": nome, "idade": idade, "telefone": telefone}
        pacientes.append(paciente)

        #Feedback para mostrar que o processo foi concluído.
        print("Paciente cadastrado com sucesso!")
        sleep(2)

    # 2 - Mostrar lista de pacientes
    #Procura na lista todos os pacientes já cadastrados, Caso não existam, mostra um aviso.
    elif opcao == 2:
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            #Usa um for para percorrer toda a lista e enumera eles para dar uma impressão de lsita mesmo.
            print("Lista de pacientes:")
            numero = 1
            for p in pacientes:
                print(f"{numero}. Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
                numero += 1
        sleep(3)

    # 3 - Estatísticas simples
    #Mostra o número de pacientes, a idade média de deles e qual é o mais velho e o mais novo.
    elif opcao == 3:
        if len(pacientes) == 0:
            print("Nenhum paciente cadastrado.")
        else:
            #Pega todas as idades dos pacientes e soma elas.
            soma = 0
            for p in pacientes:
                soma += p["idade"]

            #Operação simples de média. divide o total das somas pela quantidade de pacientes cadastrados.
            media = soma / len(pacientes)

            #Descobrir mais novo e mais velho
            #De início os pacientes mais novo e mais velho são os da primeira posição na lista.
            mais_novo = pacientes[0]
            mais_velho = pacientes[0]

            #Percorre a lista e atualiza a posição do paciente mais novo e mais velho.
            for p in pacientes:
                #Se o paciente for menor que o mais novo (O da primeira posição), atualiza a variável colocando esse paciente como mais novo.
                if p["idade"] < mais_novo["idade"]:
                    mais_novo = p

                #Mesma coisa se aplica ao mais velho, mas a diferença é que só atualiza a variável quando encontra um paciente mais velho que o atual.
                if p["idade"] > mais_velho["idade"]:
                    mais_velho = p


            #Mostra um relatório do que foi encontrado. Númemro de pacientes, a média das idades, e os nomes e idades do paciente mais novo e mais velho cadastrado.
            print("Total de pacientes:", len(pacientes))
            print("Idade média:", round(media, 1))
            print("Mais novo:", mais_novo["nome"], "-", mais_novo["idade"], "anos")
            print("Mais velho:", mais_velho["nome"], "-", mais_velho["idade"], "anos")
        sleep(4)

    # 4 - Procurar paciente
    #Procura dentro da lista de pacientes o nome de algum deles que seja o que foi digitado,ou ao menos uma parte da palavra.
    elif opcao == 4:
        #Retorna tudo o que foi digitado em letras minúsculas para facilitar a manipulação das palavras.
        nome_busca = input("Digite o nome do paciente: ").lower()
        achou = False

        #Percorre toda a lista de pacientes, e se algum tenha as letras que foram digitadas, mostra todas as informações do paciente.
        for p in pacientes:
            if nome_busca in p["nome"].lower():
                print("Nome:", p["nome"], "| Idade:", p["idade"], "| Telefone:", p["telefone"])
                achou = True

        #Caso não encontre nada, retorna um aviso.
        if not achou:
            print("Nenhum paciente encontrado com esse nome.")
        sleep(3)

    # 5 - Sair
    #Encerra o programa com uma pequena mensagem de encerramento apenas por estética.
    elif opcao == 5:
        print("Saindo do sistema...")
        sleep(2)
        break

    # Opção inválida
    #Caso o número digitado não seka de nenhuma das opções acima, exibe a mensagem de erro e volta ao início do loop.
    else:
        print("Opção inválida. Tente novamente!")
        sleep(2)

    print("")
