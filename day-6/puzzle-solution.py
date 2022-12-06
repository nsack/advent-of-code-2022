def find_marker(input_str: str, marker_length: int):
    """
    """
    for i in range(len(input_str)):
        if marker_length == len(set(input_str[i:i+marker_length])):
            break

    return i + marker_length

def puzzle_solution():
    marker_length = 4
    marker_length_part_2 = 14
    with open("puzzle-input.txt", "r") as f:
        # read the lines
        input_str = f.read()
    print(find_marker(input_str, 4))
    print(find_marker(input_str, 14))


puzzle_solution()
