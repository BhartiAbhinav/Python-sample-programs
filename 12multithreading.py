from threading import Thread
import time
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(2)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(2)
t1=Hello()
t2=Hi()
t1.start()
time.sleep(0.5)
t2.start()
time.sleep(0.5)
t1.join()
t2.join()
