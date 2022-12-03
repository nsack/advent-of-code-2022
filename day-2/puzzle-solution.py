def get_winner_part_1(opp_input:str, my_input:str):
    """
    """
    ## X == Rock, Y == Paper, Z == Scissors
    ## A == Rock, B == Paper, C == Scissors
    input_mapping = {
        "X": "rock",
        "A": "rock",
        "Y": "paper",
        "B": "paper",
        "Z": "scissors",
        "C": "scissors"
    }

    index_mapping = {
        0: "rock",
        1: "paper",
        2: "scissors"
    }

    #               | ROCK (A)  | PAPER (B) | SCISSOR (C)
    #   ROCK (X)    |  -1       | 1         | 0
    # . PAPER (Y)   |  1        | -1        | 2
    # . SCISSOR (Z) |  0        | 2         | -1
    #
    move_mapping = [
        [-1, 1, 0],
        [1, -1, 2],
        [0, 2, -1]
    ]
    opp_input_type = input_mapping[opp_input]
    my_input_type = input_mapping[my_input]
    opp_move = list(index_mapping.values()).index(opp_input_type)
    my_move = list(index_mapping.values()).index(my_input_type)

    winner = move_mapping[opp_move][my_move]

    round_score = 0
    # Add points for the outcome
    if winner == my_move:
        round_score += 6
    if winner == -1:
        round_score += 3
    else:
        round_score += 0

    # Add points for the move type
    if my_input_type == "rock":
        round_score += 1
    elif my_input_type == "paper":
        round_score += 2
    else:
        round_score += 3
    
    return round_score


def puzzle_solution_part_1(file_name:str = "puzzle-input.txt"):
    """
    """
    my_score = 0
    with open(file_name, "r") as f:
        for line in f:
            input_moves = line.strip().split(" ")
            round_score = get_winner_part_1(opp_input=input_moves[0], my_input=input_moves[1])
            my_score += round_score

    return my_score


def get_winner_part_2(opp_input:str, my_input:str):
    """
    """
    ## X == Rock, Y == Paper, Z == Scissors
    ## A == Rock, B == Paper, C == Scissors
    input_mapping = {
        "A": "rock",
        "B": "paper",
        "C": "scissors"
    }

    index_mapping = {
        0: "rock",
        1: "paper",
        2: "scissors"
    }

    #               | ROCK (A)  | PAPER (B) | SCISSOR (C)
    #   ROCK (X)    |  -1       | 1         | 0
    # . PAPER (Y)   |  1        | -1        | 2
    # . SCISSOR (Z) |  0        | 2         | -1
    #
    move_mapping = [
        [-1, 1, 0],
        [1, -1, 2],
        [0, 2, -1]
    ]

    opp_input_type = input_mapping[opp_input]
    my_input_type = None
    if my_input == "X":
        # Need to lose
        if opp_input_type == "rock":
            my_input_type = "scissors"
        elif opp_input_type == "scissors":
            my_input_type = "paper"
        else:
            my_input_type = "rock"
    elif my_input == "Y":
        # Need to draw
        my_input_type = opp_input_type
    elif my_input == "Z":
        # Need to win
        if opp_input_type == "rock":
            my_input_type = "paper"
        elif opp_input_type == "scissors":
            my_input_type = "rock"
        elif opp_input_type == "paper":
            my_input_type = "scissors"
        else:
            pass
    else:
        pass

    opp_move = list(index_mapping.values()).index(opp_input_type)
    my_move = list(index_mapping.values()).index(my_input_type)

    print(opp_input, my_input, opp_input_type, my_input_type)

    winner = move_mapping[opp_move][my_move]

    round_score = 0
    # Add points for the outcome
    if winner == my_move:
        round_score += 6
    if winner == -1:
        round_score += 3
    else:
        round_score += 0

    # Add points for the move type
    if my_input_type == "rock":
        round_score += 1
    elif my_input_type == "paper":
        round_score += 2
    else:
        round_score += 3
    
    return round_score


def puzzle_solution_part_2(file_name:str = "puzzle-input.txt"):
    """
    """
    my_score = 0
    with open(file_name, "r") as f:
        for line in f:
            input_moves = line.strip().split(" ")
            round_score = get_winner_part_2(opp_input=input_moves[0], my_input=input_moves[1])
            my_score += round_score

    return my_score


#print(puzzle_solution_part_1())
print(puzzle_solution_part_2())