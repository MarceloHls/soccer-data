
# source env/bin/activate


echo $AIRFLOW_HOME

#export AIRFLOW_HOME=/home/data-eginner/Documents/Soccer_Data/airflow/
#export env=/home/data-eginner/Documents/Soccer_Data/env/bin/activate



echo "\n Instalação de pacotes"

echo "\n-------------------------------------------------------------"
echo "Airflow 2.3.3"

AIRFLOW_VERSION=2.3.3
PYTHON_VERSION="$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
# For example: 3.7
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.3.3/constraints-3.7.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

echo "\n-------------------------------------------------------------"
echo "Pandas"

pip install pandas 

echo "\n-------------------------------------------------------------"
echo "Beautiful Soup"


pip install beautifulsoup4

echo "\n-------------------------------------------------------------"
echo "lxml"


pip install lxml 

echo "\n-------------------------------------------------------------"
echo "Iniciaando airflow"




export AIRFLOW_HOME=~/soccer-data/airflow
airflow standalone