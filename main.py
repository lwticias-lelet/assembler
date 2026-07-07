import os
import sys

from parser.parser import Parser
from code.code import Code
from symbol_table.symbol_table import SymbolTable


def to_binary(value):
    if value < 0 or value > 32767:
        raise ValueError(f"valor fora do limite de 15 bits: {value}")

    return "0" + format(value, "015b")


def first_pass(input_file, symbol_table):
    parser = Parser(input_file)
    rom_address = 0

    while parser.has_more_instructions():
        parser.advance()

        if parser.instruction_type() == "L_INSTRUCTION":
            symbol_table.add_entry(parser.symbol(), rom_address)
        else:
            rom_address += 1


def second_pass(input_file, output_file, symbol_table):
    parser = Parser(input_file)
    code = Code()

    with open(output_file, "w", encoding="utf-8") as output:
        while parser.has_more_instructions():
            parser.advance()
            instruction_type = parser.instruction_type()

            if instruction_type == "A_INSTRUCTION":
                symbol = parser.symbol()

                if symbol.isdigit():
                    address = int(symbol)
                else:
                    address = symbol_table.add_variable(symbol)

                output.write(to_binary(address) + "\n")

            elif instruction_type == "C_INSTRUCTION":
                comp = code.comp(parser.comp())
                dest = code.dest(parser.dest())
                jump = code.jump(parser.jump())

                output.write("111" + comp + dest + jump + "\n")


def assemble(input_file):
    if not os.path.exists(input_file):
        raise FileNotFoundError("arquivo nao encontrado")

    if not input_file.endswith(".asm"):
        raise ValueError("o arquivo precisa terminar com .asm")

    output_file = os.path.splitext(input_file)[0] + ".hack"
    symbol_table = SymbolTable()

    first_pass(input_file, symbol_table)
    second_pass(input_file, output_file, symbol_table)

    return output_file


def main():
    if len(sys.argv) != 2:
        print("Uso: python main.py arquivo.asm")
        return

    try:
        output_file = assemble(sys.argv[1])
        print("Arquivo gerado:", output_file)

    except Exception as error:
        print("Erro:", error)


if __name__ == "__main__":
    main()