import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



@st.cache
def load_data():
    df = pd.read_csv("Data_netapp.csv")
    df = df.dropna()
#     df = df[(df['Punishment']!=0)&(df['Type of punishment']!='0')]
    df['Type'].replace('Traffic and Criminal cases','Traffic and criminal cases',inplace= True)

    return df

df = load_data()

def show_explore_page():
    st.title("Explore the data")

    data = df["Type"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.subheader("Cases Comparison")

    st.pyplot(fig1)
    
    st.subheader("Pending cases")

    pending = df[(df['Status'] == 'Pending')]
    data= pending.groupby(["Type"]).size()
    tc = pending.groupby(["Type"]).size()['Traffic cases']
    cc = pending.groupby(["Type"]).size()['Criminal cases']
    tcc = pending.groupby(["Type"]).size()['Traffic and criminal cases']
    st.write(f"The pending traffic, criminal cases and cases involing both MVA and IPC acts are : {tc}, {cc} and {tcc} respectively")
    
    st.bar_chart(data)
    
    st.subheader("Different punishments")
    
    data= df.groupby(["Punishment"]).size()
    st.bar_chart(data)
