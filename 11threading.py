from _thread import start_new_thread as tdd
import time
def func(i):
    fact = 1
    while(i>0):
        fact=fact*i
        i-=1
    print(fact)
tdd(func,(1,))
time.sleep(0.5)
tdd(func,(2,))
time.sleep(0.5)

tdd(func,(3,))
time.sleep(0.5)

tdd(func,(4,))
time.sleep(0.5)
input()
