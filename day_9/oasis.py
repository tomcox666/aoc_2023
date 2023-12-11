def process_data(data):
    return [[int(elem) for elem in line.strip().split(" ")] for line in data.strip().split("\n")]

def dfx_stack(vector, historic=False):
    stack = list([vector])
    while set(stack[-1]) != {0}:
        stack.append([stack[-1][elem + 1] - stack[-1][elem] for elem, content in enumerate(stack[-1][:-1])])
    ls = len(stack) - 1
    for x, content in enumerate(stack[1:]):
        stack[ls - x - 1].append(stack[ls - x][-1] + stack[ls - x - 1][-1])
        stack[ls - x - 1].insert(0, stack[ls - x - 1][0] - stack[ls - x][0])
    return stack[0][0] if historic else stack[0][-1]

def sum_of_extrapolates(data, historic=False):
    return sum(dfx_stack(line, historic) for line in data)

if __name__ == "__main__":
    with open("puzzle_input.txt", "r") as ifile:
        idata = ifile.read().strip()
    print("Sum of extrapolates, part 1: {}, part 2: {}".format(sum_of_extrapolates(process_data(idata)), sum_of_extrapolates(process_data(idata), historic=True)))