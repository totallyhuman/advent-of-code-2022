def part1(x):
    total = 0

    for i in x:
        o = 'ABC'.index(i[0])
        m = 'XYZ'.index(i[1])

        total += [3, 6, 0][(m - o) % 3] + (m + 1)
    
    return total

def part2(x):
    total = 0

    for i in x:
        o = 'ABC'.index(i[0])
        m = (o + 'YZX'.index(i[1])) % 3

        total += 'XYZ'.index(i[1]) * 3 + (m + 1)
    
    return total

with open('02.in') as f:
    s = f.read()
    x = [i.split() for i in s.splitlines()]

    print(part1(x))
    print(part2(x))