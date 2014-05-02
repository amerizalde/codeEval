import debug_print

from sys import argv

"""
Given numbers x and n, where n is a power of 2, print out the smallest multiple
of n that is greater than x
"""

def smallest_product(this):
    for i in xrange(len(this)):
        this[i] = int(this[i])
    x, n = this
    i = 2
    product = n
    if product <= x:
        while product <= x:
            product = n * i
            i += 1
        print "{} x {} == {} is greater than {}".format(i, n, product, x)
    else:
        print "{} is already greater than {}".format(product, x)


_, filename = argv

with open(filename) as txt:
    for line in txt:
        this = line.split(",")
        if len(this) == 2:
            smallest_product(this)

    txt.close()
