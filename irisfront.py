import streamlit as st
import pickle
st.write("Enter the detail require to find which species does a flower belong")
a=st.number_input("Enter the sepal length")
b=st.number_input("Enter the sepal width")
c=st.number_input("Enter the petal length")
d=st.number_input("Enter the petal width")
if st.button("Predict"):
    with open(r"C:\Users\nanda\PycharmProjects\akira\iris_model.pkl", "rb") as file:
        loaded_model = pickle.load(file)
    result = loaded_model.predict([[a,b,c,d]])
    st.write(result)