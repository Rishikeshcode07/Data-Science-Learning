## Widgets means interactive apllications


import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter your name:") ## i CAN GIVE MY TEXT IN TEXTBOX

## creating a slider with value 0 to 100 and the last one is your input which is minimum
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}.")


## Select box is a dropdown box
options=["Python","Java","C++","JavaScript"]
choice=st.selectbox("Choose your favorite language:",options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello ,{name}")


data ={
    "Name": ["John","Jane","Jake","Jill"],
    "Age": [28,24,35,40],
    "City": ["New York","Los Angeles","Chicago","Houston"]
}  

df = pd.DataFrame(data)
df.to_csv("Sampledata.csv")
st.write(df)


## For uploading a file
uploaded_file= st.file_uploader("Choose a CSV file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)