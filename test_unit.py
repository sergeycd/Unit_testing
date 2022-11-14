from main import col_book

class TestBooksCollector:

    def test_books_rating_is_dict(self):
        assert type(col_book.books_rating) == dict

    def test_favorites_is_list(self):
        assert type(col_book.favorites) == list

    # Тестирование добавления книги
    def test_add_new_book_name_book_will_add(self, name_book):
        col_book.add_new_book(name_book)
        assert "Унесенные ветром" in col_book.books_rating and col_book.books_rating["Унесенные ветром"] == 1


    # Проверка корректности установки рейтинга
    def test_set_book_rating_name_rating_get_actual_rating(self, name_book, rating_book):
        col_book.set_book_rating(name_book, rating_book)
        assert col_book.books_rating["Унесенные ветром"] == 6


    #Проверка получения рейтинга по названию книги
    def test_get_book_rating_name_get_rating_of_book(self, name_book):
        assert col_book.get_book_rating(name_book) == col_book.books_rating[name_book]

    # Проверка фильтрации книг по рейтингу
    def test_get_books_with_specific_rating_rating_get_list_with_names_of_books(self, rating_book):
        assert type(col_book.get_books_with_specific_rating(rating_book)) == list and len(col_book.get_books_with_specific_rating(rating_book)) == 1

    # Проверяем словарь books_rating
    def test_get_books_rating_get_dict(self, name_book, rating_book):
        assert col_book.books_rating == {name_book: rating_book}

    #Проверяем добавление книги в избранное
    def test_add_book_in_favorites_name_book_will_add_in_flist(self, name_book):
        col_book.add_book_in_favorites(name_book)
        assert name_book in col_book.favorites

    #Проверяем удаление книги из избранного
    def test_delete_book_from_favorites(self, name_book):
        col_book.delete_book_from_favorites(name_book)
        assert len(col_book.favorites) == 0

    #Проверяем список любимых книг
    def test_get_list_of_favorites_books(self):
        assert type(col_book.favorites) == list and len(col_book.favorites) == 0
