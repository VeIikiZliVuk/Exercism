def is_valid(isbn):
    isbn = isbn.replace("-", "").upper()
    #bez crtica i neka bude velikim slovima
    #isbn_new = list(isbn_1)

    # duzina mora biti tacno 10
    if len(isbn) != 10:  
        return False

    #svi osim zadnje cifre moraju biti brojevi
    if not isbn[:-1].isdigit():
        return False

    #posljednji mora biti broj tri ili X
    if isbn[-1].isdigit():
        digit = int(isbn[-1])
    elif isbn[-1] == "X":
        digit = 10
    else:
        return False

#prvih devet pretvoriti u brojeve
    digits = [int(ch) for ch in isbn[:-1]]
    digits.append(digit)

    #napraviti
#digits.append(digit)

    total = sum(digit * weight for digit, weight in zip(digits, range(10, 0, -1)))
    return total % 11 == 0


#for char in isbn:
    #if char.isdigit():
        #return int(char)
    #else:
        #return False
    #if char.isalpha():
        #char == 10
    #else: 
       # return False

    #digits.append(digit)



#sracuna slucajeve X 
    #if (isbn[0]*10 + isbn[1]*9 + isbn[2]*8 + isbn[3]*7 + isbn[4]*6 + isbn[5]*5 + isbn[6]*4 + isbn[7]*3 + isbn[8]*2 + isbn[9]*1) % 11 == 0:
        #return True
    #else:
        #return False
