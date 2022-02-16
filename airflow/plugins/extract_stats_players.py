from os import remove
import urllib.request 
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import column



class Extract_stats_players():

    def __init__(
        self,
        url:str = None,
        columns:list = None ):

        self.url = url or'https://fbref.com/en/comps/{}/stats/{}'
        self.columns = columns or  [
            "Rk","Player","Nation","Pos","Squad","Age","Born","MP",
            "Starts","Min","90s","Gls","Ast","G-PK","PK","PKatt",
            "CrdY","CrdR","Gls Media","Ast Media","G+A","G-PK","G+A-PK",
            "xG","npxG","xA","npxG+xA","xG","xA","xG+xA","npxG","npxG+xA","Matches"]
        pass


    def get_html(self,params):
        url_full = self.url.format(*params)
        print(f"Acess: {url_full}")
        html_table = urllib.request.urlopen(url_full).read() 
        soup = BeautifulSoup(html_table, "html.parser")
        return str(soup).replace("<!--","").replace("-->","")



    def get_table(self,html):
        df = pd.read_html(html)
        return df[2]


    def edit_header(self,df:pd.DataFrame):
        try:
            df.columns = self.columns
        except:
           pass

        return df


    def run(self,*params):
        return self.edit_header(
            self.get_table(
                self.get_html(params)
            )
        )
        

