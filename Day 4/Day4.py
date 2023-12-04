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

lines = cleanInput("Day 4/input.txt")

points = 0
for l in lines:
  matching = 0
  for winning in l[0]:
    if winning in l[1]:
      matching += 1
  if matching > 0:
    points += (2 ** (matching - 1))

print(points)

# 960 too low
# 52728 too high
# 52508 too high
# Part 1 - 26346