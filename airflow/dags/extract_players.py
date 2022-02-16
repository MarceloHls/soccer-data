from ast import PyCF_ONLY_AST
from doctest import testfile
import py_compile
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow import DAG
from datetime import datetime,timedelta

from pandas import value_counts


from extract_stats_players import Extract_stats_players
from save_data import save_json

from os.path import join


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    # Exemplo: Inicia em 20 de Janeiro de 2021
    'start_date': datetime.now(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    # Em caso de erros, tente rodar novamente apenas 1 vez
    'retries': 1,
    # Tente novamente após 30 segundos depois do erro
    'retry_delay': timedelta(seconds=30),
    # Execute uma vez a cada 15 minutos 
    'schedule_interval': '*/2 * * * *'
}

DATALAKE_PATH = join("datalake/players")


def values_function():
     return [
         {"code_ligue":9,"name_ligue":"Premier-League-Stats","table_name":"premier_ligue_players"},
         {"code_ligue":13,"name_ligue":"Ligue-1-Stats","table_name":"ligue_one_players"}
         ]


with DAG(
    dag_id="extract_stat_players",
    default_args=default_args,
) as dag:

    def save_data(data):
        save_json(
            data = data,
            path_datalake= DATALAKE_PATH,
            stage="raw",
            table="premier_ligue",
            date=datetime.today().strftime('%Y/%m/%d'))
        print("Dados salvos")


    def task_extrat_save_playes(**kwargs):
        param = kwargs["param"]
        data = Extract_stats_players().run(
            param['code_ligue'],
            param['name_ligue']
        )
        print("Extraiu o dados")

        save_json(
            data=data,
            path_datalake= DATALAKE_PATH,
            stage="raw",
            table=param['table_name'],
            date=datetime.today().strftime('%Y/%m/%d')
            )

    def teste(param,**kwargs):
        name_task = f"extract_{param['name_ligue']}_players"
        return PythonOperator(
            task_id=name_task,
            python_callable=task_extrat_save_playes,
            op_kwargs={"param":param}
        )


    push_func = PythonOperator(
        task_id='push_func',
        provide_context=True,
        python_callable=values_function,
        dag=dag)

    complete = DummyOperator(
        task_id='All_jobs_completed',
        dag=dag)



    for i in values_function():
        push_func >> teste(i) >> complete