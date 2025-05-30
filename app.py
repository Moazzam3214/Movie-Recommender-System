import numpy as np
import streamlit as st
import pandas as pd
import pickle
import requests
import os
from dotenv import load_dotenv

load_dotenv()
# Load movie data
movie_dict = pickle.load(open('pickles/movie_dict.pkl', 'rb'))
similarity = pickle.load(open('pickles/similarity.pkl', 'rb'))

df = pd.DataFrame(movie_dict)


def recommend(movie_title):
    try:
        movie_index = df[df['title'] == movie_title].index[0]
        distance = similarity[movie_index]
        movie_list = sorted(list(enumerate(distance)),
                            reverse=True, key=lambda x: x[1])[1:6]

        # Create a list to store recommended movie titles and posters
        recommended_movies = []
        posters = []
        for movie in movie_list:
            movie_id = df.iloc[movie[0]].get('id', None)
            if movie_id is None:
                continue
            recommended_movies.append(df.iloc[movie[0]].title)
            posters.append(fetch_poster(movie_id))

        return recommended_movies, posters
    except IndexError:
        # Return empty lists if the movie is not found
        return [], []


def fetch_poster(movie_id):
    tmdb_api_key = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {tmdb_api_key}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data['posters']:
            return 'https://image.tmdb.org/t/p/w500' + data['posters'][0]['file_path']
    return 'https://via.placeholder.com/500x750?text=No+Poster+Available'


st.title('Movie Recommender')
movie_title = st.selectbox(
    "Type or select a movie from the dropdown",
    df['title']
)

if st.button('Get Recommendations'):
    if movie_title:
        # Get recommendations
        recommended_movies, posters = recommend(movie_title)

        # Display recommendations
        if recommended_movies:
            st.write('Recommended Movies:')
            cols = st.columns(len(recommended_movies))
            for i, (movie, poster) in enumerate(zip(recommended_movies, posters)):
                with cols[i]:
                    st.text(movie)
                    st.image(poster, use_container_width=True)
        else:
            st.write(
                'Sorry, no recommendations found or movie not found in the database.')
    else:
        st.write('Please enter a movie name.')
