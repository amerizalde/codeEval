
from sys import argv

def main(filename):
    with open(filename) as txt:
        for line in txt:
            print line.lower()


if __name__ == "__main__":
    _, filename = argv
    main(filename)
