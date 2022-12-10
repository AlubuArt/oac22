with open('input.txt', 'r') as l:
  lines = l.readlines()

  def findRange(l):
    range_1 = []
    range_2 = []
    for i in range(l[0], l[1]+1):
      range_1.append(i)
    for k in range(l[2], l[3]+1):
      range_2.append(k)
    return range_1, range_2
    

def fullyContains(input):


  s = set(input[1])
  k = set(input[0])

  temp_1 = [x for x in input[0] if x not in s]
  temp_2 = [x for x in input[1] if x not in k]

  if (len(temp_1) != 0):
    return 1
  if (len(temp_2) != 0):
    return 1
  else:
    return 0

def p1():

  result = []
  for line in lines:

    line=list(map(int, line.strip().replace('-', ',').split(',')))

    result.append(fullyContains(findRange(line)))
  
  print(sum(result))


 

    
def contains(input):


  s = set(input[1])
  k = set(input[0])

  temp_1 = [x for x in input[0] if x in s]

  if len(temp_1) > 0:
    return temp_1
   
 

def p2():

  result = []
  for line in lines:
    line=list(map(int, line.strip().replace('-', ',').split(',')))
    if line is type([]):
      result.append(contains(findRange(line)))

  print(result)
  
   

    
   

    

p2()

