from board import Board


def game():
    board = Board()
    player = str(input("Do you want to be 'x' or '0'? "))
    while True:
        if player == 'x' or player == '0':
            break
        else:
            player = str(input("Try again! You can choose only 'x' or '0': "))
    if player == 'x':
        print("You make the first step.")
        player1 = player
      #  player2 = computer
    else:
        "Your opponent makes the first step."
     #  player1 = computer
        player2 = player

    print(board)


game()