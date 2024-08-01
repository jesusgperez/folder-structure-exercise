import pytest
from faker import Faker
from services import FolderStructure

faker = Faker()


@pytest.fixture
def folder_structure():
    tree = {
        'root': {
            'home': {},
            'documents': {},
            'bin': {}
        },
        'etc': {
            'postgresql': {}
        },
        'var': {
            'www': {
                'website': {}
            }
        },
        'tmp': {}
    }

    return FolderStructure(tree=tree)
