def score(x, y):
    #if x<=1 and y<=1:
        #return 10
    #if 1<x<=5 and y<=5:
        #return 5
    #if 5<x<=10 and y<=10:
        #return 1
    #return 0

    z_squared = x**2 + y**2
    if z_squared <= 1**2:
        return 10
    if 1**2 < z_squared <= 5**2:
        return 5
    if 5**2 < z_squared <= 100:
        return 1
    return 0
