import numpy as np

arr = np.arange(0, 11)
print(arr[8])

print(arr[:])

print(arr[1:5])

print(arr[:5])

print(arr[5:])

# broadcasting

arr[0:5] = 100
print(arr)

r = np.array([[5, 0, 15], [20, 25, 30], [25, 40, 40]])

print(r.shape)

print(r[0])
print(r[2])

print(r[1][1])
# or
print(r[1, 1])

print(r[:2])
print(r[:2, 1:])

# conditional selections
mp = np.arange(1, 11)

print(mp)
print(mp[mp > 4])

print(len(mp))