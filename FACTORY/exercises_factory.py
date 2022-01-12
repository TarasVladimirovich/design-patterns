

class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f'- ID: {self.id}, Name: {self.name}'


class PersonFactory:
    id = 0

    def create_person(self, name):
        p = Person(PersonFactory.id, name)
        PersonFactory.id += 1
        return p


if __name__ == '__main__':
    p1 = PersonFactory().create_person('Taras')
    p2 = PersonFactory().create_person('Pasha')
    p3 = PersonFactory().create_person('Ivan')
    print(p1)
    print(p2)
    print(p3)