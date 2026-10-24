import pandas as pd

from functions import (
    add_student_metrics,
    get_class_summary,
    get_subject_analysis,
    get_top_performers,
    get_attendance_analysis,
    search_student
)


# Load the student dataset
df = pd.read_csv("students.csv")

# Calculate student performance metrics
df = add_student_metrics(df)


print("=" * 60)
print("       STUDENT PERFORMANCE ANALYTICS SYSTEM")
print("=" * 60)

print("\nDataset loaded successfully!")
print(f"Total students: {len(df)}")

while True:
    print("\n" + "=" * 60)
    print("MAIN MENU")
    print("=" * 60)

    print("1. View Student Data")
    print("2. Class Performance Summary")
    print("3. Subject-wise Analysis")
    print("4. Top 5 Performers")
    print("5. Attendance Analysis")
    print("6. Search Student")
    print("7. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        print("\n" + "=" * 60)
        print("\nSTUDENT PERFORMANCE DATA")
        print("=" * 60)
        print(df.to_string(index=False))

    elif choice == "2":
        print("\n" + "=" * 60)
        print("\nCLASS PERFORMANCE SUMMARY")
        print("=" * 60)
        summary = get_class_summary(df)

        for key, value in summary.items():
            print(f"{key}: {value}")

    elif choice == "3":
        print("\n" + "=" * 60)
        print("\nSUBJECT-WISE ANALYSIS")
        print("=" * 60)
        subject_analysis = get_subject_analysis(df)
        print(subject_analysis.to_string(index=False))

    elif choice == "4":
        print("\n" + "=" * 60)
        print("\nTOP 5 PERFORMERS")
        print("=" * 60)
        top_students = get_top_performers(df)
        print(top_students.to_string(index=False))

    elif choice == "5":
        print("\n" + "=" * 60)
        print("\nATTENDANCE ANALYSIS")
        print("=" * 60)
        attendance = get_attendance_analysis(df)

        for key, value in attendance.items():
            print(f"{key}: {value}")

    elif choice == "6":
        student_id = input("\nEnter Student ID: ")

        student = search_student(df, student_id)

        if student.empty:
            print("Student not found.")
        else:
            print("\n" + "=" * 60)
            print("\nSTUDENT PERFORMANCE")
            print("=" * 60)
            print(student.to_string(index=False))

    elif choice == "7":
        print("\nThank you for using the Student Performance Analytics System!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 7.")