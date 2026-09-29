
from timetable import timetable
from assignment_tracker import assignment_tracker
from study_progress import study_progress
from cgpa_calculator import cgpa_calculator

#display the project title
print("===== ACADEMIC COMPASS =====")
print("Student Schedule,Assignment and progress tracking system")
print("========================================================")

while True:

    print("\n1. Timetable")
    print("2. Assignment tracker")
    print("3. Study Progress")
    print("4. CGPA Calculator")
    print("5. Exit")

#get the user's choice
    choice=int(input("Enter your choice:"))

#display the main menu
    if choice==1:
        print("\nOpening Timetable feature...")
        timetable()

    elif choice==2:
        print("\nOpening Assignment Tracker...")
        assignment_tracker()

    elif choice==3:
        print("Opening Study progess...")
        study_progress()

    elif choice==4:
        print("Opening CGPA Calculator...")
        cgpa_calculator()

    elif choice==5:
        print("Thank you for using Academic Compass !")

    else:
        print("Invalid choice")
