#array with pyhton and big o notaion'
 #list is called array in python
    #array is a collection of similar data types
List=[10,20,30,40]

# time complexity of append operation in list is O(1)
List.append(50) #Time  complexity of append operation in list is O(1)
print(List)

#ACCESSING LIST ELEMENT
#ACCES ANY ELEMENT
print(List[2]) #O(1)
#accessing from the 2nd last element
print(List[-2]) #O(1)

#insert at any index in list
List.insert(2,100) #O(n)
print(List)

# delete an element
List.remove(50)
print(List)
del List[2] #O(n)

#iterate in a list or traverse

for  i in range(len(List)):
      print(List[i]) #O(n)

#search in a list
if 60 in List:
      print("yes")
else:
      print("no")
