import re
from data import CommandOptions, VALID_PATH_REGEX
from typing import List


class BaseValidator:
    @classmethod
    def validate_path(cls, path: str) -> bool:
        if path == '/':
            return True

        if not re.match(pattern=VALID_PATH_REGEX, string=path):
            print(f'Invalid path: {path}')
            return False
        
        return True

    @classmethod
    def validate_command_length(cls, command: List[str], length: int) -> bool:
        if len(command) != length:
            print(f'Invalid command length for {command[0]}')
            return False
        
        return True


class CommandValidator(BaseValidator):
    def __init__(self, raw_command: str, options: List[str]) -> None:
        self.raw_command = raw_command
        self.options = options
        self.clean_command: List[str] = ''

    def validate(self) -> bool:
        command_units = self.raw_command.split(' ')

        if not command_units:
            print('Invalid command')
            return False

        command = command_units[0]

        if command not in self.options:
            print('Command not in the options')
            return False

        command = CommandOptions(command)

        command_units[0] = command

        self.clean_command = command_units

        if command in [CommandOptions.CREATE, CommandOptions.DELETE]:
            self.create_delete_validate()
        elif command == CommandOptions.MOVE:
            self.move_validate()

        return True

    def create_delete_validate(self) -> bool:
        if not self.validate_command_length(command=self.clean_command, length=2):
            return False

        path = self.clean_command[1]

        return self.validate_path(path=path)

    def move_validate(self) -> bool:
        if not self.validate_command_length(
            command=self.clean_command, length=3
        ):
            return False
        
        from_path = self.clean_command[1]
        to_path = self.clean_command[2]

        return (
            self.validate_path(path=from_path) and
            self.validate_path(path=to_path)
        )

