# Script para limpeza de dados

def clean_data(df):
    """
    Função para limpeza básica dos dados.
    """
    df = df.dropna()
    return df
