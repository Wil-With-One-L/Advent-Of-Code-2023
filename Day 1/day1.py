def getLines(filename):
  lines = open(filename).readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
  return lines


def getFirstDigit(input):
  while (len(input) > 0):
    if input[0] in ['0','1','2','3','4','5','6','7','8','9']:
      return input[0]
    else:
      input = input[1:]

def getLastDigit(input):
  while (len(input) > 0):
    if input[-1] in ['0','1','2','3','4','5','6','7','8','9']:
      return input[-1]
    else:
      input = input[:-1]



lines = getLines("Day 1/input.txt")

total = 0

for l in lines:
  tens = getFirstDigit(l)
  ones = getLastDigit(l)
  total += int(tens+ones)

print(total)

# Part 1 - 55386