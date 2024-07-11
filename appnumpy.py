import numpy as np

mylist = [1,2,3,4]
np.array(mylist)

print(mylist)
print(type(mylist))

arr = np.array(mylist)
print(type(arr))
print(arr)

a = np.arange(0,10)
print(a)

a = np.arange(0,10,2)
print(a)

print(np.zeros((5,5)))
print(np.zeros((1,5)))
print(np.ones((2,5)))

print(np.random.randint(1,60,(3,3)))

print(np.linspace(1,20,30))

print(np.random.seed(101))
print(np.random.randint(0,100,10))
print(np.random.randint(0,100,10))

arr=np.random.randint(0,100,10)

print(arr)

print("Max:: ",arr.max(),"Min:: ",arr.min(),"Mean:: ",arr.mean(),"ArgMax:: ",arr.argmax(),"ArgMin:: ",arr.argmin())

print(arr.reshape(5,2))

mat = np.arange(0,100).reshape(10,10)
print(mat)

print(mat[5,2])

print(mat[:,2])

print(mat[2,:].reshape(2,5))

print(mat[mat > 50])