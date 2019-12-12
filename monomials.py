###This program finds out all the possible monomials in the 6x6 board.


from pprint import pprint
import copy

#List of monomials in state 0 where state 0 is when all quads are in rotation 0
monomials = [
     ['0000', '0010', '0020', '1000', '1010'],# 16
     ['0010', '0020', '1000', '1010', '1020'],# 16
     ['0000', '0110', '0220', '3000', '3110'],# 16
     ['0110', '0220', '3000', '3110', '3220'],# 16 
     ['0000', '0100', '0200', '2000', '2100'],# 16
     ['0100', '0200', '2000', '2100', '2200'],# 16
     ['0010', '0110', '0210', '2010', '2110'],# 16
     ['0110', '0210', '2010', '2110', '2210'],# 16
     ['0010', '0120', '1200', '3010', '3120'],# 64
     ['0020', '0120', '0220', '2020', '2120'],# 16
     ['0120', '0220', '2020', '2120', '2220'],# 16 
     ['1000', '1100', '1200', '3000', '3100'],# 16
     ['1100', '1200', '3000', '3100', '3200'],# 16
     ['1010', '1110', '1210', '3010', '3110'],# 16
     ['1110', '1210', '3010', '3110', '3210'],# 16
     ['1010', '1100', '0220', '2010', '2100'],# 64
     ['1020', '1120', '1220', '3020', '3120'],# 16
     ['1120', '1220', '3020', '3120', '3220'],# 16
     ['1020', '1110', '1200', '2020', '2110'],# 16
     ['1110', '1200', '2020', '2110', '2200'],# 16
     ['0100', '0110', '0120', '1100', '1110'],# 16
     ['0110', '0120', '1100', '1110', '1120'],# 16
     ['0100', '0210', '2020', '3100', '3210'],# 64
     ['0200', '0210', '0220', '1200', '1210'],# 16
     ['0210', '0220', '1200', '1210', '1220'],# 16
     ['2000', '2010', '2020', '3000', '3010'],# 16
     ['2010', '2020', '3000', '3010', '3020'],# 16
     ['2100', '2110', '2120', '3100', '3110'],# 16
     ['2110', '2120', '3100', '3110', '3120'],# 16
     ['2200', '2210', '2220', '3200', '3210'],# 16
     ['2210', '2220', '3200', '3210', '3220'],# 16
     ['2210', '2120', '3000', '1210', '1120'],# 64
                                              # 704
]
empty = []#array that will get all the different combination of monomials
          #including duplicates

#All the rotate functions do is make sure to rotate it's own quadrant,
#and add the monomials that are made by rotating that quadrant including
#duplicates

#This function rotates quadrant 3 which is the last layer to get
#all the different combinations 
def rotate_4(quadrant, array):
    boolean = False
    direction = "0"
    count = 0
    while count < 4:

        for i in range(len(array)):

            for j in range(len(array[i])):

                if monomials[i][j].startswith(quadrant):
                    array[i][j] = array[i][j][:-1] + direction
                    boolean = True
            if(boolean == True):
                boolean = False
                array_1 = copy.deepcopy(array[i])
                empty.append(array_1)
            
        direction = str((int(direction) + 1))
        count = count + 1

#This function rotates quadrant 2 which is the second to last layer
#to get all the different combinations
def rotate_3(quadrant, array):
  direction = "0"
  count = 0
  boolean = False
  while count < 4:

    for i in range(len(array)):

      for j in range(len(array[i])):

        if monomials[i][j].startswith(quadrant):
          array[i][j] = array[i][j][:-1] + direction
          boolean = True
      if(boolean == True):
          boolean = False
          array_1 = copy.deepcopy(array[i])
          empty.append(array_1)
    rotate_4("3", array)
    direction = str((int(direction) + 1))
    count = count + 1

#This function rotates quadrant 1 which is the second layer to get
#all the different combinations
def rotate_2(quadrant, array):
  direction = "0"
  count = 0
  boolean = False
  while count < 4:

    for i in range(len(array)):

      for j in range(len(array[i])):

        if monomials[i][j].startswith(quadrant):
          array[i][j] = array[i][j][:-1] + direction
          boolean = True  
      if(boolean == True):
          boolean = False
          array_1 = copy.deepcopy(array[i])
          empty.append(array_1)
    rotate_3("2", array)
    direction = str((int(direction) + 1))
    count = count + 1

#This function rotates quadrant 0 which is the first layer to get
#all the different combinations
def rotate_1(quadrant, array):
  empty = copy.deepcopy(monomials)  
  direction = "0"
  count = 0
  boolean = False
  while count < 4:
    array = copy.deepcopy(monomials)

    for i in range(len(array)):

      for j in range(len(array[i])):

        if monomials[i][j].startswith(quadrant):
          array[i][j] = array[i][j][:-1] + direction
          boolean = True  
      if(boolean == True):
          boolean = False
          array_1 = copy.deepcopy(array[i])
          empty.append(array_1)
    rotate_2("1", array)
    direction = str((int(direction) + 1))
    count = count + 1

#call rotate_1 to start the rotations starting with all the quadrants being 0
rotate_1("0", monomials)
#Since empty has duplicates, here we take away the duplicates.
empty_1 = []
for i in empty:
    if i not in empty_1:
        empty_1.append(i)
