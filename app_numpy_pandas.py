import numpy as np
import pandas as pd

mat = np.arange(0,50).reshape(10,5)

print(mat)

df = pd.DataFrame(data=mat,columns=['A','B','C','D','E'])

print(df)