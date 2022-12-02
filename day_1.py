# https://adventofcode.com/2022/day/1

dir = "inputs/day_1.txt"
with open(dir, "r") as f:
    input = f.read()

total_cals = [sum(map(int, cals.split("\n"))) for cals in input.split("\n\n")]

# Find the Elf carrying the most Calories
print("Total Calories from heaviest Elf:", max(total_cals))


############# PART 2 ###############

# now need top 3 elves
top_3 = sorted(total_cals, reverse=True)[:3]
print("Top 3 total cals:", sum(top_3))
