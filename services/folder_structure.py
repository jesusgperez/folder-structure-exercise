import json
from typing import Dict, List
from data import CommandOptions, STORAGE_FILE


class FolderStructure:
    def __init__(
        self,
        tree: Dict = {},
        command: List[str] = None
    ) -> None:
        self.tree = tree
        self.command = command
        self.indent = 2

    def find_folder(self, path: str) -> Dict:
        keys = path.split('/')

        sub_dict = self.tree

        for key in keys[:-1]:
            sub_dict = sub_dict[key]

        return sub_dict

    def create(self) -> None:
        path = self.command[1]
        keys = path.split('/')
        update_tree = self.find_folder(path=path)
        update_tree[keys[-1]] = {}


    def list(self) -> None:
        return self._list_recursive(
            tree=self.tree, indent=self.indent
        )

    def _list_recursive(self, tree: Dict, indent: int):
        if not tree:
            return

        str_indent = ' ' * indent

        for key in tree.keys():
            print(f'{str_indent}{key}')
            self._list_recursive(
                tree=tree[key], indent=self.indent + indent
            )

    def move(self) -> None:
        from_path = self.command[1]
        to_path = self.command[2]

        from_folder = self.find_folder(path=from_path)
        from_key = from_path.split('/')[-1]

        if to_path == '/':
            to_folder = self.tree
        else:
            to_folder = self.find_folder(path=to_path)
            to_key = to_path.split('/')[-1]

        buffer = from_folder[from_key]
        del from_folder[from_key]

        if to_path != '/':
            to_folder[to_key][from_key] = buffer
            return

        to_folder[from_key] = buffer
        

    def delete(self) -> None:
        path = self.command[1]
        keys = path.split('/')
        delete_tree = self.find_folder(path=path)
        del delete_tree[keys[-1]]


    def execute(self):
        command_obj = self.command[0]

        if command_obj == CommandOptions.CREATE:
            self.create()
        elif command_obj == CommandOptions.DELETE:
            self.delete()
        elif command_obj == CommandOptions.MOVE:
            self.move()
        else:
            self.list()


class FolderBuilder:
    def __init__(self) -> None:
        self.structure = FolderStructure()

    def add_command(self, command: List[str]):
        self.structure.command = command
        return self
    
    def add_tree(self, tree: Dict):
        self.structure.tree = tree
        return self

    def build(self) -> FolderStructure:
        return self.structure


class PersistanceManager:
    def __init__(self, builder: FolderBuilder) -> None:
        self.builder = builder

    def load(self) -> FolderBuilder:
        with open(STORAGE_FILE, 'r') as f:
            content = f.readline()
            tree = json.loads(content or b'{}')

        self.builder.add_tree(tree=tree)

    def save(self) -> None:
        with open(STORAGE_FILE, 'w') as f:
            f.write(json.dumps(self.builder.build().tree))
