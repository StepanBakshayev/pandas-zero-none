import numpy as np
import pandas as pd 

df = pd.DataFrame([[np.nan, 2, np.nan, 0], 
                    [3, 4, np.nan, 1], 
                    [np.nan, np.nan, np.nan, 5], 
                    [np.nan, 3, np.nan, 4]], 
                    columns=list('ABCD'))
print(df)
"""
In [8]: df
Out[8]: 
     A    B   C  D
0  NaN  2.0 NaN  0
1  3.0  4.0 NaN  1
2  NaN  NaN NaN  5
3  NaN  3.0 NaN  4
"""

df_zero_c = df.fillna(value={'C': 0})
print(df_zero_c)
"""
Out[9]: 
     A    B    C  D
0  NaN  2.0  0.0  0
1  3.0  4.0  0.0  1
2  NaN  NaN  0.0  5
3  NaN  3.0  0.0  4
"""