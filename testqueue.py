#encoding: utf-8
#from queue import Queue
from node import Queue

mening = input("Skriv en mening: ")

myq = Queue()
for ordet in mening.split():  # dela upp meningen i ord
    myq.put(ordet)            # och sätt in varje ord i kön

while not myq.isempty():      # alla element tas ut ur kön
    print(myq.get())          # och skrivs ut

print()                       # tom rad
print(myq.get())              # None skrivs ut eftersom kön är tom
