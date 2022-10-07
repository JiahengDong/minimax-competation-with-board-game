
from queue import Queue

def num_of_pieces_diff(state, player_value, op_player_value):
    num_p = 0
    num_op = 0
    for row in range(len(state)):
        for col in range(len(state)):
            if state[row][col] == player_value:
                num_p += 1
            elif state[row][col] == op_player_value:
                num_op += 1
    
    return num_p-num_op

def coord_neighbours(coord, state):
    '''find neighbours of the current coordinate'''
    n = len(state)
    row = coord[0]
    col = coord[1]
    adjacent_cells = [(row-1, col-1), (row-1, col), (row, col+1), (row+1, col+1), (row+1, col), (row, col-1)]
    real_adjacent = []
    
    for cell in adjacent_cells:
        if 0 <= cell[0] < n and 0<= cell[1] < n:
            real_adjacent.append(cell)

    return real_adjacent

def find_con(start_coord, state, visited):
    #visited -- record all the cell has been visited
    player_value = state[start_coord]
    connection = set()
    queue = Queue(0)
    queue.put(start_coord)
    
    while not queue.empty():
        #print("queue start")
        curr_coord = queue.get()
        connection.add(curr_coord)
        for coord in coord_neighbours(curr_coord, state):
            
            if coord not in connection and state[coord] == player_value:
                visited.append(coord)
                queue.put(coord)
    
    return list(connection), visited

def find_con_win_direction_length(connection, player):
    row_index = []
    col_index = []
    for cell in connection:
        row_index.append(cell[0])
        col_index.append(cell[1])

    if player == "red":
        l = max(row_index) - min(row_index)
    elif player == "blue":
        l = max(col_index) - min(col_index)

   
    return l

def max_con_length(state, player, player_value, op_player_value):
    cons_len_p = [0]
    cons_len_op = [0]
    visited = []

    #loop through all cell on board
    for row in range(len(state)):
        for col in range(len(state)):
            if state[row][col] == player_value and (row, col) not in visited:
                visited.append((row,col))
                start_coord = (row,col)
                connection, visited = find_con(start_coord, state, visited)

                #we consider that 2 or more cells can make up a connection
                if len(connection) >= 2:
                    cons_len_p.append(find_con_win_direction_length(connection, player))
            
            if state[row][col] == op_player_value and (row, col) not in visited:
                visited.append((row,col))
                start_coord = (row,col)
                connection, visited = find_con(start_coord, state, visited)

                #we consider that 2 or more cells can make up a connection
                if len(connection) >= 2:
                    cons_len_op.append(find_con_win_direction_length(connection, player))
                
   
    return max(cons_len_p) - max(cons_len_op), len(cons_len_p) - len(cons_len_op)

def utility(state, player, player_value, op_player_value):
    max_lenth_diff, num_con_diff = max_con_length(state, player, player_value, op_player_value)
    score = 0.82*num_of_pieces_diff(state, player_value, op_player_value) +  0.56*max_lenth_diff + 0.2*num_con_diff
    return score



