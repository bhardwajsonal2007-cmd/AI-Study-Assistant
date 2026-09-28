import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# ==========================================
# AI STUDY ASSISTANT
# ==========================================

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)

# ==========================================
# STUDENT DATA
# ==========================================

students = {
    "Name": ["Aarav", "Riya", "Kabir", "Ananya", "Sahil"],
    "Maths": [78, 65, 45, 88, 55],
    "Python": [85, 72, 50, 91, 60],
    "ML": [80, 68, 42, 86, 58],
    "Study_Hours": [3, 2, 1, 4, 2]
}

df = pd.DataFrame(students)

df["Average"] = df[["Maths", "Python", "ML"]].mean(axis=1)

# ==========================================
# MACHINE LEARNING MODEL
# ==========================================

X = df[["Maths", "Python", "ML", "Study_Hours"]]
y = df["Average"]

model = LinearRegression()
model.fit(X, y)

# ==========================================
# TITLE
# ==========================================

st.title("📚 AI Study Assistant")

st.write(
    "Personalized Study Recommendation System"
)

st.divider()

# ==========================================
# STUDENT DETAILS
# ==========================================

st.header("👤 Enter Your Details")

name = st.text_input("Student Name")

maths = st.number_input(
    "Maths Marks",
    min_value=0,
    max_value=100,
    value=70
)

python_marks = st.number_input(
    "Python Marks",
    min_value=0,
    max_value=100,
    value=75
)

ml = st.number_input(
    "ML Marks",
    min_value=0,
    max_value=100,
    value=72
)

study_hours = st.number_input(
    "Daily Study Hours",
    min_value=0,
    max_value=15,
    value=3
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)

# ==========================================
# PREDICTION
# ==========================================

if st.button("🔮 Predict Performance"):

    new_student = [[
        maths,
        python_marks,
        ml,
        study_hours
    ]]

    predicted_average = model.predict(new_student)[0]

    # ======================================
    # PREDICTION
    # ======================================

    st.subheader("📊 Prediction")

    st.metric(
        "Predicted Average",
        f"{predicted_average:.2f}"
    )

    if predicted_average >= 75:
        st.success("Excellent performance!")

    elif predicted_average >= 60:
        st.info("Good performance!")

    elif predicted_average >= 40:
        st.warning("Needs more practice.")

    else:
        st.error("Needs significant improvement.")

    # ======================================
    # WEAK SUBJECT
    # ======================================

    if maths <= python_marks and maths <= ml:
        weak_subject = "Maths"

    elif python_marks <= maths and python_marks <= ml:
        weak_subject = "Python"

    else:
        weak_subject = "ML"

    st.subheader("🎯 Focus Subject")

    st.write(
        f"You should spend extra study time on **{weak_subject}**."
    )

    # ======================================
    # ATTENDANCE
    # ======================================

    st.subheader("📅 Attendance Analysis")

    if attendance >= 75:
        st.success(
            f"Attendance is {attendance}%. Good attendance!"
        )

    else:
        st.warning(
            f"Attendance is {attendance}%. "
            "Try to improve your attendance."
        )

    # ======================================
    # AI RECOMMENDATION
    # ======================================

    st.subheader("🤖 AI Recommendation")

    if predicted_average >= 75:

        st.write(
            "Your performance is excellent. "
            "Continue your current study routine "
            "and revise regularly."
        )

    elif predicted_average >= 60:

        st.write(
            "Your performance is good. "
            "Increase revision and practice, "
            "especially in your weak subject."
        )

    elif predicted_average >= 40:

        st.write(
            "Focus more on your weak subjects "
            "and practice daily."
        )

    else:

        st.write(
            "Follow a daily study plan and focus "
            "on strengthening your basics."
        )

    # ======================================
    # STUDY PLAN
    # ======================================

    st.subheader("📚 Personalized Study Plan")

    if study_hours < 2:
        goal = 3

    elif study_hours < 4:
        goal = 4

    else:
        goal = 5

    st.write(
        f"**Recommended daily study goal: {goal} hours**"
    )

    if study_hours < goal:

        st.write(
            f"Try to study {goal - study_hours} "
            f"more hour(s) today."
        )

    else:

        st.write(
            "Great! You are already meeting your study goal."
        )

    st.write(
        f"🎯 Give extra attention to **{weak_subject}**."
    )
# ======================================
    # MARKS COMPARISON
    # ======================================

    st.subheader("📈 Marks Comparison")

    chart_data = pd.DataFrame({
        "Subject": ["Maths", "Python", "ML"],
        "Marks": [maths, python_marks, ml]
    })

    st.bar_chart(
        chart_data.set_index("Subject")
    )
    # ======================================
    # STUDENT SUMMARY
    # ======================================

    st.divider()

    st.subheader("📋 Student Summary")

    st.write(
        "**Name:**",
        name if name else "Student"
    )

    st.write("**Maths:**", maths)
    st.write("**Python:**", python_marks)
    st.write("**ML:**", ml)
    st.write("**Study Hours:**", study_hours)
    st.write("**Attendance:**", f"{attendance}%")
    st.write("**Focus Subject:**", weak_subject)
    st.write(
        "**Predicted Average:**",
        f"{predicted_average:.2f}"
    )
