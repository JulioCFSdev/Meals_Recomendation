import pandas as pd
import numpy as np

def DefineEuclideanDistance(food1, food2):
    distance = 0
    total = 0

    food2 = food2.transpose()

    for key in food1:
        if key in food2:
            distance += pow(abs(food1[key].iloc[0] - food2[key]), 2)
            total += 1
    return np.sqrt(distance)

def computeNearestNeighbor(food_preference, food_dataframe):
    distance_list = []
    foods_list = food_dataframe["Nome"].tolist()

    predictor_collunns = breakfast_df.columns[-4:]
    
    for food in foods_list:
        if food != food_preference["Nome"]:
            distance = DefineEuclideanDistance(food_dataframe[food_dataframe["Nome"] == food][predictor_collunns], food_preference[predictor_collunns])
            distance_list.append((distance, food_dataframe[food_dataframe["Nome"] == food].iloc[0].iloc[0]))

    distance_list.sort()
    return distance_list

def calculate_daily_caloric_expenditure(weight, height, age, gender, activity_level):
    # Harris-Benedict Formula
    if gender.lower() == 'male':
        caloric_expenditure = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender.lower() == 'female':
        caloric_expenditure = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Gender should be 'male' or 'female'")
    
    activity_levels = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    caloric_expenditure *= activity_levels.get(activity_level.lower(), 1.2)
    
    return caloric_expenditure

def recomendation(food_preference_name, food_dataframe_normalizated, food_dataframe, caloric_expenditure_porcent):
    food_preference = food_dataframe_normalizated[food_dataframe_normalizated["Nome"] == food_preference_name].iloc[0]

    nearest_food_list = computeNearestNeighbor(food_preference, food_dataframe_normalizated)

    list_double_food_recomendation = []
    food_total = 0
    for food_recomendations in nearest_food_list:
        breakfast_recomendation_calories = food_dataframe[food_dataframe["Nome"] == food_recomendations[1]].iloc[0].iloc[2]
        if(breakfast_recomendation_calories < caloric_expenditure_porcent and food_total == 0):
            nearest_food_status = GetFoodStatusList(food_recomendations, food_dataframe)
            list_double_food_recomendation.append(nearest_food_status)
        elif(breakfast_recomendation_calories < caloric_expenditure_porcent and food_total == 1):
            nearest_food_status = GetFoodStatusList(food_recomendations, food_dataframe)
            list_double_food_recomendation.append(nearest_food_status)
        elif(food_total >= 2):
            break
        food_total = food_total + 1

    return list_double_food_recomendation


def GetFoodStatusList(food, food_dataframe):
    food_status_list = []
    for food_status in food_dataframe[food_dataframe["Nome"] == food[1]].iloc[0]:
        food_status_list.append(food_status)
    food_status_list.pop(0)
    nearest_food_completed = food + tuple(food_status_list)
    return nearest_food_completed

#acess in dataframe name value
##print(breakfast_df[breakfast_df["Nome"] == "omelete de espinafre"].iloc[0].iloc[0])

#acess in dataframe food values
#print(breakfast_df[breakfast_df["Nome"] == "omelete de espinafre"].iloc[0])

breakfast_normalizated_df = pd.read_csv("datasets/breakfast_normalizated.csv")
breakfast_df = pd.read_csv("datasets/Delicias da Debora e Julio - Cafe da Manha.csv")

brunch_normalizated_df = pd.read_csv("datasets/brunch_normalizated.csv")
brunch_df = pd.read_csv("datasets/Delicias da Debora e Julio - Almoço.csv")

dinner_normalizated_df = pd.read_csv("datasets/dinner_normalizated.csv")
dinner_df = pd.read_csv("datasets/Delicias da Debora e Julio - Janta.csv")


'''
input data:

weight - int
height - float
age - int
gender - {male, female}
activity_level - {sedentary, light, moderate, active, very active}
food_name - {str on dataset}

'''

# Example of usage
weight = 70  # in kg
height = 1.75  # in meters
age = 30  # in years
gender = 'male'
activity_level = 'active'

daily_caloric_expenditure = calculate_daily_caloric_expenditure(weight, height, age, gender, activity_level)

breakfast_recomendation = recomendation("omelete de espinafre", breakfast_normalizated_df, breakfast_df, daily_caloric_expenditure/3)

brunch_recomendation = recomendation("Salmão defumado com salada de folhas verdes e molho de mostarda e mel", brunch_normalizated_df, brunch_df, daily_caloric_expenditure/3)

dinner_recomendation = recomendation("Filé mignon suíno com abóbora assada", dinner_normalizated_df, dinner_df, daily_caloric_expenditure/3)

'''

recomendation output:
[
tuple1 (food_similarity_data_1, 
        food_name_1, 
        food_proportion_1, 
        food_Calories_1, 
        food_carbohydrates_1, 
        food_proteins_1, 
        food_fat_1), 

tuple2 (food_similarity_data_2, 
        food_name_2, 
        food_proportion_2, 
        food_Calories_2, 
        food_carbohydrates_2, 
        food_proteins_2, 
        food_fat_1),
]

'''

print("----------------------BREAKFAST RECOMENDATION-----------------------------------------")

print(breakfast_recomendation)

print("----------------------BRUNCH RECOMENDATION-----------------------------------------")

print(brunch_recomendation)

print("----------------------DINNER RECOMENDATION-----------------------------------------")

print(dinner_recomendation)

print("-------------------------------------------------------------------------------------")