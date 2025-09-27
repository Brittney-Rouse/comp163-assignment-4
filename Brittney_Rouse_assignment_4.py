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
        social_points = social_points + 30
    else:
        career_field = "'Junior Hacker'"
        print("'A junior hacker. You've definitely got some skills, but keep going!'")
        social_points = social_points + 15
elif (user_choice in study_options) and (user_choice == "Math"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Well-Known Engineer'"
        print("'A well-known engineer. You're famous for making things that help your team.'")
        social_points = social_points + 30
    else:
        career_field = "'Average Engineer'"
        print("'While not famous, you're a pretty solid engineer. Get to building!'")
        social_points = social_points + 15
elif (user_choice in study_options) and (user_choice == "English"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Famous Sourcerer'"
        print("'A famous sorcerer! You can easily cast spells, whether against the enemy or to aid your teammates.'")
        social_points = social_points + 30
    else:
        career_field = "'Sourcerer's Apprentice'"
        print("'A sorcerer's apprentice. While you know some spells, there's many more to learn!'")
        social_points = social_points + 15
elif (user_choice in study_options) and (user_choice == "History"):
    if (4.0 >= current_gpa >= 2.5) or social_points > 50:
        career_field = "'Legendary Knight'"
        print("'Wow! You're a legendary knight with a mighty sword. Many enemies fall beneath your blade!'")
        social_points = social_points + 30
    else:
        career_field = "'Scarred Soldier'"
        print("'A soldier scarred from their battles - you're mighty, but you can improve your fighting skills!'")
        social_points = social_points + 15
else:
    print(f"{user_choice} not in study_options")

print(f"Congrats! You've chosen {career_field}.")


user_answer = input("Do you accept this quest to save the world? Yes / No   ")
if user_answer == "Yes":
    if (current_gpa >= 3.0) and (study_hours >= 40) and (social_points >= 55):
        print("You're the best of the best! You'll easily defeat the competition.")
        team_formation = input("Would you like to form a team? Yes/ No   ")
        if team_formation == "Yes":
            print("Alright! Get out there and fight!")
            final_check = True
        else:
            print("A solo adventurer? Well, that won't be a problem for you. Good luck!")
            final_check = True
    elif (current_gpa >= 2.0) and  (study_hours >= 30) and (social_points >= 35):
        print("Alright! You're a solid fighter, so this world won't be very difficult for you.")
        team_formation = input("Would you like to form a team? Yes / No   ")
        if team_formation == "Yes":
            print("Nice! Go get some buddies and fight!!")
            final_check = True
        else:
            print("Are you sure? Teammates are always better in a situation like this. Either way, good luck!")
            final_check = True
    else:
        print("Well, you might want to train more first! At this rate, you'll get destroyed your first day out!")
        final_check = True
elif user_answer == "No":
    if (current_gpa >= 3.0) and (study_hours >= 40) and (social_points >= 55):
        print("Oh... Are you sure? We could really use you out there! You're a powerhouse")
        second_choice = input("Are you sure you don't want to go on the quest? Yes / No   ")
        if second_choice == "Yes":
            print("Oh. Okay then. Have fun not saving the world...")
            final_check = True
        elif second_choice == "No":
            print("Oh boy! Really?! Thank you so much!!")
            print("You're the best of the best! You'll easily defeat the competition.")
            team_formation = input("Would you like to form a team? Yes/ No   ")
            if team_formation == "Yes":
                print("Alright! Get out there and fight!")
                final_check = True
            else:
                print("A solo adventurer? Well, that won't be a problem for you. Good luck!")
                final_check = True
    elif (current_gpa >= 2.0) and (study_hours >= 30) and (social_points >= 35):
        print("Oh... Are you sure? We could really use you out there! You're a powerhouse!")
        second_choice = input("Are you sure? Yes / No   ")
        if second_choice == "Yes":
            print("Really? But you'd be so good out there...")
            final_check = True
        elif second_choice == "No":
            print("Alright! I knew you really wanted to go.")
            print("You're a solid fighter, so this world won't be very difficult for you.")
            team_formation = input("Would you like to form a team? Yes/ No   ")
            if team_formation == "Yes":
                print("Nice! Go get some buddies and fight!!")
                final_check = True
            else:
                print("Are you sure? Teammates are always better in a situation like this. Either way, good luck!")
                final_check = True
    else:
        print("Well, that's alright. You seem like you need more training anyway! We'll check back up on you in a year or so. Good luck out there!")
        final_check = True
else:
    print("Invalid Choice")
    final_check = False


#ChatGPT helped me realize I could use "is" here! :) I knew I needed to put an "is" somewhere, but I just
#couldn't think of a spot. Thankfully, it recommended this!
if final_check is True:
    print(f"Final Stats:")
    print(f"Current GPA: {current_gpa}")
    print(f"Study Hours: {study_hours}")
    print(f"Social Points: {social_points}")
    print(f"Stress Level: {stress_level}")
elif final_check is not True:
    print("Try again.")