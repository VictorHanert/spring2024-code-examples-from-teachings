class Deck:
    def __init__(self, cards, label=''):
        self.cards = cards
        self.label = label

    def __repr__(self):
        return f'Deck({self.cards}, {self.label})'
    
    def __str__(self):
        return f'This is your deck: {self.cards}'
    
    def __add__(self, other):
        combined_cards = self.cards + other.cards
        combined_label = f'{self.label}_{other.label}'
        return Deck(combined_cards, combined_label)

    def __len__(self):
        return len(self.cards)
    
    def __getitem__(self, key):
        return self.cards[key]
    
    def __setitem__(self, key, value):
        self.cards[key] = value
    
    def __delitem__(self, key):
        del self.cards[key]
    
    def additem(self, item):
        self.cards.append(item)

# Creating instances of the Deck class
deck1 = Deck(['A', 'K', 7, 4], label='Deck1')
deck2 = Deck(['Q', 10, 9, 3], label='Deck2')
deck3 = Deck([], label='Deck3')

# Testing the methods
print(deck1)
print(deck2)
deck3 = deck1 + deck2
