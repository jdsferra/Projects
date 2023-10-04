from RUN import *
import json
def main():
    # x = makeAIStrichords()
    # w = dictmake(makeAIStrichords())
    # with open("test.json", 'w') as f:
    #     json.dump(w, f)
    # with open("test.json", 'r') as f:
    #     x = json.load(f)
    # print(x)
    x = bigasslistmake()
    w = dictmake(x)
    with open("nexttest.json", 'w') as f:
        json.dump(w, f, indent = 4)    
if __name__ == "__main__":
    main()