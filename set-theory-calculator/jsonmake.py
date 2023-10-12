from RUN import *
import json
def main():
    x = bigasslistmake()
    w = dictmake(x)
    with open("calculatordict.json", 'w') as f:
        json.dump(w, f, indent = 4)    
if __name__ == "__main__":
    main()