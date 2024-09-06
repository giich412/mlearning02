import streamlit as st
import pandas as pd

st.title('Machine Learning App 02')

st.info('This App builds Machine Learning Model etc....')

st.write('This App builds Machine Learning Model')

st.set_page_config(page_title='CSV File Reader', layout='wide')
st.header('Single File Upload')
upload_file = st.file_uploader('Upload your CSV file')
df = pd.read_csv(upload_file)
st.dataframe(df, width=1800, height=1200)

