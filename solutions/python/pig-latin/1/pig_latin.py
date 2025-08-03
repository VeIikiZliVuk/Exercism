#def translate(text):
    #vowy = ""
    #if text[0] == "a" or text[0] == "e" or text[0] == "o" or text[0] == "i" or text[0] == "u":
        #vowy = text + "ay"
        #return vowy
        
def translate(text):
    if " " in text:
        phrase = text.split()
        translated_phrase = []
        for word in phrase:
            translated_phrase.append(translate(word))
        return " ".join(translated_phrase)
    else:
            
        #vowels = ["a", "e", "i", "o", "u"]
        #consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        text = text.lower()
        vow_duos = ["xr", "yt"]
        cons_threes = ["thr", "sch"]
        if len(text) < 2:
            return text + "ay"
        if len(text) == 2 and text[1] == "y":
            return text[1] + text[0] + "ay"
        if text[0] in vowels or text[:2] in vow_duos:
            return text + "ay"
        if text[:3] in cons_threes:
            return text[3:] + text[:3] + "ay"
    #if text[0] in consonants and text[1] in consonants and text[2] in consonants:
        #cons3_text = text[3:] + text[0]+text[1]+text[2]
        #return cons3_text + "ay"
        if text[0] == "q" and text[1] == "u":
            return text[2:] + text[0]+text[1] + "ay"
        if text[0] in consonants and text[1:3] == "qu":
            return text[3:] + text[:3] + "ay"
        if text[0] in consonants and text[1] in consonants:
            cons2_text = text[2:] + text[0]+text[1]
            return cons2_text + "ay"
        cons_text = text[1:] + text[0]
        return cons_text + "ay"
        #if text[0] == "q" and text[1] == "u":
            #return text[2:] + text[0]+text[1] + "ay"
    