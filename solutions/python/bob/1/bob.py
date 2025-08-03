def response(hey_bob):
    if hey_bob.isspace() or hey_bob == "":
        return "Fine. Be that way!"
    if hey_bob == hey_bob.upper() and hey_bob[-1] == "?" and any(char.isalpha() for char in hey_bob):
        return "Calm down, I know what I'm doing!"
    if hey_bob.strip()[-1] == "?":
        return "Sure."
    if hey_bob == hey_bob.upper() and any(char.isalpha() for char in hey_bob):
        return "Whoa, chill out!"
    
    return "Whatever."
