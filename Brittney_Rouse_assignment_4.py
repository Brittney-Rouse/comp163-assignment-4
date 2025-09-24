student_name = "Brittney Rouse"
current_gpa = 4.0
study_hours = 20
social_points = 72
stress_level = 30

print(f"Student Name: {student_name}")
print(f"Starting Stats:")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

student_name = "Brittney Rouse"
current_gpa = 4.0
study_hours = 20
social_points = 72
stress_level = 30

print(f"Student Name: {student_name}")
print(f"Starting Stats:")
print(f"Current GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

print(f"Choose Your Course Load:")
print(f"A: Light (12 credits)")
print(f"B: Standard (15 credits)")
print(f"C: Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "Light":
    if current_gpa <= 2.0:
        stress_level = stress_level + 5
        study_hours = study_hours + 4
    elif current_gpa <= 3.0:
        stress_level = stress_level + 3
        study_hours = study_hours + 3
    elif current_gpa <= 4.0:
        stress_level = stress_level + 2
        study_hours = study_hours + 2
elif choice == "Standard":
    if current_gpa <= 2.0:
        stress_level = stress_level + 7
        study_hours = study_hours + 7
    elif current_gpa <= 3.0:
        stress_level = stress_level + 10
        study_hours = study_hours + 10
    elif current_gpa <= 4.0:
        stress_level = stress_level + 12
        study_hours = study_hours + 12
elif choice == "Heavy":
    if current_gpa <= 2.0:
        stress_level = stress_level + 15
        study_hours = study_hours + 20
    elif current_gpa <= 3.0:
        stress_level = stress_level + 14
        study_hours = study_hours + 18
    elif current_gpa <= 4.0:
        stress_level = stress_level + 14
        study_hours = study_hours + 18
else:
    print("Invalid input.")

print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")

print(f"Stress Level: {stress_level}")
