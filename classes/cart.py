from classes.errors import ItemNotFoundError

class Cart:
    """
    Represents a cart for storing and managing items.

    Attributes:
        items (dict): A dictionary containing the items in the cart.
    """
    def __init__(self):   
        """
        Initializes a Cart object.
        """     
        self._items = []       

    @property
    def items(self):
        """
        Item property
        """
        return self._items

    @items.setter
    def items(self, value):
        """
        Setter  for the items property
        """
        self._items = value

    @items.deleter    
    def items(self):
        """
        Deleter for the items property
        """
        self._items = []

    def add_item(self, item, quantity):
        """
        Adds an item to the cart with the specified quantity.

        Args:
            item (str): The item to add.
            quantity (int): The quantity of the item to add.
        """  
        self._items.append((item, quantity)) 
           
    def remove_item(self, item):
        """
        Removes an item from the cart.

        Args:
            item (str): The item to remove.

        Raises:
            ItemNotFoundError: If the item is not found in the cart.
        """
        for i, (cart_item, _) in enumerate(self._items):
            if cart_item == item:
                del self._items[i]
                break
        else:
            raise ItemNotFoundError("Item not found in the cart.")    

    def calculate_total(self, store, rewards_member): 
        """
        Calculates the price, tax, quantity and total for every item.

        Args:
            store (Store): The store object containing the inventory and pricing information.
            rewards_member (bool): Indicates whether the customer is a rewards member.

        
        Returns:
            dict: The price of the item.
        """      
        result = {}
        for item, quantity in self._items:           
            price = store.get_item_price(item, rewards_member)                        
            subtotal = price * quantity
            taxes = 0.0    
            if store.get_item_tax_status(item) == 'Taxable':
                taxes = subtotal * 0.065
                subtotal *= 1.065  # Apply 6.5% tax rate
            result[item] = {
                    "quantity": int(quantity),
                    "unit_price": price,
                    "unit_tax" : taxes,
                    "total": subtotal,
                }                                   
        return result