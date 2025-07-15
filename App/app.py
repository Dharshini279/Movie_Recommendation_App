import pickle
import pandas as pd
from scipy.sparse import load_npz
import streamlit as st

ratings=pd.read_csv(r"E:\Dharshini ESECian\Placement\Project\D_Project\Movie_Recommendation_system\Datasets\ratings.csv")
movies=pd.read_csv(r"E:\Dharshini ESECian\Placement\Project\D_Project\Movie_Recommendation_system\Datasets\movies.csv")
with open("models/als_model.pkl","rb") as f:
    model=pickle.load(f)
with open("models/cosine_sim.pkl","rb") as f:
    sim=pickle.load(f)
with open("models/new.pkl","rb") as f:
    new_df=pickle.load(f)
with open("models/user_map.pkl","rb") as f:
    user_map=pickle.load(f)
interaction_csr=load_npz("models/interaction_matrix.npz")

def recommend_collaborative(user_id,top_n=5):
    if user_id not in user_map:
        return get_popular_movies(top_n)
    uid=user_map[user_id]
    u_inter=interaction_csr[uid]
    try:
        recs=model.recommend(uid,u_inter,N=top_n)
        if not recs:
            return get_popular_movies(top_n)
        movie_ids=[int(i[0]) for i in recs]
        movies['id']=movies['id'].astype(int)
        matched_movies=movies[movies['id'].isin(movie_ids)]
        if matched_movies.empty:
            return get_popular_movies(top_n)
        return matched_movies['title'].tolist()
    except Exception as e:
        return get_popular_movies(top_n)

def get_popular_movies(n=5,basepool=50):
    top_movie_ids=ratings['movieId'].value_counts().head(basepool).index.tolist()
    return movies[movies['id'].isin(top_movie_ids)].sample(n=n)['title'].tolist()

def recommend_content(movie_name, top_n=5):
    if movie_name not in new_df['title'].values:
        return []
    idx=new_df[new_df['title'] == movie_name].index[0]
    sim_scores=list(enumerate(sim[idx]))
    sim_scores=sorted(sim_scores,key=lambda x: x[1],reverse=True)[1:top_n+1]
    return [new_df.iloc[i[0]].title for i in sim_scores]    

def hybrid_Recommend(user_id=None,fallback_movie='Inception',top_n=5):
    if user_id is not None:
        collab_recs=recommend_collaborative(user_id,top_n)
        if collab_recs and "User not found" not in collab_recs[0]:
            return collab_recs
    if fallback_movie in new_df['title'].values:
        return recommend_content(fallback_movie)
    return get_popular_movies(top_n)

# ---------- STREAMLIT UI ---------- #
st.set_page_config(page_title="🎬 Movie Recommender",layout="centered")
st.title("Movie Recommendation System")

col1, col2=st.columns(2)

with col1:
    user_input=st.text_input("Enter User ID (optional)", placeholder="e.g., 1")
with col2:
    movie_input=st.text_input("Enter a movie you like", value="Inception")

if st.button("Get Recommendations"):
    try:
        user_id=int(user_input.strip()) if user_input.strip() else None
    except:
        st.warning("Please enter a valid numeric User ID.")
        user_id=None

    movie_name=movie_input.strip()
    results=hybrid_Recommend(user_id=user_id,fallback_movie=movie_name)
    st.subheader("Recommended Movies:")
    for i, title in enumerate(results,1):
        st.write(f"{i}.{title}")
