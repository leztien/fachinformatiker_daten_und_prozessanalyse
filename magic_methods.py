"""
Seite 166, 175
"""

from random import shuffle


class Abstract:
    __counter = 0
    def __init__(self):
        self.__class__.__counter += 1
        self._id = self.__counter
    def __str__(self):
        return f"{self.__class__.__name__}({self._id})"
    

class Object(Abstract):
    def __eq__(self, other): # __ne__ ist nicht nötig
        return self._id == other._id
    
    def __lt__(self, other): # wird for Sortierung verwendet
        return self._id < other._id
    
    def __ge__(self, other): # Gegenteil von "less than"
       return not(self < other)
   
    def __repr__(self):
        return super().__str__()



objects = [Object() for _ in range(10)]
shuffle(objects)

o1, o2, o3, *_ = objects

b = o1 != o2

b = o2 >= o3
print(b, o2, o3)

objects.sort()
print(objects)
