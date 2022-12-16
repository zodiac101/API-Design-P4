import grpc

from service import inventory_service_pb2, book_pb2
from service.inventory_service_pb2_grpc import InventoryServiceStub


class InventoryClient:
    """
    Client code for the inventory server.
    """
    def __init__(self, host, port):
        """
        Initialize the client object.
        :param host: host of the server.
        :param port: port of the server.
        """
        self.host = host
        self.port = port

    def get_book(self, ISBN):
        """
        Get the title of a book from the inventory server.
        :param ISBN: ISBN of the book to get the title of.
        :return: Book object and response message.
        """
        if not ISBN:
            return None, 'ISBN is required'
        try:
            with grpc.insecure_channel(f'{self.host}:{self.port}') as channel:
                stub = InventoryServiceStub(channel)
                response = stub.GetBook(inventory_service_pb2.GetBookRequest(ISBN=ISBN))
                if not response.response_status.code:
                    return response.book, response.response_status.message
                return None, response.response_status.message
        except Exception as e:
            return None, str(e)

    def create_book(self, ISBN, title, author, year, genre):
        """
        Create a book in the inventory server.
        :param ISBN: ISBN of the book to create.
        :param title: Title of the book to create.
        :param author: Author of the book to create.
        :param year: Year of the book to create.
        :param genre: Genre of the book to create.
        :return: True if the book was created successfully, False otherwise. Along with the response message.
        """

        try:
            genre = book_pb2.Genre.Value(genre)
        except ValueError:
            return False, 'Invalid genre'

        try:
            year = int(year)
        except ValueError:
            return False, 'Invalid year'

        try:
            book = book_pb2.Book(
                ISBN=ISBN,
                title=title,
                author=author,
                year=year,
                genre=book_pb2.Genre.Value(genre)
            )
        except ValueError:
            return False, 'Invalid book'

        try:
            with grpc.insecure_channel(f'{self.host}:{self.port}') as channel:
                stub = InventoryServiceStub(channel)
                response = stub.CreateBook(inventory_service_pb2.CreateBookRequest(book=book))
                if not response.response_status.code:
                    return True, response.response_status.message
                return False, response.response_status.message
        except Exception as e:
            return False, str(e)

