"""
A Very Simple Student Grade Tracker

Creating a dictionary where keys are student names and values are lists of their test scores
Add a new student, Add a grade for existing student, Calculate average grade for each student
Find the student with highest average
Display all students and their grades in a formatted table
"""

def create_grade_tracker():
    return {}

def add_student(grade_book, student_name):
    if student_name not in grade_book:
        grade_book[student_name] = []
        print(f"Student {student_name} added successfully.")
    else:
        print(f"Student {student_name} already exists.")

def add_grade(grade_book, student_name, grade):
    if student_name in grade_book:
        grade_book[student_name].append(grade)
        print(f"Grade {grade} added for {student_name}.")
    else:
        print(f"Student {student_name} not found.")

def calculate_average(grade_book):
    averages = {}
    for student, grades in grade_book.items():
        averages[student] = sum(grades) / len(grades) if grades else 0
    return averages

def find_highest_average(grade_book):
    averages = calculate_average(grade_book)
    if not averages:
        return None, 0
    return max(averages.items(), key=lambda x: x[1])

def display_grades(grade_book):
    print("\nStudent Grade Report")
    print("-" * 50)
    print(f"{'Student Name':<20} {'Grades':<20} {'Average':<10}")
    print("-" * 50)
    
    averages = calculate_average(grade_book)
    for student, grades in grade_book.items():
        avg = averages[student]
        grades_str = ", ".join(f"{g:.1f}" for g in grades) if grades else "No grades"
        print(f"{student:<20} {grades_str:<20} {avg:.1f}")

# Example usage
def main():
    grade_book = create_grade_tracker()
    
    # Adding students and grades
    add_student(grade_book, "Alice")
    add_student(grade_book, "Bob")
    add_student(grade_book, "Charlie")
    
    add_grade(grade_book, "Alice", 85)
    add_grade(grade_book, "Alice", 90)
    add_grade(grade_book, "Bob", 78)
    add_grade(grade_book, "Bob", 82)
    add_grade(grade_book, "Charlie", 95)
    
    # Display all grades
    display_grades(grade_book)
    
    # Find student with highest average
    top_student, top_avg = find_highest_average(grade_book)
    if top_student:
        print(f"\nTop Student: {top_student} with average {top_avg:.1f}")

if __name__ == "__main__":
    main()
