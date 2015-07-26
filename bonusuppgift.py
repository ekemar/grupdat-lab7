#encoding: utf-8
from queue import Queue
import random
import math

queue = Queue()
buckets = []
 
for _ in range(10):
    buckets.append(Queue())
#print(buckets)
m = 200 #number of numbers
n = 5 #highest number will be 10**n
orignalSeq = []

for _ in range(m):
   number = random.randint(0, 10**n-1)
   orignalSeq.append(number)
   queue.put(number)
print("Vi börjar med ordningen:", orignalSeq)

for i in range(0, n):
    #1
    while not queue.isempty():
        x = queue.get()
        #print("queue.get ger", x)
        y  = int(x / 10**i)
        k = y % 10
        buckets[k].put(x)
        
    #2
    for bucket in buckets:
        while not bucket.isempty():
            x = bucket.get()
            queue.put(x)

finalSeq = []
while not queue.isempty():
    finalSeq.append(queue.get())
print()
print("Vi har sorterat talen, kolla!", finalSeq)
