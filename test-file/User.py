class User:
    """ This is a class to represent an user and its personal information.

    Parameters
    ----------
    fullname: str
        User's full name.
    age: int
        User's age in years.
    email: str
        User's email.
    """

    def __init__(self, fullname, age, email):
        self.fullname = fullname
        self.age = age
        self.email = email

    def __str__(self):
        return self.fullname + ", " + str(self.age) + " years old, " + \
            self.email + "."

    def __eq__(self, other):
        if type(other) is type(self):
            return (self.fullname == other.fullname) and (self.age == other.age)
        else:
            return False

    def __hash__(self):
        return hash(self.fullname) + self.age
