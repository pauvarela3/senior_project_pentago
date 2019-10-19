from pprint import pprint
import copy
print('\n')

monomials = [
    ['0000', '0010', '0020', '2000', '2010'],
    ['0010', '0020', '2000', '2010', '2020'],
    ['0000', '0110', '0220', '3000', '3110'],
    ['2010', '2100', '0220', '1010', '1100'],
    ['1210', '1120', '3000', '2210', '2120']
]

empty = []



def rotate_4(quadrant, array):
    direction = "0"
    count = 0
    while count < 4:

        array = copy.deepcopy(monomials)

        for i in range(len(array)):

            for j in range(len(array[i])):

                if monomials[i][j].startswith(quadrant):
                    array[i][j] = array[i][j][:-1] + direction

        direction = str((int(direction) + 1))
        count = count + 1
        empty.append(array)

# rotate_4("0", monomials)
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def rotate_3(quadrant, array):
  direction = "0"
  count = 0
  while count < 4:

    array = copy.deepcopy(monomials)

    for i in range(len(array)):

      for j in range(len(array[i])):

        if monomials[i][j].startswith(quadrant):
          array[i][j] = array[i][j][:-1] + direction

    rotate_4("3", array)
    empty.append(array)
    direction = str((int(direction) + 1))
    count = count + 1


# rotate_3("0", monomials)
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
def rotate_2(quadrant, array):
  direction = "0"
  count = 0
  while count < 4:

    array = copy.deepcopy(monomials)

    for i in range(len(array)):

      for j in range(len(array[i])):

        if monomials[i][j].startswith(quadrant):
          array[i][j] = array[i][j][:-1] + direction

    rotate_4("2", array)
    empty.append(array)
    direction = str((int(direction) + 1))
    count = count + 1


# rotate_2("0", monomials)
# print("value of empty after loop: ")
# pprint(empty)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

def rotate_1(quadrant, array):
  direction = "0"
  count = 0
  while count < 4:

    array = copy.deepcopy(monomials)

    for i in range(len(array)):

      for j in range(len(array[i])):

        if monomials[i][j].startswith(quadrant):
          array[i][j] = array[i][j][:-1] + direction

    rotate_2("1", array)
    empty.append(array)
    direction = str((int(direction) + 1))
    count = count + 1


rotate_1("0", monomials)
print("value of empty after loop: ")
pprint(empty)








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