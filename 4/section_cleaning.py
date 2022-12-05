count = 0
with open("input") as file:
    for line in file.readlines():
        line.strip("/n")
        elf_a_sections, elf_b_sections = line.split(",")
        elf_a_start, elf_a_stop = [int(x) for x in elf_a_sections.split("-")]
        elf_b_start, elf_b_stop = [int(x) for x in elf_b_sections.split("-")]
        elf_a_list = list(range(elf_a_start, elf_a_stop+1))
        elf_b_list = list(range(elf_b_start, elf_b_stop+1))
        if any(item in elf_a_list for item in elf_b_list) or any(item in elf_b_list for item in elf_a_list):
            count +=1

print(count)