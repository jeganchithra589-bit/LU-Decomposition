# LU Decomposition 

## AIM:
To write a program to find the LU Decomposition of a matrix.

## Equipments Required:
1. Hardware – PCs
2. Anaconda – Python 3.7 Installation / Moodle-Code Runner

## Algorithm


## Program:
(i) To find the L and U matrix
```
/*
Program to find the L and U matrix.
Developed by: Jegan P
RegisterNumber:21225240061
import numpy as np
from scipy.linalg import lu
matrix=np.array(eval(input()))
p,l,u=lu(matrix)
print(l)
print(u)
*/
```
(ii) To find the LU Decomposition of a matrix
```
/*
Program to find the LU Decomposition of a matrix.
Developed by: Jegan P
RegisterNumber: 212225240061
import numpy as np
from scipy.linalg import lu_factor,lu_solve
matrix=np.array(eval(input()))
constant=np.array(eval(input()))
piv,lu=lu_factor(matrix)
result=lu_solve((piv,lu),constant)
print(result)

*/
```

## Output:
<img width="1920" height="1080" alt="Screenshot (220)" src="https://github.com/user-attachments/assets/95a2b7d6-f857-410c-8dac-9859fc2ee2d8" />

<img width="1920" height="1080" alt="Screenshot (221)" src="https://github.com/user-attachments/assets/4fb751b1-77f3-4231-b045-4429f9b2eb2d" />




## Result:
Thus the program to find the LU Decomposition of a matrix is written and verified using python programming.

