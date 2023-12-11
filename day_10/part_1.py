def parseInput(fileName):
    with open(fileName) as file:
        allSegments = [list(line.strip()) for line in file]

    start = findStart(allSegments)

    adjacentToStart = inferAdjacentForStart(start[0], start[1], allSegments)

    toCheck = adjacentToStart
    segments = set([start] + adjacentToStart)

    while len(toCheck) > 0:
        checkNext = toCheck.pop(0)

        adjacent = adjacentTo(checkNext[0], checkNext[1], allSegments)

        for segment in adjacent:
            if segment not in segments:
                segments.add(segment)
                toCheck.append(segment)

    return start, list(segments)


def inferAdjacentForStart(segmentX, segmentY, allSegments):
    north, south, east, west = ordinalsOf(segmentX, segmentY)
    toCheck = [
        (north[0], north[1], set(['|', '7', 'F'])),
        (south[0], south[1], set(['|', 'L', 'J'])),
        (east[0], east[1], set(['-', 'J', '7'])),
        (west[0], west[1], set(['-', 'L', 'F']))
    ]

    out = []

    for checkX, checkY, checkFor in toCheck:
        if not inBounds(checkX, checkY, allSegments):
            continue

        if allSegments[checkY][checkX] in checkFor:
            out.append((checkX, checkY))

    return out


def adjacentTo(x, y, allSegments):
    north, south, east, west = ordinalsOf(x, y)
    toCheck = {
        '|': [north, south],
        '-': [east, west],
        'L': [north, east],
        'J': [north, west],
        '7': [west, south],
        'F': [east, south]
    }

    return toCheck[allSegments[y][x]]


def ordinalsOf(x, y):
    return (x, y-1), (x, y+1), (x+1, y), (x-1, y)


def inBounds(x, y, grid):
    if not 0 < y < len(grid):
        return False

    if not 0 < x < len(grid[y]):
        return False

    return True


def findStart(input):
    for y, row in enumerate(input):
        for x, tile in enumerate(row):
            if tile == 'S':
                return (x, y)


start, pipe = parseInput('puzzle_input.txt')

print(int(len(pipe) / 2))