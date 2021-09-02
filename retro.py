def hayl(no):
    for i in range(18):
        if no < pow(10, i):
            ipo = i-1
            break
    return ipo

def mery(no, ipo):
    j = 9
    for i in range(9):
        to = j*pow(10, ipo)
        if no >= to:
            fir = j
            break
        j = j-1
    return fir
