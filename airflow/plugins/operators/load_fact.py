from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadFactOperator(BaseOperator):

    ui_color = '#F98866'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id = "",
                 table = "",
                 delete_load = False,
                 sql = "",
                 append_only = "",
                 *args, **kwargs):

        super(LoadFactOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id = redshift_conn_id
        self.table = table
        self.delete_load = delete_load
        self.sql = sql
        self.append_only = append_only

    def execute(self, context):
        self.log.info(f"Connecting to Redshift")
        redshift = PostgresHook(postgres_conn_id = self.redshift_conn_id)

        if not self.append_only:
            self.log.info(f"Delete {self.table} fact table")
            redshift.run("DELECT FROM {}".format(self.table))
            
            redshift.run("INSERT INTO {} {}".format(self.table, self.sql))
            
        self.log.info(f"Insert data into {self.table} fact table")
        
        if self.append_only:
            redshift.run("INSERT INTO {} {}".format(self.table, self.sql))
