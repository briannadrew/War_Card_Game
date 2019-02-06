##############################################################################################################################################################################################################
#Program Name: War Card Game
#Author: Brianna Drew
#Date Created: October 7th, 2016
#Last Modified: February 4th, 2017
#Description: A program that imitates the classic card game, WAR, between two people (see instructions below for more details.
##############################################################################################################################################################################################################
import random, time, itertools, os, sys #import sub-programs that give ability to randomize, control time, control system (pausing, quitting), and to integrate items (2D array). 
player_hand = [] #empty array that will hold the cards in the player's hand.
computer_hand = [] #empty array that will hold the cards in the computer's hand.
inPlay = True #boolean variable that determines whether main program loop will run or not.
war = False #boolean variable that determines whether there is a war or not.

################################################## INTRO/INSTRUCTIONS/RULES ######################################################
print "Let's play a game of WAR!!!"
time.sleep(1) #1 second delay.
print " "
print "INSTRUCTIONS:"
print "Each player is dealt half of the cards in a full deck of cards. They are stacked face down and on the count of three, each player flips the card over."
time.sleep(6) #6 second delay.
print "The player with the higher card gets both players' cards. If the cards are equal, then WAR begins! (please note that suits do not matter whatsoever)."
time.sleep(6)
print "In the event of war, Each player draws the next first 3 cards in their deck, flipping only the last one. Whichever card is higher, that player will get all 8 cards."
time.sleep(6)
print "If a war keeps occurring following a war, the player who eventually has the higher card recieves ALL of the cards that were drawn that neither player had 'won' back yet."
time.sleep(6)
print "The game ends when one player ends up with at least 43 of the cards and the other is left with at most, none (Basically, when one of the players reaches less than 10 cards left). PLEASE NOTE: Aces are played low in this particular game."
time.sleep(6)
print "When you are ready, press any key to start the game..."
print " "
os.system("pause") #pauses system, user presses any key to begin game of war. #######((((((EXTRA FEATURE)))))#######

############################### SORTING OF CARDS INTO EACH DECK ########################################

deck = list(itertools.product(['Club', 'Spade', 'Heart', 'Diamond'],range(1,14))) #creates 2D list of cards, meaning 14 X 4 (52) items are created, 14 cards for each suit. (2D because each card is assigned number and suit).
random.shuffle(deck) #randomly shuffles items in deck list.

for x in range (26): #The first half of shuffled cards in deck list are added to player hand vlist and removed from deck list.
    player_hand.append(deck[x])
    deck.remove(deck[x])

computer_hand = deck #computer hand list is the 26 other cards that are remaining in the deck list.

########################## FUNCTION THAT SHOWS PLAYER THEIR HAND AND TELLS THEM HOW MANY CARDS THEY HAVE, AND HOW MANY CARDS THE OTHER PLAYER (COMPUTER) HAS EACH ROUND ########################

def count_down():
    print "YOUR HAND (Note that 1 is Ace, 11 is Jack, 12 is Queen, and 13 is King):"
    print " "
    print player_hand
    print " "
    print "# OF CARDS IN YOUR HAND:", len(player_hand)
    print "# OF CARDS IN THEIR HAND:", len(computer_hand)
    print " "
    time.sleep(.5) #half second delay

######################## FUNCTIONS THAT TAKE THE FIRST CARD FROM EACH PLAYER'S DECK AND DETERMINES IT TO BE THEIR MOVE EACH ROUND BY ###################
######################## REMOVING IT FROM THEIR HAND LIST AND MAKING IT THEIR CURRENT MOVE VARIABLE #####################################################

def com_move():
    compmove = computer_hand[0]
    computer_hand.remove(computer_hand[0])
    return compmove

def player_move():
    playermove = player_hand[0]
    player_hand.remove(player_hand[0])
    return playermove

##################### FUNCTION THAT COMPARES EACH PLAYER'S MOVE CARD WITH EACH OTHER TO DETERMINE WHICH IS HIGHER OR LOWER, OR IF IT'S A TIE (WAR!!!) #############################

def card_compare(computer_move,players_move,war):

    if int(computer_move[1]) > int(players_move[1]): #If the computer's move card (number) is higher than the player's...
        print " "
        print "Sorry! You lost that round!" #The computer wins, player loses.
        print " "
        computer_hand.append(computer_move) #Both move cards go into the computer's hand.
        computer_hand.append(players_move)
    
    elif int(computer_move[1]) < int(players_move[1]): #If the player's move card (number) is higher than the computer's...
        print " "
        print "Yay! You won that round!" #The player wins, computer loses.
        print " "
        player_hand.append(players_move) #Both move cards go into the player's hand.
        player_hand.append(computer_move)

    else: #If both move cards are equal...
        war_compare(computer_move,players_move) #Call function that declares war, and return both move variables.

########################################### FUNCTION THAT HANDLES CARDS WHEN THERE IS A WAR ##############################################

def war_compare(computer_move,players_move):
    player_war = [] #Lists that will hold each player's move cards during war (4 cards each)
    computer_war = []
    while True: #While main program is running...
        if len(computer_hand) < 4 or len(player_hand) < 4: #If either hand has less than 4 cards, a war cannot take place because either player cannot have a negative amount of cards.
            break #break loop, continues with regular card comparison.
            print 'Insufficient cards.' 
        for x in range (3): #removes first 3 cards from each player's hand and adds them to their respective war lists.
            computer_war.insert(0,computer_hand[x])
            computer_hand.remove(computer_hand[x])
            player_war.insert(0,player_hand[x])
            player_hand.remove(player_hand[x])
            
        print ' '
        print 'THIS MEANS WAR!!!'
        print ' '
        print 'COMPUTER:'
        print computer_war[2]
        print computer_war[1]
        print 'THEIR WAR MOVE:'
        print computer_war[0]
        print ' '
        print 'YOU:'
        print player_war[2]
        print player_war[1]
        print 'YOUR WAR MOVE:'
        print player_war[0]
        print ' '
        if computer_war[0][1] > player_war[0][1]: #if the FIRST card in the computer's war list is higher than that of the player's...
            print ' '
            print 'Sorry! You lost that round!'
            computer_hand.append(computer_move) #Add the 2 originals move cards AND the 6 war cards to the computer's hand.
            computer_hand.append(players_move)
            computer_hand.extend(computer_war)
            computer_hand.extend(player_war)
            break
        elif computer_war[0][1] < player_war[0][1]: #if the FIRST card in the player's war list is higher than that of the computer's...
            print ' '
            print 'Yay! You won that round!'
            player_hand.append(players_move) #Add the 2 originals move cards AND the 6 war cards to the player's hand.
            player_hand.append(computer_move)
            player_hand.extend(player_war)
            player_hand.extend(computer_war)
            break
        else: #If there is ANOTHER tie...
            print ' '
            print 'ANOTHER WAR!!!'

    inPlay = True

counter = 0 #Counter that will keep track of how many rounds take place.

#########################################################################################################
######################################### MAIN PROGRAM LOOP #############################################
#########################################################################################################

while True:

    counter+=1 #Number of turns increases by 1.
    print 'Turn: '+str(counter)
    if counter == 5: #Every 5 turns...
        random.shuffle(player_hand) #shuffle each hand again.
        random.shuffle(computer_hand)
    count_down() #calls function to show player their hand and to re-iterate how many cards are in each hand.

    if len(computer_hand) < 10 or len(player_hand) < 10: #If either hand reaches less than 10 cards... (game ends).
        print " "
        time.sleep(.5)
        print "GAME OVER!"
        if len(computer_hand) < 10: #If the computer's hand reached less than 10 cards...
            print " "
            time.sleep(1)
            print "YAY! YOU WON THE GAME!" #You won.
        elif len(player_hand) < 10: #If the player's hand reached less than 10 cards...
            print " "
            time.sleep(1)
            print "SORRY! YOU LOST THE GAME!" #You lost.
        time.sleep(1)
        print " "
        print "BYE! COME BACK AND PLAY AGAIN SOME TIME! :)"
        
        time.sleep(3) #3 second delay.
        sys.exit(0) #exit system.
        
##    counter+=1 #Number of turns increases by 1.
##    print 'Turn:'+str(counter)
##    if counter == 5: #Every 5 turns...
##        random.shuffle(player_hand) #shuffle each hand again.
##        random.shuffle(computer_hand)
##    count_down() #calls function to show player their hand and to re-iterate how many cards are in each hand.

    computer_move = com_move() #calls function to determine the computer's move.
    players_move = player_move() #calls function to determine the player's move.
    print "THEIR MOVE:" #prints each player's move.
    print computer_move
    print " "
    print "YOUR MOVE:"
    print players_move
    time.sleep(.5)

    card_compare(computer_move,players_move,False) #Calls card compare function to determine the winner of the round (war is set to False so it does not automatically declare war each round).
    
    computer_move = [] #Resets computer and player's move after each round.
    players_move = []
            
        








