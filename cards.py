class Card:
    def __init__(self, value):
        self.value = value
        self.is_revealed = False
        
    def __str__(self) -> str:
        return f"{self.value}"
    
    def __eq__(self, other: object) -> bool:
        return self.value == other.value
    
    def reveal(self):
        self.is_revealed = True
    
    def render(self, is_revealed = False):
        if self.is_revealed or is_revealed:
            return self.value
        else:
            return "   "
    
if __name__ == "__main__":
    card1 = Card("dog")
    card2 = Card("dog")
    card3 = Card("cat")
    
    print(f"{card1} == {card2}", card1 == card2)
    print(f"{card1} == {card3}", card1 == card3)