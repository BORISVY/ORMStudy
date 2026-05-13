from sqlalchemy import ForeignKey, String, create_engine
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, sessionmaker
import os
import bcrypt

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(255))
    tasks: Mapped[List["Task"]] = relationship(back_populates="autor")

class Task(Base):
    __tablename__ = "tasks"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(40), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(200))
    autor: Mapped["User"] = relationship(back_populates="tasks")

engine = create_engine("sqlite:///database.db")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def login():
    os.system('cls')
    print("___Login___")
    email = input("Email: ")
    password = input("Senha: ")
    user = session.query(User).filter_by(email=email).first()
    if user:
        password_bytes = password.encode('utf-8')
        hashed_bytes = user.password.encode('utf-8')
        if bcrypt.checkpw(password_bytes, hashed_bytes):
            print(f"Bem-vindo de volta, {user.username}!")
            input("\nPressione Enter para continuar...")
            return user
    print("Email ou senha inválidos!")
    input("\nPressione Enter para continuar...")
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
    
def main():
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
            logged_user = login()

        if opt == "2":
            new_user()
        
        elif opt == "0":
            print("Saindo...")
            break
 
        else:
            print("Opção inválida.")
            input("\nPressione Enter para continuar...")
        continue

    os.system('cls')
    print(f"\n___ Menu Principal (Logado como: {logged_user.username}) ___")
    print("1 - Cadastrar Usuário")
    print("2 - Editar Nome de Usuário")
    print("3 - Deletar Usuário")
    print("4 - Localizar Usuário por Nome")
    print("5 - Localizar Todos os Usuários")
    print("6 - Adicionar Tarefa")
    print("7 - Editar Nome da Tarefa")
    print("8 - Editar Descrição da Tarefa")
    print("9 - Completar Tarefa")
    print("10 - Reabrir tarefa")
    print("11 - Imprimir Tarefas")
    print("12 - Localizar Tarefa por Titulo")
    print("13 - Localizar Tarefa por Descrição")
    print("14 - Deletar Tarefa")
    opt = input("Escolha uma opção: ")

    if opt == "1":
        new_user()
        
if __name__ == "__main__":
    main()
                