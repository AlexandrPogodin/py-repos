def f(x):
    if x <= -2:
        a = 1 - (x + 2)**2
        return a
    if x <= 2 and x > -2:
        a = -(x/2)
        return a
    if x > 2:
        a = ((x-2)**2)+1
        return a
