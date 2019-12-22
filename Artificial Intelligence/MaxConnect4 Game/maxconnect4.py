import time
import sys
from MaxConnect4Game import *
import os

def oneMoveGame(currentGame,depth):
    begin=time.time()
    if currentGame.pcount == 42:
        print ('GAME OVER')
        sys.exit(0)
    currentGame.aiPlay(int(depth))
    end=time.time()
    totaltime=end-begin
    print ('Game state after move:')
    currentGame.printboard()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    currentGame.printtofile()
    currentGame.gfile.close()
    print("Time taken by Computer, for this move is " +str(totaltime))

def interactiveGame(currentGame,n_chance,depth,inFile):
    if n_chance=="human-next":
        while currentGame.countI() != 42:
            print("Human; It's your Turn")
            humanMove = int(input("Enter the column number [1-7], to make your move: "))
            if not 0 < humanMove < 8:
                print("Invalid column number, enter the correct column number [1-7]")
                continue
            if not currentGame.playPiece(humanMove - 1):
                print("The selected column is full; enter the column number [1-7]")
                continue

            if os.path.exists("input.txt"):
                currentGame.gfile = open(inFile, 'r')
            else:
                game_state = "0000000\n0000000\n0000000\n0000000\n0000000\n0000000\n1"
                text_file = open("input.txt", "w")
                text_file.write(game_state)
                text_file.close()
            try:
                currentGame.gfile = open("human.txt", 'w')
                currentGame.printtofile()
                currentGame.printboard()
                currentGame.gfile.close()
                if (currentGame.countI() == 42):
                    break
                else:
                    print("Computer will strategize for " + str(depth) + " move(s) ahead")
                    if currentGame.currentTurn == 1:
                        currentGame.currentTurn = 2
                    elif currentGame.currentTurn == 2:
                        currentGame.currentTurn = 1
                    currentGame.aiPlay(int(depth))
                    currentGame.gfile = open("computer.txt", 'w')
                    print "Computer has made a move at column " + str(currentGame.ccolumn + 1)
                    currentGame.printtofile()
                    currentGame.printboard()
                    currentGame.countScore()
                    print 'Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score)
                    currentGame.gfile.close()
            except Exception,e:
                print(e)
    else:
        currentGame.aiPlay(int(depth))
        currentGame.gfile = open("computer.txt", 'w')
        print "Computer has made a move at column " + str(currentGame.ccolumn + 1)
        currentGame.printtofile()
        currentGame.gfile.close()
        currentGame.printboard()
        currentGame.countScore()
        print 'Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score)
        interactiveGame(currentGame, "human-next", depth, inFile)
    if currentGame.countI() == 42:
        print('GAME OVER')
    print('Game state after move:')
    currentGame.printboard()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    if currentGame.player1Score > currentGame.player2Score:
        print("Player 1 is the Winner")
    elif currentGame.player2Score > currentGame.player1Score:
        print("Player 2 is the winner")
    elif currentGame.player1Score == currentGame.player2Score:
        print("Game resulted in tie")



def main(argv):
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]
    depth=argv[4]
    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)
    if game_mode=='interactive':
        n_chance=argv[3]
        if not n_chance=='computer-next' and not n_chance=='human-next':
            print("Invalid player name for an interactive game")
            sys.exit(2)
    else:
        outFile=argv[3]
    currentGame = maxConnect4Game()
    try:
        currentGame.gfile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")
    file_lines = currentGame.gfile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gfile.close()
    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printboard()
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    if game_mode == 'interactive':
        if currentGame.currentTurn == 1:
            print("Human playing as" + str(currentGame.currentTurn))
            print("Computer playing as " + str('2'))
        else:
            print("Human playing as" + str(currentGame.currentTurn))
            print("Computer playing as " + str('2'))
        interactiveGame(currentGame,n_chance,depth,inFile)
    else:
        try:
            currentGame.gfile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame,depth)


if __name__ == '__main__':
    main(sys.argv)