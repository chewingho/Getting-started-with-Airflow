from airflow.models import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import timedelta
import random

args = {
    'owner': 'kateho',
    'start_date': days_ago(1) 
}

dag = DAG(dag_id = 'my_sample_dag', default_args = args, schedule_interval = None)

def run_this_func(**context):
    received_value = context['ti'].xcom_pull(key = 'random_value')
    print('hi, I received the value', received_value)

def always_fails(**context):
    if random.random() > 0.5:
        raise Exception('Exception')
    print('I am ok')

def push_to_xcom(**context):
    random_value = random.random()
    context['ti'].xcom_push(key = 'random_value', value = random_value)
    if random.random() > 0.5:
        raise Exception('Exception')
    print('I am ok')

def branch_func(**context):
    if random.random() < 0.5:
        return 'say_hi_task'
    return 'say_hello_task'

def print_hi(**context):
    received_value = context['ti'].xcom_pull(key = 'random_value')
    print('hi, I received the value', received_value)

def print_hello(**context):
    received_value = context['ti'].xcom_pull(key = 'random_value')
    print('hello, I received the value', received_value)

with dag:
    run_this_task = PythonOperator(
        task_id = 'run_this',
        python_callable = push_to_xcom,
        provide_context = True,
        retries = 10,
        retry_delay = timedelta(seconds = 1)
    )

    branch_op = BranchPythonOperator(
        task_id = 'branch_task',
        python_callable = branch_func,
        provide_context = True        
    )
    
    run_this_task3 = PythonOperator(
        task_id = 'say_hi_task',
        python_callable = print_hi,
        provide_context = True
    )

    run_this_task4 = PythonOperator(
        task_id = 'say_hello_task',
        python_callable = print_hello,
        provide_context = True
    )

    run_this_task >> branch_op >> [run_this_task3, run_this_task4]