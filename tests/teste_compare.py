import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import assemble


def read_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines() if line.strip()]


def compare(asm_file, cmp_file):
    hack_file = assemble(asm_file)

    generated = read_file(hack_file)
    expected = read_file(cmp_file)

    if generated == expected:
        print("OK:", asm_file)
    else:
        print("ERRO:", asm_file)

        for i, (g, e) in enumerate(zip(generated, expected), start=1):
            if g != e:
                print("Linha:", i)
                print("Gerado :", g)
                print("Esperado:", e)
                break


def main():
    if len(sys.argv) != 3:
        print("Uso: python tests/test_compare.py arquivo.asm arquivo.cmp")
        return

    compare(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()