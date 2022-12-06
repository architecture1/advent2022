with open("./Day6.txt", "r") as input_file:
    cleaned = input_file.readlines()

    string = cleaned[0]

    for i in range(len(string) - 3):
        first, second, third, fourth = string[i], string[i+1], string[i+2], string[i+3]

        seen = {first, second, third, fourth}

        if len(seen) == 4:
            print(i + 4)
            break

    for i in range(len(string) - 13):
        curr = set(string[i:i+14])

        if len(curr) == 14:
            print(i+14)
            break

