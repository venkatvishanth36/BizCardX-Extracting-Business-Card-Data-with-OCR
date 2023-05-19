
import sqlite3
import mysql.connector as mysql
import easyocr as ocr  #OCR
import streamlit as st  #Web App
from PIL import Image #Image Processing
import numpy as np #Image Processing
import pandas as pd
import re 
from sympy import expand, symbols

#title
st.title("Extract Text from Images")

#subtitle
st.markdown("Optical Character Recognition")

st.markdown("")

#image uploader
image = st.file_uploader(label = "Upload your Image here",type=['png','jpg','jpeg'])


@st.cache
def load_model(): 
    reader = ocr.Reader(['en'],model_storage_directory='.')
    return reader 

reader = load_model() #load model

if image is not None:

    input_image = Image.open(image) #read image
    st.image(input_image) #display image

    with st.spinner("🤖 AI is at Work! "):
        

        result = reader.readtext(np.array(input_image))

        result_text = [] #empty list for results


        for text in result:
            result_text.append(text[1])

        st.write(result_text)
    st.success("Here you go!")
    st.balloons()
else:
    st.write("Upload an Image")
    
image_path=r"C:\Users\KKR\OneDrive\Desktop\Venkatesh\BizCardX Extracting Business Card Data with OCR\Business cards\1.png"
read=ocr.Reader(['en'],['EN'])
result=read.readtext(image_path,detail=0,paragraph=False)
im =Image.open(image_path)
k={'Company_name':"",'Name':"",'Designation':"",'Number':"",'Email':"",'Website':"",
    'Area':"",'Pincode':""}

k['Name']=result_text[0]
k['Designation']=result_text[1]
for i in range(len(result_text)):
    if re.findall("[a-zA-Z0-9]+ [a-zA-Z0-9]+ [ St]+",result_text[i]):
        k['Area']=(result_text[i])
    if re.search('[^- +a-zA-z]{6}',result_text[i]):
        res=result_text[i]
        result = [int(result_text[i]) for result_text[i] in res.split() if result_text[i].isdigit()]
        k['Pincode']=result_text[i]
    if re.findall("[^A-Z0-9.-_+~!@#$ %&*()]+@+[a-zA-Z0-9]+.[a-z]+",result_text[i]):
        k['Email']=result_text[i]
    if re.findall("[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]",result_text[i]):
        k['Number']=result_text[i]
    if re.findall('[^ ,0-9!@#$%&*()_+]+[A-Za-z]+.com',result_text[i]):
        k["Website"]=result_text[i]

cn = ""  # adding company name
for i in result_text:
    if i not in k.values():
        if i.isalpha():
            print(i)
            cn = cn + ' ' + i
k['Company_name'] = cn

st.dataframe(k)


st.caption("Made by Venkatesh")

