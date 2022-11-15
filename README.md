# Project: Data-Pipeline-with-Airflow
## Introduction
Sparkify is a music streaming company that decide to use Apache Airflow for automating and monitoring their data warehouse ETL piplines. The source data resides in S3 and needs to be processed in Sparkify's data warehouse in Amazon Redshift. The source datasets consist of JSON logs that tell about user activity in the application and JSON metadata about the songs the users listen to.
## Datasets
Here are the s3 links for each:
```
Log data: s3://udacity-dend/log_data
Song data: s3://udacity-dend/song_data
```
## Structure
```
└───airflow                      
|   |               
│   └───dags                     
│   |   │ udac_example_dag.py    # contains the tasks and dependencies of the DAG. 
|   |   |
|   └───plugins
│       │  
|       └───helpers
|       |   | sql_queries.py     # contains the SQL queries that is used by create_tables.py in creating DB.
|       |
|       └───operators
|       |   | stage_redshift.py  # contains StageToRedshiftOperator that copies JSON data from AWS S3 to staging tables in the AWS Redshift. 
|       |   | load_dimension.py  # contains LoadDimensionOperator that loads a dimension table from data in the staging table(s).
|       |   | load_fact.py       # contains LoadFactOperator that loads a fact table from data in the staging table(s).
|       |   | data_quality.py    # contains DataQualityOperator that is used to run checks on the data itself.
```
