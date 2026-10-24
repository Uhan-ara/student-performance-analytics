import pandas as pd

from functions import add_student_metrics


# Load the student dataset
df = pd.read_csv("students.csv")

# Calculate Total, Average, Grade and Result
df = add_student_metrics(df)

# Display the first 5 students
print(df.head())