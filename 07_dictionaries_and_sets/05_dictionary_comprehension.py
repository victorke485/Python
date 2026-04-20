import random
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}
# new_dict = {new_key:new_value for (key,value) in dict.items() if items}

names = ["Alex", "Ann", "Brian", "Victor", "James"]
student_score = {name:random.randint(1, 100) for name in names}
print(student_score)

passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
print(passed_students)