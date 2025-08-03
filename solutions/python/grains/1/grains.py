def square(number):
    if number == 1:
        return 1
    if 1 < number <= 64:
        return 2 ** (number-1)
    raise ValueError("square must be between 1 and 64")
    


def total():
    total_num = []
    for number in range(2,65):
        total_num.append(square(number))
    return sum(total_num) + 1
        
