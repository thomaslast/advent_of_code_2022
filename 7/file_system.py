from collections import defaultdict
from pathlib import Path

results_dict = defaultdict(int)
current_dir = Path("/")
with open("input") as file:
    for line in file:
        line = line.strip("\n")
        if line[0] == "$":
            if "cd" == line.split(" ")[1]:
                if ".." == line.split(" ")[2]:
                    results_dict[current_dir.parent] += results_dict[current_dir]
                    current_dir = current_dir.parent
                else:
                    current_dir = current_dir / line.split(" ")[2]
            elif "ls" == line.split(" ")[1]:
                pass
        elif line[0:3] == "dir":
            pass
        else:
            results_dict[current_dir] += int(line.split(" ")[0])
    while current_dir != Path("/"):
        results_dict[current_dir.parent] += results_dict[current_dir]
        current_dir = current_dir.parent


total_filesystem = 70000000
unused_space_required = 30000000

space_free = total_filesystem - results_dict[Path("/")]
space_to_clear = unused_space_required - space_free

best_candidate = 70000000

for dir, size in results_dict.items():
    if size > space_to_clear and size < best_candidate:
        best_candidate = size

print(best_candidate)
