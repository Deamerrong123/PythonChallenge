from first import firstDuplicate
import timeit
from getData import getData
import time

a = [2,3,1,4,5,3,4,2]

print(firstDuplicate(a))
print("------------------")
print("Should print out 4")
print()

b = [1,1,2,2,1]
print(firstDuplicate(b))
print("-------------------")
print("Shoule print out 1")
print()



c = getData()
start = time.time()
firstDuplicate(c)
end = time.time()
print(end - start)

print()

