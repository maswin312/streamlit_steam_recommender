import streamlit as st
import pandas as pd
import requests

similar_item = pd.read_csv("similar_item.csv")
games_list = pd.read_csv("games_list.csv")
st.title("Steam Games Recommender")
# games_list

# for i in games_list.game_title:
#     st.write(i)


game_name = st.selectbox(
    "Pick your favorite game",
    games_list.game_title,
)


game_id = games_list[games_list["game_title"] == game_name]
# game_id
st.write(game_id["game_title"].iloc[0])
st.image(game_id["header_image"].iloc[0], caption=game_id["short_description"].iloc[0])

# game_id["game_id"].iloc[0]

st.header("You might like :")

API_URL = "https://games-recommender-uvicorn-app-app-reload.onrender.com/predict/{}"

response = requests.get(API_URL)


def check_api_status(game_id):
    try:
        response = requests.get(
            API_URL.format(game_id)
        )  # Change the variable to the desired value
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException:
        return False


def fetch_data(game_id):
    response = requests.get(
        API_URL.format(game_id)
    )  # Change the variable to the desired value
    if response.status_code == 200:
        return response.json()
    else:
        return None


def similar_games(game_id):
    # Check API status
    api_up = check_api_status(game_id)

    if api_up:
        data = fetch_data(game_id)

        if data:
            # Transform data into dataframe
            df = pd.DataFrame(data)

            return df
        else:
            st.error("Failed to fetch data from API")
    else:
        st.warning("API is down. Please wait for 30 seconds and reload the app.")


# recommended_games = similar_item[
#     similar_item["src_game_id"] == game_id["game_id"].iloc[0]
# ]

recommended_games = similar_games(game_id["game_id"].iloc[0])

# recommended_games
col1, col2, col3 = st.columns(3)

with col1:
    st.image(recommended_games["header_image"].iloc[1])
    st.write(recommended_games["game_title"].iloc[1])
    st.write(recommended_games["short_description"].iloc[1])


with col2:
    st.image(recommended_games["header_image"].iloc[2])
    st.write(recommended_games["game_title"].iloc[2])
    st.write(recommended_games["short_description"].iloc[2])


with col3:
    st.image(recommended_games["header_image"].iloc[3])
    st.write(recommended_games["game_title"].iloc[3])
    st.write(recommended_games["short_description"].iloc[3])

col4, col5, col6 = st.columns(3)

with col4:
    st.image(recommended_games["header_image"].iloc[4])
    st.write(recommended_games["game_title"].iloc[4])
    st.write(recommended_games["short_description"].iloc[4])


with col5:
    st.image(recommended_games["header_image"].iloc[5])
    st.write(recommended_games["game_title"].iloc[5])
    st.write(recommended_games["short_description"].iloc[5])


with col6:
    st.image(recommended_games["header_image"].iloc[6])
    st.write(recommended_games["game_title"].iloc[6])
    st.write(recommended_games["short_description"].iloc[6])
