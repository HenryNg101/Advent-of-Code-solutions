input = open("input").readlines()
res_a = 0
winning_counts = [] #Count the amount of winning numbers for each card

for numbers_sets in input:
    # Filtering input
    # Divide 2 sets, then divide based on spaces
    winning_numbers, owned_numbers = [numbers_set.split(' ') for numbers_set in numbers_sets.split(' | ')]
    
    #Make it a set of winning numbers
    winning_numbers = {int(number) for number in winning_numbers if number.isnumeric()}
    owned_numbers = {int(number) for number in owned_numbers if len(number) > 0}

    #Count the amount of winning numbers you have in your set
    winning_cards_count = len(winning_numbers & owned_numbers)

    
    #Part 1 calculation
    res_a += 2 ** (winning_cards_count - 1) if winning_cards_count > 0 else 0

    #Part 2
    winning_counts.append(winning_cards_count)

#Part 2 calculations too
cards_sets_count = len(input)
copies_counts = []  #Count the amount of copies of each card, after no more scratchcards are won

for id in range(cards_sets_count):
    current_copies_count = 1 + sum(copies_counts[i] for i in range(id) if winning_counts[i] + i >= id)
    copies_counts.append(current_copies_count)


#Print final result
print(f"Part 1: {res_a}")
print(f"Part 2: {sum(copies_counts)}")