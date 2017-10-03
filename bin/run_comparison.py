
from argparse import ArgumentParser
from os import _exit
from os.path import exists, join

def main():
    arguments = ArgumentParser(description="A tool to check if there's any issue missing")
    arguments.add_argument("master_list", action='store', type=str)
    arguments.add_argument("data_dir", action='store', type=str)
    parsed = arguments.parse_args()
    try:
        lines = []
        with open(parsed.master_list, "r", encoding="utf-8") as read_file:
            lines = [x.strip() for x in read_file.readlines()]
        transtable = str.maketrans("-", "\\")
        for line in lines:
            new = line.translate(transtable)
            issue_path = join(parsed.data_dir, new)
            if not exists(issue_path):
               f = open(join("./data", "missing_issues_two.txt"), "a", encoding="utf-8")
               f.write("{}\n".format(issue_path))
               f.close()
        return 0
    except KeyboardInterrupt:
        return 131

if __name__ == "__main__":
    _exit(main())