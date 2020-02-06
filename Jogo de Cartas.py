import random
card_deck = []

for i in range(10):
    next_element = random.randrange(2, 10, 1)
    print(next_element)
    if next_element in card_deck:
        card_deck.count(next_element)
        print(card_deck.count(next_element))
        if card_deck.count(next_element) >= 4:
            card_deck.remove(next_element)
            print(card_deck)
        else:
            card_deck.append(next_element)
            print(card_deck)
    else:
        card_deck.append(next_element)
        print(card_deck)

print(card_deck)

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 21 or more
hand = []

while sum(hand) <= 21:
    hand.append(card_deck.pop())
print(hand)

