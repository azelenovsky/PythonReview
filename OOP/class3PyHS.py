from datetime import datetime as dt
from time import sleep 

class Player:
    __LVL, __HEALTH = 1, 100
    __slots__ = ['__lvl', '__health', '__birthday']
    
    def __init__(self):
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__birthday = dt.now()
        
    #getter, setter
    @property
    def lvl(self):
        return self.__lvl, f'{dt.now() - self.__birthday}'
    
    @lvl.setter
    def lvl(self, numeric):
        self.__lvl += numeric
        if self.__lvl >= 100: self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl = 1, health=100):
        cls.__LVL = lvl
        cls.__HEALTH = health
        

x = Player()
print(x.lvl)
sleep(.1)
x.lvl = 5
print(x.lvl)


