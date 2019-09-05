args = {
    'owner': 'airflow',
    'start_date': datetime(2018,7,15),
    'depands_on_past': False,
}

dag = DAG(
    dag_id='example_bash_operator',
    default_args=args,
    schedule_interval='0 0 * * *')

task = BashOperator(task_id='basic_bash_sleep_task', bash_command='sleep 5', dag=dag)

run_this_last = DummyOperator(task_id='run_this_last', dag=dag)
run_this_last.set_upstream(task)
