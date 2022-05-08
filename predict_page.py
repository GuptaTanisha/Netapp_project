import streamlit as st
import pickle
import numpy as np


def load_model():
    data = pickle.load(open('C:/Users/hp/Desktop/Netapp2/notebooks/trained_model_new_.sav','rb'))
    return data

model = load_model()


def show_predict_page():
    st.title('Prediction Page')
    offence = st.text_input('Offence')
    ok = st.button("Predict punishment")
    if ok:
        
        punishment = model.predict([offence])
        st.subheader(f"The estimated punishment is : {punishment[0]}")
