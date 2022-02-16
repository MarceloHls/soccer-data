import pandas as pd
from pathlib import Path
from os.path import join
from datetime import datetime
from extract_stats_players import Extract_stats_players



def save_json(data:pd.DataFrame,path_datalake,stage,table,date):
    path = join(path_datalake,stage,table,f"extract_date={date}")
    print(path)
    print(data)
    Path(Path(path)).mkdir(parents=True, exist_ok= True)

    
    data.to_csv(f"{path}/{table}_{datetime.strptime(date,'%Y/%m/%d')}.csv")


if __name__ == '__main__':
    DATALAKE_PATH = join("datalake")
    df = Extract_stats_players().run(
                "9",
                "Premier-League-Stats"
            )


    save_json(
            data = df,
            path_datalake= DATALAKE_PATH,
            stage="teste",
            table="teste",
            date=datetime.today().strftime('%Y/%m/%d'))


    