class Person:
    def __init__(self, name, surname, age=0):
        self.name = name
        self.surname = surname
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def set_age(self, age):
        self.age = age

    def set_surname(self, surname):
        self.surname = surname

    def set_name(self, name):
        self.name = name

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.name, self.surname, self.age)

    def __repr__(self):
        return '{0}\n{1}\n{2}'.format(self.name, self.surname, self.age)

per_1 = Person('Ihor', 'Samanchuk', 36)

per_1.set_surname('Mihelson')

print(per_1)

print(repr(per_1))