def part1(x):
    return max(sum(i) for i in x)

def part2(x):
    return sum(sorted(sum(i) for i in x)[-3:])

with open('01.in') as f:
    s = f.read()
    x = [[*map(int, i.splitlines())] for i in s.split('\n\n')]

    print(part1(x))
    print(part2(x))