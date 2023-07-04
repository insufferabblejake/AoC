import os


def do_something(input_lines: list[str]) -> None:
    print(f"There are {input_lines.__len__()} lines")
    # do something with the lines


def main() -> None:
    fpath = os.getcwd() + "/input.txt"
    file = open(fpath, "r")
    with open(fpath, "r") as file:
        input_lines = [line.rstrip() for line in file.readlines()]
        do_something(input_lines)


if __name__ == '__main__':
    main()
