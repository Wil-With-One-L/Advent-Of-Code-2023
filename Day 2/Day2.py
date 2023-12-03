def cleanInput(filename):
  lines = open(filename).readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip("\n")
    lines[i] = lines[i].replace("Game ", "")
    # lines[i] = lines[i].replace(",", "")
    lines[i] = lines[i].replace(";", ",")
    lines[i] = lines[i].replace(", ", ",")
    lines[i] = lines[i].strip("1234567890:")
    lines[i] = lines[i].strip(" ")

    lines[i] = lines[i].split(",")

  return lines

def createPairs(line):
  pairs = []
  for item in line:
    pair = item.split(" ")
    pair[0] = int(pair[0])
    pairs.append(pair)
  return pairs

lines = cleanInput("Day 2/input.txt")

total = 0

for i in range(0,100):
  red_max = 0
  green_max = 0
  blue_max = 0

  line = lines[i]

  pairs = createPairs(line)
  for pair in pairs:
    match pair[1]:
      case "red":
        red_max = max(pair[0], red_max)
      case "green":
        green_max = max(pair[0], green_max)
      case "blue":
        blue_max = max(pair[0], blue_max)
  
  power = red_max * green_max * blue_max
  total += power

print(total)

# 4723 too high
# 4649 too high
# Part 1 - 2348

# Part 2 - 76008