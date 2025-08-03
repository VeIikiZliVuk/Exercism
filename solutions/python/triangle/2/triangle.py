def equilateral(sides):
    #a = sides[0]
    #b = sides[1]
    #c = sides[2]
    a, b, c = sides
    if a == b == c and a!= 0 and a + c >= b and b + c >= a and a + b >= c:
        return True
    return False


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a==b or a==c or b==c) and (a + c >= b) and (b + c >= a) and (a + b >= c):
        return True
    return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a != b != c and a!= 0 and a != c and a + c >= b and b + c >= a and a + b >= c:
        return True
    return False
