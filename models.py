from sqlalchemy import ForeignKey, String, create_engine
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase, sessionmaker
import os

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

class Menu():
    def __init__(self):
        Session = sessionmaker(bind=engine)
        session = Session()
        while True:
            print("Menu Iniciar")
            print("1- Cadastro de Usuários")
            print("2- Consultar usuários")
            print("3- Consultar usuário por nome")
            opt = input("Selecione a opção desejada:")

            if opt == "1":
                os.system('cls')
                print("___Cadastro de Usuários___")
                username = input("Informe o nome de usuário: ")
                email = input("Informe o email: ")
                password = input("Crie a senha para usuário: ")
                new_user = User(username=username, email=email, password=password)
                session.add(new_user)
                session.commit()
                print("Usuários cadastrado com sucesso!")
            
            elif opt == "2":
                os.system('cls')
                print("____Consulta de Usuários___")
                users = session.query(User).all()
                for u in users:
                    print(f"ID: {u.id} | Nome: {u.username} | Email: {u.email}")

            elif opt == "3":
                os.system('cls')
                print("___Localizar Usuários Por Nome___")
                name_user = input("Digite o nome do usuário a ser consultado: ")
                locate_user = session.query(User).filter(User.username == name_user).first()
                if not locate_user:
                    print("Usuário não encontrado")
                else:
                    print(f"ID: {locate_user.id}, Nome: {locate_user.username}, Email: {locate_user.email}")

            else:
                print("Opção inválida.")

if __name__ == "__main__":
    Menu()
                