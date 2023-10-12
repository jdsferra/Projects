def modconvert(num):
    if num < 12:
        return num
    else:
        return num % 12
def complement(x):
    return 12 - x
def transpose (row, opci):
    transposed = [modconvert(x+opci) for x in row]
    myvariable = 'P{} {} R{}'.format(transposed[0], transposed, transposed[0])
    print(myvariable.replace('10', 'T').replace('11', 'E'))
#one big string with all the rows in it
#bring transpose into generatematrix, abstract the transpose function to be usable within the matrix making (ditch the print, do returning)
def newrow():
    prime = []
    print('Input 12 non-repeating numbers to make your prime row:')
    while len(prime) < 12: #(running list, shows user number they've already chosen- (C)lear (Q)uit)
        try: 
            pc = int(input('\n>'))    
        except ValueError:
            print("use a number- ValueError")
            continue
        if pc in prime:
            print("no repeated numbers")
            continue
        if pc > 11:
            print("only 0 thru 11")
            continue
        prime.append(pc)
    return prime
def generatematrix(row):
    Torder = []
    for x in range(12):
        if x == 0:
            Torder.append(0)
        else:
            i = row[0] - row[x]
            if i > 0:
                Torder.append(i)
            if i < 0:
                y = i + 12
                Torder.append(y)
    print(f"X  I{' I'.join(str(r) for r in row)} X")
    for x in Torder:
        transpose(row, x)
    print(f"X  RI{'RI'.join(str(r) for r in row)} X")

if __name__ == "__main__":
    generatematrix(newrow())

#loop is for coercing values into strings- otherwise it could just do it
#goes in between