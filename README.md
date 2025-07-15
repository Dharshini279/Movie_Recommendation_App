# Movie Recommendation System

This is a hybrid movie recommendation system built using **collaborative filtering** and **content-based filtering** techniques. The app is designed to suggest personalized movie recommendations based on user interactions and movie metadata — all wrapped in a simple and clean interface using **Streamlit**.

## Why I Built This

I wanted to go beyond just content-based or rating-based systems. So I built a **hybrid system** that:
- Uses **ALS collaborative filtering** to recommend movies to users based on past interactions.
- Uses **cosine similarity** to suggest similar movies based on genres, keywords, and metadata.
This helped me gain hands-on experience in preprocessing, matrix factorization, building similarity models, and deploying them in a practical, user-friendly way.

 **Model Files** are stored in a shared folder:  
 [Click here to access trained model files](https://drive.google.com/drive/folders/1Eb3uHxDvlCWNAYjG5pvbmcJ9KqzGAR2a?usp=drive_link)

These include:
- `als_model.pkl`  
- `cosine_sim.pkl`  
- `interaction_matrix.npz`  
- `new.pkl`  
- `user_map.pkl`

## Dataset Used

- **Source**: [TMDB + User Ratings dataset]
- **Files Used**:
  - `movies.csv`: Contains movie metadata like title and genres.
  - `ratings.csv`: Contains user ratings of movies.

### Data Processing Steps:
- Merged and cleaned datasets
- Mapped internal user and movie IDs
- Created a **user-item interaction matrix**
- Created a **combined "tags" column** from genres and metadata
- Preprocessed text for content filtering
- Calculated **cosine similarity matrix**

## How the Model Works

The `Movie_Recommendation_Model.ipynb` file handles everything from preprocessing to model building.

### 1. **Collaborative Filtering**
- Built using the **ALS (Alternating Least Squares)** algorithm
- Uses user-item interaction data
- Recommends movies for each user based on hidden preferences

### 2. **Content-Based Filtering**
- Processes text data from movie overviews, genres, and keywords
- Converts text into vectors using `CountVectorizer`
- Calculates similarity between movies using **cosine similarity**
- Recommends movies similar to a given movie

### 3. **Hybrid Recommendation Strategy**
- If the user is known: show ALS-based personalized recommendations
- If new or no history: fallback to content-based filtering

## Backend Logic (`app.py`)

- Loads model files from the shared model folder
- Accepts user input (user ID or movie name)
- Shows top 5 recommendations using hybrid logic
- Handles both logged-in and anonymous user flows

## Example

If the user enters their user ID (e.g. `User 50`), the app recommends:

> The Matrix  Inception  The Dark Knight  Interstellar  Fight Club

If the user types **"Iron Man"**, the content-based filter suggests:

> Iron Man 2  Avengers  Captain America  Thor  Guardians of the Galaxy

## Tech Stack

- Python  
- Pandas & NumPy  
- Scikit-learn  
- Streamlit  
- Matrix factorization (**ALS model via `implicit`**)  
- Cosine similarity  
- CountVectorizer (for content vectorization)

