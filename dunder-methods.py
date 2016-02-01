'''ojk
The following is a very simple example, but it demonstartes the power of implementing just two special methods, __getitem__ and __len__
'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._card = [Card(rank, suit) for suit in self.suits
                                       for rank in self.ranks]

    def __len__(self):
        '''
        The benefits of using bunder methods.
        
        1. You don't have to memorize arbitary method names for standard operations.
        2. It's easier to benefit from the rich Python standard libary and avoid reinventing the wheel, like the random.choice function.
        '''
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


# Notes: By leverage __len__ and __getitem__, we could treat the# deck like a python list, could do iteration and slicing. And choice, 
# reversed and sorted.
