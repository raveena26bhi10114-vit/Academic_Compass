#assignment tracker module for managing assignments
def assignment_tracker():
    print("\n====== ASSIGNMNET TRACKER =====")

    assignments = []

#get the number of assignments
    number = int(input("How many assignmnets do you have? "))

    for i in range(number):
        print("\nAssignment", i+1)

#collect assignment information
        subject = input("Enter subject name: ")
        assignment = input("Enter assignment name: ")
        deadline = input("Enter deadline: ")

        details = [subject,assignment,deadline]
        assignments.append(details)

    print("\n===== YOUR ASSIGNMNETS ======")

#display the assignment details
    for details in assignments:
        print("Subject:", details[0])
        print("Assignment:", details[1])
        print("Deadline:", details[2])
        print("------------------------")
