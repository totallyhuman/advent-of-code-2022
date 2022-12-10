def run(x):
    r = 1
    rs = []

    for i in x:
        rs.append(r)

        if i[0] == 'addx':
            rs.append(r)

            r += int(i[1])
    
    return rs

def part1(x):
    rs = run(x)

    return sum(rs[i - 1] * i for i in range(20, 221, 40))

def part2(x):
    rs = run(x)
    s = ''

    for c in range(240):
        if abs(rs[c] - (c % 40)) < 2:
            s += '#'
        else:
            s += ' '
        
        if (c + 1) % 40 == 0:
            s += '\n'
    
    return s

with open('10.in') as f:
    s = f.read()
    x = [i.split() for i in s.splitlines()]

    print(part1(x))
    print(part2(x))
