RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
PREFIX_OHMS = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]


def label(colors):
    stripes = []
    for color in colors[:3]:
        stripes.append(RESISTOR_COLORS.index(color))
    stripe1, stripe2, stripe3 = stripes
    ohm_result = (stripe1 * 10 + stripe2) * 10 ** stripe3
    
    #stripe_one_x_ten = RESISTOR_COLORS.index(colors[0]) * 10
    #stripe_two = RESISTOR_COLORS.index(colors[1])
    #added_zeroes = 10 ** RESISTOR_COLORS.index(colors[2])
    #ohm_result = (stripe_one_x_ten + stripe_two) * added_zeroes
    

    
    for zero_num, unit in PREFIX_OHMS:
        if ohm_result % zero_num == 0 and ohm_result != 0:
            return f'{ohm_result // zero_num} {unit}'
    return f'{ohm_result} ohms'

    
    #if ohm_result < 10 ** 3:
       #return f'{ohm_result} ohms' 
    #if ohm_result % 10 ** 9 == 0:
        #return f'{ohm_result // 10 ** 9} gigaohms'
    #if ohm_result % 10 ** 6 == 0:
        #return f'{ohm_result // 10 ** 6} megaohms'
    #if ohm_result % 10 ** 3 == 0:
        #return f'{ohm_result // 10 ** 3} kiloohms'  