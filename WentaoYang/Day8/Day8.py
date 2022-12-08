import math

with open("./Day8.txt", "r") as input_file:
    cleaned = [[int(y) for y in x.strip()] for x in input_file.readlines()]

    # we just need to query through each tree 

    def isValid(i, j):
        # check left row and right row
        if i == 0 or i == len(cleaned) - 1 or j == 0 or j == len(cleaned[0]) - 1:
            return True
        else:
            # this means the tree is not at the edge 
            # check all directions
            # top
            t, b, l, r = True, True, True, True

            for top in range(0, i):
                if cleaned[top][j] >= cleaned[i][j]:
                    t = False

            for top in range(i + 1, len(cleaned)):
                if cleaned[top][j] >= cleaned[i][j]:
                    b = False
            
            for top in range(0, j):
                if cleaned[i][top] >= cleaned[i][j]:
                    l = False

            for top in range(j + 1, len(cleaned[0])):
                if cleaned[i][top] >= cleaned[i][j]:
                    r = False

            return t or b or l or r 
            # left 
            # right
            # bot 

    def getScore(i, j):
        if i == 0 or i == len(cleaned) - 1 or j == 0 or j == len(cleaned[0]) - 1:
            return 0
        else:

            # this means the tree is not at the edge 
            # check all directions
            # top
            t, b, l, r = 0, 0, 0, 0

            for top in range(i - 1, -1, -1):
                t += 1
                if cleaned[top][j] >= cleaned[i][j]:
                    break
                    

            for top in range(i + 1, len(cleaned)):
                b += 1
                if cleaned[top][j] >= cleaned[i][j]:
                    break
             
            
            for top in range(j - 1, -1, -1):
                l += 1
                if cleaned[i][top] >= cleaned[i][j]:
                    break
          

            for top in range(j + 1, len(cleaned[0])):
                r += 1
                if cleaned[i][top] >= cleaned[i][j]:
                    break
        

            return t * b * l * r 

        # check top column and bottom column
    def part1():
        total = 0

        for i in range(len(cleaned)):
            for j in range(len(cleaned[0])):
                if isValid(i, j):
                    total += 1

        return total
    
    def part2():
        max_score = -math.inf

        for i in range(len(cleaned)):
            for j in range(len(cleaned[0])):
                val = getScore(i, j)
                if val > max_score:
                    max_score = val
        return max_score

    print(part1())
    print(part2())
