import numpy as np
import pandas as pd

print(np.random.seed(101))

mat = np.random.randint(1,101,(100,5))
print(mat)

df = pd.DataFrame(mat)
print(df)

df.columns = ['f1','f2','f3','f4','label']

print(df)

random_numbers = np.random.randint(0,20,(50,4))
col_names=['A','B','C','D']

df = pd.DataFrame(data=random_numbers,columns=col_names)

print(df)
