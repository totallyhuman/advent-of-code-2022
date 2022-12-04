def part1(x):
    total = 0

    for i in x:
        p1 = {*range(i[0][0], i[0][1] + 1)}
        p2 = {*range(i[1][0], i[1][1] + 1)}

        if p1 & p2 in [p1, p2]:
            total += 1
    
    return total

def part2(x):
    total = 0

    for i in x:
        p1 = {*range(i[0][0], i[0][1] + 1)}
        p2 = {*range(i[1][0], i[1][1] + 1)}

        if p1 & p2:
            total += 1
    
    return total

with open('04.in') as f:
    s = f.read()
    x = [[[*map(int, j.split('-'))] for j in i.split(',')] for i in s.splitlines()]

    print(part1(x))
    print(part2(x))
