# Script para limpeza de dados

def clean_data(df):
    """
    Função para limpeza básica dos dados.
    """
    # Exemplo: remover valores nulos
    df = df.dropna()
    return df
