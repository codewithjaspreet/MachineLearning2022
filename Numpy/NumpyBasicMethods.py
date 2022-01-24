# Important Numpy Methods

import numpy as np

mylist = [1, 2, 3]
print(type(mylist))

myArr = np.array(mylist)

print(type(myArr))

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(np.array(my_matrix))

print(np.arange(0, 10, 2))

print(np.zeros(5))

print(np.zeros((2, 5)))

print(np.ones((4, 4)))

print(np.ones(5))

print(np.linspace(0, 10, 3))  # gives evenly spaced numbers & diff from arrange

print(np.eye(5))

print(np.random.rand(1))
print(np.random.rand(5, 6))

print(np.random.randn(10))
print(np.random.randn(10))

print(np.random.randint(0, 101, 5))
print(np.random.randint(0, 101, (4, 5)))

print(np.random.seed(42))
print(np.random.rand(4))

arr = np.arange(0,25)
arr.reshape(5,4)


randArr = np.random.randint(0, 101, 10)
randArr.max()

randArr.min()

randArr.argmax()

randArr.argmin()

var = randArr.dtype

arr.shape

arr = arr.reshape(5,5)

arr.shape


