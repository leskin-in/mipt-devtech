#!/usr/bin/env python3

import re


class SimpleDis:
    # Supported instructions
    SUPPORTED_INSTRUCTIONS = {
        'LOAD_CONST',
        'STORE_NAME',
        'LOAD_NAME',

        'BINARY_ADD',
        'BINARY_SUBTRACT',
        'BINARY_MULTIPLY',
        'BINARY_POWER',

        'CALL_FUNCTION',
        'RETURN_VALUE',
        'POP_TOP',
    }

    # Instructions that do not have any parameters
    NOPARAM_INSTRUCTIONS = {
        'BINARY_ADD',
        'BINARY_SUBTRACT',
        'BINARY_MULTIPLY',
        'BINARY_POWER',

        'CALL_FUNCTION',
        'POP_TOP',
        'RETURN_VALUE',
    }

    def __call__(self, source):
        """
        Perform disassembling and return a string with Python code
        :param source:
        :return:
        """
        self._to_stack(source)
        result = []
        for s in self.queue:
            result.append(self._stack_to_string(s))
        result = "\n".join(result)
        return result

    def _to_stack(self, source):
        """
        Transform raw source into a list of stacks of commands and a jump map
        :param source: Source code
        """
        self.queue = []
        self.jump_map = {}

        source = str(source).split("\n")
        source = source[::2]

        stack = []
        for l in source:
            l = str(l)
            # UPDATE queue
            if re.fullmatch("\\s+", l) is not None:
                self.queue.append(stack)
                stack = []
                continue
            elements = l.split(maxsplit=1)

            # PROCESS line number
            if len(stack) == 0:
                elements = elements[1].split(maxsplit=1)

            # PROCESS '>>' (jump end point)
            if re.fullmatch(">>", elements[0]) is not None and len(stack) == 0:
                elements = elements[1].split(maxsplit=1)
                self.jump_map[elements[0]] = len(self.queue)
            elif re.fullmatch(">>", elements[0]) is not None:
                # TODO: Jump point inside an instruction
                raise NotImplementedError("The instructions '" + l + "' are not supported")

            # PROCESS instruction
            elements = elements[1].split(maxsplit=1)
            instruction = elements[0]
            stack_entity = []
            if instruction in SimpleDis.SUPPORTED_INSTRUCTIONS:
                stack_entity.append(instruction)
                if instruction in SimpleDis.NOPARAM_INSTRUCTIONS:
                    stack.append(tuple(stack_entity))
                    continue
            else:
                raise NotImplementedError("The instructions '" + l + "' are not supported")

            # PROCESS instruction parameters
            elements = elements[1].split(maxsplit=1)
            stack_entity.append(elements[0])
            if len(elements) > 1:
                stack_entity.append(elements[1][1:-1])

            stack.append(tuple(stack_entity))

        self.queue.append(stack)

    def _stack_to_string(self, stack_entity):
        """
        Form a line of code from a stack
        :param stack_entity: a stack entity
        :return: string - a resulting line of python code
        """
        result = ""
        lvs = []  # Local variables stack
        for e in stack_entity:
            instr = e[0]
            data_r = e[1] if len(e) > 1 else None
            data_s = e[2] if len(e) > 2 else None

            if instr == "STORE_NAME":
                result = result + data_s
                continue
            elif instr in {"LOAD_CONST", "LOAD_NAME"}:
                lvs.append(data_s)
                continue

            elif instr == "BINARY_ADD":
                opR = lvs.pop()
                opL = lvs.pop()
                result = result + str(opL) + " + " + str(opR)
            elif instr == "BINARY_SUBTRACT":
                opR = lvs.pop()
                opL = lvs.pop()
                result = result + str(opL) + " - " + str(opR)
            elif instr == "BINARY_MULTIPLY":
                opR = lvs.pop()
                opL = lvs.pop()
                result = result + str(opL) + " * " + str(opR)
            elif instr == "BINARY_POWER":
                opR = lvs.pop()
                opL = lvs.pop()
                result = result + str(opL) + " ** " + str(opR)

            elif instr == "CALL_FUNCTION":
                # TODO: Support multiple arguments
                opR = lvs.pop()
                opL = lvs.pop()
                result = result + str(opL) + "(" + str(opR) + ")"
            elif instr == "RETURN_VALUE":
                opR = lvs.pop()
                result = result + "return" + " " + str(opR)
            elif instr == "POP_TOP":
                result += "\n"

            else:
                raise NotImplementedError("Found unsupported instruction with representation '" + stack_entity + "'")

        return result


