from random import randint as random
import sys
tangdata=[]
for l in open("data.txt",encoding="utf-8").readlines():
    tangdata.append(l.replace("\n","").split(" = "))
moto=open(sys.argv[1],"r",encoding="utf-8").read()
data=moto.split(" ")
f=open("japanese-"+sys.argv[1],"w",encoding="utf-8")
asss=0
for i in data:
    for j in tangdata:
        if(i==j[1]):
            f.write(j[0])
            break
        