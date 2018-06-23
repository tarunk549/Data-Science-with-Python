# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import pandas as pd

path = '../resources/'

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file + path, sep='\t', comment='#', na_values=['NA', 'NaN', "Nothing"])

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()