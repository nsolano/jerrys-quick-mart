from classes.errors import InsufficientQuantityError, ItemNotFoundError


class Store:
    """
    Represents a store with inventory and pricing information.

    Attributes:
        inventory_file (str): The path to the inventory file.
        inventory (dict): A dictionary containing the inventory information.
    """
    def __init__(self, inventory_file):
        """
        Initializes a Store object with the given inventory file.

        Args:
            inventory_file (str): The path to the inventory file.
        """
        
        self._inventory = {}
        self.file = inventory_file
        self._load_inventory(inventory_file)

    def _load_inventory(self, inventory_file):
        """
        Loads the inventory from the inventory file.

        Returns:
            dict: A dictionary containing the inventory information.
        """
        with open(inventory_file, "r") as file:
            for line in file:
                (
                    item_and_quantity,
                    reg_price,
                    mem_price,
                    tax_status,
                ) = line.strip().split(", ")
                item, quantity = item_and_quantity.strip().split(": ")
                self._inventory[item] = {
                    "quantity": int(quantity),
                    "regular_price": float(reg_price[1:]),  # Removing '$' sign
                    "member_price": float(mem_price[1:]),  # Removing '$' sign
                    "tax_status": tax_status,
                }

    def save_inventory(self):
        """
        Saves the inventory to the inventory file.

        Returns:
            file: A modified inventory file.
        """

        with open(self.file, "w") as file:
            for item, details in self._inventory.items():
                quantity = details["quantity"]
                regular_price = details["regular_price"]
                member_price = details["member_price"]
                tax_status = details["tax_status"]                
                file.write(
                    f"{item}: {quantity}, ${regular_price:.2f}, ${member_price:.2f}, {tax_status}\n"
                )

    def get_item_price(self, item, rewards_member):
        """
        Retrieves the price of the given item.

        Args:
            item (str): The item to retrieve the tax status for.
            rewards_member (bool): Indicates whether the customer is a rewards member.

        Returns:
            str: The price of the item.

        Raises:
            ItemNotFoundError: If the item is not found in the inventory.
        """
        if item in self._inventory:
            return (
                self._inventory[item]["member_price"]
                if rewards_member
                else self._inventory[item]["regular_price"]
            )
        raise ItemNotFoundError("Item not found in the inventory.")

    def get_item_tax_status(self, item):
        """
        Retrieves the tax status of the given item.

        Args:
            item (str): The item to retrieve the tax status for.

        Returns:
            str: The tax status of the item.

        Raises:
            ItemNotFoundError: If the item is not found in the inventory.
        """
        
        if item in self._inventory:
            return self._inventory[item]["tax_status"]
        else:
            raise ItemNotFoundError(f"{item} not found in the inventory.")

    def update_inventory(self, item, quantity):
        """
        Updates the inventory by reducing the quantity of the given item.

        Args:
            item (str): The item to update.
            quantity (int): The quantity to subtract from the current inventory.
        """
        self._inventory[item]["quantity"] -= quantity

    def is_item_available(self, item, quantity):
        if item in self._inventory:
            if self._inventory[item]["quantity"] >= quantity:
                return True
            else:
                raise InsufficientQuantityError(
                    "Insufficient quantity available for the item."
                )
        else:
            raise ItemNotFoundError("Item not found in the inventory.")
