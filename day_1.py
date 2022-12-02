dir = "inputs/day_1.txt"
with open(dir, "r") as f:
    input = f.read()

total_cals = [sum(list(map(int, cals.split("\n")))) for cals in input.split("\n\n")]

# Find the Elf carrying the most Calories
print("Total Calories from heaviest Elf:", max(total_cals))
