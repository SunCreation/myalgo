import test
import stats
import numpy as np
print(stats.means([1,2,3,4,5]))

import numpy as np

# 아래 A와 B는 결과적으로 같은 ndarray 객체를 생성합니다. 
A = np.arange(5)
B = np.array([0,1,2,3,4])  # 파이썬 리스트를 numpy ndarray로 변환

# 하지만 C는 좀 다를 것입니다. 
C = np.array([0,1,2,3,'4'])

# D도 A, B와 같은 결과를 내겠지만, B의 방법을 권합니다. 
D = np.ndarray((5,), np.int32, np.array([0,1,2,3,4]),)



print(A)
print(type(A))
print("--------------------------")
print(B)
print(type(B))
print("--------------------------")
print(C)
print(type(C))
print("--------------------------")
print(D)
print(type(D))

print(np.__version__)