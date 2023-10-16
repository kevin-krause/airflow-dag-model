from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow import DAG
import sys

server_repo_path = '/path/to/server/repository'

# Define default_args for the DAG
default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 10, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Create a DAG instance
dag = DAG(
    'generic_example_dag',
    default_args=default_args,
    description='A generic example DAG',
    schedule_interval=timedelta(days=1),
    catchup=False,  # Prevent backfilling
)

# Define the Python functions to be used as tasks
def task1_function():
    """
    This is the function for task1.
    replace this function with your specific logic.
    """
    # Append the server repository path to the sys path
    sys.path.append(server_repo_path)
    import your_module  # Replace with the actual module you want to use

    # Your specific logic here
    result = your_module.some_function()
    print(f"Task 1 executed. Result: {result}")

def task2_function():
    """
    This is the function for task2.
    replace this function with your specific logic.
    """
    print("Task 2 executed")

# Create task instances
task1 = PythonOperator(
    task_id='task1',
    python_callable=task1_function,
    dag=dag,
)

task2 = PythonOperator(
    task_id='task2',
    python_callable=task2_function,
    dag=dag,
)

# Define the order of execution using task dependencies
task1 >> task2  # This means task1 should run before task2
