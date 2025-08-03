def value(colors):
    
    colors_dict = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}
    
    colors_num = []
    #This'll be our final result, two digits: first band - first digit, second band - second digit.
    
    for key, value in colors_dict.items():
        if colors[0] == key:
            colors_num.append(value*10)
        if colors[1] == key:
            colors_num.append(value)
    return colors_num[0] + colors_num[1]
    
