from service.book_pb2 import Book, Genre


def fetch_book_data():
    """
    This function is used to fetch the book data from the database (or any other source).
    It is hardcoded in the example for simplicity. In a real application, this function would
    fetch the data from a database.
    :return: dict of books. Key is ISBN and value is Book object
    """
    data = {
        "1": Book(ISBN="1", title="The Lord of the Rings", author="J.R.R. Tolkien", year=1954, genre=Genre.FANTASY),
        "2": Book(ISBN="2", title="The Hobbit", author="J.R.R. Tolkien", year=1937, genre=Genre.FANTASY),
        "3": Book(ISBN="3", title="The Hitchhiker's Guide to the Galaxy", author="Douglas Adams", year=1979, genre=Genre.ADVENTURE),
    }
    return data