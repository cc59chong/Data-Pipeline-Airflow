from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow import DAG

class StageToRedshiftOperator(BaseOperator):
    
    # copies JSON data from AWS S3 to staging tables in AWS Redshift
    
    ui_color = '#358140'
    
    #create a task
    template_fields = ("s3_key",)
    copy_sql = """
        COPY {}
        FROM '{}'
        ACCESS_KEY_ID '{}'
        SECRET_ACCESS_KEY '{}'
        REGION '{}'
        JSON '{}'
    """
        
    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 aws_credentials_id = "",
                 table = "",
                 s3_bucket = "",
                 s3_key = "",
                 json = "auto",
                 region = "us-west-2",
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.aws_credentials_id = aws_credentials_id
        self.table = table
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.region = region
        self.json = json
        

    def execute(self, context):
        
        # get aws credentials
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()
        
        # get redshift connection
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        # Clear the table
        self.log.info(f"Clearing data from {self.table} Redshift table")
        redshift.run("DELETE FROM {}".format(self.table))
        
        # Load the data from the rendered s3 path
        self.log.info('Copying data from AWS S3 to AWS Redshift')

        rendered_key = self.s3_key.format(**context)
        s3_path = "s3://{}/{}".format(self.s3_bucket, rendered_key)

        formatted_sql = StageToRedshiftOperator.copy_sql.format(
            self.table,
            s3_path,
            credentials.access_key,
            credentials.secret_key,
            self.region,
            self.json
        )
        
        self.log.info('formatted_sql')
        redshift.run(formatted_sql)
