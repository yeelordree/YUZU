class yzu:
    def __init__(self, path: str):
        self.path = path

    def parse(self):
        with open(self.path) as file:
            contents = list(filter(lambda a : bool(a), [line.strip() for line in file]))

        self.num_qbits: int = contents.pop(0)[-1]

        result = {}
        instructions = []
        [result.update({label: instructions}) for item in contents if (label := item) and item.endswith(':') or instructions.append(item)]

        print(f'(+) creating a quantum circuit with {self.num_qbits} qbits')

        print(len(result))
        return result


main = yzu('h.yuzu')
print(main.parse())