#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df=pd.read_csv("dataset.csv")
print(df)


# In[4]:


import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))
plt.plot(df.index, df['SGPA'], marker='o', linestyle='-', color='b', label='SGPA')

plt.xlabel("Sl No")
plt.ylabel("SGPA")
plt.title("Sl No vs SGPA")
plt.legend()
plt.grid(True)
plt.show()


# In[6]:


import pandas as pd

# Drop NaN rows (if not already done)
df = df.dropna().reset_index(drop=True)

# Mean
mean_sgpa = df['SGPA'].mean()

# Mode (can return multiple values if there are ties)
mode_sgpa = df['SGPA'].mode()

# Standard Deviation
std_sgpa = df['SGPA'].std()

print("Mean SGPA:", mean_sgpa)
print("Mode SGPA:", mode_sgpa.values)  # .values to see actual values
print("Standard Deviation of SGPA:", std_sgpa)



# In[4]:


import pandas as pd

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Age': [25, 37, 'NaN', 29, 42, 55, 23, 29, 'NaN', 45],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Income': [50000, 62000, 45000, 54000, 'NaN', 100000, 52000, 70000, 200000, 85000],
    'Occupation': ['Engineer', 'Data Scientist', 'NaN', 'Product Manager', 'Sales', 'Executive', 'NaN', 'Product Manager', 'NaN', 'Executive'],
    'Years Employed': [2, 5, 3, 'NaN', 8, 30, 1, 6, 15, 'NaN'],
    'Satisfaction Level': [0.8, 'NaN', 0.6, 0.7, 0.5, 0.9, 0.4, 0.7, 0.9, 'NaN'],
    'Purchase History': ['High', 'Medium', 'Low', 'High', 'Low', 'High', 'Medium', 'High', 'Low', 'High']
}

df = pd.DataFrame(data)
df = df.replace('NaN', pd.NA)
display(df)


missing_values_isnull = df.isnull()
non_missing_values_notnull = df.notnull()

display(missing_values_isnull)
display(non_missing_values_notnull)


# In[ ]:




