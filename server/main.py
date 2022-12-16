import logging
from server.inventory_server import InventoryServer

if __name__ == '__main__':
    """
    Main entry point for the inventory server. Enables logging and starts the server.
    """
    logging.basicConfig()
    logging.getLogger().setLevel(logging.INFO)

    server = InventoryServer()
    server.start_server()

