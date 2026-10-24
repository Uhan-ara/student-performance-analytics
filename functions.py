import numpy as np
import pandas as pd


SUBJECTS = ["Python", "Mathematics", "Data_Analysis", "AI", "Database"]


def calculate_total(marks):
    return int(np.sum(marks))

def calculate_average(marks):
    return round(float(np.mean(marks)), 2)

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"

def check_result(marks, attendance):
    minimum_subject_mark = np.min(marks)

    if minimum_subject_mark >= 40 and attendance >= 75:
        return "Pass"
    else:
        return "Fail"

def add_student_metrics(df):
    result = df.copy()

    result["Total"] = result[SUBJECTS].apply(
        lambda row: calculate_total(row.values),
        axis=1
    )

    result["Average"] = result[SUBJECTS].apply(
        lambda row: calculate_average(row.values),
        axis=1
    )

    result["Grade"] = result["Average"].apply(assign_grade)

    result["Result"] = result.apply(
        lambda row: check_result(
            row[SUBJECTS].values,
            row["Attendance"]
        ),
        axis=1
    )

    return result

def get_class_summary(df):
    summary = {
        "Total Students": len(df),
        "Passed": int((df["Result"] == "Pass").sum()),
        "Failed": int((df["Result"] == "Fail").sum()),
        "Pass Percentage": round(
            (df["Result"] == "Pass").mean() * 100, 2
        ),
        "Class Average": round(df["Average"].mean(), 2),
        "Highest Average": round(df["Average"].max(), 2),
        "Lowest Average": round(df["Average"].min(), 2)
    }

    return summary

def get_subject_analysis(df):
    analysis = []

    for subject in SUBJECTS:
        analysis.append({
            "Subject": subject,
            "Average": round(df[subject].mean(), 2),
            "Highest": int(df[subject].max()),
            "Lowest": int(df[subject].min())
        })

    return pd.DataFrame(analysis)

def get_top_performers(df, n=5):
    top_students = df.sort_values(
        by="Average",
        ascending=False
    ).head(n)

    return top_students[
        ["Student_ID", "Name", "Department", "Average", "Grade", "Result"]
    ]

def get_attendance_analysis(df):
    return {
        "Average Attendance": round(df["Attendance"].mean(), 2),
        "Highest Attendance": int(df["Attendance"].max()),
        "Lowest Attendance": int(df["Attendance"].min()),
        "Students Below 75%": int((df["Attendance"] < 75).sum())
    }

def search_student(df, student_id):
    result = df[
        df["Student_ID"].str.upper() == student_id.upper()
    ]

    return result

