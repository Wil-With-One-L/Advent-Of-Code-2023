def cleanInput(filename):
  lines = open(filename).readlines()
  for i in range(0, len(lines)):
    lines[i] = lines[i].strip("\n")
  return lines

def cleanSeeds(lines):
  seeds = []
  line = lines[0].split()[1:]
  for i in range(0, len(line)):
    line[i] = int(line[i])

  i = 0
  while i < len(line):
    seeds.append([line[i], line[i + 1]])
    i += 2

  return seeds

# returns a list with 7 maps
def cleanMaps(lines):
  # order[0] = seed-to-soil, order[1] = soil-to-fertilizer, etc.
  maps = []

  curr_map = []
  i = 0

  while i < len(lines):
    line = lines[i]
    if line == "":
      maps.append(curr_map)
      i += 1
      curr_map = []
    else:
      temp = line.split()
      for j in range(0, len(temp)):
        temp[j] = int(temp[j])
      curr_map.append(temp)
    
    i += 1

  maps.append(curr_map)
  return maps

def findMinLocation(loc_map):
  min_loc = loc_map[0][0]
  for mapping in loc_map:
    min_loc = min(mapping[0], min_loc)

  return min_loc
  

lines = cleanInput("Day 5/input.txt")
seeds = cleanSeeds(lines)
maps = cleanMaps(lines[3:])

# min_location = int(seeds[0][0])

# for seed_pair in seeds:
#   # for curr_num in range(int(seed_pair[0]), int(seed_pair[0]) + int(seed_pair[1])):
#   for map_idx in range(0,7): # each map
#     for mapping in maps[map_idx]: # each possible range in map
#       start = int(mapping[1])
#       end = start + int(mapping[2])

#       seed_num_min = int(seed_pair[0])
#       seed_num_max = seed_num_min + int(seed_pair[1])

#       if (seed_num_min < start or seed_num_max >= end):
#         break

#       print(seed_num_min, seed_num_max)

#       if (curr_num >= start and curr_num < end):
#         diff = curr_num - start
#         curr_num = int(mapping[0]) + diff
#         break
#   min_location = min(min_location, curr_num)

# print(min_location)

# ===========

# New idea: Start from the locations, work back up until you find a compatible seed

min_location = findMinLocation(maps[6])
# print(min_location)

check = 0

while check < 100000000000:
  print(f"\r{check}", end = "")
  curr_num = check
  for map_idx in range(6, -1, -1):
    # check if curr_num is within map[5]'s range
    for mapping in maps[map_idx]:
      start = mapping[0]
      end = start + mapping[2]
      if (curr_num < end and curr_num >= start): # if it is, continue upwards 
        # curr num becomes the above map number
        diff = curr_num - start
        curr_num = mapping[1] + diff
        break
  
  found = False
  for seed_pair in seeds:
    start = seed_pair[0]
    end = start + seed_pair[1]
    if (curr_num < end and curr_num >= start):
      print("FOUND: ", check)
      found = True

  if found:
    break

  check += 1
  


# Part 1 - 313045984

# 26788781 too high
# Part 2 - 20283860