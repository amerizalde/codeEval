# import debug_print
import pprint, re
from sys import argv

""" Maximizing weight to cost ratio

    First, parsing the input file.

    Each line of file has 2 main variables:
        the package limit
        the available packages to choose from

    Each available choice has 3 variables:
        the identifier for this choice
        the weight of this choice
        the cost of this choice

    The objective is to choose the assortment of packages
    that costs the most, while remaining under the package limit.

    If two choices have the same cost, pick the one with the least
    weight.

    If the only choice available weighs more than the package limit
    then return what?
"""


class Item(object):
    rank = 0

    def __init__(self, index, weight, cost):
        self.index = int(index)
        self.weight = float(weight)
        self.cost = float(cost)
        self.rank()

    def rank(self):
        self.rank = self.cost / self.weight

def conversion(choices):
    convert = []
    for a in choices:
        a = a.split(",")
        x = re.findall(r"[0-9]+", a[0])
        y = re.findall(r"[0-9]*\.[0-9]*", a[1])
        z = re.findall(r"[0-9]+", a[2])

        convert.append(
            Item(
                int("".join(x)),
                float("".join(y)),
                int("".join(z))
                )
            )
    return convert


def cull_noise(choices):
    for item in choices:
        if item.weight > int(problem):
            choices.remove(item)


if __name__ == "__main__":
    _, filename = argv
    weight_limit = 0
    cost_counter = 0
    printout = {}
    with open(filename) as txt:
        for line in txt:
            problem = line.split(" ")
            pack_limit, choices = problem[0], problem[2:]
            printout[pack_limit] = {"choices": choices}
        txt.close()

    # the printout key is the weight limit
    # the value is the list of choices
    # after culling noise, rank items by weight to cost ratio
    for problem in printout:
        printout[problem]["choices"] = conversion(printout[problem]["choices"])
        cull_noise(printout[problem]["choices"])

    # save the best choice order for each problem
    for max_weight in printout:
        printout[max_weight]["choices"] = sorted(
            printout[max_weight]["choices"],
            key=lambda k: k.rank)

    # while weight_limit is less than problem
    # add item.weight to weight_limit
    # add item.cost to cost_counter
    for problem, order in printout.iteritems():
        weight_limit = 0
        item_number = 0
        quantity = 0

        choices = order["choices"]
        index = 0
        # pprint.pprint(choices)
        if choices != []:
            while weight_limit < int(problem):
                weight_limit += choices[index].weight
                cost_counter += choices[index].cost
                item_number = choices[index].index
                quantity += 1
                index += 1

        printout[problem]["solution"] = "{}, {}".format(item_number, quantity)

    for problem in printout:
        pprint.pprint(printout[problem]["solution"])
