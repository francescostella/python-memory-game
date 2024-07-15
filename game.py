import os
from boards import Board

class Game:
    def __init__(self):
        self.is_game_over = False
    
    def start(self, is_debug = False):
        self.board = Board()

        while not self.is_game_over:
            os.system("clear")
            
            if is_debug:
                print("Is game over: ", self.check_if_game_over(), "\n") # DEV
            
            print("               MEMORY GAME\n")
            
            self.board.draw(is_debug)
            
            # prompt the user asking for 2-cards pick
            first_choice = input("Choose first card:  ")
            second_choice = input("Choose second card:  ")
            
            try:
                first_card = self.board.items[int(first_choice[1]) - 1][first_choice[0].upper()]
                second_card = self.board.items[int(second_choice[1]) - 1][second_choice[0].upper()]
            except (IndexError, TypeError, ValueError):
                print("An invalid card position has been chosen.")
                self.pause()
            else:
                # 1. get cards from the board
                print(f"{first_choice.upper()}: {first_card}")
                print(f"{second_choice.upper()}: {second_card}")
                
                # 2. compare cards
                print("Are cards equal?  ", "Yes" if first_card == second_card else "No")
                
                # 3. IF eq => flip cards
                if first_card == second_card:
                    first_card.reveal()
                    second_card.reveal()
                
                # check on each move IF game is over
                # setting self.is_game_over = False
                # will exit the game loop
                self.is_game_over = self.check_if_game_over()

    def pause(self):
        input("Press <ENTER> to continue...")

    def check_if_game_over(self):
        self.is_game_over = True
        
        for row in self.board.items:
            for key, card in row.items():
                if not card.is_revealed:
                    self.is_game_over = False
            
        return self.is_game_over

game = Game()
game.start(is_debug = True)
