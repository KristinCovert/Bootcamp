__author__ = 'student'

print """ Welcome to Tic-Tac-Toe"""

#player1 = raw_input('Who is player 1? ')
#player2 = raw_input('Who is player 2? ')

display_board_top = '|1|2|3|'
display_board_middle = '|4|5|6|'
display_board_bottom = '|7|8|9|'

swap_board = {1: ('|', ' '), 2: ('|', ' '), 3: ('|', ' '), 4: ('|', ' '),
              5: ('|', ' '), 6: ('|', ' '), 7: ('|', ' '), 8: ('|', ' '), 9: ('|', ' ')}

print swap_board

for key in swap_board:
    print str(range(key=1, 3)) + display_board_top

active_board_top = [('|', '  '), ('|', '  '), ('|', '  ', '|')]
active_board_middle = [('|', ' '), ('|', ' '), ('|', ' ', '|')]
active_board_bottom = [('|', ' '), ('|', ' '), ('|', ' ', '|')]


print display_board_top + "\t\t\t" + str(active_board_top[0][0])*2 + str(active_board_top[2])



player1_scorecard = []
player2_scorecard = []

#Board_position_value = {1: 8, 2: 1, 3: 6, 4: 3, 5: 5, 6: 7, 7: 4, 8: 9, 9: 2}

player1_turn = input('Please tell us where you want to move ' + player1 + ': ')

Swap_board[player1_turn] = "x"

print Swap_board

print active_board_top
print active_board_middle
print active_board_bottom



player2_turn = input ('And, where would you like to move ' + player2 + ': ')

Swap_board[player2_turn] = "o"


print Swap_board