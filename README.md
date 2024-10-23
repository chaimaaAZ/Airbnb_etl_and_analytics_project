# Airbnb ETL and Analytics project
![airbnb_dashboard](https://github.com/user-attachments/assets/4592a5d4-6aee-413d-ab4b-d0b465f42ca5)
1. [ Project Overview ](#introduction)
3. [ Project Architecture ](#arch)

<a name="introduction"></a>
## 🔬 Project Overview 

This is an end to end data engineering project in which I developed an ELT pipeline to extract, analyze, and visualize insights from Sydney  Airbnb data.

### 💾 Dataset

This is a  dataset that captures neighborhoods, listings, reservations and reviews of Sydney Airbnb data on December 10th, 2022.


The dataset link: [Dataset](https://www.kaggle.com/datasets/samibrahim/airbnb-sydney?)

### 🎯 Project Goals

- Set up prefect local environment 
- Create a data pipeline from scratch using prefect workflow.
- Upload data from MongoDB to Snowflake using dlt hub.
- Integrate dbt and run data models with prefect.
- Ingest data into Snowflake Warehouse.
- Visualize insights using PowerBI.
<a name="arch"></a>
## 📝 Project Architecture

The end-to-end data pipeline includes the following steps:

- Downloading, processing, and uploading the initial dataset to *MongoDB*
- Moving the data from MongoDB to snowflake using dlt hub.
- Transforming the data in the Data Warehouse and preparing it for the dashboard *(dbt)*
- Creating the dashboard *(PowerBI)*
  
You can find the detailed information on the diagram below:
![airbnb_etl_pipeline](https://github.com/user-attachments/assets/28bc1a6e-7601-4644-80fb-7f2e7ae84e45)
### 🔧 Pipeline on Prefect
![prefect workflow](https://github.com/user-attachments/assets/eaedd6ca-daf9-4e53-9dda-d5cc89128bb3)

