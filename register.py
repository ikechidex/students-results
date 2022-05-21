from students import student

name = input("\nEnter name for new student: ")
age = input("\nEnter age for new student: ")
gender = input("Enter student gender: ")

test_student = student(name, age, gender)
print(f"Welcome to TechApprentice Academy.\n--------------\n FINA RESULT SHEET.\n-------------\n Student Name: {test_student.name}.\n Student Age: {test_student.age}.\n Student Gender: {test_student.gender}")

test_student.enter_score()

print(f"\nSubjects for {test_student.name} are:\n{test_student.subjects}")
