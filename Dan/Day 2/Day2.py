WIN = "win"
DRAW = "draw"
LOSE = "lose"
WIN_VAL = 6
DRAW_VAL = 3
LOSE_VAL = 0
WIN_MAP = {"A": "Y", "B": "Z", "C": "X"}
DRAW_MAP = {"A": "X", "B": "Y", "C": "Z"}
LOSE_MAP = {"A": "Z", "B": "X", "C": "Y"}
RESULT_MAP = {"X": LOSE, "Y": DRAW, "Z": WIN}
VALUE_MAP = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
FILE = "input.txt"
TEST_FILE = "test_input.txt"
PART_1 = False


def calculate_score(match_list):
    return sum([determine_outcome(match) for match in match_list])


def determine_outcome(match_text):
    score = 0
    their_hand = match_text[0]
    if PART_1:
        our_hand = match_text[-1]
        if WIN_MAP[their_hand] == our_hand:
            score += WIN_VAL
        elif DRAW_MAP[their_hand] == our_hand:
            score += DRAW_VAL
    else:
        match_result = RESULT_MAP[match_text[-1]]
        if match_result == WIN:
            score += WIN_VAL
            our_hand = WIN_MAP[their_hand]
        elif match_result == LOSE:
            our_hand = LOSE_MAP[their_hand]
        else:
            score += DRAW_VAL
            our_hand = their_hand
    return score + VALUE_MAP[our_hand]


if __name__ == "__main__":
    with open(FILE) as f:
        matches_list = f.read().splitlines()

    print(calculate_score(matches_list))
