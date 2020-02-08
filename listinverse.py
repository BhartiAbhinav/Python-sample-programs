def reverse(array):
    n = array
    first = 0
    last = len(array) - 1
    while first < last:
      holder = n[first]
      n[first] = n[last]
      n[last] = holder
      first += 1
      last -= 1
    return n
a=int(input())
n=[]
for i in range(a):
    b=input()
    n.append(b)
print(reverse(n))
