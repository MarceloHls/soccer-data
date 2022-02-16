# from datetime import datetime,timedelta
# from extract_stats_players import Extract_stats_players
# from save_data import save_json

# from os.path import join


# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     # Exemplo: Inicia em 20 de Janeiro de 2021
#     'start_date': datetime.now(),
#     'email': ['airflow@example.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     # Em caso de erros, tente rodar novamente apenas 1 vez
#     'retries': 1,
#     # Tente novamente após 30 segundos depois do erro
#     'retry_delay': timedelta(seconds=30),
#     # Execute uma vez a cada 15 minutos 
#     'schedule_interval': '*/2 * * * *'
# }

# DATALAKE_PATH = join("datalake")



# # with DAG(
# #     dag_id="extract_stat_players",
# #     default_args=default_args,
# # ) as dag:

# def save_data(data):
#     save_json(
#         data = data,
#         path_datalake= DATALAKE_PATH,
#         stage="raw",
#         table="playes_premier_ligue",
#         date=datetime.today().strftime('%Y/%m/%d'))
#     print("Dados salvos")


# def task_extrat_save_playes(param):
#     print(param)
#     data = Extract_stats_players().run(
#         param['code_ligue'],
#         param['name_ligue
#     )
#     print("Extraiu o dados")

#     save_data(
#         data=data,
#         path_datalake= DATALAKE_PATH,
#         stage="raw",
#         table=param.table_name,
#         date=datetime.today().strftime('%Y/%m/%d')
#         )

# teste = {
#         'code_ligue':9,
#         "name_ligue":"Premier-League-Stats",
#         "table_name":"premier_ligue_players"}

# task_extrat_save_playes(teste)