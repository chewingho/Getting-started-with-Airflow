from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from airflow.contrib.hooks.fs_hook import FSHook
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.contrib.hooks.fs_hook import FSHook
import os


from datetime import timedelta
import random

args = {
    'owner': 'kate',
    'start_date': days_ago(1) 
}

dag = DAG(dag_id = 'my_file_sample_dag', default_args = args, schedule_interval = None)


'''def say_hi(**context):
    print('hi')
'''

def print_file_content(**context):
    hook = FSHook('my_tmp_file_path')
    path = os.path.join(hook.get_path(), 'test.txt')
    with open (path, 'r') as fp:
        print(fp.read())

    #os.remove(path)

with dag:
    sensing_task = FileSensor(
        task_id = 'sensing_task',
        filepath = 'test.txt',
        fs_conn_id = 'my_tmp_file_path',
        poke_interval = 10
    )
    '''
    run_this_task = PythonOperator(
        task_id = 'say_hi_task',
        python_callable = say_hi,
        provide_context = True,
        retries = 10,
        retry_delay = timedelta(seconds = 1)
    )
    '''

    print_file_task = PythonOperator(
        task_id = 'print_file_task',
        python_callable = print_file_content,
        provide_context = True,
        retries = 10,
        retry_delay = timedelta(seconds = 1)
    )

    
    sensing_task >> print_file_task