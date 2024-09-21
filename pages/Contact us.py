import streamlit as st
from send_email import send_email
import pandas as pd

st.title('The Best Company')

st.write('We are the best company doing the best stuff. Yup easy best company.')

df = pd.read_csv('topics.csv')



with st.form(key='contact_form'):
    user_email = st.text_input("Your Email Address")
    topic = st.selectbox("What topic do you want to discuss?", df['topic'])
    raw_message = st.text_area('Message')
    button = st.form_submit_button()
    if button:
        send_email(topic, raw_message, user_email)
        st.info('Message was Sent!')