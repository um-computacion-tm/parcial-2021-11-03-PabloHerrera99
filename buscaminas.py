import random

class Buscaminas():
    def __init__(self, rows, cols, bombs):
        self.flags = 0
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        self.show = [[' ' for x in range(rows)]for y in range(rows)]
        self.board = self.board_generator()

    
    def show_board(self):
            result = 'Inicial \n'
            for row in range(8):
                print(self.board[row])
            result += '\nCompleto \n'
            print('\n')
            for row in range(8):
                print(self.show[row])
    
    def question(self, movs):
        row = input('row')
        col = input ('col')
        if movs == 'flag':
            return 'flag' 
        if movs == 'uncover':
            return 'uncover'

    def play(self, mov, row, col):
        if mov == 'flag':
            if self.show[row][col] != 'F':
                self.show[row][col] = 'F'
                self.flags += 1
            else:
                self.show[row][col] = ' '
                self.flags -= 1

        if mov == 'uncover':
            self.uncover(row, col)
            self.lose()
            self. win()


    def lose(self):
        j=0
        for i in range(8): 
            for j in range(8):
                if self.board[i][j] == 'B' and self.show[i][j] == 'B':
                    j += 0
        if j > 0:
            return True 


    def win(self):
        self.wcont = self.bombs
        for i in range(8): 
            for j in range(8):
                if self.board[i][j] == 'B' and self.show[i][j] == 'F':
                   self.wcont -=1
        if self.wcont == self.flags:
            return True



    def uncover(self, row, col):
        self.show [row][col] = self.board[row][col]
        
    def board_generator(self):

        a = [[[0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]]]
        r = 0
        bm = 4

        for i in range(8):
            for j in range(8):
                r = random.randint(0,1)
                a[i][j] = r
                if a[i][j] == 0 and bm != 0:
                    a[i][j] = 100
                    bm -= 1
                else:
                    a[i][j] = 0

        for i in range(8):
            for j in range(8):
                if a[i][j] == 100:
                    if i-1 >= 0 and a[i-1][j] != 100:
                        a[i-1][j] += 1
                    if j-1 >= 0 and i-1 >= 0 and a[i-1][j-1] != 100:
                        a[i-1][j-1] += 1
                    if j+1 <= 3 and i-1 >= 0 and a[i-1][j+1] != 100:
                        a[i-1][j+1] += 1
                    if i+1 <= 3 and a[i+1][j] != 100:
                        a[i+1][j] += 1
                    if j-1 >= 0 and i+1 <= 3 and a[i+1][j-1] != 100:
                        a[i+1][j-1] += 1
                    if j+1 <= 3 and i+1 <= 3 and a[i+1][j+1] != 100:
                        a[i+1][j+1] += 1
                    if j-1 >= 0 and a[i][j-1] != 100:
                        a[i][j-1] += 1
                    if j+1 <= 3 and a[i][j+1] != 100:
                        a[i][j+1] += 1
        for i in range(8):
            for j in range(8):
                if a[i][j] == 100:
                    a[i][j] = 'B'
        return (a)

