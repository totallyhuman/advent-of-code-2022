def part1(x):
    for i in range(4, len(x) + 1):
        p = x[i - 4:i]

        if len({*p}) == 4:
            return i

def part2(x):
    for i in range(14, len(x) + 1):
        p = x[i - 14:i]

        if len({*p}) == 14:
            return i

with open('input/06.in') as f:
    s = f.read()
    x = s

    print(part1(x))
    print(part2(x))
