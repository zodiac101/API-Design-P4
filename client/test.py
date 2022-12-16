import unittest
from unittest.mock import Mock

from client.get_book_titles import get_book_title
from client.inventory_client import InventoryClient
from service import book_pb2


class TestClient(unittest.TestCase):
    """
    Test class for the client
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor
        Creates a mock client and a real client object
        """
        super().__init__(*args, **kwargs)

        # Create a mock client
        self.mock_client = Mock(spec=InventoryClient)
        def mock_return_books(ISBN):
            if ISBN == '1':
                return book_pb2.Book(
                    ISBN='1',
                    title='The Lord of the Rings',
                    author='J.R.R. Tolkien',
                    year=1954,
                    genre=book_pb2.Genre.Value('FANTASY')
                ), 'Book with ISBN 1 found'
            elif ISBN == '2':
                return book_pb2.Book(
                    ISBN='2',
                    title='The Hobbit',
                    author='J.R.R. Tolkien',
                    year=1937,
                    genre=book_pb2.Genre.Value('FANTASY')
                ), 'Book with ISBN 2 found'

            return None, 'Book with ISBN {} not found'.format(ISBN)
        self.mock_client.get_book.side_effect = mock_return_books

        # Create a real client
        self.real_client = InventoryClient('localhost', 50051)


    def run_assertions(self, client, ISBNs, expected_titles):
        """
        Run the assertions for the test cases
        :param client: Client object of type InventoryClient
        :param ISBNs: ISBNs to pass to the get_book_title function
        :param expected_titles: Expected titles of the books
        :return: None
        """
        titles = get_book_title(client, ISBNs)
        self.assertEqual(titles, expected_titles)

    def test_mock_client_get_book_titles_correct(self):
        """
        Test the get_book_title function with a mock client (correct)
        :return: None
        """
        self.run_assertions(self.mock_client, ['1', '2'], ['The Lord of the Rings', 'The Hobbit'])

    def test_mock_client_get_book_titles_incorrect(self):
        """
        Test the get_book_title function with a mock client (incorrect)
        :return: None
        """
        self.run_assertions(self.mock_client, ['1', '2', '4'], ['The Lord of the Rings', 'The Hobbit'])

    def test_real_client_get_book_titles_correct(self):
        """
        Test the get_book_title function with a real client (correct)
        :return: None
        """
        self.run_assertions(self.real_client, ['1', '2'], ['The Lord of the Rings', 'The Hobbit'])

    def test_real_client_get_book_titles_incorrect(self):
        """
        Test the get_book_title function with a real client (incorrect)
        :return: None
        """
        self.run_assertions(self.real_client, ['1', '2', '4'], ['The Lord of the Rings', 'The Hobbit'])


