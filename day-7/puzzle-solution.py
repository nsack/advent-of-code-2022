from collections import defaultdict

path = []
folders = defaultdict(int)
with open("puzzle-input.txt", "r") as f:
    # iterate the list of commands
    for command in f:
        # if the command is "$ cd .." we need to remove it from the current path
        # this is navigating back to root and we're starting over, so we don't care about it 
        # in the working directory list
        if command[:7] == "$ cd ..":
            path.pop()
        # if the command is any other type of cd we'll append it to the current path so we know where 
        # we are in the working tree
        elif command[:4] == "$ cd":
            path.append(command.strip()[5:])
        # if it didn't meet the other two criteria it should be a file and we can check it's size
        elif command[0].isdigit():
            # the file will come in like this: size, file name
            # we only carry about the size itself, so we'll ditch the file name
            size, _ = command.split()
            # iterate the path length and append it to folders with a size
            for i in range(len(path)):
                folders["/".join(path[:i + 1])] += int(size)

# Figure out which folders have a size that sums up to less than 100000
print(sum(size for size in folders.values() if size < 100000))

# Figure out which folder is the largest that meets the size to free up space
print(min([size for size in folders.values() if folders["/"] - size <= 40000000]))