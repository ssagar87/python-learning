#task1

student_name = input("Enter student name:")
student_marks_dict = {
    "Ritik Singh": 85,
    "Ram Krishna": 99,
    "Ravi Kumar": 78,
    "Rahul Sharma": 92
}

# Check if student exists
if student_name in student_marks_dict:
    print(f"{student_name}'s: {student_marks_dict[student_name]}")
else:
    print(f"{student_name} not found")


#task 2

number_List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = number_List[0:5]
print("Extracted first five elements:",first_five)

reversed_list = first_five[::-1]
print("Reversed extracted elements:",reversed_list)

