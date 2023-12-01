def words_to_numbers(input_string):
    word_to_number = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e',
    }

    for word, number in word_to_number.items():
        input_string = input_string.replace(word, number)

    return input_string

def sum_of_first_and_last_digits(line):
    line = line.strip()
    digits = [int(char) for char in line if char.isdigit()]
    return int(str(digits[0]) + str(digits[-1]))

def main(file_path):
    calibration_sum_1, calibration_sum_2 = 0, 0

    with open(file_path, 'r') as file:
        for line in file:
            calibration_sum_1 += sum_of_first_and_last_digits(line)
            integer_line = words_to_numbers(line)
            calibration_sum_2 += sum_of_first_and_last_digits(integer_line)

    print(f"Solution to problem 1: {calibration_sum_1}")
    print(f"Solution to problem 2: {calibration_sum_2}")    

if __name__ == "__main__":
    infile_path = 'calibration_input.txt'
    main(infile_path)
