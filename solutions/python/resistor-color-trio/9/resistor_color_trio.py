RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIX_OHMS = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]


def label(colors):
    stripes = [RESISTOR_COLORS.index(color) for color in colors[:3]]
    frst_color, scnd_color, thrd_color = stripes
    ohm_result = (frst_color * 10 + scnd_color) * 10 ** thrd_color
    
    for zero_num, unit in PREFIX_OHMS:
        if ohm_result % zero_num == 0 and ohm_result != 0:
            return f'{ohm_result // zero_num} {unit}'
    return f'{ohm_result} ohms'