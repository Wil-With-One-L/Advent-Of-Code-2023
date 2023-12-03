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

red_max = 12
green_max = 13
blue_max = 14

lines = cleanInput("Day 2/input.txt")

print(createPairs(lines[0]))

total = 0

for i in range(0,100):
  broken = False
  line = lines[i]

  pairs = createPairs(line)
  for pair in pairs:
    match pair[1]:
      case "red":
        if pair[0] > red_max:
          broken = True
          break
      case "green":
        if pair[0] > green_max:
          broken = True
          break
      case "blue":
        if pair[0] > blue_max:
          broken = True
          break
  
  if broken == False:
    total += i + 1

print(total)

# 4723 too high
# 4649 too high
# Part 1 - 2348