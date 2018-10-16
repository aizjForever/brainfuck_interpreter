import sys
def readFile(path):
    with open(path, "rt") as f:
        return f.read()


class Brainfuck(object):
    def __init__(self,code,bits = 8,enable_precheck = False):
        def pre_processing(code):
            res = ""
            for c in code:
                if c in "+-><[].,":
                    res += c
            return res
        self.code = pre_processing(code)
        self.pointer = 0
        self.data_array = dict()
        self.output = []
        self.num_brackets = 0
        self.enable_precheck = enable_precheck
        self.bits = bits

    def run(self):
        def plus(self):
            if self.pointer not in self.data_array:
                self.data_array[self.pointer] = 0
            if (self.data_array[self.pointer] == 2 ** self.bits / 2 - 1):
                self.data_array[self.pointer] = -1 * 2 ** self.bits / 2
            else:
                self.data_array[self.pointer] += 1

        def minus(self):
            if self.pointer not in self.data_array:
                self.data_array[self.pointer] = 0
            if (self.data_array[self.pointer] == -1 * 2 ** self.bits / 2):
                self.data_array[self.pointer] = 2 ** self.bits / 2 - 1
            else:
                self.data_array[self.pointer] -= 1
        def greater(self):
            self.pointer += 1
        def smaller(self):
            self.pointer -= 1
        def find_next_r_bracket(index,code):
            count = 1
            i = index + 1
            while count != 0 and i < len(code) :
                if code[i] == "]":
                    count -= 1
                elif code[i] == "[":
                    count += 1
                i += 1

            return i - 1
        def is_valid(index,code):
            if index < 0: return False
            if index >= len(code): return False
            return True

        def find_prev_l_bracket(index,code):
            count = 1
            i = index - 1
            while count != 0 and i >= 0:
                if code[i] == "[":
                    count -= 1
                elif code[i] == "]":
                    count += 1
                i -= 1

            return i + 1
        def dot(self):
            val = self.data_array[self.pointer] if (self.pointer in self.data_array) else 0
            #print(chr(val))
            self.output.append(chr(val))

        def comma(self):
            char = input("Please enter a character:")
            self.data_array[self.pointer] = ord(char)

        def pre_check(code):
            i  = 0
            for c in code:
                if c == "[":
                    i += 1
                elif c == "]":
                    i -= 1
            return i == 0

        if self.enable_precheck and (not pre_check(self.code)):
            print("Invalid Code : Brackets not in pair!")
            return

        index = 0
        while index >= 0 and index < len(self.code):
            command = self.code[index]
            if command == '+':
                plus(self)
                index += 1
            elif command == "-":
                minus(self)
                index += 1
            elif command == ">":
                greater(self)
                index += 1
            elif command == "<":
                smaller(self)
                index += 1
            elif command == "[":
                if (self.pointer not in self.data_array) or self.data_array[self.pointer] == 0:
                    a = find_next_r_bracket(index,self.code)
                    if a != None:
                        index = a + 1
                    else:
                        index = 0
                        break
                else:
                    index += 1

            elif command == "]":
                if (self.pointer in self.data_array) and self.data_array[self.pointer] != 0:
                    a = find_prev_l_bracket(index,self.code)
                    if a != None:
                        index = a + 1
                    else:
                        index = 0
                        break
                else:
                    index += 1
            elif command == ".":
                dot(self)
                index += 1
            elif command == ",":
                comma(self)
                index += 1
            else:
                break
        
        if index == len(self.code):
            print("Output: " + "".join(self.output))
            return
        else:
            print("Code Invalid!")
            return
if len(sys.argv) != 4 or sys.argv[3] not in ["True","False"] or int(sys.argv[2])<=0:
    print("Invalid Input!")
else:
    code = sys.argv[1]
    code = readFile(code)
    bits_num = int(sys.argv[2])
    ep = sys.argv[3]
    programme1 = Brainfuck(code,bits = bits_num,enable_precheck = True if ep == "True" else False)
    print(programme1.code)

    programme1.run()
