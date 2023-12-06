def cleanInput(filename):
  lines = open(filename).readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip("\n").split()[1:]
    for j in range(0, len(lines[i])):
      lines[i][j] = int(lines[i][j])
  return lines

def calculateWaysToBeat(time, record_distance):
  count = 0
  for hold_time in range(1, time):
    # will move (hold_time) mm per second for (time_left) seconds
    time_left = time - hold_time
    trav_distance = hold_time * time_left
    if trav_distance > record_distance:
      count += 1
  return count

lines = cleanInput("Day 6/input.txt")

score = 1

for i in range(0, len(lines[0])):
  score *= calculateWaysToBeat(lines[0][i], lines[1][i])

print(score)

# Part 1 - 281600