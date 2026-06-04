import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck:
  ranks = [str(n) for n in range(2, 11)] + list('JQKA')
  suits = 'spades diamonds clubs hearts'.split()
  def __init__(self):
    self._cards = [Card(rank, suit) for suit in self.suits
                                    for rank in self.ranks]
    def __len__(self):
      return len(self._cards)
    def __getitem__(self, position):
      return self._cards[position]

Python Data Model, Special Methods, and a Card Deck Example

This chapter explains how Python's Data Model works through special methods (also called dunder methods like __len__, __getitem__, __add__, etc.). These methods allow custom classes to behave like built-in Python objects.

1. FrenchDeck Example

A FrenchDeck class is created using:

namedtuple for representing cards (Card(rank, suit)).
__len__ to return the number of cards (52).
__getitem__ to access cards by index.

Because of these methods, the deck automatically supports:

len(deck)
Indexing (deck[0])
Slicing (deck[:3])
Iteration (for card in deck)
Reverse iteration (reversed(deck))
Membership testing (card in deck)
Random selection (random.choice(deck))
Sorting with a custom key function.


2. Benefits of Special Methods

Special methods allow custom objects to:

Behave like standard Python collections.
Work seamlessly with Python's built-in functions and libraries.
Avoid creating custom method names for common operations.


3. How Special Methods Work

Special methods are usually called by Python automatically:

len(obj) → obj.__len__()
for item in obj → obj.__iter__() or obj.__getitem__()
str(obj) → obj.__str__()
repr(obj) → obj.__repr__()

Developers generally implement these methods rather than calling them directly.

4. Vector Class Example

A simple 2D Vector class demonstrates operator overloading using:

__repr__ → readable object representation.
__abs__ → vector magnitude.
__bool__ → truth value.
__add__ → vector addition (v1 + v2).
__mul__ → scalar multiplication (v * 3).

Example:

v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2   # Vector(4, 5)

abs(Vector(3, 4))   # 5.0

Vector(3, 4) * 3   # Vector(9, 12)

5. __repr__ vs __str__
__repr__ is for developers/debugging and should be unambiguous.
__str__ is for end-user display.
If only one is implemented, Python developers usually prefer __repr__.
