def parse(x, i = 1, f = {}):
    while i < len(x):
        l = x[i].split()[1:]

        if l[0] == 'ls':
            i += 1

            while i < len(x) and not x[i].startswith('$'):
                c = x[i].split()

                if c[0] == 'dir':
                    f[c[1]] = {}
                else:
                    f[c[1]] = int(c[0])
                
                i += 1
        elif l[0] == 'cd':
            if l[1] == '..':
                return (f, i)
            else:
                f[l[1]], i = parse(x, i + 1, f[l[1]])
        
            i += 1
    
    return (f, i)

def size(f):
    if type(f) is int:
        return f

    return sum(map(size, f.values()))

def sizes(f):
    if type(f) is int:
        return []

    return sum(map(sizes, f.values()), []) + [size(f)]

def part1(x):
    return sum(i for i in sizes(x) if i <= 100000)

def part2(x):
    return min(i for i in sizes(x) if i >= 30000000 - (70000000 - size(x)))

with open('07.in') as f:
    s = f.read()
    x = parse(s.splitlines())[0]

    print(part1(x))
    print(part2(x))
