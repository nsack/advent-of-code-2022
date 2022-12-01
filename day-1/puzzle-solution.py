def parse_input(file_name: str ="puzzle-input.txt"):
    """
    """
    with open(file_name, "r") as f:
        elves = f.read().split("\n\n")

    return elves


def puzzle_solution(elves: list):
    """
    """
    calories = [sum(map(int, elf.split())) for elf in elves]
    max_calories = max(calories)

    return max_calories, sum(sorted(calories)[-3:])

elves = parse_input()
print(puzzle_solution(elves))
