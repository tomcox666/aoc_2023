import re
from functools import reduce
from operator import mul

def get_game_ID(line):

    id = re.search(r'Game (\d+):', line)
    return int(id.group(1))

def check_colour_limits(line):

    colour_limits = {'blue': 14, 'red': 12, 'green': 13}
    games = re.split(r';\s*', line)

    for game in games:
        colour_counts = {'blue': 0, 'red': 0, 'green': 0}
        cubes = re.split(r',\s*', game)
        for cube in cubes:
            match = re.search(r'(\d+)\s+(\w+)', cube)
            if match:
                count, colour = int(match.group(1)), match.group(2)
                colour_counts[colour] += count
                if colour_counts[colour] > colour_limits[colour]:
                    return False
    return True

def check_min_cubes(line):

    colour_counts = {'blue': 0, 'red': 0, 'green': 0}
    games = re.split(r';\s*', line)

    for game in games:
        cubes = re.split(r',\s*', game)
        for cube in cubes:
            match = re.search(r'(\d+)\s+(\w+)', cube)
            if match:
                count, colour = int(match.group(1)), match.group(2)
                if colour_counts[colour] < count:
                    colour_counts[colour] = count
                else:
                    pass
    return colour_counts

def main(file_path):
    sum_of_ids = 0
    total_sum = 0

    with open(file_path, "r") as file:
        for line in file:
            colour_counts = check_min_cubes(line)
            total_sum += reduce(mul, colour_counts.values())
            if check_colour_limits(line):
                game_ID = get_game_ID(line)
                sum_of_ids += game_ID
    
    print("Sum of ID's with valid number of cubes (part 1): {}".format(sum_of_ids))
    print(f"Total sum of minimum cubes (part 2): {total_sum}")

if __name__ == "__main__":
    infile_path = 'tst_puzzle_input.txt'
    main(infile_path)
