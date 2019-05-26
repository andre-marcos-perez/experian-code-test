class User:

    def __init__(self, fullname, age, email):
        self.fullname = fullname
        self.age = age
        self.email = email

    def __str__(self):
        return self.fullname + ", " + str(self.age) + " years old, " + \
            self.email + "."

    def __eq__(self, other):
        return (self.fullname == other.fullname) and (self.age == other.age)
