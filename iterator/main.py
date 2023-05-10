from iterator.book import Book
from iterator.book_shelf import BookShelf


def main() -> None:

    book_shelf = BookShelf(4)
    book_shelf.append_book(Book("Around the World in 80 Days"))
    book_shelf.append_book(Book("Bible"))
    book_shelf.append_book(Book("Cinderella"))
    book_shelf.append_book(Book("Daddy-Long-Legs"))

    # 明示的にIteratorを使う方法
    it = book_shelf.__iter__()
    while True:
        try:
            book = next(it)
        except StopIteration:
            break
        print(book.name)
    print()

    # for文を使う方法
    for book in book_shelf:
        print(book.name)
    print()


if __name__ == "__main__":
    main()
