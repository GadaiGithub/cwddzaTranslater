from random import randint as random
import MeCab,sys
tangdata=[]
for l in open("data.txt",encoding="utf-8").readlines():
    tangdata.append(l.replace("\n","").split(" = "))
moto=open(sys.argv[1],"r",encoding="utf-8").read()
print(moto)
data=MeCab.Tagger("-Owakati").parse(moto).split(" ")
f=open("translate-"+sys.argv[1],"w",encoding="utf-8")
for i in data:
    for j in tangdata:
        if(j[0]==i):
            f.write(f"{j[1]} ")
            break
        