import pickle
movies=pickle.load(open('movies.pkl', 'rb'))
sim=pickle.load(open('sim.pkl', 'rb'))
def recommend(movie):
    movie=movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found."]
    index=movies[movies['title'].str.lower()==movie].index[0]
    distances=sorted(list(enumerate(sim[index])), reverse=True, key=lambda x: x[1])
    result=[movies.iloc[i[0]].title for i in distances[1:6]]
    return result