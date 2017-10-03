
from argparse import ArgumentParser
from os import _exit, scandir
from os.path import exists, join

def count_files(path):
    for n in scandir(path):
        if n.is_file() and n.path.endswith(".pdf"):
            yield n.path
        elif n.is_dir():
            yield from count_files(n.path)

def main():
    arguments = ArgumentParser(description="A tool to check if there's any issue missing")
    arguments.add_argument("data_dir", action='store', type=str)
    parsed = arguments.parse_args()
    try:
        gen = count_files(parsed.data_dir)
        total = 0
        for n in gen:
            total += 1
        print("total issues currently in owncloud=%s" % str(total))
        return 0
    except KeyboardInterrupt:
        return 131

if __name__ == "__main__":
    _exit(main())