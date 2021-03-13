ct = 0

def nodiag (x, y, u, v):
    ux = u - x; vy = v - y
    return False if ux == vy or ux == -vy else True

a = set ()

for x in range (3):
    for y in range (3):
        for u in {0,1,2} - {x}:
            for v in {0,1,2} - {y}:
                if nodiag (x, y, u, v): 
                    if (x, y, u, v) in a or (u, v, x, y) in a: continue
                    else: a.add ((x, y, u, v))
                    ct += 1
                    print (x, y, u, v, end = "   ")
print (ct)
