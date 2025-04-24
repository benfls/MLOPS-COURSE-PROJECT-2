from utils.helpers import *
from config.path_config import *

similar_user = find_similar_users(7895, USER_WEIGHTS_PATH, USER2USER_ENCODED, USER2USER_DECODED)
print(similar_user)

user_preference = get_user_preferences(7895, RATING_DF, DF)
print(user_preference)
#get_user_recommendation(similar_users, user_pref, df, synopsis_df, rating_df)

