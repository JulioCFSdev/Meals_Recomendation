import pandas as pd

def z_score_normalization(dataframe):
    df_normalizated = (dataframe - dataframe.mean()) / dataframe.std()
    return df_normalizated

df_breakfast = pd.read_csv("datasets\Delicias da Debora e Julio - Cafe da Manha.csv")

df_brunch = pd.read_csv("datasets\Delicias da Debora e Julio - Almoço.csv")

df_dinner = pd.read_csv("datasets\Delicias da Debora e Julio - Janta.csv")

def normalize_food_dataframe(dataframe, meal_name):
    identify_collunns = dataframe.iloc[:, :2]

    normalize_collunns = dataframe.columns[-4:]

    dataframe[normalize_collunns] = dataframe[normalize_collunns].astype(float)

    df_predictor_normalizated = z_score_normalization(dataframe[normalize_collunns])

    df_predictor_normalizated = pd.concat([identify_collunns, df_predictor_normalizated], axis=1)

    df_predictor_normalizated.info()

    file_path = 'datasets/' + meal_name + '_normalizated.csv'

    df_predictor_normalizated.to_csv(file_path, index=False)

normalize_food_dataframe(df_brunch, "brunch")

normalize_food_dataframe(df_brunch, "dinner")