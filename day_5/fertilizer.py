def convert_number(number, conversion_map):
    for dest_start, src_start, length in conversion_map:
        if number >= src_start and number < src_start + length:
            return dest_start + (number - src_start)
    return number

def find_lowest_location(seed_numbers, conversion_maps):
    current_numbers = seed_numbers.copy()

    for conversion_map in conversion_maps:
        new_numbers = []
        for number in current_numbers:
            new_number = convert_number(number, conversion_map)
            new_numbers.append(new_number)
        current_numbers = new_numbers

    return min(current_numbers)

def read_conversion_maps(file):
    with open(file, 'r') as f:
        lines = f.readlines()[1:]  # Exclude the first line

    maps = []
    current_map = []

    for line in lines:
        line = line.strip()
        if line:
            if line.endswith("map:"):
                if current_map:
                    maps.append(current_map)
                current_map = []
            else:
                current_map.append(tuple(map(int, line.split())))

    if current_map:
        maps.append(current_map)

    return maps

if __name__ == "__main__":
    input_file = "puzzle_input.txt"

    with open(input_file, 'r') as f:
        input_data = f.read()

    input_lines = input_data.split('\n')

    seed_numbers = list(map(int, input_lines[0].split()[1:]))
    conversion_maps = read_conversion_maps(input_file)

    lowest_location = find_lowest_location(seed_numbers, conversion_maps)
    print(f"The lowest location number is: {lowest_location}")