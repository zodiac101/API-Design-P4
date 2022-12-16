from concurrent import futures

import google
import grpc

from server.Database import fetch_book_data
from service import inventory_service_pb2_grpc, inventory_service_pb2, status_pb2

class InventoryServer(inventory_service_pb2_grpc.InventoryServiceServicer):
    """
    This is the server class which implements the gRPC service.
    """

    def __init__(self):
        """
        This function is used to initialize the server.
        """
        self.data = None
        super().__init__()

    def load_data(self):
        """
        This function is used to load the data from the database.
        :return: None
        """
        self.data = fetch_book_data()

    def CreateBook(self, request, context):
        """
        This function is used to create a book in the database. It corresponds to the CreateBook gRPC method.
        :param request: request object of the CreateBook gRPC method
        :param context: context object of the CreateBook gRPC method
        :return: CreateBookResponse object
        """
        try:
            ISBN = request.book.ISBN
            if ISBN in self.data:
                test =  inventory_service_pb2.CreateBookResponse(
                    response_status=status_pb2.ResponseStatus(
                        code=grpc.StatusCode.ALREADY_EXISTS.value[0],
                        message="Book with ISBN {} already exists".format(ISBN)
                    )
                )
                return test
            else:
                self.data[ISBN] = request.book
                test = inventory_service_pb2.CreateBookResponse(
                    response_status=status_pb2.ResponseStatus(
                        code=grpc.StatusCode.OK.value[0],
                        message="Book with ISBN {} created".format(ISBN)
                    )
                )
                return test
        except Exception as e:
            return inventory_service_pb2.CreateBookResponse(
                response_status=status_pb2.ResponseStatus(
                    code=grpc.StatusCode.INTERNAL.value[0],
                    message="{}".format(e)
                )
            )


    def GetBook(self, request, context):
        """
        This function is used to get a book from the database. It corresponds to the GetBook gRPC method.
        :param request: Request object of the GetBook gRPC method
        :param context: Context object of the GetBook gRPC method
        :return: GetBookResponse object
        """
        try:
            ISBN = request.ISBN
            if ISBN in self.data:
                return inventory_service_pb2.GetBookResponse(
                    book=self.data[ISBN],
                    response_status=status_pb2.ResponseStatus(
                        code=grpc.StatusCode.OK.value[0],
                        message="Book with ISBN {} found".format(ISBN)
                    )
                )
            else:
                return inventory_service_pb2.GetBookResponse(
                    response_status=status_pb2.ResponseStatus(
                        code=grpc.StatusCode.NOT_FOUND.value[0],
                        message="Book with ISBN {} not found".format(ISBN)
                    )
                )
        except Exception as e:
            return inventory_service_pb2.GetBookResponse(
                response_status=status_pb2.ResponseStatus(
                    code=grpc.StatusCode.INTERNAL.value[0],
                    message="{}".format(e)
                )
            )

    def start_server(self):
        """
        This function is used to start the server.
        :return: None
        """
        inventory_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.load_data()
        inventory_service_pb2_grpc.add_InventoryServiceServicer_to_server(self, inventory_server)
        inventory_server.add_insecure_port('[::]:50051')
        inventory_server.start()
        inventory_server.wait_for_termination()