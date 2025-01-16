import streamlit as st
import pandas as pd
import time
import os 
table1=pd.DataFrame({"Flow Modules":["Ezwich Reconciliation",
"GHQR Inbound Reconciliation", 
"GHQR Outbound Reconciliation",
"GIP Reconciliation",
"MasterCard OFF-US Reconciliation",
"ROU Reconciliation",
"VISA OFF-US Reconciliation",
"W2A Reconciliation",
"W2S Reconciliation",
"A2W Reconciliation",
"Yellosave Reconciliation" ,
"EZWICH Clearing",
"GHQR Settlement",
"GIP_Clearing",
"Mastercard_Off_Us_Clearing",
"Visa_Bulk_Settlement",
"Visa_Off_Us_Clearing",
"Yellosave Reversal",
"MoMo On POS (Blue Penguin)",
"ROU Preparation",
"W2A/W2S Settlement",
"Express Transit Callover Report",
"Transit Callover Report","Total"
],"Total":[144,
107,
109,
144,
153,
516,
184,
84,
87,
88,
218,
166,
177,
114,
151,
177,
147,
181,
150,
157,
93,
70,
82,
3499],"Successful":[139,
95,
98,
124,
149,
504,
180,
71,
78,
78,
194,
156,
166,
98,
146,
168,
141,
174,
144,
149,
82,
62,
70,
3266
],"FAILED":[5,
12,
11,
20,
4,
12,
4,
13,
9,
10,
24,
10,
11,
16,
5,
9,
6,
7,
6,
8,
11,
8,
12,
233
]})
st.title                ("RPA AUTOMATION")
st.header("")
st.text("")
st.subheader("Review On RPA Chart")
st.markdown("We are focusing on successful runs, failed runs, the total number of runs, the reasons for failures, the approach taken to resolve them, and the proposed way forward.     ")
st.markdown("[Google](https://www.google.com)")
st.markdown("---")
st.caption("All Processes")
st.metric(label="RPA Processes",value="35")
st.markdown("---")
st.subheader("PERSISTENT ERRORS")
st.markdown("""**Timeout Issues** :  Modules not running within scheduled time  File with wrong parameters<br>
<br>**Data Access Errors** : Unable to launch excel / read open items / Unable to query the database.<br>
<br>**Output Folder Errors** : Error message indicating that the output folder was not created.<br>
<br>**Production Environment Issues** : Power automate desktop expiry.<br>
<br>**Module Delays :** Modules queuing causing delays.<br>
<br>**File Naming Errors :** Naming convention of files submitted by officers.""", unsafe_allow_html=True)
st.markdown("---")
st.subheader("SOLUTIONS TO ENCOUNTERED PROBLEMS")
st.markdown("""Implemented monitoring dashboard to detect and display duration and completion.<br>
<br>Implemented error handling, incident response and logging of issues to keep records of problems faced on a daily base.<br>
<br>Automated folder creation as part of the workflow process.<br>
<br>Reprioritize module execution based on criticality.
Educated officers on file naming conventions to minimize errors.""", unsafe_allow_html=True)
st.markdown("---")
st.header("RPA DATA AND PERFORMANCE 2024")
st.dataframe(table1, use_container_width=True)
html_table = table1.to_html(index=False)
st.markdown(html_table, unsafe_allow_html=True)
#st.table(table1)
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
