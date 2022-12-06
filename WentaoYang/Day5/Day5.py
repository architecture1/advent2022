with open("./Day5.txt", "r") as input_file:
    cleaned = [x[:-1] for x in input_file.readlines()]

    # get the position of each number and then match it
    # need to get value of each one

    stack = {i+1: [] for i in range(9)}

    # obtain elements of each stack
    for i in range(9):
        position = cleaned[8].find(str(i + 1))
        print(position)
        for j in range(7, -1, -1):
            current = cleaned[j]

            if len(current) > position:
                if current[position] != " ":
                    stack[i+1].append(current[position])

    for i in range(10, len(cleaned)):
        message = cleaned[i].split(" ")

        amount, old, new = int(message[1]), int(message[3]), int(message[5])

        # part 1
        # for j in range(amount):
        #     stack[new].append(stack[old].pop())

        # part 2
        temp = []
        for j in range(amount):
            temp.append(stack[old].pop())

        stack[new].extend(temp[::-1])

    for i in range(9):
        print(stack[i+1][-1])




