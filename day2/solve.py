with open('day2/input.txt') as l:
  lines = l.readlines()

# a = rock / 1
# B = paper / 2
# c = siccor / 3

# x = rock / 1
# y = paper / 2
# z = siccor / 3
myList = []
myPoints = []


def p1():
  for line in lines: 
    myList.append(line.strip())
    
  for line in myList:
    if line == "A X":
      myPoints.append(4)
    if line == "A Y":
      myPoints.append(8)
    if line == "A Z":
      myPoints.append(3)
    if line == "B X":
      myPoints.append(1)
    if line == "B Y":
      myPoints.append(5)
    if line == "B Z":
      myPoints.append(9)
    if line == "C X":
      myPoints.append(7)
    if line == "C Y":
      myPoints.append(2)
    if line == "C Z":
      myPoints.append(6)
    


def p2():
  for line in lines: 
    myList.append(line.strip())
    
  for line in myList:
    if line == "A X":
      myPoints.append(3) 
    if line == "A Y":
      myPoints.append(4)
    if line == "A Z":
      myPoints.append(8)
    if line == "B X":
      myPoints.append(1)
    if line == "B Y":
      myPoints.append(5)
    if line == "B Z":
      myPoints.append(9)
    if line == "C X":
      myPoints.append(2)
    if line == "C Y":
      myPoints.append(6)
    if line == "C Z":
      myPoints.append(7)



p2()
print(len(myList))
print(sum(myPoints))