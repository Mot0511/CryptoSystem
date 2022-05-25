rlines = []
def lines(file):
    f = open(file, 'r')
    for i in f:
        rlines.append(i.strip())

    return rlines