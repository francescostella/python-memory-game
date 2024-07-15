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
        print(
f"""
    |   A   |   B   |   C   |   D   |
   1|  {self.items[0]['A'].render(is_debug)}  |  {self.items[0]['B'].render(is_debug)}  |  {self.items[0]['C'].render(is_debug)}  |  {self.items[0]['D'].render(is_debug)}  |
   2|  {self.items[1]['A'].render(is_debug)}  |  {self.items[1]['B'].render(is_debug)}  |  {self.items[1]['C'].render(is_debug)}  |  {self.items[1]['D'].render(is_debug)}  |
   3|  {self.items[2]['A'].render(is_debug)}  |  {self.items[2]['B'].render(is_debug)}  |  {self.items[2]['C'].render(is_debug)}  |  {self.items[2]['D'].render(is_debug)}  |
   4|  {self.items[3]['A'].render(is_debug)}  |  {self.items[3]['B'].render(is_debug)}  |  {self.items[3]['C'].render(is_debug)}  |  {self.items[3]['D'].render(is_debug)}  |
"""
    )
    