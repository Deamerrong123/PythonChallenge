from first import firstDuplicate, firstDuplicate2, firstDuplicate3
import timeit
from getData import getData3
import time

a = [2,3,1,4,5,3,4,2]

print(firstDuplicate(a))
print(firstDuplicate2(a))
print(firstDuplicate3(a))
print("------------------")
print("Should print out 3")
print()

b = [1,1,2,2,1]
print(firstDuplicate(b))
print(firstDuplicate2(b))
print(firstDuplicate3(b))
print("-------------------")
print("Shoule print out 1")
print()



c = getData3()
'''
print(c.count(33978))
print()
start = time.time()
print(firstDuplicate(c))
end = time.time()
print(end - start)

start = time.time()
print(firstDuplicate2(c))
end = time.time()
print(end - start)

start = time.time()
print(firstDuplicate3(c))
end = time.time()

print(end - start)
'''
print()

