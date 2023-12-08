import itertools
import pandas as pd

filename = "puzzle_input.txt"
with open(filename, "r") as file:
    instructions = [*file.readlines()[0].strip()]

df = pd.read_csv(filename, sep="[^A-Z]+", engine="python", index_col=0, 
    skiprows=2, usecols=[0, 1, 2], names=["P", "L", "R"], header=None)

pos = "AAA"
for i, inst in enumerate(itertools.cycle(instructions)):
    pos = df.loc[pos][inst]
    if pos == "ZZZ":
        break
print(i + 1)