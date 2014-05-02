import random

txt = []
a = random.randint(0, 9)
b = random.randint(0, 9)
c = random.randint(10, 999)

for i in xrange(100):
    txt.append((str(random.randint(10, 999)),
            str(random.randint(0, 4)),
            str(random.randint(0, 4))))

# create a file from a list
with open("test_input.txt", 'w') as target:
        for line in txt:
            target.write(",".join(line) + "\n")
        target.close()
