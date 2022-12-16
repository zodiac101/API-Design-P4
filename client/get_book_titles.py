from client.inventory_client import InventoryClient


def get_book_title(grpc_client, ISBNs):
    """
    Get the title of a books from the inventory server.
    :param grpc_client: Client object to communicate with the server.
    :param ISBNs: ISBNs of the books to get the title of.
    :return: List of titles of the books.
    """
    list_of_books = []
    for ISBN in ISBNs:
        response, message = grpc_client.get_book(ISBN)
        if response:
            list_of_books.append(response.title)
            continue
    return list_of_books


if __name__ == '__main__':
    """
    Main entry point for the client. Creates a client object and calls the get_book_title function.
    """
    inventory_client = InventoryClient('localhost', 50051)
    test_ISBNs = ['2', '1']
    books_list = get_book_title(inventory_client, test_ISBNs)
    print(books_list)