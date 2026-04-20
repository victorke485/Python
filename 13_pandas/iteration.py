import pandas as pd

student_dict = {
    "student": ["Alex", "Amani", "Victor"],
    "score": [78, 34, 90]
}

student_data_frame = pd.DataFrame(student_dict)
# print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)