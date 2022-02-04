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
        self.__lvl += Player.__typeTest(numeric)
        if self.__lvl >= 100: self.__lvl = 100

    @classmethod
    def set_cls_field(cls, lvl = 1, health=100):
        cls.__LVL = Player.__typeTest(lvl)
        cls.__HEALTH = Player.__typeTest(health)
        
    @staticmethod
    def __typeTest(val):
        if isinstance(val, int):
            return val
        else:
            raise TypeError("Must be int!")
        

