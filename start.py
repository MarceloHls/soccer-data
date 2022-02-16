import os 

try:
    os.system(
    "chmod +x commands_airflow.sh"
    "./commands_airflow.sh")
except:
    pass

os.system("sudo apt install xdotool")

os.system("airflow scheduler")
os.system("xdotool key ctrl+shift+t")
os.system("airflow webserver")

