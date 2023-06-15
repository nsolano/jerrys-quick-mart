from classes.cart import Cart
from classes.customer import Customer
from classes.receipt import Receipt
from classes.store import Store

from classes.errors import InvalidInputError

store = Store("databases/inventory.txt")
cart = Cart()
customer = Customer(False)  # Regular customer by default
receipt = Receipt("assets/receipt.txt")


class StoreMenu:
    """
    Represents a menu for a store application.

    Attributes:
        menu_options (dict): A dictionary mapping menu options to their descriptions.
    """

    def __init__(self):
        """
        Initializes a StoreMenu object.
        """
        self.menu_options = {
            "1": "Select customer type",
            "2": "Add item to cart",
            "3": "Remove item",
            "4": "View cart",
            "5": "Checkout and print receipt",
            "6": "Cancel transaction",
            "7": "Exit",
        }

    def display_menu(self):
        """
        Displays the menu options.
        """
        print("===== Jerrys Quick Mart =====")
        for option, description in self.menu_options.items():
            print(f"{option}. {description}")

    def get_user_choice(self):
        """
        Gets the user's choice from the menu.

        Returns:
            str: The user's choice.
        """
        user_choice = input("Enter your choice: ")
        return user_choice

    def validate_choice(self, choice):
        """
        Validates the user's choice.

        Args:
            choice (str): The user's choice.

        Returns:
            bool: True if the choice is valid, False otherwise.

        Raises:
            InvalidInputError: If the choice is not valid.
        """
        if choice in self.menu_options:
            return True
        raise InvalidInputError

    def process_choice(self, choice):
        """
        Processes the user's choice and performs the corresponding action.

        Args:
            choice (str): The user's choice.
        """
        if choice == "1":
            self.select_customer_type()
        elif choice == "2":
            self.add_item_to_cart()
        elif choice == "3":
            self.delete_item_from_cart()
        elif choice == "4":
            self.view_cart()
        elif choice == "5":
            self.checkout()
        elif choice == "6":
            self.cancel_transaction()
        elif choice == "7":
            print("Exiting...")
            exit()

    def select_customer_type(self):
        """
        Prompts the user to select the customer type (rewards member or regular customer).
        """
        customer_type = input("Are you a rewards member? (Y/N): ")
        rewards_member = True if customer_type.upper() == "Y" else False
        customer.rewards_member = rewards_member
        print(customer)

    def add_item_to_cart(self):
        """
        Prompts the user to add an item to the cart.
        """
        item = input("Enter the item: ")
        quantity = int(input("Enter the quantity: "))
        store.is_item_available(item, quantity)
        cart.add_item(item, quantity)
        store.update_inventory(item, quantity)
        print(f"{quantity} {item}(s) added to the cart.")

    def delete_item_from_cart(self):
        """
        Prompts the user to remove an item from the cart.
        """
        item_name = input("Enter the name of the item to remove (All for empty cart): ")
        if item_name.title() == "All":
            del cart.items
        else:
            cart.remove_item(item_name)

    def view_cart(self):
        """
        Displays the contents of the cart.
        """
        print("--- Cart ---")
        for item, quantity in cart.items:
            print(f"{item}: {quantity}")

    def checkout(self):
        """
        Performs the checkout process.
        """
        rewards_member = customer.rewards_member
        print("Checkout successful!")         
        receipt.generate_receipt(cart, store, rewards_member)               
        store.save_inventory()
        del cart.items

    def cancel_transaction(self):
        """
        Cancels the current transaction and clears the cart.
        """
        del cart.items
        print("Transaction canceled. Cart cleared.")
