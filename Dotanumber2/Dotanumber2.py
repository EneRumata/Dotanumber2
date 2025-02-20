import requests
import random

class BaseArray:
    def __init__(self):
        self._heroes = []
        
    def GetArray(self):
        return self._heroes

            
class JsonArray(BaseArray):
    def __init__(self):
        self._heroes = requests.get('https://www.dota2.com/datafeed/herolist?language=russian')
        self._heroes = self._heroes.json()["result"]['data']['heroes']
        
    def GetElement(self,index,key):
        return self._heroes[index][key]


class HeroArray(BaseArray):
    def AddArray(self,newhero):
        self._heroes.append(newhero)

    def GetRandom(self):
        return self._heroes[random.randint(0,len(self._heroes)-1)]


def main():
    HeroArrayes = [HeroArray(),HeroArray(),HeroArray(),HeroArray(),HeroArray()]

    MAIN_ARRAY = JsonArray()
        
    for i in range(len(MAIN_ARRAY.GetArray())-1):
        HeroArrayes[MAIN_ARRAY.GetElement(i,'primary_attr')].AddArray(MAIN_ARRAY.GetElement(i,'name_loc'))
        HeroArrayes[4].AddArray(MAIN_ARRAY.GetElement(i,'name_loc'))

    
    random.seed()
    print("RANDOM DOTA HEROES BY BOD47 AND ENERUMATA")

    while True:
        print()
        print()
        print(HeroArrayes[0].GetRandom())
        print(HeroArrayes[1].GetRandom())
        print(HeroArrayes[2].GetRandom())
        print(HeroArrayes[3].GetRandom())
        print(HeroArrayes[4].GetRandom())
        print()
        print()
        print("Type 0 to roll again or anything else to quit")
        UserInputStr = input()
        if UserInputStr!='0':
            break
    
    
    #print(type(MAIN_ARRAY.GetArray()))
    #print(len(MAIN_ARRAY.GetArray()))
    #print(HeroArrayes[0].GetArray())
    #print(HeroArrayes[1].GetArray())
    #print(HeroArrayes[2].GetArray())
    #print(HeroArrayes[3].GetArray())
    #print(HeroArrayes[4].GetArray())

if __name__ == "__main__":
    main()
