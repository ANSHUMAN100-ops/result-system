import streamlit as st
import pandas as pd

st.set_page_config(page_title="Result System", layout="centered")
st.title("Smart Student Result System")

@st.cache_data
def load_data():
    return []

if 'results' not in st.session_state:
    st.session_state.results = []

with st.form("form"):
    name = st.text_input("Student Name")
    roll = st.text_input("Roll No")
    c1, c2 = st.columns(2)
    hindi = c1.number_input("Hindi", 0, 100, 20)
    eng = c2.number_input("English", 0, 100, 20)
    math = c1.number_input("Math", 0, 100, 20)
    sci = c2.number_input("Science", 0, 100, 20)
    sst = st.number_input("SST", 0, 100, 20)
    submit = st.form_submit_button("Add Result")

    if submit:
        total = hindi+eng+math+sci+sst
        per = total/5
        st.session_state.results.append([name, roll, total, per])
        st.success(f"Added! Total: {total}")

if st.session_state.results:
    df = pd.DataFrame(st.session_state.results, columns=["Name","Roll","Total","%"])
    st.table(df)
