#time table module to mangae student's time table
def timetable():
    print("===== TIMETABLE =====")

    timetable_list = []

#get the number of subjects from the user
    number = int(input("Hoe many subjects do you have in a day? "))

    for i in range(number):
        print("\nEnter details for subject",i+1)

#collect the subject and class timing details
        subject = input("Enter subject name: ")
        day = input("Enter day: ")
        time = input("Enter class time: ")

        details = [subject,day,time]
        timetable_list.append(details)

    print("\n===== YOUR TIMETABLE =====")

#display the student's time table 
    for details in timetable_list:
        print("Subject:" , details[0])
        print("Day:" , details[1])
        print("Time:" , details [2])
        print("-----------------------")
              
        
                 
