import pytest
from unittest.mock import MagicMock
from services import FolderStructure
from data import CommandOptions


@pytest.mark.parametrize('command', [
    CommandOptions.CREATE,
    CommandOptions.DELETE,
    CommandOptions.LIST,
    CommandOptions.MOVE
])
def test__file_structure__execute(command, mocker, folder_structure):
    mock = MagicMock()
    mocker.patch.object(
        FolderStructure,
        command.value.lower(),
        return_value=mock
    )

    folder_structure.command = [command, '']

    folder_structure.execute()

    getattr(FolderStructure, command.value.lower()).assert_called()


@pytest.mark.parametrize(
    'path', [
        'root/videos',
        'root/images',
        'lib',
        'root/documents/document1'
    ],
)
def test__file_structure__create(path, folder_structure):
    folder_structure.command = [CommandOptions.CREATE, path]

    folder_structure.execute()

    chain = path.split('/')

    sub_folder = folder_structure.tree

    for folder in chain:
        assert folder in sub_folder
        sub_folder = sub_folder[folder]


@pytest.mark.parametrize(
    'path', [
        'var/www/website',
        'etc',
        'root/home'
    ]
)
def test__file_structure__delete(path, folder_structure):
    folder_structure.command = [CommandOptions.DELETE, path]

    folder_structure.execute()

    chain = path.split('/')

    sub_folder = folder_structure.tree

    for folder in chain[:-1]:
        sub_folder = sub_folder[folder]

    assert chain[-1] not in sub_folder


@pytest.mark.parametrize(
    'from_to', [
        ('var/www/website', 'etc'),
        ('etc', 'root/documents'),
        ('root/home', 'var/www')
    ]
)
def test__file_structure__move(from_to, folder_structure):
    folder_structure.command = [CommandOptions.DELETE, *from_to]

    folder_structure.execute()

    obj = from_to[0].split('/')

    chain = from_to[1].split('/')

    sub_folder = folder_structure.tree

    for folder in chain:
        sub_folder = sub_folder[folder]

    assert obj[-1] not in sub_folder




