import random

class Tic_Tac_Toe():
    
    def __init__(self):
        self.matrix = [[' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' '], [' ', '|', ' ', '|', ' ']]


    def mat(self, position, value):
        """
            This method adds values in matrix.
        """ 
        position_list = [[0, 0], [0, 2], [0, 4], [1, 0], [1, 2], [1, 4], [2, 0], [2, 2], [2, 4]]
        k = 0
        self.matrix[position_list[position - 1][0]][position_list[position - 1][1]] = value
        for row in self.matrix:
            print(' '.join(str(x) for x in row))
            if k != 2:
                print('--+---+--')
                k += 1
            else:
                pass
            

    def game(self, parameter, pos):
        """
            This method identifies 'X' and 'O'.
        """
        if parameter % 2 == 0:
            self.mat(pos, 'X')
        else:
            self.mat(pos, 'O')


    def check_position(self, pos_list):
        """
            This method checks whether there is a value in the given position.
        """
        if len(pos_list) != len(set(pos_list)):
            pos_list.pop()
            return False
        else:
            return True
        

    def check_winner(self, value):
        """
            This method identifies the winner (if it exists).
        """
        return ((self.matrix[0][0] == self.matrix[0][2]) and (self.matrix[0][0] == self.matrix[0][4]) and (self.matrix[0][0] == value) or 
            (self.matrix[1][0] == self.matrix[1][2]) and (self.matrix[1][0] == self.matrix[1][4]) and (self.matrix[1][0] == value) or
            (self.matrix[2][0] == self.matrix[2][2]) and (self.matrix[2][0] == self.matrix[2][4]) and (self.matrix[2][0] == value) or
            (self.matrix[0][0] == self.matrix[1][0]) and (self.matrix[0][0] == self.matrix[2][0]) and (self.matrix[0][0] == value) or
            (self.matrix[0][2] == self.matrix[1][2]) and (self.matrix[0][2] == self.matrix[2][2]) and (self.matrix[0][2] == value) or
            (self.matrix[0][4] == self.matrix[1][4]) and (self.matrix[0][4] == self.matrix[2][4]) and (self.matrix[0][4] == value) or
            (self.matrix[0][0] == self.matrix[1][2]) and (self.matrix[0][0] == self.matrix[2][4]) and (self.matrix[0][0] == value) or
            (self.matrix[0][4] == self.matrix[1][2]) and (self.matrix[0][4] == self.matrix[2][0]) and (self.matrix[0][4] == value))
        

    def check_starter(self):
        """
            This method inputs players name.
        """
        players = []
        player1 = input('Enter a player 1 name: ')
        player2 = input('Enter a player 2 name: ')
        players.append(player1)
        players.append(player2)
        if random.choice(players) == player1:
            return player1, player2
        else:
            return player2, player1
    

def main():
    pos_list = []
    parameter = 0  
    tic_obj = Tic_Tac_Toe()
    player1, player2 = tic_obj.check_starter()
    print('Game will start with', player1)
    while parameter != 9:
        if parameter % 2 == 0:
            print('{} enter Your position:'.format(player1))
            while True:
                try:
                    pos = int(input())
                    if pos in range(1, 10):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Oops!!! That was no valid number. Try again...")
        else:
            print('{} enter Your position:'.format(player2))
            while True:
                try:
                    pos = int(input())
                    if pos in range(1, 10):
                        break
                    else:
                        raise ValueError
                except ValueError:
                    print("Oops!!! That was no valid number. Try again...")
        pos_list.append(pos)
        if tic_obj.check_position(pos_list):
            tic_obj.game(parameter, pos)  
            parameter += 1
        else:
            print('This position are busy. Please enter again!!!')
        if parameter >= 5:
            if tic_obj.check_winner('X'):
                print('Congratulations!!! Game won ', player1)
                break
            elif tic_obj.check_winner('O'):
                print('Congratulations!!! Game won ', player2)
                break
            elif parameter == 9:
                print('Game Over')
            else:
                pass

if __name__ == '__main__':
    main()