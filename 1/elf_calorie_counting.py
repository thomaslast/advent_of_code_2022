current_calories = 0
all_totals = []
with open("input", "r") as file:
    for line in file.readlines():
        line = line.strip("\n")
        if line == "":
            all_totals.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
all_totals = sorted(all_totals)

print(sum(all_totals[-3:]))
