def calculate_points(winning_numbers, your_numbers):
    points = 0
    for num in your_numbers:
        if num in winning_numbers:
            points += 1
            winning_numbers.remove(num)
    return points

def calculate_total_points(cards):
    total_points = 0
    for card in cards:
        winning_numbers, your_numbers = card.split('|')
        winning_numbers = list(map(int, winning_numbers.split()))
        your_numbers = list(map(int, your_numbers.split()))
        points = calculate_points(winning_numbers.copy(), your_numbers)
        total_points += 2 ** (points - 1) if points > 0 else 0
    return total_points

def main(file):
    with open(file, 'r') as f:
        scratchcards = [line.strip() for line in f.readlines()]

    total_points = calculate_total_points(scratchcards)
    print(f"Total points: {total_points}")

if __name__ == "__main__":
    file = "puzzle_input.txt"
    tst_file = "tst_puzzle_input.txt"
    main(tst_file)
