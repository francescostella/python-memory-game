import os
from boards import Board

class Game:
    def __init__(self):
        self.is_game_over = False
        self.exit_game = False
    
    def start(self, is_debug = False):
        self.board = Board()
        
        first_card = None
        second_card = None

        while not self.is_game_over and not self.exit_game:
            os.system("clear")
            
            print("Enter EXIT to quit the game.\n")
            print("               MEMORY GAME\n")
            
            self.board.draw(is_debug)
            
            if first_card and second_card:
                first_label = first_choice.upper() if first_choice.upper() else "Card 1"
                second_label = second_choice.upper() if second_choice.upper() else "Card 2"
                
                print(f"{first_label}: {first_card}")
                print(f"{second_label}: {second_card}")
                
                if first_choice.upper() == second_choice.upper():
                    print("You need to pick two distinct cards.\n")
                else:
                    print("Are cards equal?  ", "Yes" if first_card == second_card else "No", "\n")
            
            if is_debug:
                print("DEBUG: Is game over: ", self.check_if_game_over(), "\n") # DEV

            # prompt the user asking for 2-cards pick
            first_choice = input("Choose first card:  ")
            
            if first_choice.upper() == "EXIT":
                self.exit_game = True
                print("Exiting the game...")
                break
            
            second_choice = input("Choose second card:  ")
            
            if second_choice.upper() == "EXIT":
                self.exit_game = True
                print("Exiting the game...")
                break
            
            try:
                # 1. get cards from the board
                first_card = self.board.items[int(first_choice[1]) - 1][first_choice[0].upper()]
                second_card = self.board.items[int(second_choice[1]) - 1][second_choice[0].upper()]
            except (IndexError, KeyError, TypeError, ValueError):
                print("An invalid card position has been chosen.")
                self.pause()
            else:
                # IF cards are eq then flip both cards
                if first_card == second_card and first_choice.upper() != second_choice.upper():
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

if __name__ == "__main__":
    Game().start(is_debug = True)
