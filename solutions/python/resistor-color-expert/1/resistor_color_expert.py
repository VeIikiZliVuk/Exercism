RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIX_OHMS = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]
TOLERANCE_COLORS = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5,
                    "silver": 10}


def resistor_label(colors):

    
    if len(colors) == 4:
        color_one, color_two, color_three = [RESISTOR_COLORS.index(color) for color in colors[:3]]
        color_four = TOLERANCE_COLORS[colors[3]]
        ohm_value = (color_one * 10 + color_two) * 10 ** color_three
    elif len(colors) == 5:
        color_one, color_two, color_three = [RESISTOR_COLORS.index(color) for color in colors[:3]]
        color_four = RESISTOR_COLORS.index(colors[3])
        color_five = TOLERANCE_COLORS[colors[4]]
        ohm_value = (color_one * 100 + color_two * 10 + color_three ) * 10 ** color_four
    elif len(colors) == 1:
        ohm_value = 0
        
    for zero_num, unit in PREFIX_OHMS:
            if ohm_value >= zero_num:
                value = ohm_value / zero_num 
                if len(colors) == 4:
                    return f'{value:g} {unit} ±{color_four}%'
                elif len(colors) == 5:
                    return f'{value:g} {unit} ±{color_five}%'
    if len(colors) == 4:
        return f'{ohm_value} ohms ±{color_four}%'
    elif len(colors) == 5:
        return f'{ohm_value} ohms ±{color_five}%'
    elif len(colors) == 1:
        return f'0 ohms'