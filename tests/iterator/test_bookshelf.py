import pytest

from iterator.book import Book
from iterator.book_shelf import BookShelf


@pytest.fixture
def init_book_shelf():
    book_shelf = BookShelf(2)
    book_shelf.append_book(Book("AAA"))
    return book_shelf


def test_get_book_at(init_book_shelf):
    assert init_book_shelf.get_book_at(0) == Book("AAA")


def test_append_book(init_book_shelf):
    print(init_book_shelf.get_length())
    init_book_shelf.append_book(Book("BBB"))
    assert init_book_shelf.get_length() == 2


def test_get_length(init_book_shelf):
    assert init_book_shelf.get_length() == 1
