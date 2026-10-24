# Student Performance Analytics System

A Python-based Student Performance Analytics System that analyzes student academic performance using NumPy and Pandas.

The system processes student marks and attendance data to calculate individual performance metrics, assign grades, determine pass/fail status, and generate class-level and subject-wise performance insights.

## Project Objective

The objective of this project is to develop a simple and practical student performance analytics system using Python programming fundamentals, NumPy, and Pandas.

The system is designed to:

- Calculate total and average marks for each student
- Assign grades based on average performance
- Determine Pass/Fail status using marks and attendance
- Analyze overall class performance
- Perform subject-wise analysis
- Identify top-performing students
- Analyze attendance
- Search for individual student performance

## Technologies Used

- Python
- NumPy
- Pandas

## Python Concepts Used

- Variables and data types
- Conditional statements
- Loops
- Functions
- Lists and dictionaries
- File handling
- Data processing
- Data analysis

## Dataset

The project uses a CSV dataset named `students.csv` containing performance information for 25 students.

The dataset includes the following fields:

| Column | Description |
|---|---|
| Student_ID | Unique ID assigned to each student |
| Name | Student name |
| Department | Student's department |
| Attendance | Attendance percentage |
| Python | Python subject marks |
| Mathematics | Mathematics subject marks |
| Data_Analysis | Data Analysis subject marks |
| AI | Artificial Intelligence subject marks |
| Database | Database subject marks |

The dataset contains realistic student records across the CSE, IT, and ECE departments.

## Implementation

The system is implemented using reusable Python functions to keep the code organized and easy to maintain.

### 1. Data Loading

The `students.csv` file is loaded into a Pandas DataFrame using `pd.read_csv()`.

### 2. Performance Calculation

For every student, the system calculates:

- **Total Marks** — sum of marks across all five subjects
- **Average Marks** — mean of marks across all five subjects
- **Grade** — assigned according to the student's average
- **Result** — determined using subject marks and attendance

### 3. Grading System

The grading rules used in the project are:

| Average Marks | Grade |
|---:|:---:|
| 90–100 | A+ |
| 80–89.99 | A |
| 70–79.99 | B |
| 60–69.99 | C |
| 50–59.99 | D |
| Below 50 | F |

### 4. Pass/Fail Rule

A student is marked **Pass** only when:

- Every subject mark is at least 40
- Attendance is at least 75%

Otherwise, the student is marked **Fail**.

### 5. Class Analysis

The system calculates:

- Total number of students
- Number of passed students
- Number of failed students
- Pass percentage
- Class average
- Highest average
- Lowest average

### 6. Subject-wise Analysis

For each subject, the system calculates:

- Average marks
- Highest marks
- Lowest marks

### 7. Top Performers

The system sorts students according to their average marks and displays the top five performers.

### 8. Attendance Analysis

The system calculates:

- Average attendance
- Highest attendance
- Lowest attendance
- Number of students below 75% attendance

### 9. Student Search

Users can search for an individual student using their Student ID and view their complete performance record.

## Key Features

- Reads student data from a CSV file
- Uses Pandas for data loading and analysis
- Uses NumPy for numerical calculations
- Calculates total and average marks
- Automatically assigns grades
- Determines Pass/Fail status
- Generates class performance statistics
- Performs subject-wise analysis
- Displays the top five performers
- Analyzes student attendance
- Allows searching for a student by Student ID
- Provides an interactive command-line menu

## Project Structure

```text
student-performance-analytics/
│
├── main.py
├── functions.py
├── students.csv
├── test_functions.py
├── README.md
└── requirements.txt
```

## How to Run

### 1. Install the required libraries

Open a terminal in the project folder and run:

```bash
python -m pip install pandas numpy
```

## Results

The system successfully processes the student dataset and generates the following types of analysis:

- Individual student total and average marks
- Grade and Pass/Fail status
- Overall class performance summary
- Subject-wise average, highest, and lowest marks
- Top five performers
- Attendance statistics
- Individual student performance through Student ID search

The application processes 25 student records from the dataset and presents the analysis through an interactive command-line menu.

## Challenges and Learning

### Challenges

- Designing reusable functions for different performance calculations
- Handling multiple student records using Pandas DataFrames
- Applying conditions for grade and Pass/Fail classification
- Combining NumPy calculations with Pandas data processing
- Organizing the project into separate Python files
- Testing the application and checking different menu options

### Learning Outcomes

Through this project, I gained practical experience in:

- Python functions, loops, and conditional statements
- NumPy numerical operations
- Pandas DataFrames and data analysis
- Reading and processing CSV files
- Creating reusable and structured Python code
- Performing basic student performance analysis
- Testing and organizing a Python project
- Preparing a project for GitHub submission

## GitHub Repository

GitHub repository link will be added after the project is uploaded.