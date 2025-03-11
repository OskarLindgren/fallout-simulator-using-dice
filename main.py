from random import randint
import csv

## Defs

START = 100
RUNS = 100
OUTPUT_LOCATION = "Drive:/Wherever/you/want/output.csv"

def roll() -> int:
    return randint(1,6)

def roll_all(n_dice:int) -> list[int]:
    results = []
    for _ in range(n_dice):
        results.append(roll())
    return results

def wipe_dice(dice_left:int, results:list) -> int:
    return dice_left-results.count(6)

## Simulate

graphs = []
for run in range(RUNS):
    print(run, end="\r")
    graph = []
    dice_left = START
    while dice_left > 0:
        dice_left = wipe_dice(dice_left, roll_all(dice_left))
        graph.append(dice_left)
    graphs.append(graph)

## CSV

max_length = max(len(g) for g in graphs)
padded_graphs = [g + [None] * (max_length - len(g)) for g in graphs]
transposed = list(map(list, zip(*padded_graphs)))

with open(OUTPUT_LOCATION, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Roll #"] + [f"Run {i+1}" for i in range(len(graphs))])
    for i, row in enumerate(transposed, start=1):
        writer.writerow([i] + row)

print("Done!")
