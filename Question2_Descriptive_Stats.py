import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
# load csv in
df = pd.read_csv("data.csv", header=None)

df.plot(x=0, y=1)
print("Data Appears to not be trending in any direction, value has no correlation to index")
plt.show()

print("Data's Distribution Appears to be symmetrical and unimodal")
df[1].plot.hist(bins=20)
plt.show()

print("Descriptive Statistics about the data:")
med = df[1].quantile(0.5)
print("     Average/Mean is:            " + str(df[1].mean()))
print("     Median is:                  " + str(med))
print("     Mode is:                  " + str(df[1].value_counts().idxmax()))

print("     Standard deviation is:       " + str(df[1].std()))
print("     Variance is:                " + str(df[1].var()))
print("     Minimum is:                " + str(df[1].min()))
print("     Maximum is:                " + str(df[1].max()))
print("     Quantile Data (25-50-75):")
Q1 = df[1].quantile(0.25)
Q3 = df[1].quantile(0.75)
print("             0.25    " + str(Q1))
print("             0.5    " + str(med))
print("             0.75    " + str(Q3))
print("     Inter Quantile Range (IQR) is:  " + str(Q3-Q1))
