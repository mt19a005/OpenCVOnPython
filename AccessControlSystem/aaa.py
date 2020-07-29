import os
from Data import Name 
import bbb

path = "./rensyu"
def addTrainData():
    for fileName in os.listdir(path):
        # print(fileName[0:1])
        if fileName[0:1] == "0":
            Name.Taguwa[1] += 1
            print(Name.Taguwa[1])
    
    bbb.prin()

addTrainData()