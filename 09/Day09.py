import fileinput
from itertools import permutations

NUMBERS = [int(line.strip()) for line in fileinput.input()]
PREAMBLE = 25

def encoding_error(data):
    for i in range(PREAMBLE, len(data)):
        num = int(data[i])
        for x, y in permutations(data[i - PREAMBLE: i], 2):
            if int(x) + int(y) == num:
                break
        else:
            return num
    return -1

def part_2(data):
    for i in range(len(data)):
        sum = int(data[i])
        j = i + 1
        nums = [data[i]]
        while sum < 50047984 and i + j < len(data):
            sum += int(data[j])
            nums.append(int(data[j]))
            if sum == 50047984:
                return nums, min(nums) + max(nums)
            j+=1
    return -1

print(f"The answer for part 1 is: {encoding_error(NUMBERS)}")
print(f"The answer for part 2 is: {part_2(NUMBERS)}")