a=input()
b=input()
alen=0
blen=0
r=0
for i in a:
    alen=alen+1
for i in b:
    blen=blen+1
if alen==blen:
    for i in a:
        for j in b:
            if i==j:
                r=r+1
    if r==alen:
        print("True")
    else:
        print("false")
else:
    print("flase")
