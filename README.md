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
## Airflow Data Pipeline
1. To go to the Airflow UI: run Airflow locally, open http://localhost:8080 in Google Chrome (other browsers occasionally have issues rendering the Airflow UI).
2. Click on the **Admin** tab and select **Connections**.
![image](https://github.com/cc59chong/Data-Pipeline-Airflow/blob/main/images/admin-connections.png)<br>
3. Under **Connections**, select **Create**.
![image](https://github.com/cc59chong/Data-Pipeline-Airflow/blob/main/images/create-connection.png)<br>
4. On the create connection page, enter the following values:
   * **Conn Id**: Enter ```aws_credentials```.
   * **Conn Type**: Enter ```Amazon Web Services```.
   * **Login**: Enter your **Access key ID** from the IAM User credentials you downloaded earlier.
   * **Password**: Enter your **Secret access key** from the IAM User credentials you downloaded earlier.
select **Save and Add Another**.
![image](https://github.com/cc59chong/Data-Pipeline-Airflow/blob/main/images/connection-aws-credentials.png)<br>
5. On the next create connection page, enter the following values:
   * **Conn Id**: Enter ```redshift```.
   * **Conn Type**: Enter ```Postgres```.
   * **Host**: Enter the endpoint of your Redshift cluster, excluding the port at the end. You can find this by selecting your **cluster** in the Clusters page of the Amazon Redshift console. See where this is located in the screenshot below. IMPORTANT: Make sure to **NOT** include the port at the end of the Redshift endpoint string.
   * **Schema**: Enter ```dev```. This is the Redshift database you want to connect to.
   * **Login**: Enter ```awsuser```.
   * **Password**: Enter the password you created when launching your Redshift cluster.
   * **Port**: Enter ```5439```.
select **Save**.
![image](https://github.com/cc59chong/Data-Pipeline-Airflow/blob/main/images/cluster-details.png)<br>
![image](https://github.com/cc59chong/Data-Pipeline-Airflow/blob/main/images/connection-redshift.png)<br>
## ETL Process in Airflow UI
![image](https://github.com/cc59chong/Data-Pipeline-Airflow/blob/main/images/Working%20DAG%20with%20correct%20task%20dependencies.png)<br>

