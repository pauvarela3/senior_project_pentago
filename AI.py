#AI Programming Script with backstage gameboard
### This Python Program contains what the AI is looking at and how it should act
### based on the parameters it is given, however this is the offensive AI.
### This program builds upon a board that acts as a scoring board, which is used
### to figure out where the AI should put their piece based on the state of the board.
### In the end, what it is trying to do is finishing up monomials.


from pprint import pprint
import monomials #import monomials so you have a list of all the monomials in the board
nodes = []#node array used to represent all 36 nodes in the board
monomial_objects = []#monomial array used to represent all 704 monomials in the board
changed = False #global variable used to see if you changed the values to look ahead or if you didn't

#BEING USED
#Monomial objects used to represent each monomial in the board
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
    #update the score of the monomial based on the taken status of nodes it's related to
    def monomial_score_update(self, taken):
        #CHANGE THE TAKEN TO 1 IF YOU WANT THE AI TO BE SECOND PLAYER
        if taken == 0:
            self.__score = self.__score*4
        #CHANGE THE TAKEN TO 0 IF YOU WANT THE AI TO BE SECOND PLAYER
        elif taken == 1:
            self.__score = self.__score*0
    #reset the monomial score for the looking in advance
    def monomial_score_reset(self):
        self.__score = int(self.__score/4)
    #Update the score of the monomials based on how many rotations away it is from completion
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
                self.__passing = 2
            elif rotations_away >= 2 and self.__passing == 0:
                self.__score = self.__score*1
        self.__passed = True
    #Add the nodes the monomial is related to
    def add_node(self, i):
        self.__nodes[self.__iterator] = i
        self.__iterator += 1
    #Update if the monomial is complete
    def update_complete(self):
        self.__complete = True
    #Reset passed so you can update with rotations again
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
    #Used to reset the board (the monomial's status)
    def reset(self):
        self.__score = 1
        self.__passed = False
        self.__passing = 0
        self.__complete = False

#BEING USED
#Node objects used to represent each space in the board
class node:
    __quad = 0
    __row = 0
    __col = 0
    __rotation = 0
    __string = ""
    __monomials = []
    __taken = 2
    __score = 0
    def __init__(self,quad = 0, col = 0, row = 0, rotations = 0, string = "", monomials = [], taken = 2, score = 0):
        self.__quad = quad
        self.__col = col
        self.__row = row
        self.__rotations = rotations
        self.__string = string
        self.__monomials = monomials
        self.__taken = taken
        self.__score = score
    #Connecting the monomials the node is related to
    def monomials_constructor(self,monomial):
        self.__monomials.append(monomial)
    #Updating if the node has been taken by the AI or by the player
    def update_taken_state(self,taken):
        self.__taken = taken
    #Updating score
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
    #Used to reset the board (The node's status)
    def reset(self):
        self.__score = 0
        self.__taken = 2

#BEING USED
#In here we define the backboard, basically defining the
#pentago board for the AI to recognize
def defining_backboard():
    global nodes
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
        #The node connects to 4 different positoins because of the different
        #rotations each quad can be at.
        positions = string[1] + string[2]
        for rotations in range(4):
            string = string[:-1] + str(rotations)
#################################################################################
#In here it's the first col of the first row
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
##################################################################################
#Define the node object and append it to the array nodes
        nodes.append(node(quad, col, row, rotation, string, monomials_1, taken))
        monomials_1 = []#here you reset the monomials_1 list to get the other node monomials

#All this is used to move along the board to make sure that all the nodes have their respective
#have their respectives spots on the board
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
        #Make sure that you stay within the 0-2 row and columns (This is to stay withing the
        #range of rows and columns based on the quad).
        if col >= 3:
            col_based_on_quad = col%3
        else:
            col_based_on_quad = col
        if row >= 3:
            row_based_on_quad = row%3
        else:
            row_based_on_quad = row
            
#BEING USED  
#This function constructs the list of monomials
def monomial_constructor(score):
    global monomial_objects
    passing = 0
    passed = False
    iterator = 0
    complete = False
    for i in monomials.empty_1:
        nodes = [0] * 5
        monomial_objects.append(monomial(i, nodes, score, passed, passing, iterator,complete))

#BEING USED
#This function updates the scores of the monomials based on the piece dropped (not rotations)
#and also updates the state of the node (wether the node is taken by the AI or by the player).
#This function also tells the AI if a monomial is complete so that it doesn't try to complete
#the monomial if it already is completed.
def score_taking(variable_number,turn):
    global nodes
    for i in range(36):
        if i == variable_number:
            nodes[i].update_taken_state(turn)
            for j in range (len(nodes[i].return_monomials())):
                nodes[i].return_monomials()[j].monomial_score_update(turn)
                if nodes[i].return_monomials()[j].return_score() >= 1024:
                    nodes[i].return_monomials()[j].update_complete()

#BEING USED
#This function updates the scores of the monomials based on the current
#rotations of the board. This function also calls the adding_scores function
#since this is the last step for the end of the turn. This function also returns
#the highest scoring monomial of that specified rotation, that way in the pentago
#game, the AI goes for the highest scoring rotation(quad rotates right/left, etc.)
#thus continuing to connect the monomial and trying to win the game.
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

#BEING USED
#This function updates the scores of the nodes based on the scores of the
#monomials in the current board. Basically, add all the scores of the monomials
#the node is related to, and that's the score of the node.
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

#NOT BEING USED
#This function looks at every node and sends a list of the highest scoring nodes
#based on the current board and how many connections to different monomials the
#node has.
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

#BEING USED
#This function affects the scores so that the AI sees one step in the future
def score_taking_in_advance(variable_number,turn):
    global nodes
    global changed
    if nodes[variable_number].return_state() == 2: 
        for j in range (len(nodes[variable_number].return_monomials())):
            nodes[variable_number].return_monomials()[j].monomial_score_update(turn)
        changed = True

#BEING USED
#This function reverts the scores that were affected by the AI looking up ahead
#one move
def revert_score_taking_in_advance(variable_number,turn):
    global nodes
    for j in range (len(nodes[variable_number].return_monomials())):
        nodes[variable_number].return_monomials()[j].monomial_score_reset()

#BEING USED
#This function looks at every monomial in the board and looks for the highest
#scoring one so it prioritizes finishing it up if there's no better monomial
#in the current rotation, it then picks the best spot it could put it based on
#the spots that specified monomial has in it. It uses the two functions above,
#to look ahead and see how the scores will be affected if a piece is put in
#a specified space. (Looks through all the current open spaces)
def look_at_score_monomial():
    highest_monomial_score = 0
    list_with_highest_monomial_score = []
    highest_score = 0
    variable_number = 0
    global monomial_objects
    global nodes
    global changed
    for i in range(36):
        score_taking_in_advance(i, 0)
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

#Experimental: NOT BEING USED
#This function looks ahead in rotations, it basically puts a piece in every:
#spot that is open and looks at how the score will be affected based on the rotation
#with a piece of the opponent already taken into account
#This is experimental because it makes it so that the AI doesn't rotate where it
#needs to finish a monomial because it thinks it already did it. Atleast, that's,
#what we predict
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
    monomial_index = 0
    for i in range(36):
        score_taking_in_advance(i,0)
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

#BEING USED
#This function is used to connect the nodes with monomials specifically
#monomials -> nodes that way the monomial can have a list of the nodes
#it's part of.
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

#BEING USED
#This function resets the board
def reset_board():
    global nodes
    global monomial_objects
    for i in range(36):
        nodes[i].reset()
    for i in range(len(monomial_objects)):
        monomial_objects[i].reset()



defining_backboard()
connect_nodes_with_monomials()

