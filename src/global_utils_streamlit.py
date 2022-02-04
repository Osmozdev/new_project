import streamlit as st


def sidebar_main_page():
    list_of_courses = ['Azure Fundamentals (AZ-900)',
                       'Google Cloud Fundamentals',
                       'Hadoop Ecosystem',
                       'Statistics for DS and DA',
                       'Spark with Pyspark',
                       'Machine Learning',
                       'Dataiku',
                       'Scraping using python',
                       'Web app using Streamlit and Python']
    course_selection = st.sidebar.radio(label="Select your course", options=list_of_courses)
    list_of_language = ['French', 'English']
    st.sidebar.radio(label="Select your language", options=list_of_language)

    return course_selection
