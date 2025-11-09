import os

CHAT_ID_FILE = "subscribers.txt"

def save_chat_id(chat_id: int):
    """Salva um chat_id no arquivo, se ele já não existir."""
    try:
        if not os.path.exists(CHAT_ID_FILE):
            with open(CHAT_ID_FILE, "w") as f:
                pass 

        with open(CHAT_ID_FILE, "r") as f:
            existing_ids = f.read().splitlines()
          
        if str(chat_id) not in existing_ids:
            with open(CHAT_ID_FILE, "a") as f:
                f.write(f"{chat_id}\n")
            print(f"Novo ID salvo: {chat_id}")
            
    except Exception as e:
        print(f"Erro ao salvar chat_id: {e}")
        
def get_all_chat_ids():
    """Busca todos os chat_ids salvos"""
    try:
        with open(CHAT_ID_FILE, "r") as f:
            ids = f.read().splitlines()
        return ids
    except FileNotFoundError:
        print("Arquivo de IDs não encontrado.")
        return []