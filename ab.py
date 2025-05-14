import streamlit as st

with st.form("my_form"):
    st.write("Please fill in the details")
    Cus_Name = st.text_input(label="Name", placeholder="Enter your name")
    Cus_age = st.text_input(label="Age", placeholder= "Enter your age")


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Age:",Cus_age)
        st.write("Thank you")
