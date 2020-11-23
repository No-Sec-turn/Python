#test21.py

import numpy as np

a1 = np.array([0,1,2,3,4,5])
print(a1)
print(a1.dtype)

a2 = np.array([0.5,1,0.0001,3,4,5])
print(a2)
print(a2.dtype)

a3=np.arange(0,11,2)
print(a3)
print(a3.shape)

a4 = np.arange(12).reshape(4,3)
print(a4)

#문자를 숫자로 변환
str1 = np.array(['1.567', '5.123', '9','8'])
str1.astype(float)

print(str1.dtype)