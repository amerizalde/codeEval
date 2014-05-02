from sys import argv

def main(filename):
    with open(filename) as txt:
        for line in txt:
            # create list
            output = line.split(" ")
            # reverse list
            output.reverse()
            # join and print
            print " ".join(output)

if __name__ == "__main__":
    _, filename = argv
    main(filename)