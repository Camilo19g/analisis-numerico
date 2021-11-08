
def euler(f, x, y, h, m):
    u = []
    v = []
    for i in range(m):
        y = y + h*f(x, y)
        x = x + h
        y = round(y, 2)
        x = round(x, 2)
        u += [x]
        v += [y]
        print(f"🟢 y'({x}) = {y}")
    return [u, v]