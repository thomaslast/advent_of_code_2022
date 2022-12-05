from collections import defaultdict

boxes_dict = defaultdict(list)

with open("input", "r") as boxes:
    for index, line in enumerate(boxes.readlines()):
        if index < 8:
            for column, position in enumerate(range(0, len(line), 4)):
                box = line[position:position+4].strip(" ").strip("\n")
                if box != "":
                    boxes_dict[column+1].insert(0, box)
        elif index > 9:
            _, amount_to_move, _, column_from, _, column_to = [x.strip("/n") for x in line.split(" ")]
            amount_to_move = int(amount_to_move)
            column_from = int(column_from)
            column_to = int(column_to)
            boxes_to_move = boxes_dict[column_from][len(boxes_dict[column_from])-amount_to_move:]
            boxes_dict[column_to].extend(boxes_to_move)
            boxes_dict[column_from] = boxes_dict[column_from][:-amount_to_move]
        else:
            pass

print([boxes_dict[column][-1] for column in range(1,10)])