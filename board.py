class Board:

    def __init__(self):
        self.board = [[' ' for k in range(3)] for i in range(3)]

    def __str__(self):
        print_board = ''
        for i in range(3):
            print_board += ' -----------\n'
            for k in range(3):
                if k < 2:
                    print_board += '| ' + str(self.board[i][k]) + ' '
                else:
                    print_board += '| ' + str(self.board[i][k]) + ' |'
            print_board += '\n'
        print_board += ' -----------'
        return print_board
