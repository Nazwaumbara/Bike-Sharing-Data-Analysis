# Bike Sharing Data Analysis

## Overview

This project involves the analysis of bike sharing data to gain insights into bike rental patterns based on various factors, including time of day, season, and environmental conditions. The analysis is visualized using Streamlit, allowing for an interactive experience.

## Features

- **Total Bike Rentals on Holidays**: A line chart displaying bike rentals on holidays by hour.
- **Casual Rentals by Season**: A box plot showing casual bike rentals distributed across different seasons.
- **Impact of Humidity**: A regression plot illustrating the relationship between humidity and casual rentals during winter.
- **Heatmap of Rentals**: A heatmap visualizing bike rentals by hour and day of the week.
- **Conclusions and Recommendations**: Summarized insights and suggestions based on the analysis.

## Technologies Used

- Python
- Streamlit
- Pandas
- Seaborn
- Matplotlib

## Installation

To run this project locally, follow these steps:
### Prerequisites
- Python 3.11
- `pip` or `pipenv` package manager

### Steps to Set Up Locally

1. Clone or extract the project from the ZIP file:
```bash
   unzip project-analysis.zip
   cd analisis_data
   ```
2. Create a virtual environment (recommended):
``` bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
3. Install the required dependencies:
```bash
   pip install -r requirements.txt
```
4. Running the Streamlit App
``` bash
   streamlit run dashboard.py
```