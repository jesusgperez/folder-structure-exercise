from data import CommandOptions
from services import (
    FolderStructure, 
    CommandValidator,
    PersistanceManager,
    FolderBuilder
)


if __name__ == '__main__':
    print('''
            Welcome to the file structure app, please select one of the next options:
            CREATE <path>: Creates a new folder
            LIST: Lists the current folder structure
            MOVE <path_from> <path_to>: Moves a given folder to another place
            DELETE <path>: Deletes a given folder
            EXIT: exit the application
          ''')
    
    command = ''

    command_options = CommandOptions.list()

    folder_builder = FolderBuilder()

    persistance = PersistanceManager(builder=folder_builder)

    persistance.load()

    while True:
        command = input('Introduce a command: ')

        if command == CommandOptions.EXIT.value:
            persistance.save()
            print('Successfully exited the application')
            break

        validator = CommandValidator(
            raw_command=command, options=command_options
        )

        if not validator.validate():
            continue

        folder_builder.add_command(command=validator.clean_command)

        structure = folder_builder.build()

        try:
            structure.execute()
        except KeyError:
            print('No such directory')
