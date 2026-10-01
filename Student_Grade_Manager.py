courses = ["Python", "Java", "HTML", "Database"]
for course in courses:
    print(course)

unique_courses = set(courses)
print(unique_courses)

students = {}

def add_student():
    name = input("Enter student name: ")

    try: 
    score = int(input("Enter student score: "))

    if score < 0 or score > 100:
        print("Score must be between 0 and 100")
    else:
        students[name] = score
        print("Student added successfully")

    except ValueError:
        print("Please enter a number for the score")

def get_grade(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

while True:
    # Menu
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
       for name, score in students.items():
            print("Name:", name)
            print("Score:", score)
            print("Grade:", get_grade(score))

    elif choice == "3":
        print("Goodbye")

        break
    else:
        print("Invalid choice")

