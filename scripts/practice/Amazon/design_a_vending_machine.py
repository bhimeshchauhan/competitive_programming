"""

Here is my Python Code version of the java solution provided in the original post link.
The requirement is to design a Vending Machine which

Accepts coins of 1,5,10,25 Cents i.e. penny, nickel, dime, and quarter.
Allow user to select products Coke(25), Pepsi(35), Soda(45)
Allow user to take refund by canceling the request.
Return selected product and remaining change if any
Allow reset operation for vending machine supplier.

"""

from abc import ABC
from enum import Enum


class Inventory:
    def __init__(self):
        self.inventory = {}

    def get_quantity(self, item):
        return self.inventory[item]

    def add(self, item):
        self.inventory[item] += 1

    def deduct(self, item):
        self.inventory[item] -= 1

    def has_item(self, item):
        return self.inventory[item] > 0

    def clear(self):
        for item in self.inventory.keys():
            self.inventory[item] = 0
            # or self.inventory = {}

    def put(self, item, quantity):
        self.inventory[item] = quantity


class ITEMS(Enum):
    PEPSI = 1
    COKE = 2
    SODA = 3


class Item(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name


class Coke(Item):
    def __init__(self):
        super(Coke, self).__init__(ITEMS.COKE, 25)


class Pepsi(Item):
    def __init__(self):
        super(Pepsi, self).__init__(ITEMS.PEPSI, 35)


class Soda(Item):
    def __init__(self):
        super(Soda, self).__init__(ITEMS.SODA, 45)

# Do similar with Coins too


# Factory class to create instance of Vending Machine, this can be extended to create instance of
# different types of vending machines.
class VendingMachineFactory:
    def createVendingMachine(self):
        return VendingMachine()


class VendingMachine:
    def __init__(self):
        self.item_inventory = Inventory()
        self.cash_inventory = Inventory()
        self.total_sales = 0
        self.current_balance = 0
        self.current_item = None
        self.initialize_inventories()

    def initialize_inventories(self):
        all_items = [Coke(), Pepsi(), Soda()]
        for item in all_items:
            self.item_inventory.put(item, 5)

        # all_coins
        # ....

    def selectItemAndGetPrice(self, item):
        if self.item_inventory.has_item(item):
            self.current_item = item
            return self.current_item.get_price()
        # Change this to an exception whenever you can
        return "Sold Out, Please buy another item"

    def insertCoin(self, coin):
        self.current_balance += coin.get_denomination()
        self.cash_inventory.add(coin)

    def collectItemAndChange(self):
        item = self.collectItem()
        self.total_sales += self.current_item.get_price()
        change = self.collectChange()

        return (item, change)

    def collectItem(self):
        if self.isFullPaid():
            if self.hasSufficientChange():
                self.item_inventory.deduct(self.current_item)
                return self.current_item
            return "Not Sufficient change in Inventory"
        return "Price not full paid"

    def hasSufficientChange(self):
        change_amt = self.current_balance - self.current_item.get_price()
        if self.getChange(change_amt):
            return True
        return False

    def isFullPaid(self):
        return self.current_balance >= self.current_item.get_price()

    def collectChange(self):
        change_amt = self.current_balance - self.current_item.get_price()
        change = self.getChange(change_amt)
        self.updateCashInventory(change)
        self.current_balance = 0
        self.current_item = None
        return change

    def getChange(self, amount):
        # Add stuff to extract denominations
        pass

    def updateCashInventory(self, change):
        for c in change:
            self.cash_inventory.deduct(c)
