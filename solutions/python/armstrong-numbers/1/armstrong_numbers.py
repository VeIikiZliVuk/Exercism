def is_armstrong_number(number):
    digits = str(number)
    power = len(digits)
    result = 0
    for dig in digits:
        result += int(dig)**power
    return result == number
    
