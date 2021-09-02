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
no = int(input("Please enter the number: "))
ipo = po = hayl(no)
firs = 0
for i in range(po+1):
    fira = mery(no, ipo)
    no = no-(fira*pow(10, ipo))
    firs = firs + fira*pow(10, (po-ipo))
    ipo = ipo - 1
print("The number is: ", firs)