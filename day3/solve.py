with open('input.txt', 'r') as l:
  input = l.readlines()
  lines = [lines.strip() for lines in input]

appearsInBothRuckSacks = []

def splitStrings(line):

      half_length = len(line) // 2
      first_half, second_half = line[:half_length], line[half_length:]
      return first_half, second_half

def compareStrings(a, b):
    for i in a:
      if i in b:
        appearsInBothRuckSacks.append(i)
        return

def prioritizeItems(input):  

  numbers = []

  for char in input:
    if char.islower() == True:
      number = ord(char) - 96
      numbers.append(number)
    else:
      number = ord(char) - 38
      numbers.append(number)     
  return numbers

def p1():

  for line in lines: 
    a, b = splitStrings(line)
    compareStrings(a, b)
      
  result = prioritizeItems(appearsInBothRuckSacks)
  print(sum(result))


p1()

# Part Two

def groupInThree(list):
  return zip(*[iter(list)]*3)

def compareThreeString(a, b, c):
  for i in a:
    if i in b:
      for z in c:
        if i in c:
          return i

def findBadge(list):
  badges = []
  groups = set(groupInThree(list))
  for l in groups:
    badge = compareThreeString(l[0], l[1], l[2])
    badges.append(badge)
  return badges
    

def p2(input):
  badges = findBadge(input)
  prioritized = sum(prioritizeItems(badges))
  print(prioritized)

p2(lines)