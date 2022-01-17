from abc import ABC
from collections.abc import Iterable


class ValueContainer(Iterable, ABC):

    @property
    def sum(self):
        result = 0
        for i in self:
            for c in i:
                result += c
        return result


class SingleValue(ValueContainer):
    def __init__(self, value):
        self.value = value

    def __iter__(self):
        yield self.value


class ManyValues(list, ValueContainer):
    pass


if __name__ == '__main__':
    single_value = SingleValue(11)
    other_value = ManyValues()
    other_value.append(22)
    other_value.append(33)

    all = ManyValues()
    all.append(single_value)
    all.append(other_value)

    print(all.sum)
