#cgpa_calculator module to calculate the cgpa
def cgpa_calculator():
    print("\n===== CGPA CALCULATOR =====")

#grade points table
    grade_points = {
        "S": 10,
        "A": 9,
        "B": 8,
        "C": 7,
        "D": 6,
        "E": 5,
        "F": 0,
        "N": 0
    }

    print("S = 10")
    print("A = 9")
    print("B = 8")
    print("C = 7")
    print("D = 6")
    print("E = 5")
    print("F/N = 0")

#get the number of subjects
    number =int(input("\nHow many subjects do you have? "))

    total_points = 0

    for i in range(number):
        print("\nSubject", i + 1)

#get the subject name
        subject = input("Enter subject name: ")

#calculate the average grade point 
        while True:
            grade = input("Enter grade: ").upper()
            if grade in grade_points:
                break
            print("Invalid grade. Try S, A, B, C, D, E, F or N.")

        point = grade_points[grade]
        total_points = total_points + point

        print(subject, "Grade:", grade)
        print(subject, "Grade Point:", point)

    cgpa = total_points / number

#display the calculated cgpa
    print("\n===== CGPA RESULT =====")
    print("Total Grade Points:", total_points)
    print("Your CGPA:", round(cgpa, 2))
