
from argparse import ArgumentParser
from os import _exit
from os.path import exists, join

def main():
    arguments = ArgumentParser(description="A tool to check if there's any issue missing")
    arguments.add_argument("missing_issues", action='store', type=str)
    parsed = arguments.parse_args()
    try:
        lines = []
        with open(parsed.missing_issues, "r", encoding="utf-8") as read_file:
            lines = [x.strip() for x in read_file.readlines()]
        lines = sorted(lines)
        for line in lines:
            f = open(".\data\sorted_mising_issues_two.txt", "a", encoding="utf-8")
            f.write("{}\n".format(line))
            f.close()
        return 0
    except KeyboardInterrupt:
        return 131

if __name__ == "__main__":
    _exit(main())