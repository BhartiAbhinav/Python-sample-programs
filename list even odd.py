def func(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd
mylist=[10,2,34,56,78,34,65,76,23,45,67,90]
e,o=func(mylist)
print("Even={} and Odd={}".format(e,o))