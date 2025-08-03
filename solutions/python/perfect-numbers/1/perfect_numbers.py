def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
                
    x_list = []
    for x in range(1,number):
        if number % x == 0:
            x_list.append(x)
    if sum(x_list) == number:
        return "perfect"
    if sum(x_list) < number:
        return "deficient"
    if sum(x_list) > number:
        return "abundant"
