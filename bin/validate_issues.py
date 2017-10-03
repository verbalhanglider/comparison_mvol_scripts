from argparse import ArgumentParser
from os import _exit, scandir, listdir
from os.path import exists
import re

def _find_files(path):
    for n in scandir(path):
        if n.is_dir():
            yield from _find_files(n.path)
        match = re.compile(r"mvol[\\]\d{4}[\\]\d{4}[\\]\d{4}$").search(n.path)
        if match and n.is_dir():
            yield n.path

def main():
    arguments = ArgumentParser()
    arguments.add_argument("data_dir", type=str, action='store')
    parsed = arguments.parse_args()
    try:
        gen = _find_files(parsed.data_dir)
        for n_item in gen:
            path = n_item
            object_parts = listdir(path)
            jpeg = False
            alto = False
            tif = False
            dc = False
            for part in object_parts:
                if part == 'JPEG':
                    jpeg = True
                if part == 'ALTO':
                    alto = True
                if part == 'TIFF':
                    tif = True
                if 'dc.xml' in part:
                    dc = True
            if not jpeg & alto & tif & dc:
                if not exists("./data/invalids.txt"):
                    f = open("./data/invalids.txt", "w", encoding="utf-8")
                    f.write("{}\n".format(n_item))
                    f.close()
                else:
                    f = open("./data/invalids.txt", "a", encoding="utf-8")
                    f.write("{}\n".format(n_item))
                    f.close()
            else:
                if not exists("./data/valids.txt"):
                    f = open("./data/valids.txt", "w", encoding="utf-8")
                    f.write("{}\n".format(n_item))
                    f.close()
                else:
                    f = open("./data/valids.txt", "a", encoding="utf-8")
                    f.write("{}\n".format(n_item))
                    f.close()
        return 0
    except KeyboardInterrupt:
        return 131

if __name__ == "__main__":
    _exit(main())