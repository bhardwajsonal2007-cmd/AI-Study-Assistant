print("AI STUDY ASSISTANT")

name = input("Enter your name: ")
print("Hello", name)

study_hours = int(input("Enter study hours: "))
marks = int(input("Enter your marks: "))
attendance = int(input("Enter attendance: "))

print("\n--- STUDENT REPORT ---")
print("Name:", name)
print("Study Hours:", study_hours)
print("Marks:", marks)
print("Attendance:", attendance)

percentage = marks

if percentage >= 75:
    grade = "Distinction"
elif percentage >= 60:
    grade = "First Class"
elif percentage >= 40:
    grade = "Pass"
else:
    grade = "Fail"

print("Percentage:", percentage)
print("Grade:", grade)

if attendance < 75:
    print("Warning: Attendance is below 75%")
else:
    print("Attendance is good")

print("Keep studying!")
print("\n--- AI RECOMMENDATION ---")

if marks < 40:
    print("Focus more on your studies and practice daily.")
elif marks < 60:
    print("You need more practice. Try studying for 2-3 hours daily.")
elif marks < 75:
    print("Good progress! Increase your study time and revise regularly.")
else:
    print("Excellent performance! Keep revising and maintain consistency.")

if study_hours < 2:
    print("Recommendation: Increase your daily study hours.")
elif study_hours >= 4:
    print("Great! You are giving enough time to your studies.")
    print("\n--- SUBJECT MARKS ---")

maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
ml = int(input("Enter ML marks: "))

print("\nSubject Performance:")
print("Maths:", maths)
print("Python:", python)
print("ML:", ml)
print("\n--- FOCUS SUBJECT ---")

if maths <= python and maths <= ml:
    print("Focus more on Maths.")
elif python <= maths and python <= ml:
    print("Focus more on Python.")
else:
    print("Focus more on ML.")
    print("\n--- STUDY PLAN ---")

if maths <= python and maths <= ml:
    print("Spend extra time on Maths today.")
elif python <= maths and python <= ml:
    print("Spend extra time on Python today.")
else:
    print("Spend extra time on ML today.")

if study_hours < 2:
    print("Suggested study time: 2-3 hours")
elif study_hours < 4:
    print("Suggested study time: 3-4 hours")
else:
    print("Suggested study time: 4+ hours")
    print("\n--- REVISION REMINDER ---")

if maths < 60:
    print("Revise Maths today.")
    
if python < 60:
    print("Revise Python today.")

if ml < 60:
    print("Revise ML today.")

if maths >= 60 and python >= 60 and ml >= 60:
    print("All subjects are doing well. Keep revising regularly!")
    print("\n--- OVERALL PERFORMANCE ---")

average = (maths + python + ml) / 3

print("Average Marks:", average)

if average >= 75:
    print("Performance: Excellent")
elif average >= 60:
    print("Performance: Good")
elif average >= 40:
    print("Performance: Average")
else:
    print("Performance: Needs Improvement")
    print("\n--- PERSONALIZED MESSAGE ---")

if average >= 75 and study_hours >= 3:
    print("Excellent! You are performing well and maintaining good study habits.")
elif average >= 60:
    print("Good progress! Increase your practice and keep studying consistently.")
elif average >= 40:
    print("You are on the right track. Focus more on your weak subjects.")
else:
    print("Don't worry. Start with small daily goals and improve step by step.")

print("\nKeep going,", name, "!")
print("\n--- DAILY STUDY GOAL ---")

if study_hours < 2:
    goal = 3
elif study_hours < 4:
    goal = 4
else:
    goal = study_hours + 1

print("Today's Study Goal:", goal, "hours")

if study_hours < goal:
    print("Try to study", goal - study_hours, "more hour(s) today.")
else:
    print("Great! You have completed today's study goal.")


print("\n--- FINAL AI SUMMARY ---")

print("Student:", name)
print("Overall Average:", average)
print("Grade:", grade)

if maths <= python and maths <= ml:
    weak_subject = "Maths"
elif python <= maths and python <= ml:
    weak_subject = "Python"
else:
    weak_subject = "ML"

print("Focus Subject:", weak_subject)

print("\n--- FINAL RECOMMENDATION ---")

if average >= 75:
    print("You are performing very well.")
elif average >= 60:
    print("Your performance is good. Keep improving.")
elif average >= 40:
    print("You need more practice and revision.")
else:
    print("You need to focus more on your studies.")

if attendance < 75:
    print("Also improve your attendance.")
else:
    print("Your attendance is good.")

print("\nAI Study Assistant completed successfully!")