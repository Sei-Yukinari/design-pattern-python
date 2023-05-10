from collections.abc import Iterable, Iterator

from book import Book


class BookShelf(Iterable):
    def __init__(self, maxsize: int) -> None:
        self._books: list[Book] = [Book("")] * maxsize
        self._last = 0

    def get_book_at(self, index: int) -> Book:
        return self._books[index]

    def append_book(self, book: Book) -> None:
        self._books[self._last] = book
        self._last += 1

    def get_length(self) -> int:
        return self._last

    def __iter__(self) -> Iterator[Book]:
        return BookShelfIterator(self)


class BookShelfIterator(Iterator):
    def __init__(self, book: BookShelf) -> None:
        self._book = book
        self._index = 0

    def _has_next(self) -> bool:
        if self._index < self._book.get_length():
            return True
        else:
            return False

    def __next__(self) -> Book:
        if not self._has_next():
            raise StopIteration()
        book = self._book.get_book_at(self._index)
        self._index += 1
        return book
