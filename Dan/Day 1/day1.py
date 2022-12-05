def get_total_calories(calorie_list_input):
    total_calories = []
    total_calorie = 0
    for calorie in calorie_list_input:
        if calorie == '':
            total_calories.append(total_calorie)
            total_calorie = 0
        else:
            total_calorie += int(calorie)
    return total_calories


def get_num_max_total_calories(calories_list, num_maxes):
    calories_list.sort(reverse=True)
    return sum(calories_list[:num_maxes])


if __name__ == "__main__":
    with open('input.txt') as f:
        input_list = f.read().splitlines()

    with open('input.txt') as f:
        input_list2 = f.readlines()

    calorie_list = get_total_calories(input_list)

    # Part 1
    print(get_num_max_total_calories(calorie_list, 1))

    # Part 2
    print(get_num_max_total_calories(calorie_list, 3))
