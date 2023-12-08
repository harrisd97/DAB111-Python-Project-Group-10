# Sleep Health Dataset Analysis

This project provides insights into the Sleep Health and Lifestyle Dataset, covering a wide range of variables related to sleep and daily habits.

## Project Structure

- **Build_Database.py:** Python script to create a SQLite database and import data from the CSV file.
- **Sleep_Health_Application.py:** Flask web application to visualize the dataset with pages for the index, about, and data.
- **templates/:** HTML templates for the website.

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run the database builder: `python Build_Database.py`
3. Launch the web application: `python Sleep_Health_Application.py`

## About the Dataset

- **Source of Data:** The dataset is sourced from Kaggle.
- **Size:** 374 rows x 13 columns.
- **Variables:** Gender, Age, Occupation, Sleep Duration, Quality of Sleep, Physical Activity Level, Stress Level, BMI Category, Blood Pressure, Heart Rate, Daily Steps, Sleep Disorder.

## Key Features

- **Comprehensive Sleep Metrics:** Explore sleep duration, quality, and factors influencing sleep patterns.
- **Lifestyle Factors Analysis:** Analyze physical activity levels, stress levels, and BMI categories.
- **Cardiovascular Health Examination:** Examine blood pressure and heart rate measurements.
- **Sleep Disorder Analysis:** Identify occurrences of Insomnia and Sleep Apnea.

## Additional Information

- The `Health.db` file contains the SQLite database with the imported dataset. You can use a SQLite database viewer to explore the data further.

- The website is currently set to run in debug mode (`app.run(debug=True)` in `Sleep_Health_Application.py`). For production use, consider changing this configuration.

## Project Members

- **Harish Kumar Dakshinamoorthy**
- **Akash Balu**
- **Ganesh Rajendran**
