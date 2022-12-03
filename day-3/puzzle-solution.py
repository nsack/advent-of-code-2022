import string

def split_string(str_input: str):
    """
    """
    

    return rucksack_1_items, rucksack_2_items

def get_priority(item: str):
    """
    """
    letter_priorities = dict()
    for index, letter in enumerate(string.ascii_lowercase, 1):
        letter_priorities[letter] = index

    for index, letter in enumerate(string.ascii_uppercase, 27):
        letter_priorities[letter] = index

    priority = letter_priorities.get(item[0])

    return priority

def puzzle_solution_part_1(file_name:str = "puzzle-input.txt"):
    """
    """
    total_priority = 0
    with open(file_name, "r") as f:
        for line in f:
            slice_point = len(line) // 2
            rucksack_1_items = line[0:slice_point]
            rucksack_2_items = line[slice_point:len(line)+1]
            duplicate_item = list(set(rucksack_1_items).intersection(rucksack_2_items))
            total_priority += get_priority(item=duplicate_item)

    return total_priority


def puzzle_solution_part_2(file_name:str = "puzzle-input.txt"):
    """
    """
    total_priority = 0
    with open(file_name, "r") as f:
        rucksacks = f.read().splitlines()
        rucksack_groups = list(zip(*[iter(rucksacks)]*3))

    for group in rucksack_groups:
        duplicate_item =list(set(group[0]).intersection(group[1]).intersection(group[2]))
        total_priority += get_priority(item=duplicate_item)

    return total_priority


print(puzzle_solution_part_1())
print(puzzle_solution_part_2())