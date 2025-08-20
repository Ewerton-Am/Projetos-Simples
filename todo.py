tarefas = []

def menu():
    print("\n[1] Adicionar tarefa\n[2] Listar tarefas\n[3] Remover tarefa\n[0] Sair")

def adicionar():
    tarefa = input("Digite a nova tarefa: ")
    tarefas.append(tarefa)

def listar():
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}")

def remover():
    listar()
    try:
        i = int(input("Número da tarefa para remover: "))
        tarefas.pop(i - 1)
    except (ValueError, IndexError):
        print("Entrada inválida.")

if __name__ == "__main__":
    while True:
        menu()
        opcao = input("Escolha: ")
        if opcao == "1":
            adicionar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            remover()
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
