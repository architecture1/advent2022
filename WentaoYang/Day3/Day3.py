with open("./Day3.txt", "r") as input_file:
    sacks = [x.strip() for x in input_file.readlines()]

    # we know that the sacks are even in length
    # the each half of the sacks

    total = 0
    for sack in sacks:
        first_half, second_half = set(sack[:len(sack) // 2]), set(sack[len(sack)//2:])
        ele = list(first_half.intersection(second_half))[0]

        if ele.isupper():
            total += (ord(ele) - ord("A")) + 27
        else:
            total += (ord(ele) - ord("a")) + 1

    total2 = 0
    for i in range(0, len(sacks), 3):
        first = set(sacks[i])
        second = set(sacks[i+1])
        third = set(sacks[i+2])

        first_intersection = first.intersection(second)
        ele = list(first_intersection.intersection(third))[0]

        if ele.isupper():
            total2 += (ord(ele) - ord("A")) + 27
        else:
            total2 += (ord(ele) - ord("a")) + 1
    print(total)
    print(total2)
