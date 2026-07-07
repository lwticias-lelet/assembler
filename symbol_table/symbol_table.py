class SymbolTable:
    def __init__(self):
        self.symbols = {}

        self.initialize()

        self.next_variable = 16

    def initialize(self):
        self.symbols["SP"] = 0
        self.symbols["LCL"] = 1
        self.symbols["ARG"] = 2
        self.symbols["THIS"] = 3
        self.symbols["THAT"] = 4

        self.symbols["SCREEN"] = 16384
        self.symbols["KBD"] = 24576

        for i in range(16):
            self.symbols[f"R{i}"] = i

    def add_entry(self, symbol, address):
        self.symbols[symbol] = address

    def contains(self, symbol):
        return symbol in self.symbols

    def get_address(self, symbol):
        return self.symbols[symbol]

    def add_variable(self, symbol):
        if self.contains(symbol):
            return self.get_address(symbol)

        address = self.next_variable

        self.symbols[symbol] = address

        self.next_variable += 1

        return address