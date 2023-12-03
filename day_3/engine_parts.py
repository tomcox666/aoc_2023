import numpy as np
import re

def is_valid_symbol(char):
    # Define valid symbols
    return char in ['*', '#', '+', '$']

def parse_engine_schematic(engine_schematic):
    rows = engine_schematic.strip().split('\n')
    engine_matrix = np.array([list(row) for row in rows])
    return engine_matrix

def calculate_part_number_sum(engine_matrix, file):
    part_number_sum = []
    with open(file, 'r')as f:
        lines = f.readlines()

        numbers = []
        for i in range(len(lines)):
            numbers.extend(map(lambda x: [i, x], re.finditer(r"[0-9]+", lines[i])))

        for number in numbers:
            i_box_min = number[0] - 1 if number[0] > 0 else number[0]
            i_box_max = number[0] + 2 if number[0] < engine_matrix.shape[0] else number[0] + 1
            j_box_min = number[1].start() - 1 if number[1].start() > 0 else number[1].start()
            j_box_max = number[1].end() + 1 if number[1].end() < engine_matrix.shape[1] else number[1].end()
            not_digit = np.vectorize(lambda x: not x.isdigit())(engine_matrix[i_box_min:i_box_max, j_box_min:j_box_max])
            not_dot = engine_matrix[i_box_min:i_box_max, j_box_min:j_box_max] != '.'
            if np.any(np.logical_and(not_dot, not_digit)):
                part_number_sum.append(float(number[1].group(0)))
    return sum(part_number_sum)

def main(file):
    with open(file, 'r') as f:
        engine_schematic = f.read()

    engine_matrix = parse_engine_schematic(engine_schematic)
    part_number_sum = calculate_part_number_sum(engine_matrix, file)

    print(f"Sum of part numbers: {part_number_sum}")

if __name__ == "__main__":
    file = "puzzle_input.txt"
    main(file)
