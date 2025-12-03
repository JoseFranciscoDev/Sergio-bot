class Message:
    def __init__(self, role: str, text: str) -> None:
        self.role: str = role
        self.text: str | None = text
    def __str__(self) -> str:
        return f"role: {self.role} e de text: {self.text}"


"""Um dicionario, cada indice é um id de usuario e recebe como valor outro dicionario
que nesse por sua vez tem como chave uma string e como valor deve ser um objeto Message"""
bot_history_chats: dict[int, list[Message]] = {}


def get_history(chat_id: int) -> list[Message]:
    if chat_id not in bot_history_chats:
        bot_history_chats[chat_id] = []
    return bot_history_chats[chat_id]

def add_message(chat_id: int, message: str | None, role: str) -> None:  
    history: list[Message] = get_history(chat_id)
    history.append(Message(role=role, text=str(message)))
