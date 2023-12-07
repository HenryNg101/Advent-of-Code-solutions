input = open("input").readlines()

# Get ranking of each hand, the stronger the type, the higher rank
def hand_type(mp):
    occurences_cnt = mp.values()

    # Five of a kind
    if len(mp) == 1: return 1

    # Four of a kind
    if 4 in occurences_cnt: return 2

    # Full house
    if len(mp) == 2: return 3

    # Three of a kind and two pair rules
    if len(mp) == 3: return 4 if 3 in occurences_cnt else 5

    # One pair
    if len(mp) == 4: return 6

    # High card
    return 7

#Change wild card value, for part 2, to optimize the winning chance
def convert_joker_card(occurence_mp):
    if 'J' in occurence_mp and len(occurence_mp) > 1:
        j_count = occurence_mp.pop('J')
        max_key = max(occurence_mp.keys(), key=lambda x: occurence_mp[x])
        occurence_mp[max_key] += j_count

def custom_sort_key(hand, cards_order):
    converted = ''.join([chr(cards_order[char]) for char in hand[1]])
    return (hand[0], converted)

# Sort hands and calculate final result
def calculate_total_winnings(cards_hands, cards_orders):
    cards_hands.sort(key=lambda hand: custom_sort_key(hand, cards_orders), reverse=True)
    return sum([(i+1) * cards_hands[i][2] for i in range(len(cards_hands))])


#Card order rules for both parts
cards_order_a = {
    'A': 0, 'K': 1, 'Q': 2, 'J': 3, 'T': 4, '9': 5,
    '8': 6, '7': 7, '6': 8, '5': 9, '4': 10, '3': 11, '2': 12
}
cards_order_b = {
    'A': 0, 'K': 1, 'Q': 2, 'T': 3, '9': 4, '8': 5,
    '7': 6, '6': 7, '5': 8, '4': 9, '3': 10, '2': 11, 'J': 12
}

cards_hands_a, cards_hands_b = [], []
for line in input:
    hand, bid = line.split()
    bid = int(bid)

    # Count the occurences of cards in a hand
    hand_cards_occurence_mp = {char: hand.count(char) for char in hand}
    cards_hands_a.append((hand_type(hand_cards_occurence_mp), hand, bid))
    
    # Part 2, convert joker card, then add that in
    convert_joker_card(hand_cards_occurence_mp)
    cards_hands_b.append((hand_type(hand_cards_occurence_mp), hand, bid))

print(f'Part 1: {calculate_total_winnings(cards_hands_a, cards_order_a)}')
print(f'Part 2: {calculate_total_winnings(cards_hands_b, cards_order_b)}')