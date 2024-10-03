import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

bike_hour = pd.read_csv("E:/analisis_data/dashboard/main_data.csv")

bike_hour['season'] = bike_hour['season'].astype('category')
bike_hour['season'] = bike_hour['season'].cat.rename_categories({1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'})

st.title("🚴 Bike Sharing Data Analysis")

analysis_option = st.radio(
    "Select the analysis you want to view:",
    ('Total Bike Rentals on Holidays by Hour', 
     'Casual Rentals by Season', 
     'Impact of Humidity on Casual Rentals in Winter', 
     'Bike Rentals by Hour and Day')
)

if analysis_option == 'Total Bike Rentals on Holidays by Hour':
    st.header("Total Bike Rentals on Holidays by Hour")
    non_working_days = bike_hour[bike_hour['holiday'] == 1]

    if not non_working_days.empty:
        plt.figure(figsize=(15, 8))
        sns.lineplot(data=non_working_days, x='hour', y='total', marker='o')
        plt.title('Total Bike Rentals on Holidays by Hour')
        plt.xlabel('Hour of the Day')
        plt.ylabel('Total Bike Rentals')
        plt.xticks(range(0, 24))
        plt.grid(True)
        st.pyplot(plt)
    else:
        st.write("No data available for holidays.")

elif analysis_option == 'Casual Rentals by Season':
    st.header("Casual Rentals by Season")
    plt.figure(figsize=(10, 6))
    df_season = bike_hour[['season', 'casual']]
    melted_df_season = pd.melt(df_season, id_vars='season', value_name='casual_count')
    sns.boxplot(data=melted_df_season, x='season', y='casual_count')
    plt.title('Casual Rentals by Season')
    plt.xlabel('Season')
    plt.ylabel('Casual Rentals')
    st.pyplot(plt)

elif analysis_option == 'Impact of Humidity on Casual Rentals in Winter':
    st.header("Impact of Humidity on Casual Rentals in Winter")
    humidity_df = bike_hour[bike_hour['season'] == 'winter']

    if not humidity_df.empty:
        plt.figure(figsize=(10, 6))
        sns.regplot(x='humidity', y='casual', data=humidity_df, scatter_kws={'color': 'green'}, line_kws={'color': 'orange'})
        plt.title('Impact of Humidity on Casual Rentals in Winter')
        plt.xlabel('Humidity')
        plt.ylabel('Casual Rentals')
        st.pyplot(plt)
    else:
        st.write("No winter data available.")

elif analysis_option == 'Bike Rentals by Hour and Day':
    st.header("Bike Rentals by Hour and Day")
    pivot_table = bike_hour.pivot_table(values='total', index='hour', columns='weekday', aggfunc='sum')
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f')
    plt.title('Bike Rentals by Hour and Day')
    plt.xlabel('Day of the Week')
    plt.ylabel('Hour of the Day')
    st.pyplot(plt)

st.header("Conclusion and Recommendations")
st.write("""
- The highest total bike rentals occur after 10 a.m. on weekdays.
- Warmer temperatures correlate with increased bike usage.
- Recommendations: Provide more bikes during peak hours and summer to meet user demand.
""")
