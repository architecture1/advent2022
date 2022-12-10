import math 
with open("./Day9.txt", "r") as input_file:
    cleaned = [x.strip().split(" ") for x in input_file.readlines()]
    
    visited = {(0, 0)}
    # first we need to have index for each head 
    nodes = {x:[0, 0] for x in range(10)}

    # what we can do is start from the position (0, 0)
    # each time we move to a new location we will check the distance
    # if the requirements are diff then we have to move the head and tail accordingly and add to visited

    def update(tail, head, num):
        tail_num, head_num = tail, head
        tail, head = nodes[tail_num], nodes[head_num]
        tail_x, tail_y, head_x, head_y = tail[0], tail[1], head[0], head[1]

        # do this from scratch 
        # we don't update the head value 
        if tail_x == head_x:
            # same column, but different row 
            if abs(tail_y - head_y) >= 2:
                tail_y += 1 * ((-1) ** int(tail_y > head_y))

            if tail_num == num:
                visited.add((tail_x, tail_y))

            nodes[tail_num] = [tail_x, tail_y]
            return 

        if tail_y == head_y:
            # same row, but different column 
            if abs(tail_x - head_x) >= 2:
                tail_x += 1 * ((-1) ** int(tail_x > head_x))

            if tail_num == num:
                visited.add((tail_x, tail_y))

            nodes[tail_num] = [tail_x, tail_y]
            return 
        
        # diff row and diff column 
        if abs(tail_x - head_x) >= 2 or abs(tail_y - head_y) >=2:
            tail_x += 1 * ((-1) ** int(tail_x > head_x))
            tail_y += 1 * ((-1) ** int(tail_y > head_y))
            if tail_num == num:
                visited.add((tail_x, tail_y))

            nodes[tail_num] = [tail_x, tail_y]
            return 

                          

    def move(direction, steps, num):
        # check direction
        # update the first node manually
        # then we need to update the rest with a loop 
        if direction == "U":
            # we need to increase y value 
            for i in range(steps):
                nodes[0][1] += 1
                for j in range(num - 1):
                    update(j+1, j, num -1 )
        elif direction == "D":
            for i in range(steps):
                nodes[0][1] -= 1
                for j in range(num - 1):
                    update(j+1, j, num -1)
        elif direction == "L":
            for i in range(steps):
                nodes[0][0] -= 1
                for j in range(num - 1):
                    update(j+1, j, num -1)
        else:
            for i in range(steps):
                nodes[0][0] += 1
                for j in range(num - 1):
                    update(j+1, j, num -1)
        # check how many steps
        # update the head 
        # update the tail
        # update visited 

    for motion in cleaned:
        direction, steps = motion[0], int(motion[1])
        move(direction, steps, 10)


    print(len(visited))

    max_x = -math.inf
    max_y = -math.inf
    min_x = math.inf
    min_y = math.inf

    for x, y in visited:
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)


    for i in range(max_y, min_y - 1, -1):
        curr = ""
        for j in range(min_x, max_x + 1):
            if (j, i) in visited:
                curr += " # "
            else:
                curr += " . "
        curr += "\n"
        # print(curr)

        


