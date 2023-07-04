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

    print("Priorities:", priorities)


def muck_in_rucksack(lines: list[str]) -> int:
    prio_sum = 0
    lines = [line.rstrip() for line in lines]
    for line in lines:
        size = len(line) // 2
        first: set[str] = set(line[:size])
        second: set[str] = set(line[size:])
        prio_sum += sum(priorities[elem] for elem in first.intersection(second))
    return prio_sum


def main() -> None:
    generate_priorities()
    fpath = os.getcwd() + "/input.txt"
    file = open(fpath, "r")
    print(f"Sum of prios is {muck_in_rucksack(file.readlines())}")


if __name__ == '__main__':
    main()
