
color_dict = {0:"black", 1:"brown", 2:"red", 3:"orange", 4:"yellow", 5:"green", 6:"blue", 7:"violet", 8:"grey", 9:"white"}

def color_code(color):
    for key, value in color_dict.items():
        if value == str(color):
            return key

def colors():
    colors_list = []
    for key, value in color_dict.items():
        colors_list.append(value)
    return colors_list
