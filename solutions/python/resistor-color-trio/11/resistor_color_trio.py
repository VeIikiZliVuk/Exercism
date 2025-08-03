RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIX_OHMS = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]


def label(colors):
    ohm_tens, ohm_ones, exponent = [RESISTOR_COLORS.index(color) for color in colors[:3]]
    ohm_result = (ohm_tens * 10 + ohm_ones) * 10 ** exponent
    
    for zero_num, unit in PREFIX_OHMS:
        if ohm_result % zero_num == 0 and ohm_result != 0:
            return f'{ohm_result // zero_num} {unit}'
    return f'{ohm_result} ohms'