import random

txt = []

# multiples of 2, to 100
the_twos = [i for i in xrange(100) if i % 2 == 0]

# make the list
for i in xrange(100):
    txt.append((str(int(random.randint(10, 100))), str(random.choice(the_twos))))

# create a file from a list
with open("test_input.txt", 'w') as target:
        for line in txt:
            target.write(",".join(line) + "\n")
        target.close()
