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

    #Game start
    board1 = Board()
    currentPlayer, nextPlayer = playerO, playerX

    while board1.isWinner() != True and board1.isDraw != True:
        board1.getBoard()
        move = currentPlayer.makeMove()

        while board1.isValidMove(move) != True:
            move = currentPlayer.makeMove()

        board1.updateBoard(currentPlayer.getSymbol(), move)
        nextPlayer, currentPlayer = currentPlayer, nextPlayer

    board1.getBoard()
    if board1.isWinner():
        print(f"Congratulations, {nextPlayer.getName()}, you won!")
    else:
        print("This is a draw!")

main()
