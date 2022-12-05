import re
FILE = 'input.txt'
MOVE_COMMAND = 'move'


class CrateStack:
    def __init__(self, crate_list, num_stacks):
        self.num_stacks = num_stacks
        self.crate_list = crate_list
        self.stacks = self.stack_from_list(crate_list)

    def stack_from_list(self, crate_list):
        stack = []
        for crate_index in range(self.num_stacks):
            stack.append([])

        for row in reversed(crate_list):
            for i in range(self.num_stacks):
                crate = row[i*self.get_crate_len():(i+1)*self.get_crate_len()].strip()
                if crate != '':
                    stack[i].append(crate)
        return stack

    def move_crate(self, move_n, from_x, to_y):
        temp_stack = []
        for i in range(move_n):
            temp_stack.append(self.stacks[from_x].pop())
        for i in range(move_n):
            self.stacks[to_y].append(temp_stack.pop())

    def get_crate_len(self):
        return len(self.crate_list[0].split()[0]) + 1

    def get_top_crates(self):
        return [stack[-1] for stack in self.stacks]

    def move_crates(self, command_list):
        for line in command_list:
            self.move_crate(line[0], line[1] - 1, line[2] - 1)


def get_num_stacks(input_lst):
    for line in input_lst:
        if line.lstrip()[0].isdigit():
            return int(line.split()[-1])


def get_crate_list(input_lst):
    crate_list = []
    for line in input_lst:
        if not line.lstrip()[0].isdigit():
            crate_list.append(line)
        else:
            break
    return crate_list


def get_command_list(input_lst):
    command_list = []
    for line in input_lst:
        if line != '' and MOVE_COMMAND in line:
            command_list.append([int(s) for s in re.findall(r'\b\d+\b', line)])
    return command_list


if __name__ == "__main__":
    with open(FILE) as f:
        input_list = f.read().splitlines()

    crate_stack = CrateStack(get_crate_list(input_list), get_num_stacks(input_list))
    crate_stack.move_crates(get_command_list(input_list))
    print(re.sub(r'\W', ' ', ''.join(crate_stack.get_top_crates())).replace(" ", ""))
