RESISTOR_COLORS = {"black" : 0, "brown": 1, "red" : 2, "orange" : 3, "yellow" : 4, "green" : 5, "blue" : 6, "violet" : 7, "grey" : 8, "white" : 9}
 
def label(colors):
    ohm_result = (RESISTOR_COLORS[colors[0]]*10 + RESISTOR_COLORS[colors[1]]) * 10 ** RESISTOR_COLORS[colors[2]]

    if ohm_result <= 999:
       return f'{ohm_result} ohms' 
    if ohm_result % 10 ** 9 == 0:
        return f'{ohm_result // 10 ** 9} gigaohms'
    if ohm_result % 10 ** 6 == 0:
        return f'{ohm_result // 10 ** 6} megaohms'
    if ohm_result % 10 ** 3 == 0:
        return f'{ohm_result // 10 ** 3} kiloohms'  