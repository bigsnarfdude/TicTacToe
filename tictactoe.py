#! /usr/bin/env python
'''
Tic Tac Toe Game Yo
'''

flag = 1
username_one = raw_input('What is your name of the first player? ')
username_two = raw_input('What is your name of the second player? ')
play = raw_input('Would you like to play a game %s and %s? ' % (username_one, username_two))

if play.lower() == "yes" or play.lower() == 'y':
    print "OK, let's play Tic Tac Toe"
    print "Select a position by entering your number"
else:
    print "Have a nice day %s and %s, Goodbye" % (username_one, username_two)

# need clear the screen
game_array = [ [1,2,3],
               [4,5,6],
               [7,8,9] ]

def player_decide_commit_answer(flag, answer, game_array):

    if flag == 1: 
        if int(answer) == 1:
            game_array[0][0]='x'
        elif int(answer) == 2:
            game_array[0][1]='x'
        elif int(answer) == 3:
            game_array[0][2]='x'
        elif int(answer) == 4:
            game_array[1][0]='x'
        elif int(answer) == 5:
            game_array[1][1]='x'
        elif int(answer) == 6:
            game_array[1][2]='x'
        elif int(answer) == 7:
            game_array[2][0]='x'
        elif int(answer) == 8:
            game_array[2][1]='x'
        elif int(answer) == 9:
            game_array[2][2]='x'
        else:
            print answer + " isn't there. Try again."
    
    elif flag == 2:
        if int(answer) == 1:
            game_array[0][0]="o"
        elif int(answer) == 2:
            game_array[0][1]="o"
        elif int(answer) == 3:
            game_array[0][2]="o"
        elif int(answer) == 4:
            game_array[1][0]="o"
        elif int(answer) == 5:
            game_array[1][1]="o"
        elif int(answer) == 6:
            game_array[1][2]="o"
        elif int(answer) == 7:
            game_array[2][0]="o"
        elif int(answer) == 8:
            game_array[2][1]="o"
        elif int(answer) == 9:
            game_array[2][2]="o"
        else:
            print answer + " isn't there. Try again."

def top():
    return '''
 _ _  _ _  _ _
| %s  | %s  | %s  |''' % (game_array[0][0], game_array[0][1], game_array[0][2])

def middle():
    return '''
 _ _  _ _  _ _
| %s  | %s  | %s  |'''% (game_array[1][0], game_array[1][1], game_array[1][2])

def bottom1():
    return '''
 _ _  _ _  _ _
| %s  | %s  | %s  |'''% (game_array[2][0], game_array[2][1], game_array[2][2])


bottom2 = '''
 _ _  _ _  _ _'''

def draw_board():
    print top(),
    print middle(),
    print bottom1(),
    print bottom2
    print
    print 

def toggle(flag):
    if flag == 1:
        return 2
    elif flag ==2:
        return 1



answer = ''
while answer.lower() != "quit":
    draw_board()
    answer = raw_input('Pick a number? ')
    player_decide_commit_answer(flag, answer, game_array)
    flag = toggle(flag)
