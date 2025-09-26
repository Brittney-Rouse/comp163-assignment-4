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


study_options = ["Programming", "Math", "English", "History"]

print("Choose your choice of study! This will affect you down the line...")
print(f"{study_options}")
user_choice = input()
career_field = ""

#ChatGPT helped me better organize this if-else statement. (I had accidentally made it one big
#if-statement under "if user_choice in study_options:"), as well as with indention.

if (user_choice in study_options) and (user_choice == "Programming"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Famous Hacker'"
        print("'You're a famous hacker! You're well known for how excellent your coding is.'")
    else:
        career_field = "'Junior Hacker'"
        print("'A junior hacker. You've definitely got some skills, but keep going!'")
elif (user_choice in study_options) and (user_choice == "Math"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Well-Known Engineer'"
        print("'A well-known engineer. You're famous for making things that help your team.'")
    else:
        career_field = "'Average Engineer'"
        print("'While not famous, you're a pretty solid engineer. Get to building!'")
elif (user_choice in study_options) and (user_choice == "English"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Famous Sourcerer'"
        print("'A famous sorcerer! You can easily cast spells, whether against the enemy or to aid your teammates.'")
    else:
        career_field = "'Sourcerer's Apprentice'"
        print("'A sorcerer's apprentice. While you know some spells, there's many more to learn!'")
elif (user_choice in study_options) and (user_choice == "History"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Legendary Knight'"
        print("'Wow! You're a legendary knight with a mighty sword. Many enemies fall beneath your blade!'")
    else:
        career_field = "'Scarred Soldier"
        print("'A soldier scarred from their battles - you're mighty, but you can improve your fighting skills!'")
else:
    print(f"{user_choice} not in study_options")

print(f"Congrats! You've chosen {career_field}.")