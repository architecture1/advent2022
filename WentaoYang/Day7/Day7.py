import math 
with open("./Day7.txt") as text_input:
    cleaned = [x.strip() for x in text_input.readlines()]

    current_path = ""
    parent = {}
    dir_map = {} # this associates each directory with another dir or file 
    file_map = {} # this associates each file with a size

    # this will be a n**2 solution because we will be looping through each dir and adding the size
    for line in cleaned:
        args = line.split(" ")

        if args[0] == "$":

            command = args[1]

            if command == "cd":
                dest = args[2]

                if dest == "/":
                    current_path = "/"
                elif dest == "..":
                    # we move up a directory 
                    current_path = parent[current_path]
                else:
                    # this means that we have a new directory 
                    new_path = current_path + "/" * int(current_path != "/") + dest
                    parent[new_path] = current_path
                    current_path = new_path
                
                if current_path not in dir_map:
                    dir_map[current_path] = set()
            # elif command == "ls":
                # listing out all the items in the directory 
                # we don't really have to do anything here 
        else:
            # only possible as an output of the "ls" command

            # directory
            if args[0] == "dir":
                dir_map[current_path].add(current_path + "/" * int(current_path != "/") + args[1])
            
            #file
            #### the problem is multiple files with the same name 
            # need to differentiate with the path to the file 
            else:
                file_size = int(args[0])
                file_name = current_path + "/" * int(current_path != "/") + args[1]

                file_map[file_name] = file_size
                dir_map[current_path].add(file_name)

   
    def get_dir_size(path):
        if path in file_map:
            return file_map[path]

        else:
            total = 0
            for content in dir_map[path]:
                total += get_dir_size(content)
            return total 
        

    def part_1():

        total = 0

        for directory in dir_map:
            size = get_dir_size(directory)
            
            if size <= 100000:
                print(f"{directory}: {size}")
                total += size

        return total
    
    def part_2():

        total = 70000000

        free_space = total - get_dir_size("/")
        amount_to_delete = 30000000 - free_space
        min_size = math.inf

        for directory in dir_map:
            size = get_dir_size(directory)

            if amount_to_delete <= size < min_size:
                min_size = size

        return min_size

    print(part_1())
    print(part_2())


          
