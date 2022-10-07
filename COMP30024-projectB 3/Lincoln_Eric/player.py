from Lincoln_Eric.board import board
from Lincoln_Eric.alpha_beta_minimax import *
class Player:
    color = ""
    board_size = 0
    def __init__(self, player, n):
        """
        Called once at the beginning of a game to initialise this player.
        Set up an internal representation of the game state.

        The parameter player is the string "red" if your player will
        play as Red, or the string "blue" if your player will play
        as Blue.
        """
        # put your code here
        self.color = player
        self.board_size = n
        print(self.color)
        print(self.board_size)
        board.__init__(board, n)
        self.n = 0

    def action(self):
        """
        Called at the beginning of your turn. Based on the current state
        of the game, select an action to play.
        """
        # put your code here
        # we find the differences of pieces has the highest utility score
        # so we make our agent, if we are blue, then the first step has to be "steal"
        # and as for red, in the first move, we make our agent to place in the mostly middle stage
        if self.color == "blue" and self.n == 1:
            action = ("STEAL",)
        elif self.color == "red" and self.n == 0:
            action = ("PLACE", 0, int(self.board_size/2)+1)
        else:
            action, board._data = alpha_beta_main(self.color, board)
            
        return action

    def turn(self, player, action):
        """
        Called at the end of each player's turn to inform this player of 
        their chosen action. Update your internal representation of the 
        game state based on this. The parameter action is the chosen 
        action itself. 
        
        Note: At the end of your player's turn, the action parameter is
        the same as what your player returned from the action method
        above. However, the referee has validated it at this point.
        """
        # put your code here
        #update the board of our player -- use to do the action desicions
        board.add_actions(board, player, action, self.n)
        self.n +=1
