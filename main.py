import os, services

def menu():
    logged_user = None
    while True:
        os.system('cls')     
        if not logged_user:
            print("\n___ Sistema de Tarefas ___")
            print("1 - Login")
            print("2 - Cadastrar Usuário")
            print("0 - Sair")
            opt = input("Escolha uma opção: ")

            if opt == "1":
                logged_user = services.login()
            if opt == "2":
                services.new_user()
            elif opt == "0":
                print("Saindo...")
                break
            else:
                input("\nPressione Enter para continuar...")

        else:
            os.system('cls')
            print(f"\n___ Menu Principal (Logado como: {logged_user.username}) ___")
            print("1 - Menu de Usuários")
            print("2 - Menu de Tarefas")
            print("3 - Logout")
            print("0 - Sair do Sistema")
            opt = input("Escolha uma opção: ")

            if opt == "1":
                os.system('cls')
                print(f"\n___ Menu Principal (Logado como: {logged_user.username}) ___")
                print("1 - Cadastrar Usuário")
                print("2 - Editar Nome de Usuário")
                print("3 - Deletar Usuário")
                print("4 - Localizar Usuário por Nome")
                print("5 - Localizar Todos os Usuários")
                print("0 - Retornar")
                sub_opt = input("Escolha uma opção: ")

                if sub_opt == "1":
                    services.new_user()
                elif sub_opt == "2":
                    services.edit_username()
                elif sub_opt == "3":
                    services.delete_user()
                elif sub_opt == "4":
                    services.get_user()
                elif sub_opt == "5":
                    services.get_all_users()
                elif sub_opt == "0":
                    pass
                else:
                    print("Opção inválida.")
                    input("\nPressione Enter para continuar...")

            elif opt == "2":
                print(f"\n___ Menu Principal (Logado como: {logged_user.username}) ___")
                os.system('cls')
                print("1 - Adicionar Tarefa")
                print("2 - Editar Título da Tarefa")
                print("3 - Editar Descrição da Tarefa")
                print("4 - Completar Tarefa")
                print("5 - Reabrir tarefa")
                print("6 - Imprimir Tarefas")
                print("7 - Localizar Tarefa por Titulo")
                print("8 - Localizar Tarefa por Descrição")
                print("9 - Deletar Tarefa")
                print("0 - Retornar")
                sub_opt = input("Escolha uma opção: ")

                if sub_opt == "1":
                    services.new_task(logged_user)
                elif sub_opt == "2":
                    services.edit_task_title(logged_user)
                elif sub_opt == "3":
                    services.edit_task_description(logged_user)
                elif sub_opt == "4":
                    services.complete_task(logged_user)
                elif sub_opt == "5":
                    services.reopen_task(logged_user)
                elif sub_opt == "6":
                    services.get_all_tasks(logged_user)
                elif sub_opt == "7":
                    services.get_task_by_title(logged_user)
                elif sub_opt == "8":
                    services.get_task_by_desc(logged_user)
                elif sub_opt == "9":
                    services.delete_task(logged_user)
                elif sub_opt == "0":
                    pass
                else:
                    print("Opção inválida.")
                    input("\nPressione Enter para continuar...")
                continue

            elif opt == "3":
                logged_user = None
                print("Logout realizado com sucesso!")
                input("\nPressione Enter para continuar...")

            elif opt == "0":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")
                input("\nPressione Enter para continuar...")
        
if __name__ == "__main__":
    menu()
                