from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'
    
    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 delete_load = False,
                 sql = "",
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.delete_load = delete_load
        self.sql = sql

    def execute(self, context):
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)
        
        if self.delete_load:
           self.log.info("Deleting dimension table")
           redshift.run("DELECT FROM {}".format(self.table))
            
        self.log.info("Running INSERT query to load data into dimension table from S3 to Redshift")
        redshift.run("INSERT INTO {} {}".format(self.table, self.sql))