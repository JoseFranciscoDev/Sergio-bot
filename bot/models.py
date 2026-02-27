from sqlalchemy import create_engine, Table, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
import settings  # noqa
from os import getenv

engine = create_engine(
    getenv("DB_URL"),
)

Base = declarative_base()


class Saldo(Base):
    __tablename__ = "saldo"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    saldo: Mapped[int] = mapped_column(Integer, default=0)
    user: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    user: Mapped["User"] = relationship("User", back_populates="saldo")


class User(Base):
    __tablename__ = "user"
    saldo: Mapped["Saldo"] = relationship(back_populates="user")
    __table__ = Table("user", Base.metadata, autoload_with=engine)


class Message(Base):
    __tablename__ = "message"

    __table__ = Table("message", Base.metadata, autoload_with=engine)


class Chat(Base):
    __tablename__ = "chat"

    __table__ = Table("chat", Base.metadata, autoload_with=engine)


class ChatUser(Base):
    __tablename__ = "chat_user"

    __table__ = Table("chat_user", Base.metadata, autoload_with=engine)


# print(User.metadata.tables)
# print(User.metadata.tables)
# print(User.metadata.tables)
# print(ChatUser.metadata.tables)

# from os import getenv
# import datetime
# import bot_instance
# from sqlalchemy import (
#     BigInteger,
#     Column,
#     ForeignKeyConstraint,
#     Index,
#     String,
#     TIMESTAMP,
#     Table,
#     Text,
#     text,
#     create_engine,
# )
# from sqlalchemy.dialects.mysql import TINYINT
# from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
# from sqlalchemy.ext.automap import automap_base

# engine = create_engine(
#     getenv("DB_URL", ""),
# )

# # Produzir um mapeamento automágico
# Base = automap_base()
# Base.prepare(autoload_with=engine)

# # Mapear classes (os nomes devem coincidir com as tabelas)
# print(Base.classes.user)


# class Chat(Base):
#     __tablename__ = "chat"
#     __table_args__ = (Index("id_telegram_chat", "id_telegram_chat", unique=True),)

#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     type: Mapped[str] = mapped_column(String(20), nullable=False)
#     id_telegram_chat: Mapped[Optional[int]] = mapped_column(BigInteger)
#     is_active: Mapped[Optional[int]] = mapped_column(
#         TINYINT(1), server_default=text("'1'")
#     )

#     users: Mapped[list["User"]] = relationship(
#         "User", secondary="chat_user", back_populates="chats"
#     )
#     messages: Mapped[list["Message"]] = relationship("Message", back_populates="chat")


# class Vagabundo(Base):
#     __tablename__ = "vagabundo"

#     id: Mapped[int] = mapped_column(primary_key=True)


# class User(Base):
#     __tablename__ = "user"
#     __table_args__ = (
#         Index("id", "id", unique=True),
#         Index("id_telegram_user", "id_telegram_user", unique=True),
#     )

#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     id_telegram_user: Mapped[int] = mapped_column(BigInteger, nullable=False)
#     username: Mapped[Optional[str]] = mapped_column(String(200))
#     contact: Mapped[Optional[str]] = mapped_column(String(200))
#     first_name: Mapped[Optional[str]] = mapped_column(String(200))
#     last_name: Mapped[Optional[str]] = mapped_column(String(200))
#     is_active: Mapped[Optional[int]] = mapped_column(
#         TINYINT(1), server_default=text("'1'")
#     )
#     created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
#         TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
#     )

#     chats: Mapped[list["Chat"]] = relationship(
#         "Chat", secondary="chat_user", back_populates="users"
#     )
#     messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")


# t_chat_user = Table(
#     "chat_user",
#     Base.metadata,
#     Column("id_user", BigInteger, primary_key=True),
#     Column("id_chat", BigInteger, primary_key=True),
#     ForeignKeyConstraint(["id_chat"], ["chat.id"], name="chat_user_ibfk_1"),
#     ForeignKeyConstraint(["id_user"], ["user.id"], name="chat_user_ibfk_2"),
# )


# class Message(Base):
#     __tablename__ = "message"
#     __table_args__ = (
#         ForeignKeyConstraint(
#             ["id_chat"], ["chat.id"], ondelete="RESTRICT", name="message_ibfk_1"
#         ),
#         ForeignKeyConstraint(
#             ["id_user"], ["user.id"], ondelete="RESTRICT", name="message_ibfk_2"
#         ),
#         Index("id_chat", "id_chat"),
#         Index("id_user", "id_user"),
#     )

#     id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
#     id_telegram_message: Mapped[int] = mapped_column(BigInteger, unique=True)
#     content: Mapped[str] = mapped_column(Text, nullable=False)
#     role: Mapped[str] = mapped_column(String(5), nullable=False)
#     id_chat: Mapped[int] = mapped_column(BigInteger, nullable=False)
#     id_user: Mapped[int] = mapped_column(BigInteger, nullable=False)
#     created_at: Mapped[Optional[datetime.datetime]] = mapped_column(
#         TIMESTAMP, server_default=text("CURRENT_TIMESTAMP")
#     )
#     is_active: Mapped[Optional[int]] = mapped_column(
#         TINYINT(1), server_default=text("'1'")
#     )

#     chat: Mapped["Chat"] = relationship("Chat", back_populates="messages")
#     user: Mapped["User"] = relationship("User", back_populates="messages")
