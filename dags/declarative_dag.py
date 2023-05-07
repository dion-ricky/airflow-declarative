import os
from datetime import datetime

from airflow.models import DAG
from airflow.settings import DAGS_FOLDER

from contrib.dag_generator import StandardETL


dag = DAG(
    dag_id='declarative_dag',
    schedule_interval='@once',
    start_date=datetime(2023, 5, 6)
)

config = open(os.path.join(DAGS_FOLDER, 'config', 'production.yaml'), 'r').read()

StandardETL.generate(config, dag)