import numpy as np
import math	

X=np.random.normal(0.0,1.0,(20,20))
dt=np.dtype('int32')
y =np.random.randint(-2147483648, 2147483647,size=20,dtype=dt)
theta= np.matmul(np.linalg.inv(np.matmul(np.transpose(X),X)),np.matmul(np.transpose(X),y))
print(theta)