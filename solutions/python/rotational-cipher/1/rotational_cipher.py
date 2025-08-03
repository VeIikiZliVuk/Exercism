def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alpha_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    new_text = []
    #rot = str(text[key:]) + str(text[0:key])
    #return rot
    for t in text:
        if t in alphabet:
            index = alphabet.index(t)
            new_t = alphabet[(index + key) % 26]
            new_text.append(new_t)
        elif t in alpha_caps:
            index = alpha_caps.index(t)
            new_t = alpha_caps[(index + key) % 26]
            new_text.append(new_t)
        else:
            new_text.append(t)
    return ''.join(new_text) 
        
    
