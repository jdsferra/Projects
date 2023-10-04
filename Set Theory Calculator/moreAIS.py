from RUN import *
def makeAIShexachords():
    aislist = []
    reversedaislist = []
    rejects = [[1, 1, 2, 4, 1, 3], [1, 1, 2, 4, 2, 2], [1, 1, 3, 4, 1, 2], [1, 2, 2, 4, 1, 2], [1, 2, 3, 2, 2, 2], [1, 2, 3, 3, 1, 2], [1, 2, 3, 4, 1, 1], [1, 2, 4, 1, 1, 3], 
                [1, 2, 4, 1, 2, 2], [1, 2, 4, 2, 1, 2], [1, 2, 4, 3, 1, 1], [1, 3, 1, 2, 2, 3], [1, 3, 1, 4, 1, 2], [1, 3, 2, 1, 2, 3], [1, 3, 2, 4, 1, 1], 
                [1, 3, 3, 1, 1, 3], [1, 3, 4, 1, 1, 2], [2, 1, 2, 3, 2, 2], [2, 1, 2, 4, 1, 2], [2, 1, 3, 4, 1, 1], [2, 1, 4, 1, 1, 3], [2, 2, 1, 1, 2, 4], [2, 2, 2, 1, 2, 3],
                [1, 2, 2, 3, 2, 2], [1, 3, 4, 2, 1, 1], [2, 1, 2, 3, 1, 3]]
    angels = [[1, 3, 2, 1, 2, 3]]
    for ais in angels:
        aislist.append(ais)
    for u in range(1, 3):
        for v in range(1, 4):
            for w in range(1, 5):
                for x in range(1, 5):
                    y = 1
                    z = 7
                    while y < z:
                        z = complement(u + v + w + x + y)
                        ais = [u, v, w, x, y, z]
                        if ais in reversedaislist:
                            pass
                        elif ais in rejects:
                            pass
                        elif z <= 0: #jfc the elif
                            pass
                        elif ais == [2, 2, 2, 2, 2, 2]:
                            aislist.append(ais)
                            return f'{len(aislist)}, {aislist}'
                        else:
                            for eachrotation in rr(ais):
                                reversedaislist.append(eachrotation)
                            aislist.append(ais)
                        y += 1

def makeAISnonachords():
    aislist = []
    reversedaislist = []
    rejects = [[1, 1, 1, 2, 1, 2, 2, 1, 1]]
    for r in range(1, 2):
        for s in range(1, 2):
            for t in range(1, 3):
                for u in range(1, 3):
                    for v in range(1, 3):
                        for w in range(1, 3):
                            for x in range(1, 3):
                                y = 1
                                z = 4
                                while y < z:
                                    z = complement(r + s + t + u + v + w + x + y)
                                    ais = [r, s, t, u, v, w, x, y, z]
                                    if ais in reversedaislist:
                                        pass
                                    elif ais in rejects:
                                        pass
                                    elif z <= 0: #jfc the elif
                                        pass
                                    elif ais == [1, 1, 2, 1, 1, 2, 1, 1, 2]:
                                        aislist.append(ais)
                                        return aislist
                                    else:
                                        for eachrotation in rr(ais):
                                            reversedaislist.append(eachrotation)
                                        aislist.append(ais)
                                    y += 1
    return aislist

def makeAISheptachords(): #WORKS!
    aislist = []
    reversedaislist = []
    rejects = [[1, 1, 1, 2, 3, 2, 2], [1, 1, 2, 1, 3, 2, 2], [1, 1, 2, 3, 1, 2, 2], [1, 1, 2, 3, 2, 1, 2], [1, 1, 2, 3, 3, 1, 1], [1, 1, 3, 1, 1, 2, 3],
            [1, 2, 1, 2, 3, 1, 2], [1, 2, 1, 3, 3, 1, 1], [1, 2, 2, 1, 3, 1, 2], [1, 2, 2, 2, 3, 1, 1], [1, 2, 2, 3, 1, 1, 2], [1, 2, 3, 1, 1, 1, 3], 
            [1, 2, 3, 1, 1, 2, 2], [1, 2, 3, 1, 2, 1, 2], [1, 2, 3, 1, 3, 1, 1], [1, 2, 3, 2, 2, 1, 1], [1, 2, 3, 3, 1, 1, 1], [1, 1, 2, 2, 3, 1, 2], [1, 2, 1, 1, 2, 2, 3], [1, 2, 2, 3, 2, 1, 1], [1, 2, 3, 2, 1, 1, 2]]
    angels = [[2, 1, 1, 1, 2, 2, 3], [2, 1, 1, 2, 1, 2, 3], [1, 2, 1, 1, 2, 2, 3]]
    for ais in angels:
        aislist.append(ais)
    for t in range(1, 3):
        for u in range(1, 3):
            for v in range(1, 4):
                for w in range(1,4):
                    for x in range(1, 4):
                        y = 1
                        z = 6
                        while y < z:
                            z = complement(t + u + v + w + x + y)
                            ais = [t, u, v, w, x, y, z]
                            if ais in reversedaislist:
                                pass
                            elif ais in rejects:
                                pass
                            elif z <= 0: #jfc the elif
                                pass
                            elif ais == [2, 1, 1, 1, 1, 2, 4]:
                                aislist.append(ais)
                                return aislist
                            else:
                                for eachrotation in rr(ais):
                                    reversedaislist.append(eachrotation)
                                aislist.append(ais)
                            y += 1
    return aislist
def makeAISoctachords():#WORKS!
    aislist = []
    reversedaislist = []
    angels = [[2, 1, 1, 1, 1, 1, 2, 3], [1, 1, 2, 1, 2, 2, 1, 2]]
    rejects = [ [1, 1, 2, 3, 2, 1, 1, 1], [1, 1, 2, 1, 2, 2, 1, 2], [1, 1, 2, 1, 3, 2, 1, 1], [1, 1, 2, 4, 1, 3], [1, 1, 2, 4, 2, 2], [1, 1, 3, 4, 1, 2], [1, 2, 2, 4, 1, 2], [1, 2, 3, 2, 2, 2], [1, 2, 3, 3, 1, 2], [1, 2, 3, 4, 1, 1], [1, 2, 4, 1, 1, 3], 
                [1, 2, 4, 1, 2, 2], [1, 2, 4, 2, 1, 2], [1, 2, 4, 3, 1, 1], [1, 3, 1, 2, 2, 3], [1, 3, 1, 3, 1, 3], [1, 3, 1, 4, 1, 2], [1, 3, 2, 1, 2, 3], [1, 3, 2, 4, 1, 1], 
                [1, 3, 3, 1, 1, 3], [1, 3, 4, 1, 1, 2], [1, 1, 1, 1, 2, 3, 1, 2], [1, 1, 1, 2, 1, 3, 1, 2], [1, 1, 1, 2, 2, 3, 1, 1], [1, 1, 1, 2, 3, 1, 1, 2], [1, 1, 1, 2, 3, 2, 1, 1], [1, 1, 2, 1, 2, 3, 1, 1], 
                [1, 1, 2, 1, 3, 1, 1, 2], [1, 1, 2, 2, 1, 3, 1, 1], [1, 1, 2, 2, 3, 1, 1, 1], [1, 1, 2, 3, 1, 1, 1, 2], [1, 1, 2, 3, 1, 2, 1, 1], [1, 2, 1, 1, 2, 3, 1, 1], [1, 2, 1, 1, 2, 1, 2, 2]]
    for ais in angels:
        aislist.append(ais)
    for s in range(1, 2):
        for t in range(1, 3):
            for u in range(1, 3):
                for v in range(1, 4):
                    for w in range(1, 4):
                        for x in range(1, 4):
                            y = 1
                            z = 5
                            while y < z:
                                z = complement (s + t + u + v + w + x + y)
                                ais = [s, t, u, v, w, x, y, z]
                                if ais in reversedaislist:
                                    pass
                                elif ais in rejects:
                                    pass
                                elif z <= 0:
                                    pass
                                elif ais == [1, 2, 1, 2, 1, 2, 1, 2]:
                                    aislist.append(ais)
                                    return aislist
                                else:
                                    for eachrotation in rr(ais):
                                        reversedaislist.append(eachrotation)
                                    aislist.append(ais)
                                y += 1
    return aislist

def makeAISdecachords():
    aislist = []
    reversedaislist = []
    for q in range(1, 2):
        for r in range(1, 2):
            for s in range(1, 2):
                for t in range(1, 2):
                    for u in range(1, 3):
                        for v in range(1, 3):
                            for w in range(1, 3):
                                for x in range(1, 3):
                                    y = 1
                                    z = 3
                                    while y < z:
                                        z = complement (q + r + s + t + u + v + w + x + y)
                                        ais = [q, r, s, t, u, v, w, x, y, z]
                                        if ais in reversedaislist:
                                            pass
                                        # elif ais in rejects:
                                        #     pass
                                        elif z <= 0:
                                            pass
                                        elif ais == [1, 1, 1, 1, 2, 1, 1, 1, 1, 2]:
                                            aislist.append(ais)
                                            return aislist
                                        else:
                                            for eachrotation in rr(ais):
                                                reversedaislist.append(eachrotation)
                                            aislist.append(ais)
                                        y += 1
    return aislist
def makeAIS1112(): #WORKS!
    aislist = []
    elevenchordais = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    twelvechordais = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    aislist.append(elevenchordais)
    aislist.append(twelvechordais)
    return aislist 
def setfromAISexp(ais): #from a given list as AIS, generates the prime form of the set
    newset = [0]
    for i, x in enumerate(ais[:-1]):
        newset.append(newset[i] + ais[i])
    return newset
if __name__ == "__main__":
    x = setfromAISexp([[1, 1, 1], [2, 2, 2]])
    print(x)