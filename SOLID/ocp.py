"""
Open-closed Principle
https://en.wikipedia.org/wiki/Open%E2%80%93closed_principle
software entities (classes, modules, functions, etc.) should be open for extension, but closed for modification
"""

from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


# OCP = open for extension, closed for modification
# Bad example
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color:
                yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size:
                yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    # state space explosion
    # 2 --> 3 (criteria)
    # 3 --> 7 c s w cs sw cw csw = 7 methods

    # OCP = open for extension, closed for modification


# Specification pattern
class Specification:
    def is_satisfied(self, item):
        raise NotImplementedError()

    # and operator makes life easier
    def __and__(self, other):
        print(self, other)
        return AndSpecification(self, other)


class AndSpecification(Specification):
    def __init__(self, *args):
        print(*args)
        self.args = args

    def is_satisfied(self, item):
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))


class Filter:
    def filter(self, items, spec):
        raise NotImplementedError()


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)
    car = Product('Car', Color.BLUE, Size.LARGE)

    products = [apple, tree, house, car]

    # Bad example
    print("******* BAD EXAMPLE *******")
    pf = ProductFilter()
    print('Green products (old):')
    for p in pf.filter_by_color(products, Color.GREEN):
        print(f' - {p.name} is green')

    # ^ BEFORE

    # v AFTER
    print("******* GOOD EXAMPLE *******")
    bf = BetterFilter()
    print('\nGreen products (new):')
    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('\nLarge products:')
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('\nLarge blue items:')
    # large_blue = AndSpecification(large, ColorSpecification(Color.BLUE))
    blue = ColorSpecification(Color.BLUE)
    large_blue = large & blue
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')

    print('\nLarge green items:')
    large_green = large & green
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and green')

