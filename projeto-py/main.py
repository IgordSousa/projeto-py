tarefasGeral = []


def addTarefa(n):
        if n == 1:
            nome = input(f"digite o nome da {len(tarefasGeral)+1}º tarefa: ").lower()
            for tarefa in tarefasGeral:
                if tarefa["nome"] == nome:
                    print("Já existe uma tarefa com este nome. Tente novamente.")
                    return 
            descricao = input("descreva essa tarefa: ")
            while True:
                categoria = input("""
                            selecione a categoria da tarefa:
                            1-doméstica
                            2-saúde
                            3-educação
                            4-lazer
                            """)
                match categoria:
                    case "1":
                        categoria = "doméstica"
                        break
                    case "2":
                        categoria = "saúde"
                        break
                    case "3":
                        categoria = "educação"
                        break
                    case "4":
                        categoria = "lazer"
                        break
                    case _:
                        print("digito invalido")

            while True:
                prioridade = input("digite o nivel de prioridade dessa tarefa de 1 a 5, sendo 1 para baixa e 5 para alta prioridade!: ")

                match prioridade:
                    case "1":
                        break
                    case "2":
                        break
                    case "3":
                        break
                    case "4":
                        break
                    case "5":
                        break
                    case _:
                        print("digito invalido, digite um número entre 1 e 5")
            while True:
                concluida = input("""
                        a tarefa ja foi conlcuida ?
                            1- sim
                            2- não    
                            """)
                match concluida:
                    case "1":
                        concluida = "sim"
                        break
                    case "2":
                        concluida = "não"
                        break
                    case _:
                        print("digito invalido, digite 1 p/ sim e 2 p/ não!")
            
        novaTarefa = {
        "nome": nome,
        "descrição": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": concluida
        }

        tarefasGeral.append(novaTarefa)
        

        print("tarefa listada com sucesso! ")


def concluirTarefa(n):
        if n == 2:
            if len(tarefasGeral)  == 0:
                print("não ha tarefas para concluir!")
            elif  len(tarefasGeral) != 0:
                tarefaConcluida = input("qual a tarefa deseja marcar como concluida: ").lower()
                for tarefaDaVez in tarefasGeral:
                    if tarefaDaVez["nome"] == tarefaConcluida:
                        if tarefaDaVez["concluida"] == "sim":
                            print("tarefa ja está concluida!")
                            break
                        else:
                            tarefaDaVez["concluida"] = "sim"
                            print("parabéns, Tarefa concluida!")
                            break
                    print("tarefa não encontrada")
                


def exibirCategoricamente(n):
        tarefasCategoria = []
        if n==3:
            if len(tarefasGeral) == 0:
                print("ainda não ha tarefas listadas")
            else:
                categoriaParaExibir = input("""
                                selecione a categoria que dejesa exibir:
                                1-doméstica
                                2-saúde
                                3-educação
                                4-lazer
                                """)
                match categoriaParaExibir:
                    case "1":
                        for tarefaDaVez in tarefasGeral:
                            if tarefaDaVez["categoria"] == "doméstica":
                                tarefasCategoria.append(tarefaDaVez)

                        if len(tarefasCategoria) != 0:
                            print("segue lista de tarefas classificadas como  doméstica: ")

                            for taf in tarefasCategoria:
                                print(f"""
                                nome: {taf["nome"]}
                                descrição: {taf["descrição"]}
                                concluida: {taf["concluida"]}
                                """)
                        else:
                            print("não ha tarefas listadas nessa categoria")
                    case "2":
                        for tarefaDaVez in tarefasGeral:
                            if tarefaDaVez["categoria"] == "saúde":
                                tarefasCategoria.append(tarefaDaVez)

                        if len(tarefasCategoria) != 0:
                            print("segue lista de tarefas classificadas como  saúde:")
                            for taf in tarefasCategoria:
                                print(f"""
                                nome: {taf["nome"]}
                                descrição: {taf["descrição"]}
                                concluida: {taf["concluida"]}
                                """)
                        else:
                            print("não ha tarefas listadas nessa categoria")
                    case "3":
                        for tarefaDaVez in tarefasGeral:
                            if tarefaDaVez["categoria"] == "educação":
                                tarefasCategoria.append(tarefaDaVez)

                        if len(tarefasCategoria) != 0:
                            print("segue lista de tarefas classificadas como  educação:")
                            for taf in tarefasCategoria:
                                print(f"""
                                nome: {taf["nome"]}
                                descrição: {taf["descrição"]}
                                concluida: {taf["concluida"]}
                                """)
                        else:
                            print("não ha tarefas listadas nessa categoria")

                    case "4":
                        for tarefaDaVez in tarefasGeral:
                            if tarefaDaVez["categoria"] == "lazer":
                                tarefasCategoria.append(tarefaDaVez)
                        if len(tarefasCategoria) != 0:
                            print("segue lista de tarefas classificadas como  lazer:")
                            for taf in tarefasCategoria:
                                print(f"""
                                nome: {taf["nome"]}
                                descrição: {taf["descrição"]}
                                concluida: {taf["concluida"]}
                                """)
                        else:
                            print("não ha tarefas listadas nessa categoria")

                    case _:
                        print("digito inválido")


def exibirPrioritariamente(n):
    tarefasPrioridade = []
    if  n == 4:
        if len(tarefasGeral) == 0:
            print("ainda não ha tarefas listadas")
        else:
            prioridadeParaExibir = int(input("""qual o nivel de prioridade as tarefas que busca?
                                                escolha entre 1 e 5: """))
            match prioridadeParaExibir:
                case 1:
                    for tarefaDaVez in tarefasGeral:
                        if tarefaDaVez["prioridade"] == "1":
                            tarefasPrioridade.append(tarefaDaVez)
                    if len(tarefasPrioridade) !=0:
                        print("lista das tarefas com prioridade 1:")
                        for taf in tarefasPrioridade:
                            print(f"""
                        nome: {taf["nome"]}
                        descrição: {taf["descrição"]}
                        categoria: {taf["categoria"]}
                        concluida: {taf["concluida"]}
                        """)
                    else:
                        print("não ha tarefas listadas com essa prioridade")
                case 2:
                    for tarefaDaVez in tarefasGeral:
                        if tarefaDaVez["prioridade"] == "2":
                            tarefasPrioridade.append(tarefaDaVez)
                    if len(tarefasPrioridade) !=0:
                        print("lista das tarefas com prioridade 2:")
                        for taf in tarefasPrioridade:
                            print(f"""
                        nome: {taf["nome"]}
                        descrição: {taf["descrição"]}
                        categoria: {taf["categoria"]}
                        concluida: {taf["concluida"]}
                        """)
                    else:
                        print("não ha tarefas listadas com essa prioridade")
                case 3:
                    for tarefaDaVez in tarefasGeral:
                        if tarefaDaVez["prioridade"] == "3":
                            tarefasPrioridade.append(tarefaDaVez)
                    if len(tarefasPrioridade) !=0:
                        print("lista das tarefas com prioridade 3:")
                        for taf in tarefasPrioridade:
                            print(f"""
                        nome: {taf["nome"]}
                        descrição: {taf["descrição"]}
                        categoria: {taf["categoria"]}
                        concluida: {taf["concluida"]}
                        """)
                    else:
                        print("não ha tarefas listadas com essa prioridade")
                case 4:
                    for tarefaDaVez in tarefasGeral:
                        if tarefaDaVez["prioridade"] == "4":
                            tarefasPrioridade.append(tarefaDaVez)
                    if len(tarefasPrioridade) !=0:
                        print("lista das tarefas com prioridade 4:")
                        for taf in tarefasPrioridade:
                            print(f"""
                        nome: {taf["nome"]}
                        descrição: {taf["descrição"]}
                        categoria: {taf["categoria"]}
                        concluida: {taf["concluida"]}
                        """)
                    else:
                        print("não ha tarefas listadas com essa prioridade")
                case 5:
                    for tarefaDaVez in tarefasGeral:
                        if tarefaDaVez["prioridade"] == "5":
                            tarefasPrioridade.append(tarefaDaVez)
                    if len(tarefasPrioridade) !=0:
                        print("lista das tarefas com prioridade 5:")
                        for taf in tarefasPrioridade:
                            print(f"""
                        nome: {taf["nome"]}
                        descrição: {taf["descrição"]}
                        categoria: {taf["categoria"]}
                        concluida: {taf["concluida"]}
                        """)
                    else:
                        print("não ha tarefas listadas com essa prioridade")
                case _:
                    print("digito inválido")

           
while True:
    menu = input("""
    escolha o que deseja fazer que deseja fazer ?
            1 - Adicionar tarefa
            2 - Marcar tarefa como concluída
            3 - Exibir tarefas por categoria
            4 - Exibir tarefas por prioridade
""")
    if menu == "1":
        addTarefa(int(menu))
    elif menu == "2":
        concluirTarefa(int(menu))  
    elif menu == "3":    
        exibirCategoricamente(int(menu))
    elif menu == "4":
        exibirPrioritariamente(int(menu))
    else:
        print("opção inválida")