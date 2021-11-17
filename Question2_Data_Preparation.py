import pandas as pd
# import seaborn as sns
# load csv in
df = pd.read_csv("2017.csv")

# Discover identify shape of data
print(df.shape)

# Discover which datapoints have missing value
print("\nNull entries per Category:")
print(df.apply(lambda x: sum(x.isnull()),axis=0) )

# Print any datapoints with null values,
print("\nPrinting Entries that had null values")
print(df[df.isnull().any(axis=1)])

# I notice that a manual error occured in entering the data for these 2 points, so I manually alter the values at this point
print("\n\nFixing discovered data entry error")
# Fix 1st null value error
df.at[350, 'PAY BASIS'] = "Per Annum"
df.at[350, 'POSITION TITLE'] = "DIRECTOR OF SPECIAL PROJECTS FOR CORRESPONDENCE"
# Fix 2nd null value error
df.at[250, 'PAY BASIS'] = "Per Annum"
df.at[250, 'POSITION TITLE'] = "Annum SPECIAL ASSISTANT"

# OPTIONAL: Display fixed error
# print(df.loc[350])
# print(df.loc[250])

print("Null entries per Category:")
print(df.apply(lambda x: sum(x.isnull()),axis=0) )
# Error is now fixed

# Encoding Categorical variables
print("\n\nFinding Value Counts of categories, encoding if it seems appropriate")
print("\nSTATUS")
print(df['STATUS'].value_counts())
print("\nPAY BASIS")
print(df['PAY BASIS'].value_counts())

# Encoding STATUS as 0 for detailee, 1 for employee
df = pd.get_dummies(df, columns=['STATUS'], drop_first=True)
# Encoding PAY BASIS by 1 being Per Annum
df = pd.get_dummies(df, columns=['PAY BASIS'])
# Convert Sallary to float Value
df['SALARY'] = df['SALARY'].replace('[\$,]', '', regex=True).astype(float)

#Preview new encoding
print("\nSample of the encoding of the data")
print(df.head(5))
