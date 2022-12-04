def puzzle_solution(file_name: str = "puzzle-input.txt"):
    """ """
    full_overlap_count = 0
    partial_overlap_count = 0
    with open(file_name, "r") as f:
        for line in f:
            range_list = []
            section_assignments = line.strip().split(",")
            first_section = section_assignments[0].split("-")
            second_section = section_assignments[1].split("-")
            range_list.append(
                list(range(int(first_section[0]), int(first_section[1]) + 1))
            )
            range_list.append(
                list(range(int(second_section[0]), int(second_section[1]) + 1))
            )

            if set(range_list[0]).issubset(range_list[1]):
                full_overlap_count += 1
            elif set(range_list[1]).issubset(range_list[0]):
                full_overlap_count += 1

            if set(range_list[0]).intersection(range_list[1]):
                partial_overlap_count += 1

    return full_overlap_count, partial_overlap_count


print(puzzle_solution())
