# stock.py

class Stock(object):
    """Represents a stock"""
    def __init__(self, name, shares, price):
        self._name = name
        self._shares = shares
        self._price = price

    def cost(self):
        return self._shares * self._price
