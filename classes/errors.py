class ItemNotFoundError(Exception):
    """
    Custom exception class for item not found errors.
    Raised when an item is not found in the store's inventory.
    """
    pass

class InsufficientQuantityError(Exception):
    """
    Custom exception class for insufficient quantity errors.
    Raised when the requested quantity of an item exceeds the available quantity in the store's inventory.
    """
    pass

class InvalidInputError(Exception):
    """
    Custom exception class for invalid input errors.
    Raised when an invalid input is provided in the store application's user interface.
    """
    pass