# Real Estate Data ETL & Prediction System

<h4>Project Overview</h4>
<p>This project automates the <b>ETL (Extract, Transform, Load)</b> process for real estate data and builds a machine learning model to predict housing prices. The system is designed for data analysts, real estate professionals, and businesses looking to gain insights from property data.</p>

## Features
<ul>
<li>Extracts raw real estate data from an <b>API</b> and stores it in <b>AWS S3</b>.</li>
<li>Cleans and transforms the data using <b>Python (Pandas, NumPy, etc.)</b>.</li>
<li>Loads the cleaned data into <b>Snowflake</b> for efficient storage and querying.</li>
<li>Trains a <b>Linear Regression model</b> to predict house prices.
<li>Evaluates the model using <b>K-Fold Cross Validation and GridSearchCV</b> for <b>hyperparameter tuning</b>.</li>
<li>Provides a <b>Flask web application</b> with an HTML, CSS, and JavaScript frontend for users to input parameters and get house price predictions.</li>
</ul>

## System Architecture


## Installation & Setup

<ol>
<li><strong>Set Up a Virtual Environment</li></strong>

```
$ python -m venv venv
$ source venv/bin/activate  # On Mac/Linux  
$ venv\Scripts\activate  # On Windows
```

<li><strong>Install Dependencies</li></strong>

```
$ pip install -r requirements.txt
``` 

<li><strong>Configure Environment Variables</li></strong>
Create a .env file in the project root and add the following

```
AWS_ACCESS_KEY_ID=your_aws_access_key  
AWS_SECRET_ACCESS_KEY=your_aws_secret_key 
AWS_REGION= your_aws_region_key
S3_BUCKET_NAME=bucket_name

SNOWFLAKE_USER=your_snowflake_user  
SNOWFLAKE_PASSWORD=your_snowflake_password  
SNOWFLAKE_ACCOUNT=your_snowflake_account  
SNOWFLAKE_WAREHOUSE=your_snowflake_warehouse  
SNOWFLAKE_DATABASE=your_snowflake_database  
SNOWFLAKE_SCHEMA=your_snowflake_schema  
```

<li><strong>Run the ETL Pipeline</li></strong>

```
$ python model_transormation.py
$ python model_building.py
```

<li><strong>Start the Flask Web Application</li></strong>

```
$ python server.py
```

Then open your browser and go to:
http://127.0.0.1:5000/


## Usage
<ol>
<li>The ETL pipeline fetches, cleans, and loads data from <b> AWS S3 → Snowflake.</li></b>
<li>The machine learning model is trained and optimized for housing price prediction.</li>
<li>Users can access the <b>web app</b> to predict house prices based on input parameters.</li>
</ol>

## Technologies Used
<ul>
<li><strong>Python</strong> (Pandas, NumPy, Scikit-learn, Flask)</li>
<li><strong>AWS S3</strong> (Storage)</li>
<li><strong>Snowflake</strong> (Data Warehouse)</li>
<li><strong>Machine Learning</strong> (Linear Regression, Hyperparameter Tuning)</li>
<li><strong>Flask</strong> (Web Framework)</li>
<li><strong>HTML, CSS, JavaScript</strong> (Frontend)</li>
</ul>

## Future Improvements
<ul>
<li>Automate the ETL process using Apache Airflow.</li>
<li>Implement <strong>more advanced ML models</strong> (Random Forest, Gradient Boosting).</li>
</li>Enhance the UI with <strong>React.js</strong> for a better user experience.</li>
</ul>


## Contributing
<strong>Feel free to fork the repository, create a <u>pull request</u>, or open an issue if you have suggestions!</strong>