class Item:

    category = "Pet Shop"

    def __init__(self, name, code, price, details):
        self.name = name
        self.code = code
        self.price = price
        self.details = details

    def __str__(self):
        return Item.category + ";" + self.name + ";" + self.code + ";" + \
            self.price + ";" + self.details

    def __eq__(self, other):
        return self.code == other.code
