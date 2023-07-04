import os


def do_something(lines: list[str]) -> None:
    print(f"There are {lines.__len__()} lines")
    # do something with the lines


def main() -> None:
    fpath = os.getcwd() + "/input.txt"
    file = open(fpath, "r")
    do_something(file.readlines())


if __name__ == '__main__':
    main()
