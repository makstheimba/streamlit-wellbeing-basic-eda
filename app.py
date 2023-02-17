import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('datasets/Wellbeing_and_lifestyle_data_Kaggle.csv')

df.drop(df[df['DAILY_STRESS'] == '1/1/00'].index, inplace=True)
df['DAILY_STRESS'] = df['DAILY_STRESS'].astype(int)

st.header('Wellbeing and lifestyle data')
st.write(df)
st.write(px.scatter(df, x='WEEKLY_MEDITATION', y='WORK_LIFE_BALANCE_SCORE', title='Weekly meditation and work life balance'))

shouldShowDailyStressForDifferentGender = st.checkbox('Show daily stress for different gender')
if shouldShowDailyStressForDifferentGender:
    st.write(px.histogram(df[df['GENDER'] == 'Male'], x='DAILY_STRESS', title='Daily Stress for male'))
    st.write(px.histogram(df[df['GENDER'] == 'Female'], x='DAILY_STRESS', title='Daily Stress for female'))
else:
    st.write(px.histogram(df, x='DAILY_STRESS', title='Daily Stress'))
