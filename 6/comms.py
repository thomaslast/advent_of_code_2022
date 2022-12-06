with open("input") as file:
    full_comm_string = file.readline()

for x in range(0, len(full_comm_string)):
    if len(full_comm_string[x:x+14:1]) == len(set(full_comm_string[x:x+14:1])):
        print(f"point of start message is {x+14}")
        break