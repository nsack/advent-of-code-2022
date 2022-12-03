import string

def split_string(str_input: str):
    """
    """
    slice_point = len(str_input) // 2
    rucksack_1_items = str_input[0:slice_point]
    rucksack_2_items = str_input[slice_point:len(str_input)+1]

    return rucksack_1_items, rucksack_2_items

def get_intersect_items(rucksack_items: tuple):
    """
    """

    result = set(rucksack_items[0]).intersection(rucksack_items[1])
    
    return result

def get_intersect_groups(rucksack_group: tuple):
    """
    """
    result = set(rucksack_group[0]).intersection(rucksack_group[1]).intersection(rucksack_group[2])

    return result

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
            rucksack_items = split_string(line)
            duplicate_item = list(get_intersect_items(rucksack_items))
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
        duplicate_item =list(get_intersect_groups(rucksack_group=group))
        total_priority += get_priority(item=duplicate_item)

    return total_priority


print(puzzle_solution_part_1())
print(puzzle_solution_part_2())