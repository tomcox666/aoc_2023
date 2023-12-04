def calculate_matches(winning_numbers, your_numbers):
    matches = 0
    for num in your_numbers:
        if num in winning_numbers:
            matches += 1
            winning_numbers.remove(num)
    return matches

def get_numbers_from_card(card):
    winning_numbers, your_numbers = (card.split(':', 1)[1].strip()).split('|')
    winning_numbers = list(map(int, winning_numbers.split()))
    your_numbers = list(map(int, your_numbers.split()))

    return winning_numbers, your_numbers


def calculate_total_points(cards):
    total_points = 0
    for card in cards:
        winning_numbers, your_numbers = get_numbers_from_card(card)
        points = calculate_matches(winning_numbers.copy(), your_numbers)
        total_points += 2 ** (points - 1) if points > 0 else 0
    return total_points

def calculate_total_cards(cards):
    games = [1 for _ in cards]
    for i, line in enumerate(cards):
        left, right = line.split(':')[1].split('|')
        left_list, right_list = [list(map(int, x.strip().split())) for x in (left, right)]
        for j in range(sum(1 for elem in right_list if elem in left_list)):
            if i + j + 1 < len(cards):
                games[i + j + 1] += games[i]
    
    return sum(games)

def main(file):
    with open(file, 'r') as f:
        scratchcards = [line.strip() for line in f.readlines()]

    total_points = calculate_total_points(scratchcards)
    total_cards = calculate_total_cards(scratchcards)

    print(f"Total points: {total_points}")
    print(f"Total cards: {total_cards}")

if __name__ == "__main__":
    file = "puzzle_input.txt"
    tst_file = "tst_puzzle_input.txt"
    main(file)
