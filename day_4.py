dir = "inputs/day_4.txt"
with open(dir, "r") as f:
    input = f.read()

inputs = input.split("\n")

full_pairs = 0

for input in inputs:
    pair_1, pair_2 = input.split(",")
    sec_11 = int(pair_1.split("-")[0])
    sec_12 = int(pair_1.split("-")[1])
    sec_21 = int(pair_2.split("-")[0])
    sec_22 = int(pair_2.split("-")[1])

    if sec_11 >= sec_21 and sec_12 <= sec_22:
        full_pairs += 1

    elif sec_21 >= sec_11 and sec_22 <= sec_12:
        full_pairs += 1

print("Number of full pairs:", full_pairs)


########## PART 2 ############

any_overlap = 0

for input in inputs:
    pair_1, pair_2 = input.split(",")
    sec_11 = int(pair_1.split("-")[0])
    sec_12 = int(pair_1.split("-")[1])
    sec_21 = int(pair_2.split("-")[0])
    sec_22 = int(pair_2.split("-")[1])

    if sec_22 >= sec_11 and sec_21 <= sec_12:
        any_overlap += 1

print("part 2 - Number of any overlapping pairs:", any_overlap)
