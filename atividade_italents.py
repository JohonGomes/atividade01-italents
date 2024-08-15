# Lista Inicial Vazia
lista_tarefas= []

while True: 
    # Exibe o Menu 
    print("\n ====== LISTA DE TAREFAS ======\n")
    print("(1) - Adicionar Tarefa")
    print("(2) - Exibir Lista de Tarefas")
    print("(3) - Marcar Tarefa como concluída")
    print("(4) - Remover Tarefa")
    print("(5) - Limpar Lista de Tarefas")
    print("(6) - Sair\n")

    # Solicita a escolha do usuário
    opcao = input("Escolha uma opção de 1 a 6: ")

    # Adicionar Item
    if opcao == "1":
        nova_tarefa = input("Digite uma nova tarefa: ")
        lista_tarefas.append({"nome": nova_tarefa, "concluída": False})
        print(f"Item '{nova_tarefa}' adicionada à lista!")

    # Listar Tarefas
    elif opcao == "2":
        if not lista_tarefas:
            print("A Lista de tarefas está vazia.")
        else:
            print("\nLista de Tarefas:")
            for i, item in enumerate(lista_tarefas, 1):
                status = "Concluída" if item["concluída"] else "Pendente"
                print(f"{i}. {item['nome']} - {status}")

    # Marcar Tarefa como concluída.
    elif opcao == "3":
        if not lista_tarefas:
            print("\nA Lista de tarefas está vazia.")
        else:
            for i, item in enumerate(lista_tarefas, 1):
                status = "Concluída" if item["concluída"] else "Pendente"
                print(f"{i}. {item['nome']} - {status}")
            numero_item = int(input("Digite o número da tarefa a ser concluída:  "))
            if 1 <= numero_item <= len(lista_tarefas):
                lista_tarefas[numero_item - 1]["concluída"] = True
                print(f"Item '{lista_tarefas[numero_item - 1]['nome']}' foi marcado como concluída.")
            else:
                print("Número de item inválido.")

    # Remover Item
    elif opcao == "4":
        if not lista_tarefas:
            print("A Lista de tarefas está vazia.")
        else:
            for i, item in enumerate(lista_tarefas, 1):
                status = "Concluída" if item["concluída"] else "Pendente"
                print(f"{i}. {item['nome']} - {status}")
            numero_item = int(input("Digite o número do item a ser removido: "))
            if 1 <= numero_item <= len(lista_tarefas):
                item_removido = lista_tarefas.pop(numero_item - 1)
                print(f"Item '{item_removido['nome']}' foi removido da lista.")
            else:
                print("Número de item inválido.")

    # Limpar Lista de Compras
    elif opcao == "5":
        lista_tarefas.clear()
        print("A lista de tarefas foi completamente limpa.")

    # Sair do programa
    elif opcao == "6":
        print("Saindo do programa.")
        break

    # Opção Inválida
    else:
        print("Opção Inválida - Tente novamente!")
