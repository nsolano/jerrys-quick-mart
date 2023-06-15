import unittest
from datetime import date
from classes.cart import Cart
from classes.customer import Customer
from classes.receipt import Receipt
from classes.store import Store
from classes.errors import ItemNotFoundError, InsufficientQuantityError, InvalidInputError


class StoreTest(unittest.TestCase):
    def setUp(self):
        self.store = Store("tests/test_inventory.txt")

    def test_get_item_price_regular_customer(self):
        price = self.store.get_item_price("Milk", rewards_member=False)
        self.assertEqual(price, 3.75)

    def test_get_item_price_rewards_member(self):
        price = self.store.get_item_price("Milk", rewards_member=True)
        self.assertEqual(price, 3.50)

    def test_update_inventory(self):
        initial_quantity = self.store._inventory["Milk"]["quantity"]
        self.store.update_inventory("Milk", 2)
        updated_quantity = self.store._inventory["Milk"]["quantity"]
        self.assertEqual(updated_quantity, initial_quantity - 2)

    def test_is_item_available(self):
        available = self.store.is_item_available("Milk", 5)
        self.assertTrue(available)

        with self.assertRaises(InsufficientQuantityError):
            self.store.is_item_available("Milk", 10)

    def test_get_item_tax_status(self):
        tax_status = self.store.get_item_tax_status("Milk")
        self.assertTrue(tax_status == "Tax-Exempt")

        tax_status = self.store.get_item_tax_status("Red Bull")
        self.assertFalse(tax_status == "Tax-Exempt")

    def tearDown(self):
        self.store = None


class CartTest(unittest.TestCase):
    def setUp(self):
        self.store = Store("tests/test_inventory.txt")
        self.cart = Cart()

    def test_add_item(self):
        self.cart.add_item("Milk", 2)
        self.assertEqual(len(self.cart.items), 1)
        self.assertEqual(self.cart.items[0][0], "Milk")
        self.assertEqual(self.cart.items[0][1], 2)

    def test_remove_item(self):
        self.cart.add_item("Milk", 2)
        self.cart.remove_item("Milk")
        self.assertEqual(len(self.cart.items), 0)

    def test_remove_item_not_found(self):
        with self.assertRaises(ItemNotFoundError):
            self.cart.remove_item("Water")

    def test_calculate_total_regular_customer(self):
        self.cart.add_item("Milk", 2)
        self.cart.add_item("Red Bull", 3)
        total = 0.0
        result = self.cart.calculate_total(self.store, rewards_member=False)
        for _, details in result.items():
            unit_total = details["total"]
            total += unit_total
        self.assertEqual(total, 21.2385)

    def test_calculate_total_rewards_member(self):
        self.cart.add_item("Milk", 2)
        self.cart.add_item("Red Bull", 3)
        total = 0.0
        result = self.cart.calculate_total(self.store, rewards_member=True)
        for _, details in result.items():
            unit_total = details["total"]
            total += unit_total
        self.assertEqual(total, 19.78)

    def test_calculate_total_with_tax(self):
        self.store._inventory["Milk"]["tax_status"] = "Taxable"
        self.cart.add_item("Milk", 2)
        self.cart.add_item("Red Bull", 3)
        total = 0.0
        result = self.cart.calculate_total(self.store, rewards_member=False)
        for _, details in result.items():
            unit_total = details["total"]
            total += unit_total
        self.assertEqual(total, 21.726)

    def tearDown(self):
        del self.cart.items


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.customer = Customer(rewards_member=True)

    def test_customer_creation(self):
        self.assertTrue(self.customer.rewards_member)

    def test_customer_set_rewards_member(self):
        self.customer.rewards_member = False
        self.assertFalse(self.customer.rewards_member)

    def test_customer_set_invalid_rewards_member(self):
        self.customer.rewards_member = 1
        self.assertFalse(self.customer == "Client is a rewards member")

    def tearDown(self):
        self.customer = None


class ReceiptTest(unittest.TestCase):
    def setUp(self):
        self.receipt = Receipt("tests/test_receipt.txt")
        self.cart = Cart()
        self.store = Store("tests/test_inventory.txt")

    def test_receipt_calculate_total(self):
        today = date.today()
        expected_output = [
            str(today.strftime("%B %d, %Y")) + "\n",
            "Transaction No. 000001\n",
            "Client is not a rewards member\n",
            "\n",
            "Item      Quantity      Unit Price    Tax       Total\n",
            "\n",
            "Milk:        2       x    $3.75  +   $0.00  =   $7.50\n",
            "\n",
            "**************************\n",
            "Items sold: 1\n",
            "Taxes: $0.00\n",
            "Total: $7.50\n",
        ]
        self.cart.add_item("Milk", 2)
        actual_output = []
        self.receipt.generate_receipt(self.cart, self.store, rewards_member=False)
        with open("tests/test_receipt.txt", "r") as file:
            for line in file:
                actual_output.append(line)
        self.assertEqual(expected_output, actual_output)

    def tearDown(self):
        self.receipt = None
        self.cart = None
        self.store = None


if __name__ == "__main__":
    unittest.main()
