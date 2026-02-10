# Program to find the L and U matrix.
# Developed by: Jegan P
# RegisterNumber:21225240061
import numpy as np
from scipy.linalg import lu
matrix=np.array(eval(input()))
p,l,u=lu(matrix)
print(l)
print(u)

# Program to find the LU Decomposition of a matrix.
# Developed by: Jegan P
# RegisterNumber: 212225240061
import numpy as np
from scipy.linalg import lu_factor,lu_solve
matrix=np.array(eval(input()))
constant=np.array(eval(input()))
piv,lu=lu_factor(matrix)
result=lu_solve((piv,lu),constant)
print(result)

