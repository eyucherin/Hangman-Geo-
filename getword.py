
import random

class wordList:
    list=[]
    reader=open("text.txt","r")
    read=reader.readlines()
    for i in read:
        i=i.split()
        for j in i:
            list.append(j)
    reader.close()

    index=random.randint(0,len(list)-1)
    thisWord=list[index]
