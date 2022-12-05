import re

stacks = [
    [],
    ["D","P","B","J","V"],
    ["P", "V","B","W","R","D","F"],
    ["R", "G","F","L","D","C","W","Q"],
    ["W","J","P","M","L","N","D","B"],
    ["H","N","B","P","C","S","Q"],
    ["R","D","B","S","N","G"],
    ["Z","B","P","M","Q","F","S","H"],
    ["W","L","F"],
    ["S","V","F","M","R"]
]

# part 1 solution
with open("puzzle-input.txt", "r") as f:
    lines = f.readlines()[10::]
    for line in lines:
        # The format after this match will be [crate count, starting stack, ending stack]
        crate_move = re.findall(r'[0-9]+', line)
        crate_move = [int(i) for i in crate_move]
        # pop the last element on the stack (the top) and move it to the next stack
        # this will occur one at a time for however many are in the first spot
        counter = int(crate_move[0])
        while counter > 0:
            # the stack we will pop FROM will be stacks[crate_move[1]]
            # the stack we append to will be stacks[crate_move[2]]
            crate = stacks[crate_move[1]].pop()
            stacks[crate_move[2]].append(crate)
            # reduce the counter by 1 to indicate we've made the move
            counter -= 1


# concatenate the last item starting at stack 1 to the end as the output
package_output = ""
for stack in stacks:
    if len(stack) == 0:
        pass
    else:
        package_output += stack[-1]


print(package_output)

stacks_2 = [
    [],
    ["D","P","B","J","V"],
    ["P", "V","B","W","R","D","F"],
    ["R", "G","F","L","D","C","W","Q"],
    ["W","J","P","M","L","N","D","B"],
    ["H","N","B","P","C","S","Q"],
    ["R","D","B","S","N","G"],
    ["Z","B","P","M","Q","F","S","H"],
    ["W","L","F"],
    ["S","V","F","M","R"]
]

# part 2 solution
with open("puzzle-input.txt", "r") as f:
    lines = f.readlines()[10::]
    for line in lines:
        # The format after this match will be [crate count, starting stack, ending stack]
        crate_move = re.findall(r'[0-9]+', line)
        crate_move = [int(i) for i in crate_move]
        # pop the last element on the stack (the top) and move it to the next stack
        # this will occur one at a time for however many are in the first spot
        counter = int(crate_move[0])
        # now we need to pop them all first so we can put them in order on the other stack
        crates_to_move = []
        while counter > 0:
            # the stack we will pop FROM will be stacks[crate_move[1]]
            # the stack we append to will be stacks[crate_move[2]]
            crates_to_move.append(stacks_2[crate_move[1]].pop())
            # reduce the counter by 1 to indicate we've made the move
            counter -= 1
        
        # append the crates to the new stack in the same order we pulled them
        crates_to_move.reverse()
        for i in range(0, len(crates_to_move)):
            stacks_2[crate_move[2]].append(crates_to_move[0])
            crates_to_move.pop(0)


# concatenate the last item starting at stack 1 to the end as the output
package_output = ""
for stack in stacks_2:
    if len(stack) == 0:
        pass
    else:
        package_output += stack[-1]

print(package_output)