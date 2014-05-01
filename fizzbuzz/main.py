import debug_print
import random
from sys import argv


# generate a test file
def lorem():
    txt = []
    for i in xrange(20):
        # generate 3 numbers
        # the first two being the "Fizz" and "Buzz"
        # the third being the nubmer to count to
        txt.append("{} {} {}".format(
            random.randint(1, 20),
            random.randint(1, 20),
            random.randint(21, 100)))
    with open("test_input.txt", 'w') as target:
        for line in txt:
            target.write(line + "\n")
        target.close()


def play(line):
    """ print out the sequence 1 through line[2] 
        if seq_num is divisible by both line[0] and line[1] print "FB" instead
        if seq_num is divisible by line[0], print "F" instead
        if seq_num is divisible by line[1], print "B" instead
    """
    assert len(line) == 3, "Error, expected 3 elements in list, received {}".format(len(line))
    assert type(line) == list, "Error, parse() expected a list, received {}".format(type(line))
    output = []
    a, b, N = int(line[0]), int(line[1]), int(line[2])
    for i in xrange(1, N):
        if i % a == 0 and i % b == 0:
            output.append("FB")
        elif i % a == 0:
            output.append("F")
        elif i % b == 0:
            output.append("B")
        else:
            output.append(str(i))
    return " ".join(output)


def parse(text):
    """expecting a file object"""
    for line in text:
        this = play(line.split(" "))
        print this


if __name__ == "__main__":
    lorem()
    with open("test_input.txt") as fizzbuzz:
        parse(fizzbuzz)
