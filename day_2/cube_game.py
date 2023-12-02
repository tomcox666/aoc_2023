import re

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

def main(file_path):
    sum_of_ids = 0

    with open(file_path, "r") as file:
        for line in file:
            if check_colour_limits(line):
                game_ID = get_game_ID(line)
                sum_of_ids += game_ID
    
    print("Sum of ID's for part one: {}".format(sum_of_ids))

if __name__ == "__main__":
    infile_path = 'puzzle_input.txt'
    main(infile_path)
