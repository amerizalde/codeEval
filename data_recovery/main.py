
def fix(this, maxv):
    """ fill in the missing numbers of a unordered sequence """
    a = map(int, this[1].split())
    minv = min(a)
    a.append([i for i in xrange(minv, maxv) if i not in a][0])
    return a

def parse(line):
    a = line.split(";")
    b = fix(a, len(a[0]))
    c = a[0].split()
    d = zip(b, c)
    d.sort(key=lambda k: k[0])
    return " ".join([i[1] for i in d])


def main(filename):
    with open(filename) as txt:
        for line in txt:
            print parse(line)

if __name__ == "__main__":
    test_one = "2000 and was not However, implemented 1998 it until;9 8 3 4 1 5 7 2"
    test_two = "programming first The language;3 2 1"
    test_three = "programs Manchester The written ran Mark 1952 1 in Autocode from;6 2 1 7 5 3 11 4 8 9"

    try:
        print parse(test_one)
        print parse(test_two)
        print parse(test_three)
    except Exception, e:
        print e
