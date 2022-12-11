import math

def parse(m):
    l = m.splitlines()

    r = {}

    r['i'] = [*map(int, l[1].split(': ')[1].split(', '))]
    r['o'] = l[2].split('= ')[1].split()
    r['t'] = int(l[3].split()[-1])
    r['p'] = int(l[4].split()[-1])
    r['f'] = int(l[5].split()[-1])
    r['c'] = 0

    return r

def part1(x):
    ms = [*map(parse, x)]

    for _ in range(20):
        for m in ms:
            for i in m['i']:
                if m['o'][2] == 'old':
                    y = i
                else:
                    y = int(m['o'][2])
                
                if m['o'][1] == '+':
                    w = i + y
                elif m['o'][1] == '*':
                    w = i * y
                
                w //= 3

                if w % m['t'] == 0:
                    ms[m['p']]['i'].append(w)
                else:
                    ms[m['f']]['i'].append(w)
                
                m['c'] += 1
            
            m['i'].clear()
    
    return math.prod(sorted([m['c'] for m in ms])[-2:])

def part2(x):
    ms = [*map(parse, x)]

    p = math.prod(m['t'] for m in ms)

    for _ in range(10000):
        for m in ms:
            for i in m['i']:
                if m['o'][2] == 'old':
                    y = i
                else:
                    y = int(m['o'][2])
                
                if m['o'][1] == '+':
                    w = i + y
                elif m['o'][1] == '*':
                    w = i * y

                w %= p

                if w % m['t'] == 0:
                    ms[m['p']]['i'].append(w)
                else:
                    ms[m['f']]['i'].append(w)
                
                m['c'] += 1
            
            m['i'].clear()
    
    return math.prod(sorted([m['c'] for m in ms])[-2:])

with open('input/11.in') as f:
    s = f.read()
    x = s.split('\n\n')

    print(part1(x))
    print(part2(x))
