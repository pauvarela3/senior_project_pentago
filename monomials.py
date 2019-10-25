from pprint import pprint
import copy
print('\n')

monomials = [
     ['0000', '0010', '0020', '2000', '2010'],# 16
     ['0010', '0020', '2000', '2010', '2020'],# 16
     ['0000', '0110', '0220', '3000', '3110'],# 16
     ['0110', '0220', '3000', '3110', '3220'],# 16 
     ['0000', '0100', '0200', '1000', '1100'],# 16
     ['0100', '0200', '1000', '1100', '1200'],# 16
     ['0010', '0110', '0210', '1010', '1110'],# 16
     ['0110', '0210', '1010', '1110', '1210'],# 16
     ['0010', '0120', '2200', '3010', '3120'],# 64
     ['0020', '0120', '0220', '1020', '1120'],# 16
     ['0120', '0220', '1020', '1120', '1220'],# 16 
     ['2000', '2100', '2200', '3000', '3100'],# 16
     ['2100', '2200', '3000', '3100', '3200'],# 16
     ['2010', '2110', '2210', '3010', '3110'],# 16
     ['2110', '2210', '3010', '3110', '3210'],# 16
     ['2010', '2100', '0220', '1010', '1100'],# 64
     ['2020', '2120', '2220', '3020', '3120'],# 16
     ['2120', '2220', '3020', '3120', '3220'],# 16
     ['2020', '2110', '2200', '1020', '1110'],# 16
     ['2110', '2200', '1020', '1110', '1200'],# 16
     ['0100', '0110', '0120', '2100', '2110'],# 16
     ['0110', '0120', '2100', '2110', '2120'],# 16
     ['0100', '0210', '1020', '3100', '3210'],# 64
     ['0200', '0210', '0220', '2200', '2210'],# 16
     ['0210', '0220', '2200', '2210', '2220'],# 16
     ['1000', '1010', '1020', '3000', '3010'],# 16
     ['1010', '1020', '3000', '3010', '3020'],# 16
     ['1100', '1110', '1120', '3100', '3110'],# 16
     ['1110', '1120', '3100', '3110', '3120'],# 16
     ['1200', '1210', '1220', '3200', '3210'],# 16
     ['1210', '1220', '3200', '3210', '3220'],# 16
     ['1210', '1120', '3000', '2210', '2120'],# 64
                                              # 704
]
number_of_states = 0
empty = []



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

# rotate_4("0", monomials)
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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


# rotate_3("0", monomials)
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
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


# rotate_2("0", monomials)
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

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


rotate_1("0", monomials)
print("this is the number of monomials with duplicates")
print(len(empty))


empty_1 = []
for i in empty:
    if i not in empty_1:
        empty_1.append(i)

print("Should have the duplicates cleaned off")
pprint(empty_1)
print("length of clean empty:")
print(len(empty_1))





# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # # # # # # # # # # # # # # code with comments# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# keys = ['0000', '0010', '0020', '0100', '0110', '0120', '0200', '0210', '0220' ]

# keys to be used in for loop (maybe)
# keys = [
#   ['0000', '0010', '0020', '0100', '0110', '0120', '0200', '0210', '0220'],
#   ['0001', '0011', '0021', '0101', '0111', '0121', '0201', '0211', '0221'],
#   ['0002', '0012', '0022', '0102', '0112', '0122', '0202', '0212', '0222'],
#   ['0003', '0013', '0023', '0103', '0113', '0123', '0203', '0213', '0223']
# ]

# print("keys")
# pprint(keys)


# direction = "0"
# empty = []
# count = 0
# while count < 4:

    # copying monomials array by value
    # mono_copy = copy.deepcopy(monomials)

#   # looping through each array in monomials
#   for i in range(len(mono_copy)):
#
#     # looping through each element in array
#     for j in range(len(mono_copy[i])):
#
#       two methods below=> either find by keys or find by first character
#       # if specific monomial is in keys array
#       # if monomials[i][j] in keys:
#
#       # if specific momonial's first character is a zero
#       if monomials[i][j][0] == "0":
#         mono_copy[i][j] = mono_copy[i][j][:-1] + direction
#
#   # incrementing 'direction': setting string value of direction to => integer value + 1
#   direction = str((int(direction) + 1))
#
#   # direction = str(direction)
#   count += 1
#
#
#
#
#   # print(f'value of array 'empty' after iteration direction {direction}')
#   # pprint(empty)
#
#   !when apending, either 3D or 2D:
#   # 3D array generated with arrays depicting 'states'
#   empty.append(copy.deepcopy(mono_copy))
#   # 2D array generated
#   # concatentation generates 2D array with every monomial
#   # empty = empty + copy.deepcopy(mono_copy)
#
#
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


print('\n')
