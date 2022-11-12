from Unit_testing.main import BooksCollector

class TestBooksCollector:

    def test_books_rating_is_dict(self):
        books = BooksCollector()
        assert type(books.books_rating) == dict

    def test_favorites_is_list(self):
        f_list = BooksCollector()
        assert type(f_list.favorites) == list


