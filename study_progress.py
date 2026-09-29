#study progress module for tracking academic progress
def study_progress():
    print("\n===== STUDY PROGRESS =====")

    subjects = []

    number = int(input("How many subjects do you want to track? "))

#collect the subject details
    for i in range(number):
        print("\nSubject",i+1)

        subject = input("Enter subject name: ")
        completed = int(input("Enter completed topics: "))

#validate the completed topics
        while True:
            total = int(input("Enter total topics: "))

            if completed <= total:
                break

            print("Completed topics can't be more than total topics.")

#calculate the percentage of the completed topics
            progress = (completed/total) * 100

#store the subject progress details
            details = [subject,completed,total,progress]
            subjects.append(details)

    print("\n====== STUDY PROGRESS ======")

#display the subject progress
    for details in subjects:
        print("Subject:", details[0])
        print("Completed topics:", details[1])
        print("Total topics:", details[2])
        print("Study Progress:", round(details[3], 2),"%")
        print("---------------------")
              
