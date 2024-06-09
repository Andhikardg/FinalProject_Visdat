# -*- coding: utf-8 -*-
"""Final projcet.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AMuxVvXBBNkSvWiDk2r04Ivt3vOTRiii
"""

import pandas as pd
import streamlit as st
from bokeh.plotting import figure
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.layouts import column

# Load data
file_path = 'finalproject_Pizza.csv'
pizza_sales_data = pd.read_csv(file_path)

# Data preprocessing
# pizza_sales_data['date'] = pd.to_datetime(pizza_sales_data['date'])
# pizza_sales_data['month'] = pizza_sales_data['date'].dt.to_period('M')

pizza_sales_data['date'] = pd.to_datetime(pizza_sales_data['date'])
pizza_sales_data['day'] = pizza_sales_data['date'].dt.date

# Aggregate sales by day
daily_sales = pizza_sales_data.groupby('day').agg({'price': 'sum'}).reset_index()

# Streamlit app
def final_projcet():
    st.title("Pizza Sales Dashboard")

    # Sales Over Time
    # Daily Sales Line Chart
    st.header("Daily Sales")
    source = ColumnDataSource(daily_sales)
    p = figure(x_axis_type='datetime', title="Daily Sales", plot_height=400, plot_width=700)
    p.line(x='day', y='price', source=source, line_width=2)

    # Display the chart
    st.bokeh_chart(p, use_container_width=True)

    # Popular Pizzas
    st.header("Most Popular Pizzas")
    popular_pizzas = pizza_sales_data['name'].value_counts().reset_index()
    popular_pizzas.columns = ['name', 'count']
    p2 = figure(x_range=popular_pizzas['name'], title="Most Popular Pizzas")
    p2.vbar(x=popular_pizzas['name'], top=popular_pizzas['count'], width=0.9)
    p2.xgrid.grid_line_color = None
    p2.y_range.start = 0

    # Sales by Pizza Type
    st.header("Sales by Pizza Type")
    sales_by_type = pizza_sales_data.groupby('type').agg({'price': 'sum'}).reset_index()
    p3 = figure(x_range=sales_by_type['type'], title="Sales by Pizza Type")
    p3.vbar(x=sales_by_type['type'], top=sales_by_type['price'], width=0.9)
    p3.xgrid.grid_line_color = None
    p3.y_range.start = 0

    # Sales by Pizza Size
    st.header("Sales by Pizza Size")
    sales_by_size = pizza_sales_data.groupby('size').agg({'price': 'sum'}).reset_index()
    p4 = figure(x_range=sales_by_size['size'], title="Sales by Pizza Size")
    p4.vbar(x=sales_by_size['size'], top=sales_by_size['price'], width=0.9)
    p4.xgrid.grid_line_color = None
    p4.y_range.start = 0

    # Display the charts
    st.bokeh_chart(p1, use_container_width=True)
    st.bokeh_chart(p2, use_container_width=True)
    st.bokeh_chart(p3, use_container_width=True)
    st.bokeh_chart(p4, use_container_width=True)

if __name__ == "__main__":
    final_projcet()
