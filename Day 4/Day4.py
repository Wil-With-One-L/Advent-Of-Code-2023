def cleanInput(filename):
  lines = open(filename).readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
    lines[i] = lines[i][10:]
    lines[i] = lines[i].replace("  ", " ")

    lines[i] = lines[i].split("|")
    lines[i][0] = lines[i][0].strip()
    lines[i][0] = lines[i][0].split(" ")
    lines[i][1] = lines[i][1].strip()
    lines[i][1] = lines[i][1].split(" ")
  return lines

# maps card idx to number of numbers that match winning numbers
def getMatchingNums(lines):
  output = []
  for card in lines:
    matching = 0
    for winning in card[0]:
      if winning in card[1]:
        matching += 1
      
    output.append(matching)

  return output
    
# Returns a dict with 0-219 mapped to 1
def makeCopies():
  ret = dict()
  for i in range(0, 220):
    ret[i] = 1
  return ret

def getTotal(copies):
  total = 0
  for i in range(0, 220):
    total += copies[i]
  return total

lines = cleanInput("Day 4/input.txt")
matching_nums = getMatchingNums(lines)
copies = makeCopies()
print(matching_nums)

# add a copy of the next (matching_nums[i]) cards

for idx in range(0, 220):
  matches = matching_nums[idx]

  if matches > 0:
    for i in range(idx + 1, idx + matches + 1):
      copies[i] = copies[i] + (copies[idx])

total = getTotal(copies)
print(total)


# 960 too low
# 52728 too high
# 52508 too high
# Part 1 - 26346

# Part 2 - 8467762