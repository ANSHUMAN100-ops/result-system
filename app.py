import streamlit as st
import pandas as pd
from fpdf import FPDF

st.set_page_config(page_title="Student Result System", page_icon="🎓", layout="wide")

st.title("🎓 Smart Student Result System")
st.markdown("---")

if 'students' not in st.session_state:
    st.session_state.students = []

with st.sidebar:
    st.header("➕ Add New Student")
    name = st.text_input("Student Name")
    roll = st.text_input("Roll No")
    hindi = st.number_input("Hindi Marks", 0, 100, 33)
    english = st.number_input("English Marks", 0, 100, 33)
    math = st.number_input("Math Marks", 0, 100, 33)
    science = st.number_input("Science Marks", 0, 100, 33)
    sst = st.number_input("SST Marks", 0, 100, 33)

    if st.button("Add Result"):
        total = hindi + english + math + science + sst
        percent = total / 5
        
        if percent >= 90:
            grade = "A+ (Topper)"
        elif percent >= 75:
            grade = "A (First Division)"
        elif percent >= 60:
            grade = "B (Second Division)"
        elif percent >= 33:
            grade = "C (Pass)"
        else:
            grade = "FAIL"

        st.session_state.students.append({
            "Roll No": roll,
            "Name": name,
            "Total": total,
            "Percentage": round(percent, 2),
            "Grade": grade,
        })
        st.success(f"{name}'s result has been added successfully!")

if len(st.session_state.students) > 0:
    df = pd.DataFrame(st.session_state.students)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Students", len(df))
    col2.metric("Topper %", f"{df['Percentage'].max()}%")
    col3.metric("Pass %", f"{round(len(df[df['Grade']!='FAIL'])/len(df)*100,2)}%")

    st.dataframe(df, use_container_width=True)

    topper = df.loc[df['Percentage'].idxmax()]
    st.success(f"🏆 Topper: {topper['Name']} - {topper['Percentage']}%")