from makecalcdict import *
def calcdict():
    with open('calculatordict.json', 'r') as f:
        ardict = json.loads(f.read())
    return ardict #returns angel and reject dictionary- keys are strings: values are associated arrays.
def calculate(mydict, *myset): #takes in the calcdict and then 3-12 non-repeating integers between 0 and 11.
  sortedset = sorted(myset)
  for x, y in mydict.items():
     if sortedset in y:
        return x
if __name__ == "__main__":
    calculatordict = calcdict()
    x = calculate(calculatordict, 2, 4, 5)
    print(x)