import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page configuration
st.set_page_config(page_title="Sales Dashboard", layout="wide")

# File uploader for multiple Excel files
uploaded_files = st.file_uploader("Choose Excel files", type="xlsx", accept_multiple_files=True)

if uploaded_files:
    all_data = []  # List to hold dataframes from all files

    for uploaded_file in uploaded_files:
        try:
            # Read each uploaded Excel file
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            df['Source File'] = uploaded_file.name  # Add a column to identify the source file
            all_data.append(df)
            st.success(f"Data loaded successfully from {uploaded_file.name}")
        except Exception as e:
            st.error(f"Error loading {uploaded_file.name}: {e}")

    # Concatenate all dataframes into a single dataframe
    if all_data:
        df_combined = pd.concat(all_data, ignore_index=True)

        # Display combined data
        st.title('Sales Dashboard')
        st.dataframe(df_combined)

        # Plotting
        st.subheader('Sales Over Time')
        try:
            df_combined['date'] = pd.to_datetime(df_combined['date'], errors='coerce')  # Convert 'date' to datetime
            df_combined.dropna(subset=['date', 'total'], inplace=True)  # Drop rows with missing 'date' or 'total'
            sales_over_time = df_combined.groupby('date')['total'].sum()
            sales_over_time.plot(kind='line')
            st.pyplot()
        except Exception as e:
            st.error(f"Error plotting data: {e}")
else:
    st.info("Please upload one or more Excel files to proceed.")
