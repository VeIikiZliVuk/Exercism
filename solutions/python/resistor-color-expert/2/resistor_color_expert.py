RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIX_OHMS = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]
TOLERANCE_COLORS = {"grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5, "brown": 1, "red": 2, "gold": 5,
                    "silver": 10}


def resistor_label(colors):

    
#number of colors can be 4, 5 or 1.
    #if it's 4, the first two colors give the ohm value, the 3rd one is the number of zeroes trailing, and the 4th is the tolerance.
    #if it's 5, the first three colors give the ohm value, the 4th one is the number of zeroes trailing, and the 5th is the tolerance.
    #If there's only one color, it's "black", so everything amounts to zero (0)
    if len(colors) == 4:
        frst_digit, scnd_digit, add_zeroes = [RESISTOR_COLORS.index(color) for color in colors[:3]]
        tolerance = TOLERANCE_COLORS[colors[3]]
        ohm_value = (frst_digit * 10 + scnd_digit) * 10 ** add_zeroes
    elif len(colors) == 5:
        frst_digit, scnd_digit, thrd_digit = [RESISTOR_COLORS.index(color) for color in colors[:3]]
        add_zeroes = RESISTOR_COLORS.index(colors[3])
        tolerance = TOLERANCE_COLORS[colors[4]]
        ohm_value = (frst_digit * 100 + scnd_digit * 10 + thrd_digit ) * 10 ** add_zeroes
    elif len(colors) == 1:
        return f'0 ohms'
        
    for zero_num, unit in PREFIX_OHMS:
        if ohm_value >= zero_num:
            value = ohm_value / zero_num 
            return f'{value:g} {unit} ±{tolerance}%'
    return f'{ohm_value} ohms ±{tolerance}%'