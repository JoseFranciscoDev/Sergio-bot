from dotenv import load_dotenv

DEBUG = True
COMMANDS: set = set()
env_file = ".env" if not DEBUG else ".env.local"

load_dotenv(dotenv_path=env_file, override=True)
