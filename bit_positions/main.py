
from sys import argv

""" Given a number n, and two integers p1, p2, determine if the bits at
    p1 and p2 are the same. print True or False. """

def cmp_bits(n, p1, p2):
    n = bin(n)  # convert to a binary string
    try:
        return True if n[p1] == n[p2] else False
    except Exception, e:
        return n, p1, p2, e

def main(filename):
    with open(filename) as txt:
        for line in txt:
            line = line.split(",")
            print cmp_bits(int(line[0]), int(line[1]), int(line[2]))

if __name__ == "__main__":
    _, filename = argv
    main(filename)
