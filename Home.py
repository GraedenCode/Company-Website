import streamlit as st
import pandas


def print_employee(row):
    st.header(row['first name'].title() + ' ' + row['last name'].title())
    st.write(row['role'].title())
    st.image('Images/'+ row['image'])

df = pandas.read_csv('data.csv')

st.set_page_config(layout='wide')

st.title("The Best Company")


content = '''
Our company is the best company in everything we do. We seek to meet each of our customers expectations and then some. 
With our exceptional staff behind the scenes getting the products to the customer in record speeds. We at the Best Company are here to win.
'''
st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3, vertical_alignment="center", gap='small')

with col1:
    for i,row in df[0:4].iterrows():
        print_employee(row)

with col2:
    for i, row in df[4:8].iterrows():
        print_employee(row)

with col3:
    for i, row in df[8:12].iterrows():
        print_employee(row)

