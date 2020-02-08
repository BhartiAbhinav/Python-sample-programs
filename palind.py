def palin(a):
    if len(a)<=1:
        return "True"
    else:
        if a[0]==a[-1]:
            return palin(a[1:-1])
        else:
            return "False"

a=input()
print(palin(a))
