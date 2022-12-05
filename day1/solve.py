with open('day1/input.txt', 'r') as l:
  lines = l.readlines()

def p1():
  elf_max = 0
  current_elf = 0
  for line in lines:
    if line != '\n': 
        current_elf += int(line)
    else:
      if current_elf > elf_max:
        elf_max = current_elf
      current_elf = 0
      
    
  print(elf_max)
  return elf_max

p1()


def p2():
  elf_1 = p1()
  elf_2 = 0
  elf_3 = 0
  current_elf = 0

  for line in lines:
    if line != '\n':
      current_elf += int(line)
    else: 
      if current_elf > elf_2 and current_elf != elf_1:
        elf_2 = current_elf
      else:
        if current_elf > elf_3 and current_elf != elf_1:
          elf_3 = current_elf
      current_elf = 0

  print(elf_1, elf_2, elf_3)
  print(elf_1 + elf_2 + elf_3)


p2()


        

