from settings import COMMANDS
from typing import Callable


def add_command(func: Callable):
    command = func.__name__.split("command_")
    command.pop(0)
    COMMANDS.add("".join(command))

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func

    return wrapper
