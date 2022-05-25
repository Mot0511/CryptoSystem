def lines(file):
    rlines = []
    f = open(file, 'r')
    for i in f:
        rlines.append(i.strip())

    return rlines