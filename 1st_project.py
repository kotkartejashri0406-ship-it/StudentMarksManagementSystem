# Project: Student Marks Manager system
# Concepts Used: conditional statements, loops, dictionary
# Description: Calculates average, highest, lowest and pass/fail count.

students = {}

n = int(input("Number of students : "))

if n <= 0:
    print("No students entered.")
else:
    # Input Section
    for i in range(n):
        name = input("Enter student name : ")
        mark = int(input("Enter marks : "))
        students[name] = mark

    # Average, Highest, Lowest
    average = sum(students.values()) / n
    highest = max(students.values())
    lowest = min(students.values())

    # Pass / Fail Count
    pass_count = 0
    fail_count = 0

    for name in students:
        if students[name] >= 35:
            pass_count += 1
        else:
            fail_count += 1

    # Grading System
    A_grade_students = 0
    B_grade_students = 0
    C_grade_students = 0
    D_grade_students = 0

    for name in students:
        mark = students[name]

        if mark >= 90:
            A_grade_students += 1
        elif mark >= 80:
            B_grade_students += 1
        elif mark >= 70:
            C_grade_students += 1
        elif mark >= 60:
            D_grade_students += 1

    # Above / Below Average
    abovethan_average = 0
    belowthan_average = 0

    for name in students:
        if students[name] >= average:
            abovethan_average += 1
        else:
            belowthan_average += 1

    # Topper
    topper = max(students, key=students.get)

    # Output Section
    print("\n----- Report -----")
    print("Average Marks :", average)
    print("Highest Marks :", highest)
    print("Lowest Marks :", lowest)
    print("Topper :", topper, "-", students[topper])

    print("\nNumber of students Passed :", pass_count)
    print("Number of students Failed :", fail_count)

    print("\nA Grade Students :", A_grade_students)
    print("B Grade Students :", B_grade_students)
    print("C Grade Students :", C_grade_students)
    print("D Grade Students :", D_grade_students)

    print("\nStudents >= Average :", abovethan_average)
    print("Students < Average :", belowthan_average)




