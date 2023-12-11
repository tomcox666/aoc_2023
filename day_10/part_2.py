def parseInput(fileName):
    with open(fileName) as file:
        allSegments = [list(line.strip()) for line in file]

    start = findStart(allSegments)

    adjacentToStart = inferAdjacentForStart(start[0], start[1], allSegments)

    allSegments[start[1]][start[0]] = inferTypeFor(start, adjacentToStart)

    toCheck = adjacentToStart
    segments = set([start] + adjacentToStart)

    while len(toCheck) > 0:
        checkNext = toCheck.pop(0)

        adjacent = adjacentTo(checkNext[0], checkNext[1], allSegments)

        for segment in adjacent:
            if segment not in segments:
                segments.add(segment)
                toCheck.append(segment)

    return start, list(segments), allSegments


def inferTypeFor(segment, adjacentSegments):
    relativeSegments = tuple(sorted([(x-segment[0], y-segment[1]) for x, y in adjacentSegments]))

    typeMap = {
        ((0, -1), (0, 1)): '|',
        ((-1, 0), (1, 0)): '-',
        ((0, -1), (1, 0)): 'L',
        ((-1, 0), (0, -1)): 'J',
        ((-1, 0), (0, 1)): '7',
        ((0, 1), (1, 0)): 'F'
    }

    return typeMap[relativeSegments]


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
    if not 0 <= y < len(grid):
        return False

    if not 0 <= x < len(grid[y]):
        return False

    return True


def findStart(input):
    for y, row in enumerate(input):
        for x, tile in enumerate(row):
            if tile == 'S':
                return (x, y)


def countInteriorPoints(pipe, allSegments):
    pipeSegments = set(pipe)
    numSpacesInLoop = 0

    for y, row in enumerate(allSegments):
        insideLoop = False
        prevBend = None
        for x, tile in enumerate(row):
            isPipeSegment = (x, y) in pipeSegments

            if insideLoop:
                insideLoop = not isPipeSegment or not crossedLoop(tile, prevBend)
            else:
                insideLoop = isPipeSegment and crossedLoop(tile, prevBend)

            if isPipeSegment and isBend(tile):
                prevBend = tile

            if insideLoop and not isPipeSegment:
                numSpacesInLoop += 1

    return numSpacesInLoop


def isBend(tile):
    return tile in set(['L', 'J', '7', 'F'])


def crossedLoop(tile, prevBend):
    if tile == '|':
        return True

    if prevBend == 'L' and tile == '7':
        return True

    if prevBend == 'F' and tile == 'J':
        return True

    return False


start, pipe, allSegments = parseInput('puzzle_input.txt')

print(countInteriorPoints(pipe, allSegments))