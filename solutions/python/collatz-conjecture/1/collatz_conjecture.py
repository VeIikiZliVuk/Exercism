def steps(number):
    numbers_steps = []
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    while number != 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = number * 3 + 1
        numbers_steps.append(number)
    return len(numbers_steps)
    
    
        
