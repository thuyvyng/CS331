'''
    Erich Kramer - April 2017
    Apache License
    If using this code please cite creator.

'''

# import OthelloBoard

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    #PYTHON: use obj.symbol instead
    def get_symbol(self):
        return self.symbol
    
    #parent get_move should not be called
    def get_move(self, board):
        raise NotImplementedError()



class HumanPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)

    def clone(self):
        return HumanPlayer(self.symbol)
        
#PYTHON: return tuple instead of change reference as in C++
    def get_move(self, board):
        col = int(input("Enter col:"))
        row = int(input("Enter row:"))
        return  (col, row)


class MinimaxPlayer(Player):
    def __init__(self, symbol):
        Player.__init__(self, symbol)
        if symbol == 'X':
            self.oppSym = 'O'
        else:
            self.oppSym = 'X'

    def get_move(self,board):
        valid_moves = board.actions(self.symbol)
        max = float('-inf')

        for cols, rows in valid_moves:
            temp_board = board.cloneOBoard()
            temp_board.play_move(cols, rows, self.symbol)

            utility_value = self.min_value(temp_board)
            if utility_value > max:
                max = utility_value
                best_col = cols
                best_row = rows

        if max == float('-inf'):
            print("where does this come from")
            return cols, rows
        return (best_col,best_row)

    def max_value(self,board):
        if (board.has_legal_moves_remaining('X') == False) and (board.has_legal_moves_remaining('0') == False):
            return board.count_score(self.symbol) - board.count_score(self.oppSym)

        v = float('-inf')
        possible_moves = board.actions(self.symbol)
        if len(possible_moves) == 0:
            utility_value = self.min_value(board)
            if utility_value > v:
                v = utility_value
        else:
            for col, row in possible_moves:
                temp_board = board.cloneOBoard()
                temp_board.play_move(col, row, self.symbol)
                utility_value = self.min_value(temp_board)
                if utility_value > v:
                    v = utility_value
        return v

        
    def min_value(self,board):
        if (board.has_legal_moves_remaining('X') == False) and (board.has_legal_moves_remaining('0') == False):
            return board.count_score(self.symbol) - board.count_score(self.oppSym) 
    
        v = float('inf')
        possible_moves = board.actions(self.oppSym)
        if len(possible_moves) == 0:
            utility_value = self.max_value(board)
            if utility_value < v:
                v = utility_value
        else:
            for col, row in possible_moves:
                temp_board = board.cloneOBoard()
                temp_board.play_move(col, row, self.oppSym)
                utility_value = self.max_value(temp_board)
                if utility_value < v:
                    v = utility_value
        return v





