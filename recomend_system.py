import pandas as pd
import numpy as np

breakfast_df = pd.read_csv("datasets\breakfast_normalizated.csv")

def DefineEuclideanDistance(reviews1, reviews2):
    distance = 0
    commomNumberOfReviews = 0
    commomReview = False
    reviews1_list = reviews1["app_id"].tolist()
    reviews2_list = reviews2["app_id"].tolist()
    
    for games in reviews1_list:
        if games in reviews2_list:
            distance += pow(abs(reviews1[reviews1["app_id"] == games]["is_recommended"].iloc[0] -  reviews2[reviews2["app_id"] == games]["is_recommended"].iloc[0]),2)
            commomNumberOfReviews += 1
            commomReview = True
    
    root_distance = math.sqrt(distance)
    
    if commomReview:
        return [root_distance, commomNumberOfReviews]
    else:
        return [-1, commomNumberOfReviews]

def computeNearestNeighbor(reviews, username, users):
    distance_list = []
    users_list = users["user_id"].tolist()
    
    for user in users_list:
        if user != username["user_id"].iloc[0]:
            distance = DefineEuclideanDistance(reviews[reviews["user_id"] == user], username)
            if(distance[0] >= 0):
                distance_list.append((distance[0], distance[1], users[users["user_id"] == user].iloc[0].iloc[0]))
        
    distance_list.sort()
    return distance_list

def recomendation(food_preference, food_dataframe):
    nearest = computeNearestNeighbor(food_preference, food_dataframe)[0][2]
    recommendations = []
    
    positive_filtred_reviews = reviews[reviews["is_recommended"] != 0]
    neighborRatings = reviews[reviews["user_id"] == nearest]
    
    neighbor_recomend_ratings = neighborRatings["app_id"].tolist()
    username_recomend_list = username["app_id"].tolist()

    for games in neighbor_recomend_ratings:
        if games not in username_recomend_list:
            title_game = games_book[games_book["app_id"] == games].iloc[0].iloc[1]
            steam_rating = games_book[games_book["app_id"] == games].iloc[0].iloc[7]
            recommendations.append((steam_rating, title_game))

    recommendations.sort(reverse=True)
    return recommendations
