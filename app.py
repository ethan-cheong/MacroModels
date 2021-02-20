import streamlit as st
import numpy as np
import pandas as pd
import time
from utils import provide_state
import models
import altair as alt

st.set_page_config(layout='wide')

model_choice = st.sidebar.selectbox(
    'Model',
    ['select a model', 'Solow Growth Model', 'Closed-Economy One-Period Model', 'Two-Period Model']
)

if model_choice == 'select a model':
    """
    # Macro Models
    Macroeconomic models taught in EC102. Code available [here](https://github.com/ethan-cheong/MacroModels).

    Models included:
    - Solow Growth Model
    - Closed-Economy One-Period Model
    - Two-Period Model
    """

elif model_choice == 'Solow Growth Model':
    """
    # Solow Growth Model
    Set parameters and click "draw graphs"
    """

    n_years = st.sidebar.number_input(
        label='Enter total years passed',
        min_value=1,
        value=50,
        step=1
    )

    N = st.sidebar.number_input(
        label='Enter value for N',
        min_value=1.0,
        value=1000.0,
        step=1.0
    )

    K = st.sidebar.number_input(
        label='Enter value for K',
        min_value=1.0,
        value=1000.0,
        step=1.0
    )
    n = st.sidebar.slider(
        label='Population growth rate (n)',
        min_value=0.0,
        max_value=1.0,
        value=0.05
    )

    s = st.sidebar.slider(
        label='Savings rate (s)',
        min_value=0.0,
        max_value=1.0,
        value=0.25
    )

    d = st.sidebar.slider(
        label='Depreciation rate (d)',
        min_value=0.0,
        max_value=1.0,
        value=0.10
    )

    alpha = st.sidebar.slider(
        label='Labour share of output (alpha)',
        min_value=0.0,
        max_value=1.0,
        value=0.5
    )

    z = st.sidebar.number_input(
        label='Productivity (z)',
        value=1.0,
        step=0.01
    )

    z_growth_input = st.sidebar.number_input(
        label='Productivity Growth Rate',
        value=0.0,
        step=0.01
    )


    solow = models.SolowGrowth(N, K, n, s, d, z, alpha)

    col1, col2, col3 = st.beta_columns(3)
    with col1:
        """### Total Population (N) against Time"""
        N_chart = st.line_chart(np.array([solow.N]))
        """### Total Consumption (C) against Time"""
        C_chart = st.line_chart(np.array([solow.C]))
    with col2:
        """### Total Capital (K) against Time"""
        K_chart = st.line_chart(np.array([solow.K]))
        """### Total Savings, Investment (S, I) against Time"""
        SI_chart = st.line_chart(np.array([solow.S]))
    with col3:
        """### Capital to Labour ratio (k) against Time"""
        k_chart = st.line_chart(np.array([solow.k]))
        """### Total Income (Y) against Time"""
        Y_chart = st.line_chart(np.array([solow.Y]))

    active = False

    if st.checkbox('Draw Graphs'):
        active = not active

    for i in range(n_years):
        if active:
            solow.increment()
            N_chart.add_rows([solow.N])
            C_chart.add_rows([solow.C])
            K_chart.add_rows([solow.K])
            SI_chart.add_rows([solow.S])
            k_chart.add_rows([solow.k])
            Y_chart.add_rows([solow.Y])
            time.sleep(0.005)
