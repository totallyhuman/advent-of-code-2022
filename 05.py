def part1(x, y):
    x = [i.copy() for i in x]

    for c, f, t in y:
        for i in range(c):
            x[t - 1].append(x[f - 1].pop())
    
    return ''.join(i[-1] for i in x)

def part2(x, y):
    x = [i.copy() for i in x]

    for c, f, t in y:
        x[t - 1] += x[f - 1][-c:]
        del x[f - 1][-c:]
        
    return ''.join(i[-1] for i in x)

with open('input/05.in') as f:
    s = f.read()
    c, d = s.split('\n\n')

    n = len(c.splitlines()[-1].split())
    x = [[] for i in range(n)]

    for l in c.splitlines()[:-1]:
        for i in range(1, len(l), 4):
            if l[i] != ' ':
                x[(i - 1) // 4].insert(0, l[i])
    
    y = [[*map(int, i.split()[1::2])] for i in d.splitlines()]

    print(part1(x, y))
    print(part2(x, y))
