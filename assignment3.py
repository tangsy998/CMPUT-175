# War Game 
# at line 317, there is a code，is commented，to let game pause until player press Enter

import random
class CircularQueue:
# Constructor, which creates a new empty queue:
    def __init__(self, capacity):
        if type(capacity) != int or capacity<=0:
            raise Exception ('Capacity Error')
        self.items = []
        self.capacity = capacity
        self.count=0
        self.head=0
        self.tail=0
        
# Adds a new item to the back of the queue, and returns nothing:
    def enqueue(self, item):
        if self.count== self.capacity:
            raise Exception('Error: Queue is full')
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.tail]=item
        self.count +=1
        self.tail=(self.tail +1) % self.capacity
        
# Removes and returns the front-most item in the queue.
# Returns nothing if the queue is empty.
    def dequeue(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        item= self.items[self.head]
        self.items[self.head]=None
        self.count -=1
        self.head=(self.head+1) % self.capacity
        return item
        
# Returns the front-most item in the queue, and DOES NOT change the queue.
    def peek(self):
        if self.count == 0:
            raise Exception('Error: Queue is empty')
        return self.items[self.head]
        
# Returns True if the queue is empty, and False otherwise:
    def isEmpty(self):
        return self.count == 0
        
# Returns True if the queue is full, and False otherwise:
    def isFull(self):
        return self.count == self.capacity
        
# Returns the number of items in the queue:
    def size(self):
        return self.count
        
# Returns the capacity of the queue:
    def capacity(self):
        return self.capacity

# Removes all items from the queue, and sets the size to 0
# clear() should not change the capacity
    def clear(self):
        self.items = []
        self.count=0
        self.head=0
        self.tail=0
        
# Returns a string representation of the queue:
    def __str__(self):
        str_exp = "]"
        i=self.head
        for j in range(self.count):
            str_exp += str(self.items[i]) + " "
            i=(i+1) % self.capacity
        return str_exp + "]"   
    
# # Returns a string representation of the object CircularQueue
    def __repr__(self):
        return str(self.items) + ' Head=' + str(self.head) + ' Tail='+str(self.tail) + ' ('+str(self.count)+'/'+str(self.capacity)+')'
# START WRITING YOUR PROGRAM HERE
def read_and_validate_cards():
    # TASK 1 Reading and Validating cards
    # Three Conditions
    # File Exists - raises Exception if it does not.
    # 1.Exactly 52 2.Not repeated 3.Correct Format Raises Exception if any of the 
    # above is not correct.
    # TODO
    file_name = input('Enter name of file to read > ')
    file = open(file_name,'r')
    file_data = file.read()
    card_list = file_data.splitlines()
    file.close()
    string_of_duplicates = ''
    string_of_wrong_card = ''
    suits=["D", "C", "H", "S"]
    ranks=["K","Q","J","A","2","3","4","5","6","7","8","9","0"]
    
    # check if the capacity of the card is 52 or not
    if len(card_list) != 52:
        raise Exception('Error:Number of cards in the file is','{0}.'.format(len(card_list)))
    
    # find duplicate cards 
    for index in range(len(card_list)):
        duplicate = False
        if card_list[index] != '':
            for index_later in range(index+1,len(card_list)):
                if card_list[index] == card_list[index_later]:
                    duplicate = True                                          # this card is duplicate
                    card_list[index_later] = ''                               # do not consider this card later
        
        if duplicate == True and string_of_duplicates == '':                  # for the format of the exception content
            string_of_duplicates += '{0}'.format(card_list[index])        
        elif duplicate == True:
            string_of_duplicates += ',{0}'.format(card_list[index])
    
    # check if there are duplicate cards
    if string_of_duplicates != '':
        raise Exception('Error:Duplicates found in the input file:',string_of_duplicates)
    
    
    # find wrong formate cards
    for card in card_list:
        if card[0] in ranks and card[1].upper() in suits:
            continue
        else:
            if string_of_wrong_card == '':
                string_of_wrong_card += card
            else:
                string_of_wrong_card += ','+card
    
    # chenck if there are wrong cards
    if string_of_wrong_card != '':
        raise Exception('Error:Following cards not formatted correctly:',string_of_wrong_card)
        
    return card_list

def distribute_cards(cards):
    # Task 2 Distributing cards
    # Creates Two circular Queues and return them
    # - cards is a list of valid cards that has been read from the file
    # TODO
    start = random.randint(1,2)                         # decide who get cards firstly 
    player1_cards = CircularQueue(52)                   # a queue object which represent palyer1's cards
    player2_cards = CircularQueue(52)                   # a queue object which represent palyer2's cards
    
    # distribute all cards 
    while len(cards) != 0:
        if start % 2 == 1:
            player1_cards.enqueue(cards.pop())
        else:
            player2_cards.enqueue(cards.pop())
        start += 1
    
    return player1_cards,player2_cards

def get_user_input():
    # Task 3 Asking user for input
    # prompt the user to enter the number of cards that would be facedown for war
    # will repeatedly ask the user to enter a valid value if any number other than 1 or 2 or 3
    # is entered
    # returns the number entered by the user
    # TODO
    valid = False
    valid_number = [1,2,3]
    while not valid: 
        number = int(input('Enter the number of cards down ?'))
        if number in valid_number:
            valid = True
            return number
        else:
            print('please Enter a valid number')
            
    
def compare_cards(card1,card2):
    # Task 4 Comparing Cards
    # compares card1 of player 1 with card2 of player2
    # if card1 has higher rank return 1
    # if card2 has higher rank return 2
    # if card1 is equal to card2 reurn 0
    # - card 1 is a string representing a card of player1
    # - card 2 is a string representing a card of player2
    # TODO
    rank_list = ["2","3","4","5","6","7","8","9","0","J","Q","K","A"]                   # a list of rank from small to big
    card1_index = rank_list.index(card1[0])
    card2_index = rank_list.index(card2[0])
    
    # use the positon of two cards in the rank list to deicde which is bigger
    if card1_index > card2_index:
        return 1
    elif card1_index < card2_index:
        return 2
    else:
        return 0
    
class onTable:
    # Task 5  Create a class to represent the table
    # an instance of this class represents the table
    def __init__(self):
        # self is the onTable object
        # TODO
        self.cards_list = [ ]
        self.faceUp_list = [ ]
    
    def place(self,player,card,hidden):
        # places the given card on the table
        # -self is the onTable object
        # -player is an object of type int. It is 1 for player1 or 2 for player 2
        # -card is an object of type str. It is the card being placed on the table
        # -hidden is an object of type bool. False when the card is faceup and True when facedown
        # TODO
        if player == 1:
            self.cards_list.insert(0,card)
            self.faceUp_list.insert(0,hidden)
        else:
            self.cards_list.append(card)
            self.faceUp_list.append(hidden)
            
    def cleanTable(self):
        # cleans the table by initializing the instance attributes
        # -self is the onTable object
        # TODO
        suffled_cards_list = [ ]                                    # a list store cards after shuffled
        random.shuffle(self.cards_list)                             # shuffle cards
        
        # store cards after shuffled
        for index in range(len(self.cards_list)):                   
            suffled_cards_list.append(self.cards_list[index])
            
        self.__init__()                                             # clear card lists
        return suffled_cards_list
   
    def __str__(self):
        # returns the representation of the cards on the table
        # -self is the onTable object
        # TODO
        output = '['
        for card_index in range(len(self.cards_list)):
            if card_index == (len(self.cards_list) // 2):
                output += '| '
            
            if self.faceUp_list[card_index] == False:
                output += self.cards_list[card_index] + ' '
            else:
                output += 'XX '
        return output + ']'


def main():
    # TODO - IMPLEMENT ALGORITHM HERE
    try:
        cards = read_and_validate_cards()
    except FileNotFoundError:
        print('Incorrect filename or file does not exist')
    except Exception as e:
        exception_content,exception_number = e.args 
        print(exception_content,exception_number) 
    
    else:
        player1_cards,player2_cards = distribute_cards(cards)
        number = get_user_input()
        mytable = onTable()                                                # object of onTable class 
        
        # each player put one card on the table 
        while player1_cards.size() != 0 and player2_cards.size() != 0:        
            card1 = player1_cards.dequeue()
            mytable.place(1,card1,False)
            card2 = player2_cards.dequeue()
            mytable.place(2,card2,False)
            result = compare_cards(card1,card2)
                       
        # show the picture on the table    
            print('_'*60,
                  mytable,
                  'player1 : {0}  player2 : {1}'.format(player1_cards.size(),player2_cards.size()), sep = '\n')
        
        # when war happen
            if result == 0:
                print('WAR STARTS!!!')
                
        # when both player have enough cards to join the war       
                if player1_cards.size() > number and player2_cards.size() > number:
                    for i in range(number):                                # both player put some cards (decide early) on the talbe 
                        card1 = player1_cards.dequeue()
                        mytable.place(1,card1,True)
                        card2 = player2_cards.dequeue()
                        mytable.place(2,card2,True)
        
        # when one of the player does not have enough cards         
                elif player1_cards.size()< number:
                    print('Player1 does not have enough cards!',
                          'Player2 takes all cards on table and player1 cards', 
                          '_'*60, sep = '\n')
                    while player1_cards.size() != 0:                       # since player1 dose not have enough card, just take all his cards direvtly and game over
                        player2_cards.enqueue(player1_cards.dequeue())
                    
                    reward = mytable.cleanTable()
                    while len(reward) != 0:                                # we still need take two cards on the table
                        player1_cards.enqueue(reward.pop())                    
                        
                elif player2_cards.size()< number:
                    print('Player2 does not have enough cards!',
                          'Player1 takes all cards on table and player1 cards', 
                          '_'*60, sep = '\n')  
                    while player2_cards.size() != 0:                       # since player2 dose not have enough card, just take all his cards direvtly and game over
                        player1_cards.enqueue(player2_cards.dequeue())
                    
                    reward = mytable.cleanTable()
                    while len(reward) != 0:                                # we still need to take two cards on the table
                        player2_cards.enqueue(reward.pop())                    
        
        # clean table after the war
            if result != 0:     
                reward = mytable.cleanTable()                              # reward is the list of cards, put by both player, 
            
        #  there is no war happen    
            if result == 1:
                while len(reward) != 0:                                    # since player1 won this turn, he get all the card on the talbe
                    player1_cards.enqueue(reward.pop())
                print('palyer1 takes all cards on table')                    
            if result == 2:
                while len(reward) != 0:                                    # since player2 won this turn, he get all the card on the talbe
                    player2_cards.enqueue(reward.pop())
                print('player2 takes all cards on table')                
                
         # pause = input()                                                # player press enter to continue the game
        
        
        # decide who is the winner
        if player1_cards.size() == 52:
            print('_'*60,
                  'player1 won',
                  'player1 : {0}  player2 : {1}'.format(player1_cards.size(),player2_cards.size()), sep = '\n')
        else:
            print('_'*60,
                  'player2 won',
                  'player1 : {0}  player2 : {1}'.format(player1_cards.size(),player2_cards.size()), sep = '\n')            

main()
    