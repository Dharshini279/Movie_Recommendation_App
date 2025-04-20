import streamlit as st
from model_backend import recommend
st.title("Movie Recommendation System")
movie_name=st.text_input("Enter a movie name")
if st.button("Recommend"):
    recommendations=recommend(movie_name)
    st.subheader("Top Recommendations:")
    for movie in recommendations:
        st.write(movie)