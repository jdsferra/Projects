import json
import numpy as np
def ardict():
    with open('angelsandrejects.json', 'r') as f:
        ardict = json.loads(f.read())
    return ardict #returns angel and reject dictionary- keys are strings: values are associated arrays.
def modconvert(n): #takes any number and converts to base 12 system- 15->3, 9+5 = 2
    if np.any(n < 0):
        return n + 12
    if np.any(n > 11):
        return n % 12
    else:
        return n
def complement(x): #occasionally-needed mod12 function (0,0, 2,10, 66, vv)
    if np.any(x) == 0:
        return x
    return 12-x  
def symmetrical(myset): #takes a list and returns if it's symmetrical.
    AIS = [] #Adjacency Interval Series
    for i, x in enumerate(myset[:-1]):
        y = myset[i+1]
        AIS.append(y-x)
    return AIS == AIS[::-1] #if AIS is same Fw/Bw, symmetrical set. Returns Boolean.
def AISfromset(myset):
    AIS = []
    for i, x in enumerate(myset[:-1]):
        y = myset[i+1]
        AIS.append(y-x)
    AIS.append(complement(myset[-1])) #adds the interval that takes you back to 0
    return AIS
def setfromAIS(ais): #from a given list as AIS, generates the prime form of the set
    newset = [0]
    for i, x in enumerate(ais[:-1]):
        newset.append(newset[i] + ais[i])
    return newset
def primeformformat(mylist):
  return f"({''.join(str(x) for x in mylist)})"
def rr(mylist):
  checklist = []
  for i in range(len(mylist)):
    rotatedarray = mylist[i:] + mylist[:i]
    checklist.append(rotatedarray[::-1])
  return checklist
def makeAIStrichords():
    aislist = []
    reversedaislist = []
    for x in range(1, 5):
        y = x
        z = 10
        while y < z:
            z = complement(x + y)
            ais = [x, y, z]
            if ais in reversedaislist:
                pass
            else:
                reversedaislist.append(rr(ais))
                aislist.append(ais)
            y += 1
    return aislist
def makeAIStetrachords():
    aislist = []
    reversedaislist = []
    for w in range(1, 4):
        for x in range(1, 6):
            y = w
            z = 9
            while y < z:
                z = complement(w + x + y)
                ais = [w, x, y, z]
                if ais in reversedaislist:
                    pass
                else:
                    for eachrotation in rr(ais):
                        reversedaislist.append(eachrotation)
                    aislist.append(ais)
                y += 1
    return aislist
def makeAISpentachords(ardict):
    aislist = []
    reversedaislist = []
    for v in range(1, 4):
        for w in range(1, 4):
            for x in range(1, 5):
                y = 1
                z = 8
                while y < z:
                    z = complement(v + w + x + y)
                    ais = [v, w, x, y, z]
                    if ais in reversedaislist:
                        pass
                    elif ais in ardict['rejects']:
                        pass
                    elif ais == [3, 1, 1, 3, 4]:
                        aislist.append(ais)
                        return aislist
                    else:
                        for eachrotation in rr(ais):
                            reversedaislist.append(eachrotation)
                        aislist.append(ais)
                    y += 1
def makeAIShexachords(ardict):
    aislist = []
    reversedaislist = []
    for ais in ardict['angels']: #keeps dictionary entries ordered by cardinality
        if len(ais) == 6:
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
                        elif ais in ardict['rejects']:
                            pass
                        elif z <= 0:
                            pass
                        elif ais == [2, 2, 2, 2, 2, 2]:
                            aislist.append(ais)
                            return aislist
                        else:
                            for eachrotation in rr(ais):
                                reversedaislist.append(eachrotation)
                            aislist.append(ais)
                        y += 1
def makeAISheptachords(ardict):
    aislist = []
    reversedaislist = []
    for ais in ardict['angels']:
        if len(ais) == 7:
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
                            elif ais in ardict['rejects']:
                                pass
                            elif z <= 0:
                                pass
                            elif ais == [2, 1, 1, 1, 1, 2, 4]:
                                aislist.append(ais)
                                return aislist
                            else:
                                for eachrotation in rr(ais):
                                    reversedaislist.append(eachrotation)
                                aislist.append(ais)
                            y += 1
def makeAISoctachords(ardict):
    aislist = []
    reversedaislist = []
    for ais in ardict['angels']:
        if len(ais) == 8:
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
                                elif ais in ardict['rejects']:
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
def makeAISnonachords(ardict):
    aislist = []
    reversedaislist = []
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
                                    elif ais in ardict['rejects']:
                                        pass
                                    elif z <= 0:
                                        pass
                                    elif ais == [1, 1, 2, 1, 1, 2, 1, 1, 2]:
                                        aislist.append(ais)
                                        return aislist
                                    else:
                                        for eachrotation in rr(ais):
                                            reversedaislist.append(eachrotation)
                                        aislist.append(ais)
                                    y += 1
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
def makeAIS1112():
    aislist = []
    elevenchordais = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    twelvechordais = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    aislist.append(elevenchordais)
    aislist.append(twelvechordais)
    return aislist 
def makeprimeforms(AISlist):
    primeforms = []
    for ais in AISlist:
        primeforms.append(setfromAIS(ais))
    return primeforms
def generateallsets(primeform): #takes a primeform and generates all 24 (or 12 if symmetrical) transpositions/inversions.
    allsets = []
    primeform = np.array(primeform)
    for i in range(12):
        myset = np.sort(modconvert(primeform+i))
        allsets.append(myset) #you will get some duplicates added here
    if not symmetrical(primeform):
        invertedprimeform = np.array(complement(primeform))
        for i in range(12):
            myset = np.sort(modconvert(invertedprimeform+i))
            allsets.append(np.sort(myset))
    allsets = np.unique(np.array(allsets), axis = 0) #deletes duplicates and reformats into an array
    return allsets.tolist()
def bigasslistmake(ardict):
    bigasslist = []
    realbigasslist = []
    bigasslist.append(makeAIStrichords())
    bigasslist.append(makeAIStetrachords())
    bigasslist.append(makeAISpentachords(ardict))
    bigasslist.append(makeAIShexachords(ardict))
    bigasslist.append(makeAISheptachords(ardict))
    bigasslist.append(makeAISoctachords(ardict))
    bigasslist.append(makeAISnonachords(ardict))
    bigasslist.append(makeAISdecachords())
    bigasslist.append(makeAIS1112())
    for mylist in bigasslist:
        for ais in mylist:
            realbigasslist.append(ais)
    return realbigasslist    
def dictmake(aislist):  
    mydict = {}  
    for ais in aislist:
        primeform = setfromAIS(ais)
        mydict.update({primeformformat(primeform): generateallsets(primeform)})
    return mydict
def main():
    angrejdict = ardict()
    allAIS = bigasslistmake(angrejdict)
    w = dictmake(allAIS)
    with open("calculatordict.json", 'w') as f:
        json.dump(w, f, indent = 4)   
if __name__ == "__main__":
    main()