import os


scores = {}
entities = {}

# the most interesting part of this puzzle is this relationship graph.
# Everything else can be derived from this.
# Scissors > Paper > Rock > Scissors


# Arrive at by traversing circular graph above left
winning_strategy = {}
def init_win_given_opp_move() -> None:
    winning_strategy['R'] = 'P'
    winning_strategy['P'] = 'S'
    winning_strategy['S'] = 'R'


# Arrive at by traversing circular graph above right
losing_strategy = {}
def init_lose_given_opp_move() -> None:
    losing_strategy['R'] = 'S'
    losing_strategy['P'] = 'R'
    losing_strategy['S'] = 'P'


def init_scores() -> None:
    scores['R'] = 1     # rock
    scores['P'] = 2     # paper
    scores['S'] = 3     # scissors


def init_entities() -> None:
    entities['A'] = 'R'
    entities['B'] = 'P'
    entities['C'] = 'S'


def get_entity(move: str) -> str:
    return entities[move]


# Given a move that is X, Y or Z return a score
def get_move_score(move: str) -> int:
    entity = get_entity(move)
    return scores[entity]


def get_round_score(opp_move: str, your_move: str) -> int:
    opp_entity = get_entity(opp_move)
    round_score = 0
    move_score = 0
    if your_move == 'Y':    # Tie
        round_score = 3
        move_score = scores[opp_entity]
    if your_move == 'X':    # Lose
        round_score = 0
        your_entity = losing_strategy[opp_entity]
        move_score = scores[your_entity]
    if your_move == 'Z':
        round_score = 6
        your_entity = winning_strategy[opp_entity]
        move_score = scores[your_entity]
    print(f"Round {round_score}, Move {move_score}")
    return round_score + move_score


def get_total_score(rounds: list[str]):
    total_score = 0
    rounds = [turn.rstrip() for turn in rounds]
    print(f"There are {len(rounds)} rounds")
    for turn in rounds:
        turn = turn.split(' ')
        print(f"Turn: {turn}")
        round_score = get_round_score(turn[0], turn[1])
        total_score += round_score
        # print(f"Eval {turn}: Move score {move_score}, Round score {round_score} = {move_score + round_score}")
    return total_score


def main() -> None:
    init_scores()
    init_entities()
    init_lose_given_opp_move()
    init_win_given_opp_move()
    fpath = os.getcwd() + "/input.txt"
    file = open(fpath, "r")
    print(f"Your score per the strategy guide is {get_total_score(file.readlines())}")
    # test = ["A Y", "B X", "C Z"]
    # print(f"{get_total_score(test)}")


# separate out the side effects and make it easy to test
if __name__ == '__main__':
    main()
