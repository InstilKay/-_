
import streamlit as st
import pandas as pd
import time
import os 
table1=pd.DataFrame({"RPA":[1,2,3,4,5,6,7],"Flows":[11,12,13,14,15,16,17]})
st.title                ("AUTOMATION")
st.subheader("Traning for developers")
st.header("outline programes")
st.text("These program is might to train all new developer to be come the best in the industry")
st.markdown("**Hello team** begin your training     ")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("new updates")
st.metric(label="RPA Processes",value="34")
st.markdown("---")
def converter(value):
    m,s,mm=value.split(":")
    t_s=int(m)*60+int(s)+int(mm)/1000
    return t_s
st.table(table1)
st.image("Instilkay/-_/Instil_program/dp.png")
st.video("sort.mp4")
state=st.checkbox("Do you want email",value=True)
if state:
    st.write("done")
else:
    sec=converter(str(val))
    bar=st.progress(0)
    per=sec/100
    for i in range(100):
        bar.progress(i+1)
        ts.sleep(per)
    pass
radio_btn=st.radio("List department to automate",options=("Ops","clearing","CPU","control")) 
print(radio_btn)
selectiom=st.selectbox("what is your designer",options=("nike","adidas","reebok "))
st.title("Upload files")
st.markdown("---")
image=st.file_uploader("Please upload files",type=["jpg","png"])
if image is not None:
    st.image(image)
st.title("Upload files")
st.markdown("---")
images=st.file_uploader("Please upload files",type=["jpg","png"],accept_multiple_files=True)
if image is not None:
    for image in images:
        st.image(image)
valinput=st.text_input("Enter your name ",max_chars=60)    
print(valinput)
bar=st.progress(0)
for i in range(10):
    bar.progress((i+1)*10)        
st.markdown("<h1> User Registration<h1>",unsafe_allow_html=True)
form=st.form("Form 1")
form.text_input("First name")      
form.text_input("last name")   
form.form_submit_button("submit")
st.markdown("<h1 style ='text align: center;> User Registration<h1>",unsafe_allow_html=True)
with st.form("Form 2",clear_on_submit=True):
    col1,col2=st.columns(2)
    F_N=col1.text_input("First name")
    L_N=col2.text_input("last name")
    st.text_input("Email Address")
    st.text_input("Enter Password")
    st.text_input("confirm password")
    St_state=st.form_submit_button("submit new")
    if St_state:
        if F_N  =="" and L_N=="":
            st.warning("Please fill all fields")
        else:
            st.success("submitted successfully")  
st.sidebar.write("board")   
