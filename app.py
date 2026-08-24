def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"

if __name__ == "__main__":
    marks = 82
    print("Marks:", marks)
    print("Grade:", calculate_grade(marks))