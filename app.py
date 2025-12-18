import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt


st.title(“Covid-19 Dashboard For India”)
st.markdown(‘The dashboard will visualize the Covid-19 Situation in India’)
st.markdown(‘Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people infected with the COVID-19 virus will experience mild to moderate respiratory illness and recover without requiring special treatment.’. This app gives you the real-time impact analysis of Confirmed, Deaths, active, and recovered cases of COVID-19 )
st.sidebar.title(“Visualization Selector”)
st.sidebar.markdown(“Select the Charts/Plots accordingly:”)