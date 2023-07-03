import os


# Input will be a list of integers as strings. Each element is either a
# num string  or a new line.
def get_elf_cache(lines: list[str]) -> list:
    curr_sum = 0
    elf_cache: list[int] = []
    for token in lines:
        if token != "\n":
            curr_sum += int(token.rstrip())
        else:
            elf_cache.append(curr_sum)
            curr_sum = 0
    return elf_cache


def main() -> None:
    fpath: str = os.getcwd() + "/input.txt"
    file = open(fpath, "r")
    elf_cache = get_elf_cache(file.readlines())

    # the solution for part1
    max_val, max_index = max((v, i) for i, v in enumerate(elf_cache))
    print(f"Elf {max_index} is carrying {max_val} calories")

    # part2
    elf_cache.sort(reverse=True)
    print(f"Calories carried by the top3 elfs is {sum(elf_cache[:3])}")


if __name__ == "__main__":
    main()
