#AI Programming Script with backstage gameboard
from pprint import pprint
import monomials
nodes = []
nodes_1 = []
monomial_objects = []
changed = False
class monomial:
    __monomial = []
    __nodes = [0] * 5
    __score = 1
    __passed = False
    __passing = 0
    __iterator = 0
    __complete = False
    def __init__(self,monomial = 0, nodes = [0] * 5, score =1,passed = False, passing = 0, iterator = 0, complete = False):
        self.__monomial = monomial
        self.__nodes = nodes
        self.__score = score
        self.__passed = passed
        self.__passing = passing
        self.__iterator = iterator
        self.__complete = complete
    def monomial_score_update(self, taken):
        #CHANGE THIS TO 1 IF YOU WANT THE AI TO BE SECOND PLAYER
        if taken == 1:
            #if (self.__score <= 3):
            self.__score = self.__score*4
            #elif (self.__score <= 6):
                #self.__score = self.__score*4
            #elif (self.__score <= 24):
                #self.__score = self.__score*8
            #elif (self.__score <= 192):
                #self.__score = self.__score * 16
            #elif (self.__score <= 3072):
                #self.__score = self.__score * 32
        elif taken == 0:
            self.__score = self.__score*0
    def monomial_score_reset(self):
        self.__score = int(self.__score/4)
        #print("This is the score: " + str(self.__score))
    def monomial_score_rotation_update(self, rotations_away):
        if self.__passed == False:
            if rotations_away >= 2 and self.__passing == 2:
                self.__score = int(self.__score/3)
                self.__passing = 0
            elif rotations_away >= 2 and self.__passing == 1:
                self.__score = int(self.__score/2)
                self.__passing = 0
            elif rotations_away == 1 and self.__passing == 2:
                self.__score = int(self.__score/3)
                self.__score = self.__score*2
                self.__passing = 1
            elif rotations_away == 1 and self.__passing == 0:
                self.__score = self.__score*2
                self.__passing = 1
            elif rotations_away == 0 and self.__passing == 1:
                self.__score = int(self.__score/2)
                self.__score = self.__score*3
                self.__passing = 2
            elif rotations_away == 0 and self.__passing == 0:
                self.__score = self.__score*3
                #print("Look at this monomial:" + str(self.__monomial))
                self.__passing = 2
            elif rotations_away >= 2 and self.__passing == 0:
                self.__score = self.__score*1
        self.__passed = True
    def add_node(self, i):
        self.__nodes[self.__iterator] = i
        self.__iterator += 1
    def update_complete(self):
        self.__complete = True
    def reset_passed(self):
        self.__passed = False
    def return_complete(self):
        return self.__complete
    def return_passed(self):
        return self.__passed
    def return_monomial(self):
        return self.__monomial
    def return_score(self):
        return self.__score
    def return_nodes(self):
        return self.__nodes
    def reset(self):
        self.__score = 1
        self.__passed = False
        self.__passing = 0
        self.complete = False



class node:
    #class variables
    __quad = 0
    __row = 0
    __col = 0
    __rotation = 0
    __string = ""
    __monomials = []
    __taken = 2
    __score = 0
    #constructor
    def __init__(self,quad = 0, col = 0, row = 0, rotations = 0, string = "", monomials = [], taken = 2, score = 0):
        self.__quad = quad
        self.__col = col
        self.__row = row
        self.__rotations = rotations
        self.__string = string
        self.__monomials = monomials
        self.__taken = taken
        self.__score = score
        #static methods
        #instance methods
    def monomials_constructor(self,monomial):
        self.__monomials.append(monomial)
    def update_taken_state(self,taken):
        self.__taken = taken
    def update_score(self, score):
        self.__score = score
    def return_string(self):
        return self.__string
    def return_monomials(self):
        return self.__monomials
    def return_state(self):
        return self.__taken
    def return_score(self):
        return self.__score
    def reset(self):
        self.__score = 0
        self.__taken = 2



#def main():
#    pass

#if __name__ == '__main__':
#    main()

def defining_backboard():
    global nodes
    global nodes_1
    positions = ""
    quad = 0
    col = 0
    row = 0
    rotation = 0
    score = 1
    col_based_on_quad = 0
    row_based_on_quad = 0
    string = ""
    monomials_1 = []
    taken = 2
    monomial_constructor(score)
    #############################################################################
    #In this for loop, we construct the 36 nodes in the game board
    for i in range(36):
        string = str(quad) + str(row_based_on_quad) + str(col_based_on_quad) + str(rotation)
        #########################################################################
        #In here we connect the node objects with monomial objects
        positions = string[1] + string[2]
        for rotations in range(4):
            string = string[:-1] + str(rotations)
            if positions == "00":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "021"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "222"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "203"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 2nd col in the 1st row
            elif positions == "01":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "121"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "212"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "103"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 3rd col in the 1st row
            elif positions == "02":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "221"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "202"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "003"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 1st col in the 2nd row
            elif positions == "10":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "011"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "122"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "213"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 2nd col in the 2nd row
            elif positions == "11":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "111"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "112"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "113"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 3rd col in the 2nd row
            elif positions == "12":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "211"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "102"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "013"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 1st col in the 3rd row
            elif positions == "20":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "001"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "022"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "223"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 2nd col in the 3rd row
            elif positions == "21":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "101"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "012"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "123"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
##################################################################################
#In here it's the 3rd col in the 3rd row
            elif positions == "22":
                if rotations == 0:
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 1:
                    string = string[:-3] + "201"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 2:
                    string = string[:-3] + "002"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
                elif rotations == 3:
                    string = string[:-3] + "023"
                    for j in monomial_objects:
                        for k in j.return_monomial():
                            if string == k:
                                monomials_1.append(j)
                                break
        #########################################################################
        nodes.append(node(quad, col, row, rotation, string, monomials_1, taken))
        monomials_1 = []#here you reset the monomials_1 list to get the other node monomials
        col += 1
        if col == 6:
            row += 1
            col = 0
        if col < 3:
            if row <3:
                quad = 0
            else:
                quad = 2
        else:
            if row < 3:
                quad = 1
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
def monomial_constructor(score):
    global monomial_objects
    passing = 0
    passed = False
    iterator = 0
    complete = False
    for i in monomials.empty_1:
        nodes = [0] * 5
        monomial_objects.append(monomial(i, nodes, score, passed, passing, iterator, complete))

def score_taking(variable_number,turn):
    global nodes
    for i in range(36):
        if i == variable_number:
            nodes[i].update_taken_state(turn)
            for j in range (len(nodes[i].return_monomials())):
                nodes[i].return_monomials()[j].monomial_score_update(turn)
                if nodes[i].return_monomials()[j].return_score() >= 1024:
                    nodes[i].return_monomials()[j].update_complete()
def score_taking_rotations(rotation_0,rotation_1,rotation_2,rotation_3):
    if rotation_0 == -1:
        rotation_0 = 3
    elif rotation_1 == -1:
        rotation_1 = 3
    elif rotation_2 == -1:
        rotation_2 = 3
    elif rotation_3 == -1:
        rotation_3 = 3
    elif rotation_0 == 4:
        rotation_0 = 0
    elif rotation_1 == 4:
        rotation_1 = 0
    elif rotation_2 == 4:
        rotation_2 = 0
    elif rotation_3 == 4:
        rotation_3 = 0
    global monomial_objects
    global nodes
    quad_0_passed = False
    quad_1_passed = False
    quad_2_passed = False
    quad_3_passed = False
    highest_score = 0
    rotations_away = 0
    rotations_away_total = 0
    rotation_character = ''
    quad_character = ''
    monomial_index = 0
    for j in monomial_objects:
        for k in j.return_monomial():
            rotation_character = k[3]
            quad_character = k[0]
            if quad_character == '0' and quad_0_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_0))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                quad_0_passed = True
                rotations_away = 0
            elif quad_character == '1' and quad_1_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_1))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                quad_1_passed = True
                rotations_away = 0
            elif quad_character == '2' and quad_2_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_2))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                rotations_away = 0
                quad_2_passed = True
            elif quad_character == '3' and quad_3_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_3))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                quad_3_passed = True
                rotations_away = 0

        quad_0_passed = False
        quad_1_passed = False
        quad_2_passed = False
        quad_3_passed = False
        monomial_objects[monomial_index].monomial_score_rotation_update(rotations_away_total)
        if (monomial_objects[monomial_index].return_score() > highest_score):
            highest_score = monomial_objects[monomial_index].return_score()
        monomial_index +=1
        rotations_away = 0
        rotations_away_total = 0
    adding_scores()
    for i in range(36):
        for j in range(len(nodes[i].return_monomials())):
            nodes[i].return_monomials()[j].reset_passed()
    return highest_score


def adding_scores():
    global nodes
    score = 0
    for i in range(36):
        if nodes[i].return_state() == 2:
            for j in range (len(nodes[i].return_monomials())):
                score += nodes[i].return_monomials()[j].return_score()
        else:
            score = 0
        nodes[i].update_score(score)
        score = 0
def look_at_scores():
    global nodes
    highest_score = 0
    node_for_highest_score = 0
    node_list = [0] * 36
    for i in range(36):
        node_list[i] = nodes[i].return_score()
        if nodes[i].return_score() > highest_score:
            highest_score = nodes[i].return_score()
    return node_list

def score_taking_in_advance(variable_number,turn):
    global nodes
    global changed
    for i in range(36):
        if i == variable_number and nodes[i].return_state() == 2: 
            for j in range (len(nodes[i].return_monomials())):
                nodes[i].return_monomials()[j].monomial_score_update(turn)
            changed = True

def revert_score_taking_in_advance(variable_number,turn):
    global nodes
    for i in range(36):
        if i == variable_number:
            for j in range (len(nodes[i].return_monomials())):
                nodes[i].return_monomials()[j].monomial_score_reset()

def look_at_score_monomial():
    highest_monomial_score = 0
    list_with_highest_monomial_score = []
    global changed
    highest_score = 0
    variable_number = 0
    global monomial_objects
    global nodes
    for i in range(36):
        score_taking_in_advance(i, 1)
        for j in monomial_objects:
            if j.return_score() > highest_monomial_score and j.return_complete() == False:
                highest_monomial_score = j.return_score()
                list_with_highest_monomial_score = j.return_nodes()
        if changed == True:
            revert_score_taking_in_advance(i,2)
            changed = False
    for i in list_with_highest_monomial_score:
        if nodes[i].return_score() >= highest_score:
            highest_score = nodes[i].return_score()
            variable_number = i
    return variable_number,highest_monomial_score

def score_taking_rotations_in_advance(rotation_0,rotation_1,rotation_2,rotation_3):
    if rotation_0 == -1:
        rotation_0 = 3
    elif rotation_1 == -1:
        rotation_1 = 3
    elif rotation_2 == -1:
        rotation_2 = 3
    elif rotation_3 == -1:
        rotation_3 = 3
    elif rotation_0 == 4:
        rotation_0 = 0
    elif rotation_1 == 4:
        rotation_1 = 0
    elif rotation_2 == 4:
        rotation_2 = 0
    elif rotation_3 == 4:
        rotation_3 = 0
    global changed
    global monomial_objects
    global nodes
    quad_0_passed = False
    quad_1_passed = False
    quad_2_passed = False
    quad_3_passed = False
    highest_score = 0
    rotations_away = 0
    rotations_away_total = 0
    rotation_character = ''
    quad_character = ''
    monomial_index = 0
    for j in monomial_objects:
        for k in j.return_monomial():
            rotation_character = k[3]
            quad_character = k[0]
            if quad_character == '0' and quad_0_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_0))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                quad_0_passed = True
                rotations_away = 0
            elif quad_character == '1' and quad_1_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_1))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                quad_1_passed = True
                rotations_away = 0
            elif quad_character == '2' and quad_2_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_2))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                rotations_away = 0
                quad_2_passed = True
            elif quad_character == '3' and quad_3_passed == False:
                rotations_away = abs(int(rotation_character) - int(rotation_3))
                if rotations_away == 3:
                    rotations_away = 1
                rotations_away_total += rotations_away
                quad_3_passed = True
                rotations_away = 0
                
        quad_0_passed = False
        quad_1_passed = False
        quad_2_passed = False
        quad_3_passed = False
        monomial_objects[monomial_index].monomial_score_rotation_update(rotations_away_total)
        monomial_index +=1
        rotations_away = 0
        rotations_away_total = 0

################################
    monomial_index = 0
    for i in range(36):
        score_taking_in_advance(i,1)
        for j in monomial_objects:
            if (monomial_objects[monomial_index].return_score() > highest_score):
                highest_score = monomial_objects[monomial_index].return_score()
            monomial_index +=1
        if changed == True:
            revert_score_taking_in_advance(i,2)
            changed = False
        monomial_index = 0
    for i in range(36):
        for j in range(len(nodes[i].return_monomials())):
            nodes[i].return_monomials()[j].reset_passed()
    return highest_score

def connect_nodes_with_monomials():
    global nodes
    global monomial_objects
    iterator = 0
    for i in range(36):        
        for j in range (len(nodes[i].return_monomials())):
            iterator = 0
            for k in range(len(monomial_objects)):
                if monomial_objects[k].return_monomial() == nodes[i].return_monomials()[j].return_monomial():
                    monomial_objects[k].add_node(i)
            

def reset_board():
    global nodes
    global monomial_objects
    for i in range(36):
        nodes[i].reset()
    for i in range(len(monomial_objects)):
        monomial_objects[i].reset()


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
connect_nodes_with_monomials()
#score_taking(0,0)
#score_taking_rotations(0,0,0,0)
#for i in range(36):
    #pprint(nodes_1[i].return_string())
    #pprint(str(i) + " " + nodes[i].return_string())
#connect_to_monomials()


##################################################################################
##########                                                              ##########
##########                      Printing the monomials                  ##########
##########                                                              ##########
##################################################################################
#score_taking(0,1)
#for i in range(36):
    #print(str(i))
    #for j in range(len(nodes[i].return_monomials())):
        #pprint(nodes[i].return_monomials()[j].return_monomial())
        #pprint(nodes[i].return_monomials()[j].return_score())
