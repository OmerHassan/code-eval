import itertools

n = 12
lineFormat = ('{:4d}' * n + '\n') * n
tables = [(range(i, n * i + 1, i)) for i in range(1, n + 1)]

print(lineFormat.format(*itertools.chain.from_iterable(tables))[:-1])