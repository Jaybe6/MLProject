import streamlit as st
import pickle
st.title("MPG ML Project")
displacement = st.number_input("Displacement",value=100, placeholder='enter the value for displacement')
horsepower = st.number_input("Horsepower", value=13,placeholder='Enter the value for horsepower')
weight= st.number_input("Weight", value=3000,placeholder='Enter the value for weight')
Acceleration = st.number_input("Acceleration", value=12, placeholder='Enter the value for Acceleration')
loaded_model=pickle.load(open('mpg_regession.sav','rb'))
prediction=loaded_model.predict([[displacement,horsepower,weight,Acceleration]])
st.subheader(f'predicted mpg value for above parameter is {prediction[0]}')
st.write(prediction)

