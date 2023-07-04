import os


priorities = {}


def generate_priorities() -> None:
    # Unicode code points for 'a' and 'z'
    lower_a = ord('a')
    lower_z = ord('z')
    for i in range(lower_a, lower_z + 1):
        char = chr(i)
        priority = i - lower_a + 1
        priorities[char] = priority

    # Unicode code points for 'A' and 'Z'
    upper_a = ord('A')
    upper_z = ord('Z')
    for i in range(upper_a, upper_z + 1):
        char = chr(i)
        priority = i - upper_a + 27
        priorities[char] = priority

    # print("Priorities:", priorities)


def part1_half_intersection(input_lines: list[str]) -> int:
    prio_sum = 0
    for line in input_lines:
        size = len(line) // 2
        first: set[str] = set(line[:size])
        second: set[str] = set(line[size:])
        prio_sum += sum(priorities[elem] for elem in first.intersection(second))
    return prio_sum


def part2_3intersection(input_lines: list[str]) -> int:
    prio_sum = 0
    csize = 3
    chunks_three = [input_lines[i:i + csize] for i in range(0, len(input_lines), csize)]
    """
    The other ways of incrementally finding intersections:
    i = first.intersection(second, third)
    i = set.intersection(*n_sets_in_a_list)
    """
    for chunk in chunks_three:
        first: set[str] = set(chunk[0])
        second: set[str] = set(chunk[1])
        third: set[str] = set(chunk[2])
        intersection = first & second & third
        prio_sum += sum(priorities[elem] for elem in intersection)
    return prio_sum


def main() -> None:
    generate_priorities()
    fpath = os.getcwd() + "/input.txt"
    with open(fpath, "r") as file:
        input_lines = [line.rstrip() for line in file.readlines()]
        print(f"Sum of half intersection prios is {part1_half_intersection(input_lines)}")
        print(f"Sum of 3 intersection is {part2_3intersection(input_lines)}")


if __name__ == '__main__':
    main()
