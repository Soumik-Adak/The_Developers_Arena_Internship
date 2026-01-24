
def get_grade_and_message(marks: int) -> tuple[str, str]:
    """Return (grade, message) based on marks."""
    if 90 <= marks <= 100:
        return "A", "Outstanding work! You’re mastering the material. 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very good! Keep it up and aim even higher. 👍"
    elif 70 <= marks <= 79:
        return "C", "Good effort—review a few topics and you’ll level up. 💪"
    elif 60 <= marks <= 69:
        return "D", "You’re close—focus on weak areas and practice more. 📚"
    else:  # 0–59
        return "F", "Don’t be discouraged—seek help, revise, and try again. 🚀"

def get_valid_marks() -> int:
    """Prompt until a valid integer in 0–100 is entered."""
    while True:
        raw = input("Enter marks (0-100): ").strip()
        if not raw.isdigit():
            print("Please enter a whole number between 0 and 100.")
            continue
        marks = int(raw)
        if 0 <= marks <= 100:
            return marks
        print("Marks must be between 0 and 100. Try again.")

def main():
    name = input("Enter student name: ").strip()
    marks = get_valid_marks()
    grade, message = get_grade_and_message(marks)

    print(f"\n📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()