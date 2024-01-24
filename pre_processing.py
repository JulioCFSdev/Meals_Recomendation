import pandas as pd

def z_score_normalization(dataframe):
    df_normalizated = (dataframe - dataframe.mean()) / dataframe.std()
    return df_normalizated

df_breakfast = pd.read_csv("datasets\Delicias da Debora e Julio - Cafe da manha  e Almoço - Cafe da Manha (2).csv")

identify_collunns = df_breakfast.iloc[:, :2]

normalize_collunns = df_breakfast.columns[-4:]

df_breakfast[normalize_collunns] = df_breakfast[normalize_collunns].astype(float)

df_predictor_normalizated = z_score_normalization(df_breakfast[normalize_collunns])

df_predictor_normalizated = pd.concat([identify_collunns, df_predictor_normalizated], axis=1)

df_predictor_normalizated.info()

file_path = 'datasets/breakfast_normalizated.csv'

df_predictor_normalizated.to_csv(file_path, index=False)