import streamlit as st
import numpy as np
import pandas as pd
import time
import models

st.set_page_config(layout='wide')

"""
# Macro Models
Macroeconomic models for EC102
"""

model_choice = st.sidebar.selectbox(
    'Select a model',
    ['Solow Growth Model', 'One-Period Macroeconomic Model']
)

# Options for Solow Growth Model
if model_choice=='Solow Growth Model':
    N_input = st.sidebar.number_input(
        label='Enter value for N',
        min_value=1,
        value=1000,
        step=1
    ),
    K_input = st.sidebar.number_input(
        label='Enter value for K',
        min_value=1,
        value=1000,
        step=1
    ),
    n_input = st.sidebar.slider(
        label='Population growth rate (n)',
        min_value=0.0,
        max_value=1.0,
        value=0.05
    ),
    s_input = st.sidebar.slider(
        label='Savings rate (s)',
        min_value=0.0,
        max_value=1.0,
        value=0.25
    ),
    d_input = st.sidebar.slider(
        label='Depreciation rate (d)',
        min_value=0.0,
        max_value=1.0,
        value=0.10
    ),
    alpha_input = st.sidebar.slider(
        label='Labour share of output (alpha)',
        min_value=0.0,
        max_value=1.0,
        value=0.5
    ),
    z_input = st.sidebar.number_input(
        label='Productivity (z)',
        value=1.0,
        step=0.01
    ),
    z_growth_input = st.sidebar.number_input(
        label='Productivity Growth Rate',
        value=0.0,
        step=0.01
    )
    solow = models.SolowGrowth(N_input[0], K_input[0], n_input[0], s_input[0],
                               d_input[0], z_input[0], alpha_input[0])

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        N_chart = st.line_chart(np.array([float(solow.N)]))
        C_chart = st.line_chart(np.array([float(solow.C)]))
    with col2:
        K_chart = st.line_chart(np.array([float(solow.K)]))
        SI_chart = st.line_chart(np.array([float(solow.S)]))
    with col3:
        k_chart = st.line_chart(np.array([float(solow.k)]))
        Y_chart = st.line_chart(np.array([float(solow.Y)]))

    active = False

    if st.button('Toggle Animation'):
        active = not active

    while active:
        solow.increment()
        N_chart.add_rows([float(solow.N)])
        C_chart.add_rows([float(solow.C)])
        K_chart.add_rows([float(solow.K)])
        SI_chart.add_rows([float(solow.S)])
        k_chart.add_rows([float(solow.k)])
        Y_chart.add_rows([float(solow.Y)])
        time.sleep(0.1)
