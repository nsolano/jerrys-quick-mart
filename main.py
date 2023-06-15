from classes.errors import (InsufficientQuantityError, InvalidInputError,
                    ItemNotFoundError)
from classes.logger import ErrorLogger
from interfaces.menu import StoreMenu

LOGGER = ErrorLogger()


def main():
    """
    The main function that runs the store application.
    """
    menu = StoreMenu()
    while True:
        menu.display_menu()
        choice = menu.get_user_choice()
        try:
            menu.validate_choice(choice)
            menu.process_choice(choice)
        except InvalidInputError:
            error_message = f"Invalid input: {choice}"
            print(f"{error_message}, please try again!!")
            LOGGER.log_error(error_message)
        except ItemNotFoundError as infe:
            error_message = f"Item not found error: {infe}"
            print(error_message)
            LOGGER.log_error(error_message)
        except InsufficientQuantityError as iqe:
            error_message = f"Insufficient Quantity Error: {iqe}"
            print(error_message)
            LOGGER.log_error(error_message)


if __name__ == "__main__":
    main()
