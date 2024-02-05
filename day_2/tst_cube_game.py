import functools

def possible_games(data, max_red, max_green, max_blue):
    """
    Determines which games are possible given the maximum number of cubes of each color.

    Args:
        data (str): Puzzle input data from "puzzle_input.txt".
        max_red (int): Maximum number of red cubes.
        max_green (int): Maximum number of green cubes.
        max_blue (int): Maximum number of blue cubes.

    Returns:
        list: A list of IDs of games that are possible.
    """

    possible_game_ids = []
    for line in data.splitlines():
        game_id, samples = line.split(':')
        game_id = int(game_id.strip('Game '))

        valid_game = True
        for sample in samples.split(';'):
            cubes = dict([color, int(count)] for count, color in [x.split() for x in sample.split(',')])
            if cubes.get('red', 0) > max_red or cubes.get('green', 0) > max_green or cubes.get('blue', 0) > max_blue:
                valid_game = False
                break

        if valid_game:
            possible_game_ids.append(game_id)

    return possible_game_ids

def minimum_cubes_per_game(data):
    """
    Finds the minimum number of cubes of each color required for each game.

    Args:
        data (str): Puzzle input data from "puzzle_input.txt".

    Returns:
        list: A list of tuples, where each tuple contains (game_id, min_red, min_green, min_blue).
    """

    results = []
    for line in data.splitlines():
        game_id, samples = line.split(':')
        game_id = int(game_id.strip('Game '))

        min_red = max(cubes.get('red', 0) for sample in samples.split(';') for cubes in [dict([color, int(count)] for count, color in [x.split() for x in sample.split(',')])])
        min_green = max(cubes.get('green', 0) for sample in samples.split(';') for cubes in [dict([color, int(count)] for count, color in [x.split() for x in sample.split(',')])])
        min_blue = max(cubes.get('blue', 0) for sample in samples.split(';') for cubes in [dict([color, int(count)] for count, color in [x.split() for x in sample.split(',')])])

        results.append((game_id, min_red, min_green, min_blue))

    return results

def calculate_power(cubes):
    """
    Calculates the power of a set of cubes (product of red, green, and blue).
    """

    red, green, blue = cubes
    return red * green * blue

def possible_games_discard(data, max_red, max_green, max_blue):
    """
    Determines possible games with the discard logic and finds their power.

    Args:
        data (str): Puzzle input data from "puzzle_input.txt".
        max_red (int): Maximum number of red cubes.
        max_green (int): Maximum number of green cubes.
        max_blue (int): Maximum number of blue cubes.

    Returns:
        tuple: (list of possible game IDs, sum of powers, perfect game IDs)
    """

    possible_game_ids = []
    sum_of_powers = 0
    perfect_game_ids = []

    for line in data.splitlines():
        game_id, samples = line.split(':')
        game_id = int(game_id.strip('Game '))

        remaining_red = max_red
        remaining_green = max_green
        remaining_blue = max_blue

        valid_game = True
        for sample in samples.split(';'):
            cubes = dict([color, int(count)] for count, color in [x.split() for x in sample.split(',')])
            if cubes.get('red', 0) > remaining_red or cubes.get('green', 0) > remaining_green or cubes.get('blue', 0) > remaining_blue:
                valid_game = False
                break
            remaining_red -= cubes.get('red', 0)
            remaining_green -= cubes.get('green', 0)
            remaining_blue -= cubes.get('blue', 0)

        if valid_game:
            possible_game_ids.append(game_id)
            power = calculate_power((remaining_red, remaining_green, remaining_blue))
            sum_of_powers += power

            if remaining_red == 0 and remaining_green == 0 and remaining_blue == 0:
                perfect_game_ids.append(game_id)

    return possible_game_ids, sum_of_powers, perfect_game_ids 

def get_max_color_values():
    """Gets max red, green, and blue values from user input."""
    while True:
        try:
            max_red = int(input("Enter maximum number of red cubes: "))
            max_green = int(input("Enter maximum number of green cubes: "))
            max_blue = int(input("Enter maximum number of blue cubes: "))
            if max_red <= 0 or max_green <= 0 or max_blue <= 0:
                raise ValueError("Values must be positive integers.")
            return max_red, max_green, max_blue
        except ValueError:
            print("Invalid input. Please enter positive integers.")

if __name__ == "__main__":
    with open('tst_puzzle_input.txt', 'r') as f:
        data = f.read()

    max_red, max_green, max_blue = get_max_color_values()

    # --- Part 1 ---
    possible_games = possible_games(data, max_red, max_green, max_blue)
    sum_of_ids = sum(possible_games)
    print("Part 1:")
    print(" Possible game IDs:", possible_games)
    print(" Sum of possible game IDs:", sum_of_ids)

    # --- Part 2 ---
    min_cubes = minimum_cubes_per_game(data)
    sum_of_powers = functools.reduce(
        lambda acc, x: acc + calculate_power(x[1:]), min_cubes, 0
    )
    print("Part 2:")
    print(" Sum of powers:", sum_of_powers)

    # --- Part 3 ---
    possible_games_discard, sum_of_powers_discard, perfect_games = possible_games_discard(data, max_red, max_green, max_blue)
    print("Part 3:")
    print(" Possible game IDs (discard):", possible_games_discard)
    print(" Sum of powers (discard):", sum_of_powers_discard)
    print(" Perfect game IDs:", perfect_games)