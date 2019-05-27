class Item:
    """ This is a class to represent an online sold item.

    Attributes
    ----------
    category: str
        Item's category.
    name: str
        Item's name.
    code: str
        Item's unique code.
    price: str
        Item's price in brazilian currency (BRL).
    details: str
        Item's long description.
    """

    def __init__(self, category, name, code, price, details):
        self.category = category
        self.name = name
        self.code = code
        self.price = price
        self.details = details

    def __str__(self):
        return self.category + ";" + self.name + ";" + self.code + ";" + \
            self.price + ";" + self.details

    def __eq__(self, other):
        if type(other) is type(self):
            return self.code == other.code
        else:
            return False

    def __hash__(self):
        return self.code
