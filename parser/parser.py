class Parser:
    def __init__(self, filename):
        self.instructions = []

        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.split("//")[0]
                line = "".join(line.split())

                if line:
                    self.instructions.append(line)

        self.index = 0
        self.current_instruction = None

    def has_more_instructions(self):
        return self.index < len(self.instructions)

    def advance(self):
        self.current_instruction = self.instructions[self.index]
        self.index += 1

    def instruction_type(self):
        if self.current_instruction.startswith("@"):
            return "A_INSTRUCTION"

        if self.current_instruction.startswith("(") and self.current_instruction.endswith(")"):
            return "L_INSTRUCTION"

        return "C_INSTRUCTION"

    def symbol(self):
        if self.instruction_type() == "A_INSTRUCTION":
            return self.current_instruction[1:]

        if self.instruction_type() == "L_INSTRUCTION":
            return self.current_instruction[1:-1]

        return None

    def dest(self):
        if "=" in self.current_instruction:
            return self.current_instruction.split("=")[0].strip()

        return None

    def comp(self):
        instruction = self.current_instruction

        if "=" in instruction:
            instruction = instruction.split("=")[1]

        if ";" in instruction:
            instruction = instruction.split(";")[0]

        return instruction.strip()

    def jump(self):
        if ";" in self.current_instruction:
            return self.current_instruction.split(";")[1].strip()

        return None