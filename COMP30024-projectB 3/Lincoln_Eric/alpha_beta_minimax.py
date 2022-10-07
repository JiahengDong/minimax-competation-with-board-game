
from json.encoder import INFINITY
import numpy as np
from Lincoln_Eric.board import board
from Lincoln_Eric.utility_function import utility
class alpha_beta_minimax:
    def __init__(self, player, state):
        self.n = len(state)
        self.best_state = state
        self.player = player
        self.depth = 0
        if player == "red":
            self.player_value = 1
            self.op_player = "blue"
            self.op_player_value = 2
        else:
            self.player_value = 2
            self.op_player = "red"
            self.op_player_value = 1
        
        board.__init__(board, self.n)
       
    def alpha_beta_decision(self, state):

        value = self.max_value(self, state, -INFINITY, INFINITY)
        
        return value

    def max_value(self, state, alpha, beta):
        self.depth+=1
        if self.depth >= 6:
            self.depth -= 1
            return utility(state, self.player, self.player_value, self.op_player_value)

        for s in self.actions(self, state, self.player):
           
            curr_value = self.min_value(self, s, alpha, beta)
            
            #when the alpha need to be updated -- the s in actions is recorded(because it have a greater value)
            #the action is recorded in the best_aciton(self.action record each state move)
            if(curr_value > alpha):
                alpha = curr_value
                self.best_state = s
                
            if alpha >= beta:
                self.depth -= 1
                return beta
        self.depth -= 1
        return alpha

#use to find the minimum value based on previous state
    def min_value(self, state, alpha, beta):
        self.depth+=1
        #might not need to check the cut-off state(if we think we need to do the decision based on opponent player's move)
        if self.depth >= 6:
            return utility(state, self.player, self.player_value, self.op_player_value)

        #print("min state", self.actions(self, state, self.op_player))
        for s in self.actions(self, state, self.op_player):
            beta = min(beta, self.max_value(self, s, alpha, beta))
            if beta <= alpha:
                self.depth -= 1
                
                return alpha
        
        self.depth -= 1
        return beta

    def actions(self, state, player):
        actions = []
        for row in range(self.n):
            for col in range(self.n):
                #only consider the move after the first movement
                if state[self.n - row - 1][col] == 0:
                    board._data =  np.copy(state)
                    action = ("PLACE", row, col)
                    board.add_actions(board, player, action, 2)
                    board.detect_diamond(board, player, action)
                    actions.append(board._data)
        return actions
   


def find_move(state_prev, state_curr, player, ):
    n = len(state_curr)
    if player == "red":
        player_value = 1
    else:
        player_value = 2
    state = state_curr - state_prev
    for row in range(len(state)):
        for col in range(len(state)):
            if state[row][col] == player_value:
                return ("PLACE", n - row -1, col)

    return "error: no moves"

def alpha_beta_main(player, game_board):

    state = np.copy(game_board._data)
    #initialize alpha_beta_minimax
    alpha_beta_minimax.__init__(alpha_beta_minimax, player, state)
    value = alpha_beta_minimax.alpha_beta_decision(alpha_beta_minimax, state)
    best_state = alpha_beta_minimax.best_state
    #print("alpha_beta_board", game_board._data)
    action = find_move(state, best_state, player)
    
    return action, state

