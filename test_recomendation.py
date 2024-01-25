from recomend_system import *

"""
input data:

weight - int
height - float
age - int
gender - {male, female}
activity_level - {sedentary, light, moderate, active, very active}
food_name - {str on dataset}

"""

# Example of usage
weight = 70  # in kg
height = 1.75  # in meters
age = 30  # in years
gender = "male"
activity_level = "active"

daily_caloric_expenditure = calculate_daily_caloric_expenditure(
    weight, height, age, gender, activity_level
)

breakfast_recomendation = recomendation(
    "omelete de espinafre",
    breakfast_normalizated_df,
    breakfast_df,
    daily_caloric_expenditure / 3,
)

brunch_recomendation = recomendation(
    "Salmão defumado com salada de folhas verdes e molho de mostarda e mel",
    brunch_normalizated_df,
    brunch_df,
    daily_caloric_expenditure / 3,
)

dinner_recomendation = recomendation(
    "Filé mignon suíno com abóbora assada",
    dinner_normalizated_df,
    dinner_df,
    daily_caloric_expenditure / 3,
)

"""

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

"""

print(
    "----------------------BREAKFAST RECOMENDATION-----------------------------------------"
)

print(breakfast_recomendation)
# print(
#     pd.DataFrame(
#         breakfast_recomendation,
#         columns=[
#             "Similaridade",
#             "Prato",
#             "Porção (gramas)",
#             "Calorias (gramas)",
#             "Carboidratos (gramas)",
#             "Proteína (gramas)",
#             "Gordura (gramas)",
#         ],
#     )
# )

print(
    "----------------------BRUNCH RECOMENDATION-----------------------------------------"
)

print(brunch_recomendation)

print(
    "----------------------DINNER RECOMENDATION-----------------------------------------"
)

print(dinner_recomendation)

print(
    "-------------------------------------------------------------------------------------"
)
