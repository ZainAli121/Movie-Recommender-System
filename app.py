import streamlit as st
import joblib

movies = joblib.load("movies.pkl")
similarity = joblib.load("similarity_c.pkl")

def recommend(movie):
    if movie not in movies['title'].values:
        return []
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movies_list]

st.title("🎬 Movie Recommender")

selected_movie = st.selectbox("Select a movie you like:", movies['title'].values)

if st.button("Recommend"):
    recommendations = recommend(selected_movie)
    if recommendations:
        st.success("You might also like:")
        for movie in recommendations:
            st.write("🎥", movie)
    else:
        st.warning("Movie not found in database.")
