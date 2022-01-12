class Code:
    indent_size = 2

    def __init__(self, type="", name=""):
        self.type = type
        self.name = name
        self.elements = []

    def __str(self, indent):
        lines = []
        init = "def __init__(self):"
        if not self.name:
            i = " " * (indent * self.indent_size)
            lines.append(f"{i}class {self.type}:")
            i1 = " " * ((indent + 1) * self.indent_size)
            lines.append(f"{i1}{init}")
        else:
            i1 = " " * (indent * self.indent_size)
            lines.append(f"{i1}self.{self.type} = {self.name}")
        for e in self.elements:
            lines.append(e.__str(indent + 2))

        return "\n".join(lines)

    def __str__(self):
        return self.__str(0)


class CodeBuilder:
    __root = Code()

    def __init__(self, root_name):
        self.root_name = root_name
        self.__root.type = root_name

    def add_field(self, type, name):
        self.__root.elements.append(
            Code(type, name)
        )
        return self

    def __str__(self):
        return str(self.__root)


cb = CodeBuilder("Person") \
    .add_field('name', '""') \
    .add_field('text', '""') \
    .add_field('age', '0')

print(cb)
