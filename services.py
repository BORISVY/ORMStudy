import os, bcrypt
from database import session
from models import User, Task 

def login():
    os.system('cls')
    print("___Login___")
    email = input("Email: ")
    password = input("Senha: ")
    user = session.query(User).filter_by(email=email).first()
    if user:
        password_bytes = password.encode('utf-8')
        hashed_bytes = user.password.encode('utf-8') if isinstance(user.password, str) else user.password
        if bcrypt.checkpw(password_bytes, hashed_bytes):
            print(f"Bem-vindo de volta, {user.username}!")
            input("\nPressione Enter para continuar...")
            return user
    print("Email ou senha inválidos!")
    return None

def new_user():
    os.system('cls')
    print("___Cadastro de Usuários___")
    username = input("Informe o nome de usuário: ")
    email = input("Informe o email: ")
    password = input("Crie a senha para usuário: ")

    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

    new_user = User(username=username, email=email, password=hashed_password.decode('utf-8'))
    session.add(new_user)
    session.commit()
    print("Usuários cadastrado com sucesso!")
    input("\nPressione Enter para continuar...")

def edit_username():
    os.system('cls')
    print("___Alterar Nome de Usuário___")
    username_edit = input("Informe o nome do usuário que deseja alterar: ")
    name = session.query(User).filter_by(username=username_edit).first()
    if name:
        print("\nUsuário localizado!\n")
        new_name = input("Insira o novo nome para o usuário: ")
        try:
            name.username = new_name
            session.commit()
            print("\nNome de usuário atualizado com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"\nErro ao atualizar o usuário: {e}")
    else:
        print("\nUsuário não encontrado.")
    input("\nPressione Enter para continuar...")

def delete_user():
    os.system('cls')
    print("___Deletar Usuário___")
    user = input("Informe o nome do usuário que deseja deletar: ")
    deleted_user = session.query(User).filter_by(username=user).first()
    if deleted_user:
        print("\nUsuário localizado!\n")
        confirmacao = input("\nDigite 'SIM' para confirmar a exclusão: ")
        if confirmacao.upper() == 'SIM':
            session.delete(deleted_user)
            session.commit()
            print("\nUsuário deletado com sucesso!")
        else:
            print("\nExclusão cancelada.")    
    else:
        print("\nUsuário não encontrado.")
    input("\nPressione Enter para continuar...")

def get_user():
    os.system('cls')
    print("___Localizar Usuário pelo Nome___")
    username = input("Informe o nome do usuário: ")
    user = session.query(User).filter_by(username=username).first()
    if user:   
        print(f"Usuário localizado com sucesso!")
        print(f"Segue {user.id, user.username, user.email}")
    else:
        print("\nUsuário não encontrado.")
    input("\nPressione Enter para continuar...")

def get_all_users():
    os.system('cls')
    print("___Lista de Usuários___")
    users = session.query(User).all()
    if not users:
        print("Nenhum usuário cadastrado no banco de dados.")
        return

    for user in users:
        print(f"ID: {user.id} | Usuário: {user.username} | Email: {user.email}")
        print("-" * 50)
    input("\nPressione Enter para continuar...")

def new_task(logged_user):
    os.system('cls')
    print("___Cadastro de Tarefas___")
    title = input("Informe o título da tarefa: ")
    description = input("Descreva a tarefa: ")
    
    new_task = Task(user_id=logged_user.id, title=title, description=description, completed=False)
    session.add(new_task)
    session.commit()
    print("Tarefa cadastrada com sucesso!")
    input("\nPressione Enter para continuar...")

def edit_task_title(logged_user):
    os.system('cls')
    print("___Alterar Título da Tarefa___")
    task_edit = input("Informe o título da tarefa que deseja alterar: ")
    title = session.query(Task).filter_by(title=task_edit, user_id=logged_user.id).first()
    if title:
        print("\nTarefa localizada!\n")
        new_title = input("Insira o novo título para a tarefa: ")
        try:
            title.title = new_title
            session.commit()
            print("\nTítulo da tarefa atualizado com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"\nErro ao atualizar título: {e}")
    else:
        print("\nTarefa não encontrada.")
    input("\nPressione Enter para continuar...")

def edit_task_description(logged_user):
    os.system('cls')
    print("___Alterar Descrição da Tarefa___")
    task_edit = input("Informe o título da tarefa que deseja alterar: ")
    task = session.query(Task).filter_by(title=task_edit, user_id=logged_user.id).first()
    if task:
        print("\nTarefa localizada!\n")
        new_description = input("Insira a nova descrição para a tarefa: ")
        try:
            task.description = new_description
            session.commit()
            print("\nDescrição da tarefa atualizada com sucesso!")
        except Exception as e:
            session.rollback()
            print(f"\nErro ao atualizar descrição: {e}")
    else:
        print("\nTarefa não encontrada.")
    input("\nPressione Enter para continuar...")

def complete_task(logged_user):
    os.system('cls')
    print("___Concluir Tarefa___")
    task_id = input("Informe o ID da tarefa que deseja concluir: ")
    task = session.query(Task).filter_by(id=task_id, user_id=logged_user.id).first()
    if task:
        task.completed = True
        session.commit()
        print(f"\nTarefa '{task.title}' concluída com sucesso!")
    else:
        print("\nTarefa não encontrada ou não pertence a você.")
    input("\nPressione Enter para continuar...")

def reopen_task(logged_user):
    os.system('cls')
    print("___Reabrir Tarefa___")
    task_id = input("Informe o ID da tarefa que deseja reabrir: ")
    task = session.query(Task).filter_by(id=task_id, user_id=logged_user.id).first()
    if task:
        task.completed = False
        session.commit()
        print(f"\nTarefa '{task.title}' reaberta com sucesso!")
    else:
        print("\nTarefa não encontrada ou não pertence a você.")
    input("\nPressione Enter para continuar...")

def get_all_tasks(logged_user):
    os.system('cls')
    print("___Lista de Tarefas___")
    tasks = session.query(Task).filter_by(user_id=logged_user.id).all()
    if not tasks:
        print("Nenhuma tarefa cadastrada no banco de dados.")
        return

    for task in tasks:
        status = "🟢 Concluída" if task.completed else "🔴 Aberta"
        print(f"ID: {task.id} | Título: {task.title} | Status: {status}")
        print(f"Descrição: {task.description or 'Sem descrição'}")
        print("-" * 50)
    input("\nPressione Enter para continuar...")

def get_task_by_title(logged_user):
    os.system('cls')
    print("___Localizar Tarefa pelo Título___")
    task_title = input("Informe o nome da tarefa: ")
    task = session.query(Task).filter_by(title=task_title, user_id=logged_user.id).first()
    if task:   
        status = "🟢 Concluída" if task.completed else "🔴 Aberta"
        print(f"\nTarefa localizada com sucesso!")
        print(f"ID: {task.id} | Título: {task.title} | Status: {status}")
        print(f"Descrição: {task.description or 'Sem descrição'}")
    else:
        print("\nTarefa não encontrada.")
    input("\nPressione Enter para continuar...")

def get_task_by_desc(logged_user):
    os.system('cls')
    print("___Localizar Tarefa pela Descrição___")
    task_description = input("Informe a descrição da tarefa: ")
    task = session.query(Task).filter_by(description=task_description, user_id=logged_user.id).first()
    if task:   
        status = "🟢 Concluída" if task.completed else "🔴 Aberta"
        print(f"\nTarefa localizada com sucesso!")
        print(f"ID: {task.id} | Título: {task.title} | Status: {status}")
        print(f"Descrição: {task.description or 'Sem descrição'}")
    else:
        print("\nTarefa não encontrada.")
    input("\nPressione Enter para continuar...")
    
def delete_task(logged_user):
    os.system('cls')
    print("___Deletar Tarefa___")
    title = input("Informe o título da tarefa que deseja deletar: ")
    deleted_task = session.query(Task).filter_by(title=title, user_id=logged_user.id).first()
    if deleted_task:
        print("\nTarefa localizada!\n")
        confirmacao = input("\nDigite 'SIM' para confirmar a exclusão: ")
        if confirmacao.upper() == 'SIM':
            session.delete(deleted_task)
            session.commit()
            print("\nTarefa deletada com sucesso!")
        else:
            print("\nExclusão cancelada.")    
    else:
        print("\nTarefa não encontrada.")
    input("\nPressione Enter para continuar...")