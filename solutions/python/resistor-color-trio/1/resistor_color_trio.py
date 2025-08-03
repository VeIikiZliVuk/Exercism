
colors_dict = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5, "blue":6, "violet":7, "grey":8, "white":9}

    
def label(colors):
    ohm_result = (colors_dict[colors[0]]*10 + colors_dict[colors[1]]) * 10 ** colors_dict[colors[2]]

    if colors_dict[colors[2]] == 9:
        return f'{ohm_result//10**9} gigaohms'
    if 6<= colors_dict[colors[2]] <=8:
        return f'{ohm_result//10**6} megaohms'
    if 3<= colors_dict[colors[2]] <=5:
        return f'{ohm_result//10**3} kiloohms'
    if ohm_result % 10**3 == 0 and ohm_result > 999:
        return f'{ohm_result//10**3} kiloohms'
    return f'{ohm_result} ohms'
    