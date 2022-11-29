# Project: Data-Pipeline-with-Airflow
## Introduction
Sparkify is a music streaming company that decide to use Apache Airflow for automating and monitoring their data warehouse ETL piplines. The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.
## Datasets
Here are the s3 links for each:
```
Log data: s3://udacity-dend/log_data
Song data: s3://udacity-dend/song_data
```
## Project Structure
```
└───airflow                      
|   |               
│   └───dags                     
│   |   │ udac_example_dag.py    # contains the tasks and dependencies of the DAG. 
|   |   |
|   └───plugins
│   |   │  
|   |   └───helpers
|   |   |   | sql_queries.py     # contains the SQL queries that is used in the ETL process.
|   |   |
|   |   └───operators
|   |   |   | stage_redshift.py  # contains StageToRedshiftOperator that copies JSON data from AWS S3 to staging tables in the AWS Redshift. 
|   |   |   | load_dimension.py  # contains LoadDimensionOperator that loads a dimension table from data in the staging table(s).
|   |   |   | load_fact.py       # contains LoadFactOperator that loads a fact table from data in the staging table(s).
|   |   |   | data_quality.py    # contains DataQualityOperator that is used to run checks on the data itself.
|   |   |
|   └───create_tables.sql        # contains the SQL queries used to create all the required tables in Redshift.
```
## How to Run
1. Create a Redshift cluster on your AWS account
2. Turn on Airflow by running Airflow/start.sh
3. Create AWS and Redshift connections on Airflow Web UI
4. Run udac_example _dag DAG to create tables on Redshift and trigger ETL data pipeline
