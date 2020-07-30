import os
from enum import Enum
class Name(Enum):
    Taguwa = 1
    Tsukuda = 2
    Humiyama = 3

class num():
    Taguwa = 0
    Tsukuda = 0
    Humiyama = 0

for name in Name:
    if "Taguwa" == str(name)[6:]: 
        num.str(name)[6:] += 1

print(num.Taguwa)