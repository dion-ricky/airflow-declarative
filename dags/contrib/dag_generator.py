from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

class StandardETL:

    @staticmethod
    def generate(config, dag: DAG):
        dag.add_task(
            BashOperator(
                task_id='hello_world',
                bash_command='echo hello world',
            )
        )