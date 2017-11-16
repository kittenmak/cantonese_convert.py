import json
from pprint import pprint
import time

DATA = json.load(open('source/characters-min.json'))

def convert(content):
    result = ""
    for char in content:
        try:
        # print (str(DATA[char]))
            sound = DATA[char]
            if len(sound)>1:
                result += str(sound).replace("'","").replace(", ", " / ") + " "
            else:
                result += str(sound).replace("['"," ").replace("']", " ")
        except KeyError:
            result += char
    return result
    

def main():
    a = convert("我係傻仔陳大文，多多指教")
    print(a)
if __name__ == '__main__':
    main()