import random
a = random.sample(range(1,10),9)
b = random.sample(range(1,10),8)
c = []
if(len(a)>len(b)):
    dl=a
    kr=b
else:
    dl=b
    kr=a   
for liczby in dl:
    if(liczby in kr and liczby not in c):
        c.append(liczby)
print(c)        
        