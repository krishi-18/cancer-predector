# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 22:24:23 2025

@author: admin
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('lung_cancer.sav','rb'))

def cancer_prediction(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    #print(prediction)
    return prediction[0]
      
def main():
    
    st.title('🫁 Lung Cancer Prediction Web App')
    
    col1,col2,col3=st.columns(3)

    with col1:
        idi = st.text_input('🪪 id')
    
    with col2:
        age = st.text_input('👧🏻 age')

    with col3:
        gen = st.text_input('🧬 gender')
    
    with col1:
        country = st.text_input('🏳️ country')

    with col2:
        dia = st.text_input('📅 diagnosis_date')

    with col3:
        cancer_stage = st.text_input('cancer_stage')
  
    with col1:
        family_history = st.text_input('👪 family_history')

    with col2:
        smoking_status = st.text_input('🚬 smoking_status')

    with col3:
        bmi = st.text_input('⚖️ bmi')
    with col1:
        cholesterol_level = st.text_input('❤️ cholesterol_level')

    with col2:
        hypertension = st.text_input('hypertension')

    with col3:
        asthma = st.selectbox('🫁 asthma',['No','Yes'])
        wex={
          'No':0,
          'Yes':1
        }
        we = wex[asthma]
  
    with col1:
        cirrhosis = st.text_input('cirrhosis')
    with col2:
        other_cancer = st.selectbox('other_cancer',['No','Yes'])
        wex={
          'No':0,
          'Yes':1
        }
        we = wex[other_cancer]
    with col3:
          treatment_type = st.text_input('treatment_type')
    with col1:
            end = st.text_input('📆 end_treatment_date')
    with col2:
        status = st.selectbox('survived',['No','Yes'])
        plcmnt_status={
          'No':0,
          'Yes':1
        }
        sts = plcmnt_status[status]
    
    
    diagnosis=''
    
    if st.button('Result'):
        diagnosis = cancer_prediction([float(idi),float(age),float(gen),float(country),float(dia),float(cancer_stage),float(family_history),float(smoking_status),float(bmi),float(cholesterol_level),float(hypertension),float(asthma),float(cirrhosis),float(other_cancer),float(treatment_type),float(end),float(status)])

        
    st.success(diagnosis)
    
main()
