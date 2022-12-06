with open("input") as file:
    full_comm_string = file.readline()

for x in range(0, len(full_comm_string)):
    if len(set(full_comm_string[x:x+14:1])) == 14:
        print(f"point of start message is {x+14}")
        break