"""
A & X: Rock - 1 point
B & Y: Paper - 2 Points
C & Z: Scissors - 3 points

Loss - 0 Points
Draw - 3 Points
Win - 6 points
"""

rules_dict = {
    "A": {
        "X": 4,
        "Y": 8,
        "Z": 3
    },
    "B": {
        "X": 1,
        "Y": 5,
        "Z": 9
    },
    "C": {
        "X": 7,
        "Y": 2,
        "Z": 6
    }
}
total_points = 0
with open("input", "r") as file:
    for line in file.readlines():
        line = line.strip("\n")
        opponent_selection, my_selection = line.split(" ")
        points = rules_dict[opponent_selection][my_selection]
        total_points += points

print(total_points)