import datetime
import calendar

import streamlit as st
import numpy as np
import plotly.express as px

import retrieve_data as rd
import transformations as transformations
from data_translation import get_language, PortugueseLabels


# Get application labels in portuguese
labels: PortugueseLabels = get_language('por')

# Configure Global Streamlit
st.set_page_config(layout="wide")

# Define application Dashboard
st.title(labels.TITLE)

data = rd.retrieve_data(delete_na=True)
with st.expander(labels.SEE_ENTIRE_TABLE):
    st.dataframe(data)

# Put all dashboard configuration on a expander
with st.expander(labels.CONFIGURATION_TITLE):
    ## Set the configuration details for the dashboard.
    col1, col2, col3, _ = st.columns([1, 1, 1, 2])

    # Get the first and the last day of the month to be used as default values!
    current_date = datetime.date.today()
    first_day = datetime.date(current_date.year, current_date.month, 1)
    last_day = datetime.date(current_date.year,
                            current_date.month,
                            calendar.monthrange(current_date.year,
                                                current_date.month)[1])

    with col1:
        initial = np.datetime64(
            st.date_input(labels.DATE_RANGE['initial'], value=first_day))
        
    with col2:
        final = np.datetime64(
            st.date_input(labels.DATE_RANGE['final'], value=last_day))
        
    with col3:
        amout_provisioned = st.number_input(labels.RESERVED_4_FOOD)
        
    was_pressed = st.button(labels.BUTTON_DEFAULT_LABEL)

## Summury of all that was spend/earnded on the period.
st.subheader(labels.DATA_SUMMURY)

if not was_pressed:
    st.text(labels.WAITING_2_START)
else:
    _, col1, col2, _ = st.columns([1, 4, 4, 1])

    with col1:
        fig = px.bar(
            transformations.balance_in_range(data, (initial, final)), 
            x='types', y='values',
            title="Balanço do período"
        )
        st.plotly_chart(fig)
    with col2:
        fig = px.pie(
            transformations.total_cash_by_main_categories_in_range(
                data, (initial, final)),
            names="labels",
            values="values",
            title="Valores gastos agregando as principais categorias"
        )
        st.plotly_chart(fig)
