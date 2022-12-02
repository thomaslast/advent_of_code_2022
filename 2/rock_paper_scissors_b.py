"""
A: Rock - 1 point
B: Paper - 2 Points
C: Scissors - 3 points

X - Lose
Y - Draw
Z - Win

Loss - 0 Points
Draw - 3 Points
Win - 6 points
"""

rules_dict = {
    "X": {
        "A": 3,
        "B": 1,
        "C": 2
    },
    "Y": {
        "A": 4,
        "B": 5,
        "C": 6
    },
    "Z": {
        "A": 8,
        "B": 9,
        "C": 7
    }
}
total_points = 0
with open("input", "r") as file:
    for line in file.readlines():
        line = line.strip("\n")
        opponent_selection, my_selection = line.split(" ")
        points = rules_dict[my_selection][opponent_selection]
        total_points += points

print(total_points)