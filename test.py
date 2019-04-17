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


# a big numbers list for testing, downloading from the codesignal,
c = getData3()

#print(c.count(33978))
print()
# using the 1st firstDuplicate method,
print("Now is using the first-duplicate method!!!" )
start = time.time()
print(firstDuplicate(c))
end = time.time()
print("The running time is : {} second.".format(end - start))
print("\n")

# using the second firstDuplicate method.
print("Now is using the second first-duplicate mehthod!!")
start = time.time()
print(firstDuplicate2(c))
end = time.time()
print("The running time is : {} second.".format(end - start))
print("\n")


# using the third firstDuplicate method.
print("Now, is using the thrid first-duplicate method!!")
start = time.time()
print(firstDuplicate3(c))
end = time.time()

print("The running time is : {} second.".format(end - start))

print()

