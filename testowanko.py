class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def display_deck(self):
        for card in self.cards:
            print(card)

    def compare_cards(self, card1, card2):
        if self.cards.index(card1) < self.cards.index(card2):
            print("Comparison result: the first card is smaller than the second")
        elif self.cards.index(card1) > self.cards.index(card2):
            print("Comparison result: the first card is larger than the second")
        else:
            print("Comparison result: both cards are the same")

    def sort_cards(self):
        self.cards.sort(key=lambda card: (card.rank, card.suit))

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, card):
        self.cards.remove(card)

    def move_card(self, card, new_deck):
        if card in self.cards:
            self.remove_card(card)
            new_deck.add_card(card)


# Tworzenie talii kart
deck = Deck()

# Wyświetlanie talii
print("*** DECK DISPLAY ***")
print('\x1b[38;2;255;0;0m' + f"-----------DECK DISPLAY-----------" + '\x1b[0m')
deck.display_deck()
print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

# Porównywanie kart
print('\x1b[38;2;255;0;0m' + f"-----------DECK COMPARE-----------" + '\x1b[0m')
card1 = deck.cards[0]
card2 = deck.cards[15]
deck.compare_cards(card1, card2)
print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

# Sortowanie kart
print('\x1b[38;2;255;0;0m' + f"------------DECK  SORT------------" + '\x1b[0m')
deck.sort_cards()
print("Sorted deck:")
deck.display_deck()
print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

# Dodawanie karty
print('\x1b[38;2;255;0;0m' + f"-------------DECK ADD-------------" + '\x1b[0m')
new_card = Card("Ace", "Spades")
deck.add_card(new_card)
print("Deck after adding a card:")
deck.display_deck()
print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

# Usuwanie karty
print('\x1b[38;2;255;0;0m' + f"-----------DECK  REMOVE-----------" + '\x1b[0m')
card_to_remove = deck.cards[5]
deck.remove_card(card_to_remove)
print("Deck after removing a card:")
deck.display_deck()
print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')

# Tworzenie drugiej talii kart
new_deck = Deck()

# Przenoszenie karty
print('\x1b[38;2;255;0;0m' + f"------------DECK  MOVE------------" + '\x1b[0m')
card_to_move = deck.cards[15]
deck.move_card(card_to_move, new_deck)
print("Deck after moving a card:")
deck.display_deck()
print("New deck:")
new_deck.display_deck()
print('\x1b[38;2;255;0;0m' + f"----------------------------------\n" + '\x1b[0m')