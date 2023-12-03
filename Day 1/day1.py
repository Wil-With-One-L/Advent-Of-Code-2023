num_string = dict()
num_string["one"] = "1"
num_string["two"] = "2"
num_string["three"] = "3"
num_string["four"] = "4"
num_string["five"] = "5"
num_string["six"] = "6"
num_string["seven"] = "7"
num_string["eight"] = "8"
num_string["nine"] = "9"


def getLines(filename):
  lines = open(filename).readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
  return lines


def getFirstDigit(input):
  curr_string = ""

  while (len(input) > 0):
    if input[0] in ['0','1','2','3','4','5','6','7','8','9']:
      return input[0]
    
    curr_string += input[0]
    for num in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
      if num in curr_string:
        return num_string[num]
    
    input = input[1:]

def getLastDigit(input):
  curr_string = ""

  while (len(input) > -1):
    if input[-1] in ['0','1','2','3','4','5','6','7','8','9']:
      return input[-1]
    
    curr_string = input[-1] + curr_string
    for num in ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]:
      if num in curr_string:
        return num_string[num]
    
    input = input[:-1]



lines = getLines("Day 1/input.txt")

total = 0

for l in lines:
  tens = getFirstDigit(l)
  ones = getLastDigit(l)
  total += int(tens+ones)

print(total)

# Part 1 - 55386
# Part 2 - 54824