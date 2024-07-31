from typing import List
from enum import Enum


VALID_PATH_REGEX = r'^([^/]+(?:/[^/]+)*)$'

STORAGE_FILE = 'tree.txt'

INDENT_SIZE = 2

class CommandOptions(Enum):
    CREATE = 'CREATE'
    LIST = 'LIST'
    MOVE = 'MOVE'
    DELETE = 'DELETE'
    EXIT = 'EXIT'

    @classmethod
    def list(cls) -> List[str]:
        return [e.value for e in cls]


