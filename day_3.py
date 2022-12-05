dir = "inputs/day_3.txt"
with open(dir, "r") as f:
    input = f.read()

# print(input)


def convert_char_to_int(char: str):
    # ord gives me the number in ASCII
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


running_sum = 0
for contents in input.split("\n"):
    if len(contents) % 2 != 0:
        print("something is wrong with the input all contents should be even in length")
        break
    i = len(contents) // 2
    first_half = contents[:i]
    second_half = contents[i:]
    common_char = list(set(first_half) & set(second_half))
    running_sum += convert_char_to_int(common_char[0])

print("part 1:", running_sum)


############# PART 2 ###############
running_sum = 0
inputs = input.split("\n")
for i in range(0, len(inputs), 3):
    group = inputs[i : i + 3]
    common_char = list(set(group[0]) & set(group[1]) & set(group[2]))
    running_sum += convert_char_to_int(common_char[0])

print("part 2:", running_sum)
