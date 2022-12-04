with open("./Day4.txt", "r") as input_file:
    cleaned = [[y.split("-") for y in x.strip().split(",")] for x in input_file.readlines()]

    total = 0
    total2 = 0

    for first, second in cleaned:
        first_start, first_end = int(first[0]), int(first[1])
        second_start, second_end = int(second[0]), int(second[1])

        # we just need to know if one is being contained in the other
        if (first_start >= second_start and first_end <= second_end) or\
                (second_start >= first_start and second_end <= first_end):
            total += 1

        if (second_start <= first_start <= second_end) or (first_start <= second_start <= first_end):
            total2 += 1

    print(total)
    print(total2)
