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