import random
from cards import Card

class Board:
    def __init__(self):
        self.words = [
            "cat", "dog", "fox", "cow", "owl", "bee", "pig", "ape"
        ]
        
        self.items = self.create_board()
    
    def create_board(self):
        # double the list
        list_words = self.words + self.words

        # shuffle 
        random_words = random.sample(list_words, 16)
        
        output = []
        row = {}
        
        # make board
        for index, word in enumerate(random_words):
            if index % 4 == 0 and index != 0:
                output.append(row)
                row = {}

            row[chr(65 + (index % 4))] = Card(word)
        
        output.append(row)
        
        return output
    
    def draw(self, is_debug = False):
        self.draw_grid()
        
        if is_debug:
            self.draw_grid(is_debug = True)
    
    def draw_grid(self, is_debug = False):
        counter = 1
        print("    |   A   |   B   |   C   |   D   |")
        for row in self.items:
            print_row = f"   {counter}|"
            for key, card in row.items():
                print_row += f"  {card.render(is_debug)}  |"
            print(f"{print_row}")
            counter += 1
        print("\n")
    