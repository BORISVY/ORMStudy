from sqlalchemy import ForeignKey, String, create_engine
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

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