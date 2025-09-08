"""
Ask user for their score (0-100)
Assign letter grades: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
Provide encouraging messages based on the grade
Handle invalid input (scores outside 0-100 range)
"""
def calculate_grade():
    try:
        # Get score from user
        score = int(input("Enter your score (0-100): "))
        
        # Check if score is within valid range
        if score < 0 or score > 100:
            print("Invalid input! Score must be between 0 and 100.")
            return
        
        # Determine grade and message
        if score >= 90:
            grade = 'A'
            message = "Excellent work! You're killing it!"
        elif score >= 80:
            grade = 'B'
            message = "Great job! Keep up the solid performance!"
        elif score >= 70:
            grade = 'C'
            message = "Good effort! A bit more practice will boost your score!"
        elif score >= 60:
            grade = 'D'
            message = "You passed, but let's work on getting that score up!"
        else:
            grade = 'F'
            message = "Don't give up! Let's review and try again!"
        
        # Output results
        print(f"Your grade is: {grade}")
        print(message)
    
    except ValueError:
        print("Invalid input! Please enter a number.")

# Run the calculator
calculate_grade()

