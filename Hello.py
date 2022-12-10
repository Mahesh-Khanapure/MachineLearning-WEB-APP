import streamlit as st
import numpy as np
import pickle

pipe=pickle.load(open('pred.pkl','rb'))


st.title("Hii mahesh")
Pclass=st.slider('Passenger class',1,3)
#st.text_input("passenger class",[1,2,3])
Gender=st.select_slider("Gender",['Male','Female'])
age=st.slider('Age',0,100)
sibps=st.slider('input siblings',0,10)
parch=st.slider('input parents/childeran',0,2)
fare=st.number_input('Fare Amount',0,100)
embarked=st.selectbox('choose embarked point',['S','C','Q'])
#input=[Pclass,Gender,age,sibps,parch,fare,embarked]
# x=np.array([Pclass,Gender,age,sibps,parch,fare,embarked]).reshape(1,7)

if st.button('Predict Price'):
    query=np.array([Pclass,Gender,age,sibps,parch,fare,embarked],dtype=object).reshape(1,7)
    if (pipe.predict(query)==1):
        st.title('the passenger not survived')
    else:
        st.title('the passenger is survived')
    
