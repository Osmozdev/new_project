# Import the differents web appmodules (Utils, def => streamlit)
import src.global_utils_streamlit as gu
import src.azure_course_az900 as az900
import src.google_cloud_fundamentals as google_fund
import src.statistics_course_DS as stats_course
import src.css_utils as utl

import os
import time

import streamlit as st

from PIL import Image


# Settings
st.set_page_config(layout="wide",
                   page_title='TantanDevPlace',
                   initial_sidebar_state="auto")

utl.navigation_bar()

st.set_option('deprecation.showPyplotGlobalUse', False)
# Loading CSS
utl.local_css("src/frontend/main_app.css")


course_selection = gu.sidebar_main_page()

if course_selection == "Azure Fundamentals (AZ-900)":
    az900.set_png_as_page_bg("C:/Users/hp/PycharmProjects/courses/personnal-app/images/azure_background.png")
    az900.azure_course()

if course_selection == "Statistics for DS and DA":
    stats_course.statistics_ds_course()

if course_selection == "Google Cloud Fundamentals":
    google_fund.google_cloud_course()
