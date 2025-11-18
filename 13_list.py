#   LIST
#   -> collection of ordered element
#   -> mutable
#   -> heterogeneous
#   -> allow duplicates

my_list1 = []       # empty list
my_list2 = [1]      # one element
my_list3 = [1,'a',2.5,3+4j]     # many element
my_list4 =[1,[1,2],[2,3]]       # nested list

#  Indexing or Accessing elements from list
# 1. positive indexing
a = [1,2,[1,2],(3,4),{3,4,5},{1:2,2:3,3:4}]
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

# 2. negative indexing
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])

# list slicing
print(a[:])
print(a[:len(a)])
print(a[0:])
print(a[0:3])       # start include end excluding
print(a[::-1])      # gives reverse string
print(a[0:4:2])     # every alternative element

#  modify list by using indexing
a[1] = 'a'          # replace element present at index 1 by 'a'
print(a)
a[0:2] = ['ac','ad']    # replace element in slicing
print(a)

# methods
a = [12,1,34,23,45,6,75,8,9,34]
b = list("neeta")       # list constructor also used to create list
print(b)
a.reverse()
print(a)
a.sort()
print(a)
print(a.count(34))
print(len(a))

#insert element in list
a.append(1)     # insert at end 
print(a)

a.insert(2,10000)   # insert at a specific index(index,value)
print(a)

a.extend('nit')
print(a)        # insert iterable datatype to end of list

# remove element from last

a.remove(1)   # remove specified element but if more than 1 then remove first occurance
print(a)

a.pop()   # remove last element and return the element
print(a)

a.pop(2)    # remove element present on that index
print(a)   

del a[2]    #del keyword is used to delete element present at that index
print(a)

print(b)
del b       # del use to delete whole list

c =[1,2,3,4,5]
print(c)
c.clear()   # it clear all element from list
print(c)

# Copy the list
a =[1,2,3,4,5]
b = a   # b only gives the refernce to a if modify a then b also changes

c = list(a)     # using list constructor

d = a[:]        # using slice operator

e = a.copy()

print(a)
print(b)
print(c)
print(d)
print(e)
print("-----------------------------")
a.append(6)
print(a)
print(b)
print(c)
print(d)
print(e)