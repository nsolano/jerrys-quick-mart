from datetime import date

today = date.today()


class Receipt:
    """
    Represents a receipt for a transaction.

    Attributes:
        receipt_file (str): The path to the receipt file.
    """
    def __init__(self, receipt_file):
        """
        Initializes a Receipt object with the specified receipt file.

        Args:
            receipt_file (str): The path to the receipt file.
        """
        self._receipt_file = receipt_file

    def generate_receipt(self, cart, store, rewards_member):
        """
        Generates a receipt based on the provided cart, store, and rewards membership information.

        Args:
            cart (Cart): The cart containing the items for the receipt.
            store (Store): The store object containing the inventory and pricing information.
            rewards_member (bool): Indicates whether the customer is a rewards member.
        """
        with open(self._receipt_file, "w") as file:
            file.write(today.strftime("%B %d, %Y"))
            file.write(f"\n")
            file.write(f"Transaction No. 000001")            
            file.write(f"\n")
            if rewards_member:
                file.write(f"Client is a rewards member\n")
            else:
                file.write(f"Client is not a rewards member\n")
            file.write(f"\n")
            file.write(f"Item      Quantity      Unit Price    Tax       Total\n")
            file.write(f"\n")
            total = 0.0
            taxes = 0.0
            items_sold = 0
            result = cart.calculate_total(store, rewards_member)
            for item, details in result.items():
                quantity = details["quantity"]
                unit_price = details["unit_price"]
                unit_tax = details["unit_tax"]
                unit_total = details["total"]
                total += unit_total
                taxes += unit_tax
                items_sold += 1
                file.write(
                    f"{item}:        {quantity}       x    ${unit_price}  +   ${unit_tax:.2f}  =   ${unit_total:.2f}\n"
                )
            print(f"Total amount: ${total:.2f}, Taxes: ${taxes:.2f}")
            file.write(f"\n")
            file.write(f"**************************")
            file.write(f"\n")
            file.write(f"Items sold: {items_sold}\n")
            file.write(f"Taxes: ${taxes:.2f}\n")
            file.write(f"Total: ${total:.2f}\n")
