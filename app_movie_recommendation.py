
import numpy as np #importing dependencies
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import requests
st.markdown("""<style>.stApp{
background-color: #141414; color: white;
}
h1{
color:#E50914;
text-align = center;}
</style>""", unsafe_allow_html = True)
st.title("🎬 AI Movie Recommendation System")
movies_data = pd.read_csv('movies.csv')
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('') 
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
vectorizer = TfidfVectorizer()#converting text data to feature vectors
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors) 
list_of_all_titles = movies_data['title'].tolist()
movie_name = st.selectbox("Search your favorite movie: ", list_of_all_titles)
API_KEY = "d4701630208ab424bb5b08f3896ad2f0"
def get_movie_details(movie):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie}"
    data = requests.get(url).json()
    if len(data['results']) == 0:
        return None, None, None
    movie_id = data['results'][0]['id']
    poster = data['results'][0]['poster_path']
    rating = data['results'][0]['vote_average']
    poster_url = "https://image.tmdb.org/t/p/w500/" + poster
    video_url = f"https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}"
    video_data = requests.get(video_url).json()
    trailer = None
    for vid in video_data["results"]:
        if vid["type"] == "Trailer":
            trailer = "https://www.youtube.com/watch?v=" + vid['key']
            break
    return poster_url, rating, trailer
if st.button('Recommend'):
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    if find_close_match:
        close_match = find_close_match[0]
        index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[index_of_the_movie]))
        sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1], reverse = True)
        st.subheader('Movies recommended for you: \n') 
        cols = st.columns(5)
        i = 0
        for movie in sorted_similar_movies[1:11]:
            index = movie[0]
            title_from_index = movies_data.iloc[index]['title']
            poster, rating, trailer = get_movie_details(title_from_index)
            with cols[i % 5]:
                if poster:
                    st.image(poster)
                st.write("⭐", rating)
                st.write(title_from_index)
                if trailer:
                    st.video(trailer)
            i = i + 1
          
    
  




    
  
   
    









