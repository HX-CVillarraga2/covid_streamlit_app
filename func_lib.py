
import pandas as pd
import datetime as dt
import requests
import numpy as np

#Funcion para llamar api y convertir response.json a dataframe
def upload_data(url,token):
    # if __name__=='__main__':
    headers ={'Authorization': token}
    
    response = requests.get(url, headers=headers)
    if response.status_code==200:
        data=response.json() #json a dataframe
    df = pd.DataFrame.from_dict(data)
    return df

#Funcion para cambiar nombres de columnas
def renombrar(df,colum1,colum2):
    g=df.columns.to_list()
    df.rename(columns={g[0]:colum1,g[1]:colum2}, inplace=True)
    return df

#Funcion para hacer dataframe con datos filtrados por anho
def time_filter(df,days):
    end_date= dt.date.today() 
    start_date= end_date - dt.timedelta(days=days)
    df_filtered=df.query(f"{df.date.name} >= @start_date and {df.date.name} <= @end_date")
    return df_filtered

#Valores nulos

def missing_val(df):
    na=df.isna().sum()[df.isna().sum()>0] #serie con suma de valores nan por columna
    nal=df[df.isna().any(1)] #dataframe con los valores nan
    return na,nal #tupla, puedo acceder con indice

def highlight_max(data, color='yellow'):
    '''
    highlight the maximum in a Series or DataFrame
    '''
    attr = 'background-color: {}'.format(color)
    if data.ndim == 1:  # Series from .apply(axis=0) or axis=1
        is_max = data == data.max()
        return [attr if v else '' for v in is_max]
    else:  # from .apply(axis=None)
        is_max = data == data.max().max()
        return pd.DataFrame(np.where(is_max, attr, ''),
                            index=data.index, columns=data.columns)