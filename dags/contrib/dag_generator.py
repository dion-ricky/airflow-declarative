from airflow.models import DAG
from airflow.models.baseoperator import BaseOperator
from airflow.operators.bash import BashOperator
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


class StandardETL:

    def __init__(self, config, default_args) -> None:
        self.config = config
        self.default_args = default_args

    def extract_output_path(self, table_name):
        return f"{table_name}_$dag_interval_start$.csv"

    def add_start_finish(self):
        pass

    def get_extract_task(self, table_name) -> BaseOperator:
        return BashOperator(
            task_id=f"extract_{table_name}",
            bash_command=f"echo {table_name}",
            **self.default_args
        )

    def get_transfer_task(self, table_name) -> BaseOperator:
        return BashOperator(
            task_id=f"transfer_{table_name}",
            bash_command=f"echo {table_name}",
            **self.default_args
        )

    def get_load_task(self, table_name) -> BaseOperator:
        return BashOperator(
            task_id=f"load_{table_name}",
            bash_command=f"echo {table_name}",
            **self.default_args
        )

    @staticmethod
    def generate(config, dag: DAG):
        generator = StandardETL(config, dag.default_args)
        for tbl in config.keys():
            extract = generator.get_extract_task(tbl)
            transfer = generator.get_transfer_task(tbl)
            load = generator.get_load_task(tbl)
            dag.add_task(extract)
            extract.set_downstream(transfer)
            transfer.set_downstream(load)