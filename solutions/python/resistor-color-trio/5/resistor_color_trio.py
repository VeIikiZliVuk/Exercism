RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]


def label(colors):
    stripe_one_x_ten = RESISTOR_COLORS.index(colors[0]) * 10
    stripe_two = RESISTOR_COLORS.index(colors[1])
    added_zeroes = 10 ** RESISTOR_COLORS.index(colors[2])
    ohm_result = (stripe_one_x_ten + stripe_two) * added_zeroes
    prefix_ohms = [(10 ** 9, "gigaohms"), (10 ** 6, "megaohms"), (10 ** 3, "kiloohms")]

    
    for zero_num, unit in prefix_ohms:
        if ohm_result % zero_num == 0 and ohm_result > 1000:
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