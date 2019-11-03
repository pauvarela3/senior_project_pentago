#AI Programming Script with backstage gameboard
from pprint import pprint
import monomials

score = 0
nodes = []
nodes_1 = []
monomial_objects = []
class monomial:
    __monomial = []
    __score = 0
    def __init__(self,monomial = 0, score =0):
        self.__monomial = monomial
        self.__score = score
    def return_monomial(self):
        return self.__monomial


    
class node:
    #class variables
    __quad = 0
    __row = 0
    __col = 0
    __rotation = 0
    __score = 0
    __string = ""
    __monomials = []
    #constructor
    def __init__(self,quad = 0, col = 0, row = 0, rotations = 0, score =0, string = "", monomials = []):
        self.__quad = quad
        self.__col = col
        self.__row = row
        self.__rotations = rotations
        self.__score = score
        self.__string = string
        self.__monomials = monomials
        #static methods
        #instance methods
    def monomials_constructor(self,monomial):
        self.__monomials.append(monomial)
        #print(self.__string)
    def return_string(self):
        return self.__string
    def return_monomials(self):
        return self.__monomials

#def main():
#    pass

#if __name__ == '__main__':
#    main()

def defining_backboard():
    global nodes
    global nodes_1
    quad = 0
    col = 0
    row = 0
    rotation = 0
    score = 0
    col_based_on_quad = 0
    row_based_on_quad = 0
    string = ""
    monomials_1 = []
    monomial_constructor()
    #############################################################################
    #In this for loop, we construct the 36 nodes in the game board
    for i in range(36):
        string = str(quad) + str(col_based_on_quad) + str(row_based_on_quad) + str(rotation)
        #########################################################################
        #In here we connect the node objects with monomial objects
        for rotations in range(4):
            string = string[:-1] + str(rotations)
            #pprint(string)
            for j in monomial_objects:
                for k in j.return_monomial():
                    if string == k:
                        monomials_1.append(j)
                        break
        #########################################################################
        nodes.append(node(quad, col, row, rotation, score, string, monomials_1))
        monomials_1 = []#here you reset the monomials_1 list to get the other node monomials
        col += 1
        if col == 6:
            row += 1
            col = 0
        if col < 3:
            if row <3:
                quad = 0
            else:
                quad = 1
        else:
            if row < 3:
                quad = 2
            else:
                quad = 3
        if col >= 3:
            col_based_on_quad = col%3
        else:
            col_based_on_quad = col
        if row >= 3:
            row_based_on_quad = row%3
        else:
            row_based_on_quad = row
    ##############################################################################
#This construct the list of monomial objects
def monomial_constructor():
    global monomial_objects
    for i in monomials.empty_1:
        monomial_objects.append(monomial(i, 0))

#def score_taking():
    #global monmial_objects
    #global nodes

    




#IGNORE COMMMENTED OUT STUFF
    #for i in monomial_objects:
        #pprint(index)
        #pprint(i.return_monomial())
        #index+=1
        
#def connect_to_monomials():
    #global nodes
    #nodes_1[0].monomials_constructor(monomials.empty_1)
    #for i in nodes:
        #for j in monomials.empty_1:
            #for k in j:
                #if i.return_string == k:
                    #print ("----------------------------------------------")
                    #i.monomials_constructor(j)
                    #break
        


defining_backboard()
#for i in range(36):
    #pprint(nodes_1[i].return_string())
    #pprint(str(i) + " " + nodes[i].return_string())
#connect_to_monomials()


##################################################################################
##########                                                              ##########
##########                      Printing the monomials                  ##########
##########                                                              ##########
##################################################################################

for i in range(36):
    print(str(i))
    pprint(nodes[i].return_monomials())









