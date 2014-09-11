__author__ = 'Kristin and Kalyani - K&K games'

print """
            |1|2|3|
            |4|5|6|
            |7|8|9| """



#Board_position_value = {1: 8, 2: 1, 3: 6, 4: 3, 5: 5, 6: 7, 7: 4, 8: 9, 9: 2}
Swap_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
player1_scorecard = []
player2_scorecard = []


def move():
    player_move = (Board_position_value[player_choice])
    return player_move

def player_score():
    player1_scorecard.append []



def play():
    player1 = raw_input("Enter the first player's name:")
    print ""'Thanks ' + player1
    player_choice = input('Please make your first move by telling us where on the board you want to be')
    move()

    player()

    #player()
    #print player_score
    #player2=raw_input("Enter the second player name: ")
    #player()
    #print player_score


#for value in Board_position_value.values():
    #print (value)
player()
play()

#TODO make a function to switch from one player to another