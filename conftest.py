import  pytest

from main import BooksCollector

@pytest.fixture
def name_book():
    name_book = BooksCollector.name = "Унесенные ветром"
    return name_book

@pytest.fixture
def rating_book():
    rating_book = BooksCollector.rating = 6
    return rating_book