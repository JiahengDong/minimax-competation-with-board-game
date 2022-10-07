from sre_parse import FLAGS
import numpy as np

class board:
    def __init__(self,n):
        self.n = n
        self._data = np.zeros((n, n), dtype=int)

    def add_actions(self, player, action, turn):
        order = action[0]
        if order == "PLACE":
            row = action[1]
            col = action[2]
            if player == "red":
                self._data[self.n-row-1][col] = 1
                if turn == 0:
                    self.first_row = self.n-row-1
                    self.first_col = col
            elif player == "blue":
                self._data[self.n-row-1][col] = 2
            self.detect_diamond(self, player, action)
        elif order == "STEAL" and turn == 1:
            self._data[self.first_row][self.first_col] = 0
            self._data[self.n - self.first_col -1][self.n - self.first_row - 1] = 2

       
        

    def show_action(self):
        print(self._data)

    def get_cell(self, coord):
        if 0<= coord[0] <self.n and 0<= coord[1] <self.n:
            return self._data[coord]
        return False

    def detect_diamond(self, player, action):
        
        if player == "red":
            player_value = 1
            op_player_value = 2
        else:
            player_value = 2
            op_player_value = 1

        row = self.n-action[1]-1 
        col = action[2]
        delete_position = set()
        
        adjacent_cells = [(row-1, col-1),(row-1, col), (row, col+1), (row+1, col+1), (row+1, col), (row, col-1)]
        capture_cell = [(row-1, col-2), (row-2, col-1), (row-1, col+1), (row+1, col+2), (row+2, col+1), (row+1, col-1)]

        for i in range(len(adjacent_cells)):
            #detect diamond which not adjacently
            if self.get_cell(self, adjacent_cells[i-1]) == op_player_value and self.get_cell(self, adjacent_cells[i]) == op_player_value:
                if self.get_cell(self, capture_cell[i]) == player_value:
                    delete_position.add(adjacent_cells[i-1])
                    delete_position.add(adjacent_cells[i])

            #detect adacent diamonds
            if self.get_cell(self, adjacent_cells[i-2]) == op_player_value and self.get_cell(self, adjacent_cells[i]) == op_player_value:
                if self.get_cell(self, adjacent_cells[i-1]) == player_value:
                    delete_position.add(adjacent_cells[i-2])
                    delete_position.add(adjacent_cells[i])   

        while delete_position != set():
            coord = delete_position.pop()
            self._data[coord] = 0