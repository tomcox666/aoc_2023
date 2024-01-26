mat = []
with open("puzzle_input.txt","r") as f:
    for line in f:
        if line.count("#") == 0:
            for i in range(2):
                mat.append([char for char in line.replace("\n", "")])
        else:
            mat.append([char for char in line.replace("\n", "")])

    mat = [list(x) for x in zip(*mat)]

    matt = []

    for line in mat:
        if line.count("#") == 0:
            for i in range(2):
                matt.append(line)
        else:
            matt.append(line)
    
    mat = matt

    locs = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "#":
                locs.append((i, j))


    res = 0
    
    done = set()
    
    for a in locs:
        for b in locs:
            if (a, b) not in done and (b, a) not in done and a!=b:
                done.add((a, b))
                res += (max(a[0], b[0])-min(a[0],b[0]))+(max(a[1], b[1])-min(a[1], b[1]))
    
    print(res)