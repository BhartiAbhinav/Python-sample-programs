import threading
import time


class myThread (threading.Thread):
   def __init__(self, threadID, name, counter):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
   def run(self):
      print("Starting " + self.name)
      threadLock.acquire()
      print_time(self.name,  self.counter,1)
      threadLock.release()
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      time.sleep(delay)
      print("%s: %s  %s"  % (threadName, time.ctime(time.time()),counter))
      counter -= 1

threadLock=threading.Lock()

# Create new threads
thread1 = myThread(1, "Payment", 5)
thread2 = myThread(2, "payment confirmation", 5)

# Start new Threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting Main Thread")
