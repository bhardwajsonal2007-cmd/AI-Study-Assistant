import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


# ==========================================
# 1. STUDENT DATA
# ==========================================

students = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya", "Sahil"],
    "Maths": [78, 65, 45, 88, 55],
    "Python": [85, 72, 50, 91, 60],
    "ML": [80, 68, 42, 86, 58],
    "Study_Hours": [3, 2, 1, 4, 2]
}

df = pd.DataFrame(students)

print("\n--- STUDENT DATA ---")
print(df)


# ==========================================
# 2. AVERAGE MARKS
# ==========================================

df["Average"] = df[["Maths", "Python", "ML"]].mean(axis=1)

print("\n--- AVERAGE MARKS ---")
print(df[["Name", "Average"]])


# ==========================================
# 3. TOP STUDENT
# ==========================================

top_student = df.loc[df["Average"].idxmax()]

print("\n--- TOP STUDENT ---")
print("Name:", top_student["Name"])
print("Average:", top_student["Average"])


# ==========================================
# 4. SAVE DATA
# ==========================================

df.to_csv("students_data.csv", index=False)

print("\nStudent data saved successfully!")


# ==========================================
# 5. READ SAVED DATA
# ==========================================

saved_data = pd.read_csv("students_data.csv")

print("\n--- SAVED DATA ---")
print(saved_data)


# ==========================================
# 6. DATA ANALYSIS
# ==========================================

print("\n--- DATA ANALYSIS ---")

print("Highest Average:", saved_data["Average"].max())
print("Lowest Average:", saved_data["Average"].min())
print("Overall Class Average:", saved_data["Average"].mean())


# ==========================================
# 7. SUBJECT AVERAGES
# ==========================================

print("\n--- SUBJECT AVERAGES ---")

print("Maths Average:", saved_data["Maths"].mean())
print("Python Average:", saved_data["Python"].mean())
print("ML Average:", saved_data["ML"].mean())


# ==========================================
# 8. GRAPH
# ==========================================

saved_data.plot(
    x="Name",
    y=["Maths", "Python", "ML"],
    kind="bar"
)

plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()


# ==========================================
# 9. MACHINE LEARNING DATA
# ==========================================

print("\n--- ML DATA ---")

X = saved_data[["Maths", "Python", "ML", "Study_Hours"]]
y = saved_data["Average"]

print("Input Features:")
print(X)

print("\nTarget:")
print(y)


# ==========================================
# 10. TRAIN TEST SPLIT
# ==========================================

print("\n--- TRAIN TEST SPLIT ---")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training data:", len(X_train))
print("Testing data:", len(X_test))


# ==========================================
# 11. TRAIN ML MODEL
# ==========================================

print("\n--- TRAINING ML MODEL ---")

model = LinearRegression()

model.fit(X_train, y_train)

print("ML Model trained successfully!")


# ==========================================
# 12. MODEL EVALUATION
# ==========================================

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\n--- MODEL EVALUATION ---")

print("Mean Absolute Error:", mae)
print("R2 Score:", r2)


# ==========================================
# 13. NEW STUDENT PREDICTION
# ==========================================

print("\n--- NEW STUDENT PREDICTION ---")

maths_new = int(input("Enter new student's Maths marks: "))
python_new = int(input("Enter new student's Python marks: "))
ml_new = int(input("Enter new student's ML marks: "))
study_hours_new = int(input("Enter new student's study hours: "))

new_student = [[
    maths_new,
    python_new,
    ml_new,
    study_hours_new
]]

predicted_average = model.predict(new_student)

print("\nPredicted Average:", predicted_average[0])


# ==========================================
# 14. PERFORMANCE PREDICTION
# ==========================================

if predicted_average[0] >= 75:
    print("Prediction: Excellent performance")

elif predicted_average[0] >= 60:
    print("Prediction: Good performance")

elif predicted_average[0] >= 40:
    print("Prediction: Needs more practice")

else:
    print("Prediction: Needs significant improvement")


# ==========================================
# 15. WEAK SUBJECT ANALYSIS
# ==========================================

print("\n--- WEAK SUBJECT ANALYSIS ---")

if maths_new <= python_new and maths_new <= ml_new:
    weak_subject = "Maths"

elif python_new <= maths_new and python_new <= ml_new:
    weak_subject = "Python"

else:
    weak_subject = "ML"

print("Subject needing more focus:", weak_subject)


# ==========================================
# 16. AI STUDY RECOMMENDATION
# ==========================================

print("\n--- AI STUDY RECOMMENDATION ---")

if predicted_average[0] >= 75:

    print("Your performance is excellent.")
    print("Recommendation: Continue your current study routine.")

elif predicted_average[0] >= 60:

    print("Your performance is good.")
    print("Recommendation: Increase revision and practice.")

elif predicted_average[0] >= 40:

    print("Your performance needs improvement.")
    print("Recommendation: Focus more on weak subjects and practice daily.")

else:

    print("Your performance needs significant improvement.")
    print("Recommendation: Follow a daily study plan and focus on your basics.")


# ==========================================
# 17. PERSONALIZED STUDY PLAN
# ==========================================

print("\n--- PERSONALIZED STUDY PLAN ---")

if study_hours_new < 2:

    print("Daily study goal: 3 hours")
    print("Focus on basics and regular practice.")

elif study_hours_new < 4:

    print("Daily study goal: 4 hours")
    print("Spend extra time on your weak subject:", weak_subject)

else:

    print("Daily study goal: 5 hours")
    print("Maintain your routine and revise regularly.")


# ==========================================
# 18. FINAL SUMMARY
# ==========================================

print("\n================================")
print("       AI STUDY ASSISTANT")
print("================================")

print("Predicted Average:", round(predicted_average[0], 2))
print("Focus Subject:", weak_subject)
print("Study Hours:", study_hours_new)

print("\nAI Study Assistant completed successfully!")