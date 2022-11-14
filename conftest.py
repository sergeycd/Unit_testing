import  pytest

from main import col_book

@pytest.fixture
def name_book():
    name_book = col_book.name = "Унесенные ветром"
    return name_book

@pytest.fixture
def rating_book():
    rating_book = col_book.rating = 6
    return rating_book