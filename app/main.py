
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from app.utils import plot_time_series, plot_heatmap, plot_wind_polar, plot_temp_humidity_scatter, plot_histogram, calculate_z_scores, flag_significant_points,plot_significant_points,plot_bubble_chart
# Load datasets
benin = pd.read_csv(r'D:\10 Academy_Kefya\Week 0\Analyze-Solar-Radiation-Measurement-\data\benin-malanville.csv')
sierra_leone = pd.read_csv(r'D:\10 Academy_Kefya\Week 0\Analyze-Solar-Radiation-Measurement-\data\sierraleone-bumbuna.csv')
togo = pd.read_csv(r'D:\10 Academy_Kefya\Week 0\Analyze-Solar-Radiation-Measurement-\data\togo-dapaong_qc.csv')
# Streamlit app
st.title('Solar Radiation Analysis Dashboard')

country = st.selectbox('Select Country', ['Benin', 'Sierra Leone', 'Togo'])
analysis_type = st.selectbox('Select Analysis Type', ['Time Series', 'Correlation', 'Wind', 'Temperature', 'Histograms', 'Z-Score', 'Bubble Chart'])

if analysis_type == 'Time Series':
    st.subheader('Time Series Analysis')
    if country == 'Benin':
        plot_time_series(benin)
    elif country == 'Sierra Leone':
        plot_time_series(sierra_leone)
    else:
        plot_time_series(togo)

if analysis_type == 'Correlation':
    st.subheader('Correlation Analysis')
    if country == 'Benin':
        plot_heatmap(benin)
    elif country == 'Sierra Leone':
        plot_heatmap(sierra_leone)
    else:
        plot_heatmap(togo)

if analysis_type == 'Wind':
    st.subheader('Wind Analysis')
    if country == 'Benin':
        plot_wind_polar(benin)
    elif country == 'Sierra Leone':
        plot_wind_polar(sierra_leone)
    else:
        plot_wind_polar(togo)

if analysis_type == 'Temperature':
    st.subheader('Temperature Analysis')
    if country == 'Benin':
        plot_temp_humidity_scatter(benin)
    elif country == 'Sierra Leone':
        plot_temp_humidity_scatter(sierra_leone)
    else:
        plot_temp_humidity_scatter(togo)

if analysis_type == 'Histograms':
    st.subheader('Histograms')
    if country == 'Benin':
        plot_histogram(benin)
    elif country == 'Sierra Leone':
        plot_histogram(sierra_leone)
    else:
        plot_histogram(togo)

if analysis_type == 'Z-Score':
    st.subheader('Z-Score Analysis')
    if country == 'Benin':
        calculate_z_scores(benin)
    elif country == 'Sierra Leone':
        calculate_z_scores(sierra_leone)
    else:
        calculate_z_scores(togo)

if analysis_type == 'Significant Points':
    st.subheader('Significant Points Analysis')
    if country == 'Benin':
        flag_significant_points(benin)
        plot_significant_points(benin)
    elif country == 'Sierra Leone':
        flag_significant_points(sierra_leone)
        plot_significant_points(sierra_leone)
    else:
        flag_significant_points(togo)
        plot_significant_points(togo)

if analysis_type == 'Bubble Chart':
    st.subheader('Bubble Chart')
    if country == 'Benin':
        plot_bubble_chart(benin)
    elif country == 'Sierra Leone':
        plot_bubble_chart(sierra_leone)
    else:
        plot_bubble_chart(togo)