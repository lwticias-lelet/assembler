import os
import sys

from parser.parser import Parser
from translator.code import Code
from symbol_table.symbol_table import SymbolTable


def to_binary(value):
    if value < 0 or value > 32767:
        raise ValueError(f"Valor fora do limite: {value}")

    return "0" + format(value, "015b")


def first_pass(input_file, symbol_table):
    parser = Parser(input_file)
    rom_address = 0

    while parser.has_more_instructions():
        parser.advance()

        if parser.instruction_type() == "L_INSTRUCTION":
            symbol = parser.symbol()

            if not symbol_table.contains(symbol):
                symbol_table.add_entry(symbol, rom_address)

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

                elif symbol_table.contains(symbol):

                    address = symbol_table.get_address(symbol)

                else:

                    address = symbol_table.add_variable(symbol)

                output.write(to_binary(address) + "\n")

            elif instruction_type == "C_INSTRUCTION":

                comp = code.comp(parser.comp())
                dest = code.dest(parser.dest())
                jump = code.jump(parser.jump())

                binary = "111" + comp + dest + jump

                output.write(binary + "\n")


def assemble(input_file):

    output_file = os.path.splitext(input_file)[0] + ".hack"

    symbol_table = SymbolTable()

    first_pass(input_file, symbol_table)

    second_pass(input_file, output_file, symbol_table)

    return output_file


def main():

    if len(sys.argv) != 2:
        print("Uso:")
        print("python main.py caminho/arquivo.asm")
        return

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print("Erro: arquivo não encontrado.")
        return

    if not input_file.endswith(".asm"):
        print("Erro: o arquivo deve possuir extensão .asm")
        return

    try:

        output_file = assemble(input_file)

        print("Arquivo gerado com sucesso:")
        print(output_file)

    except Exception as error:

        print("Erro durante a montagem:")
        print(error)


if __name__ == "__main__":
    main()