# -*- coding: utf-8 -*-
"""

@author: tinashe zigara
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

tanzania_loan_pred = pickle.load(open('tanzania_loan_pred.sav', 'rb'))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu(' Prediction System',
                          
                          ['Loan Default Prediction',
                           'Coming Soon',
                           'Coming Soon'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
    
# Loan Default Prediction Page
if (selected == 'Loan Default Prediction'):
    
    # page title
    st.title('Loan Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        loannumber = st.text_input('Loan Number')
        
    with col2:
        loanamount = st.text_input('Loan Amount')
    
    with col3:
        totaldue = st.text_input('Total Due')
    
    with col1:
        termdays = st.text_input('Term Days')
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Loan Test Result'):
        diab_prediction = tanzania_loan_pred.predict([[loannumber, loanamount, totaldue, termdays]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The Loan is Bad'
        else:
          diab_diagnosis = 'The Loan is Good'
        
    st.success(diab_diagnosis)
