import numpy as np
np.ndarray
array=np.arange(0,20,2)
print(array)

zeros=np.zeros(shape=(6,4))
print(zeros)
ones=np.ones(shape=(3,6))
print(ones)

np.random.seed(101)  # not return same value
rand=np.random.randint(10,100,12)
print(rand)
print(rand.max())
print(rand.argmax())
print(rand.mean())
rand=rand.reshape((3,4))
print(rand)
print(rand[:,2]) # 2.column
print(rand[1:3,2:4]) # wanted part  on matrix
cop=rand.copy()
cop[0:2,:]=333
print(cop)
print(rand)


