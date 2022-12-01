def part1(x):
    return max(sum(map(int, i.splitlines())) for i in x)

def part2(x):
    return sum(sorted(sum(map(int, i.splitlines())) for i in x)[-3:])

with open('01.in') as f:
    s = f.read()
    x = s.split('\n\n')

    print(part1(x))
    print(part2(x))