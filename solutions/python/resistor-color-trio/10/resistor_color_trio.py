RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIX_OHMS = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]


def label(colors):
    ohm_value_digit1, ohm_value_digit2, nmbr_of_zeroes = [RESISTOR_COLORS.index(color) for color in colors[:3]]
    ohm_result = (ohm_value_digit1 * 10 + ohm_value_digit2) * 10 ** nmbr_of_zeroes
    
    for zero_num, unit in PREFIX_OHMS:
        if ohm_result % zero_num == 0 and ohm_result != 0:
            return f'{ohm_result // zero_num} {unit}'
    return f'{ohm_result} ohms'