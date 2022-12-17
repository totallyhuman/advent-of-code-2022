def collides(c, rl, rp):
    for i, rr in enumerate(rl, start = rp):
        if i < len(c) and c[i] & rr:
            return True
    
    return False

def part1(x):
    c = [127]
    xi = 0

    for r in range(2022):
        c += [0, 0, 0]

        match r % 5:
            case 0:
                rl = [30]
            case 1:
                rl = [8, 28, 8]
            case 2:
                rl = [28, 4, 4]
            case 3:
                rl = [16, 16, 16, 16]
            case 4:
                rl = [24, 24]
        
        rp = len(c)
        f = True
        
        while f:
            match x[xi % len(x)]:
                case '<':
                    rl_ = [i << 1 for i in rl]

                    if not any(rr & 64 for rr in rl) and not collides(c, rl_, rp):
                        rl = rl_
                case '>':
                    rl_ = [i >> 1 for i in rl]

                    if not any(rr & 1 for rr in rl) and not collides(c, rl_, rp):
                        rl = [i >> 1 for i in rl]

            xi += 1
            
            if collides(c, rl, rp - 1):
                f = False
                break
            else:
                rp -= 1
        
        for i, rr in enumerate(rl, start = rp):
            if i < len(c):
                c[i] |= rr
            else:
                c.append(rr)
        
        c = [i for i in c if i]

    return len(c) - 1

def part2(x):
    # build up: 175 rocks
    # loop: every 1730 rocks

    br = 175
    lr = 1730
    nl, re = divmod(1000000000000 - br, lr)

    c = [127]
    xi = 0

    for r in range(br + lr + re):
        c += [0, 0, 0]

        match r % 5:
            case 0:
                rl = [30]
            case 1:
                rl = [8, 28, 8]
            case 2:
                rl = [28, 4, 4]
            case 3:
                rl = [16, 16, 16, 16]
            case 4:
                rl = [24, 24]
        
        rp = len(c)
        f = True
        
        while f:
            match x[xi % len(x)]:
                case '<':
                    rl_ = [i << 1 for i in rl]

                    if not any(rr & 64 for rr in rl) and not collides(c, rl_, rp):
                        rl = rl_
                case '>':
                    rl_ = [i >> 1 for i in rl]

                    if not any(rr & 1 for rr in rl) and not collides(c, rl_, rp):
                        rl = [i >> 1 for i in rl]

            xi += 1
            
            if collides(c, rl, rp - 1):
                f = False
                break
            else:
                rp -= 1
        
        for i, rr in enumerate(rl, start = rp):
            if i < len(c):
                c[i] |= rr
            else:
                c.append(rr)
        
        c = [i for i in c if i]

        if r == br - 1:
            b = len(c) - 1
        
        if r == br + lr - 1:
            l = len(c) - 1 - b

        if r == br + lr + re - 1:
            o = len(c) - 1 - l - b

    return b + (l * nl) + o

with open('input/17.in') as f:
    s = f.read()
    x = s

    print(part1(x))
    print(part2(x))