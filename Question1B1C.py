import pandas as pd
import pandasql as ps

# Question 1 B
name_table = {'StudentID': ['V001', 'V002', 'V003', 'V004'], 'Name': ['Abe', 'Abhay', 'Acelin', 'Adelphos']}
mark_table = {'StudentID': ['V001', 'V002', 'V003', 'V004'], 'Total_marks': [95, 80, 74, 81]}
name_table_df = pd.DataFrame(data=name_table)
mark_table_df = pd.DataFrame(data=mark_table)
def capOrLowerOnE(string):
    if 'e' in string or 'E' in string:
        return string.upper()
    return string.lower()

name_table_df['Name'] = name_table_df['Name'].apply(lambda x: capOrLowerOnE(x))
print("New name_table DataFrame is:")
print(name_table_df)

# Question 1 C

def avg_q(df_name):
    return "select AVG(Total_marks) FROM mark_table, " + df_name + " WHERE mark_table.StudentID = "+df_name+".StudentID"

def avgGradeUppercaseLowercase(name_table, mark_table):
    upper_q = """ select * from name_table where upper(Name) = Name """
    lower_q = """ select * from name_table where lower(Name) = Name """
    lower_df = ps.sqldf(lower_q)
    upper_df = ps.sqldf(upper_q)

    lower_avg = ps.sqldf(avg_q("lower_df")).at[0, 'AVG(Total_marks)']
    upper_avg = ps.sqldf(avg_q("upper_df")).at[0, 'AVG(Total_marks)']
    avg_dataframe = pd.DataFrame(data={'type_of_name': ['Uppercase', "Lowercase"], 'average_grade': [upper_avg, lower_avg]})
    return avg_dataframe;
print("\n\nDataFrame of average grades is:")
print(avgGradeUppercaseLowercase(name_table_df, mark_table_df))

