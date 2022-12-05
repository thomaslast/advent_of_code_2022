import string
import itertools


def prio(x):
    return ''.join([string.ascii_lowercase, string.ascii_uppercase]).index(x) + 1


with open("input", "r") as file:
    rucksacks = [line.strip() for line in file.readlines()]


common = [list(set(r[:len(r) // 2]).intersection(set(r[len(r) // 2:]))) for r in rucksacks]
print(sum(prio(c) for c in common))

##### part 2
unique_items = [set(r) for r in rucksacks]
badges = [set.intersection(*r) for r in zip(unique_items[::3], unique_items[1::3], unique_items[2::3])]
print(sum(prio(b) for b in badges))
