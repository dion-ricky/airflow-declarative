import os
from datetime import datetime

from airflow.models import DAG
from airflow.settings import DAGS_FOLDER

import yaml
from yaml.loader import SafeLoader

from contrib.dag_generator import StandardETL


dag = DAG(
    dag_id='declarative_dag',
    schedule_interval='@once',
    start_date=datetime(2023, 5, 7),
    default_args={
        'owner': 'foo',
        'retries': 3
    }
)

config = yaml.load(open(os.path.join(DAGS_FOLDER, 'config', 'production.yaml'), 'r'),
                   Loader=SafeLoader)

StandardETL.generate(config, dag)