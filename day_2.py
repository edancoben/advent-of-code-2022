# https://adventofcode.com/2022/day/2

move_score = {"X": 1, "Y": 2, "Z": 3}
outcome = {
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "A X": 3,
    "B Y": 3,
    "C Z": 3,
}


def rps_score(round: str):
    my_move = round[2]
    return outcome[round] + move_score[my_move]


dir = "inputs/day_2.txt"
with open(dir, "r") as f:
    input = f.read()

rps_rounds = input.split("\n")
my_total_rps_score = sum(map(rps_score, rps_rounds))

print("Strategy Guide total score:", my_total_rps_score)


############# PART 2 ###############
find_my_move = {
    "A X": "Z",
    "A Y": "X",
    "A Z": "Y",
    "B X": "X",
    "B Y": "Y",
    "B Z": "Z",
    "C X": "Y",
    "C Y": "Z",
    "C Z": "X",
}
easy_outcome = {"X": 0, "Y": 3, "Z": 6}


def rps_score_2(round: str):
    my_move = find_my_move[round]
    return move_score[my_move] + easy_outcome[round[2]]


my_total_rps_score = sum(map(rps_score_2, rps_rounds))

print("Pt 2 Strategy Guide total score:", my_total_rps_score)
