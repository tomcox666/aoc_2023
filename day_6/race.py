def get_input():
    with open('puzzle_input.txt', 'r') as f:
        input = [line.strip() for line in f.readlines()]
    return input

def a():
    wins = 1
    input = get_input()
    time = [int(t) for t in input[0].split()[1:]]
    distance = [int(d) for d in input[1].split()[1:]]
    for i in range(len(time)):
        for j in range(1, time[i]):
            if j * (time[i] - j) > distance[i]:
                wins *= time[i] - 2 * j + 1
                break

    return wins

def b():
    input = get_input()
    time = int(''.join(input[0].split()[1:]))
    distance = int(''.join(input[1].split()[1:]))
    for j in range(1, time):
        if j * (time - j) > distance:
            return time - 2 * j + 1

if __name__ == '__main__':
    print(a())
    print(b())