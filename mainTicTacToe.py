from Board import Board
from Game import Game
from Player import Player


def main():

    #Greeting and player creation
    playerO = Player(symbol = "O", name = "Player O")
    playerO.setName()
    print(f"Hello {playerO.getName()}, you will play first.")

    playerX = Player(symbol = "X", name = "Player X")
    playerX.setName()
    print(f"Hello {playerX.getName()}, you will play second.")

    #Initialize new board object and assign each player a position (current or next)
    board1 = Board()
    currentPlayer, nextPlayer = playerO, playerX

    #executes a new move as long as there is no winner or draw case
    while board1.isWinner() != True and board1.isDraw != True:
        board1.getBoard()
        move = currentPlayer.makeMove()

        #checks if move is valid. As long as it is not valid, ask for another move.
        while board1.isValidMove(move) != True:
            move = currentPlayer.makeMove()

        #update board by exchanging the number with the player sign and switch turns
        board1.updateBoard(currentPlayer.getSymbol(), move)
        nextPlayer, currentPlayer = currentPlayer, nextPlayer

    #if the game ends through a win or draw, the board is printed once more and the winner/ draw message is printed
    board1.getBoard()
    if board1.isWinner():
        print(f"Congratulations, {nextPlayer.getName()}, you won!")
    else:
        print("This is a draw!")

main()
