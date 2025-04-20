# Movie Recommendation System

This is a simple and interactive movie recommendation app built using **Streamlit**. It suggests movies that are similar to the one you pick, based on their descriptions, genres, cast, and other details — all powered by machine learning and natural language processing techniques.

## Why I Built This

I wanted to build a movie recommendation system that works purely by analyzing the content of movies — like their overviews, genres, and cast — without relying on user ratings or watch history. This project gave me hands-on experience with data preprocessing, vectorization, and deploying a recommendation model in a user-friendly app.

## Project Structure

Here’s how I’ve organized everything:

```
movie-recommendation-app/
│
├── app/                     # Main app logic
│   ├── app.py               # Streamlit frontend
│   ├── model_backend.py     # Backend model and recommendation logic
│   ├── vec.pkl              # Trained CountVectorizer
│   ├── sim.pkl              # Cosine similarity matrix
│   └── movies.pkl           # Final cleaned movie data
│
├── dataset/                 # Raw data files
│   ├── credits.csv
│   └── movies.csv
│
├── model/                   # Notebook for model development
│   └── Movie_Recommendation_Model.ipynb
│
└── README.md                # You're here :)
```

## About the Dataset

- **Source**: [TMDB 5000 Movie Dataset – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- **Files Used**:
  - `movies.csv`: Info about movies like title, overview, genres, etc.
  - `credits.csv`: Info about cast and crew

### What I Did with the Data:

- Merged both files using movie IDs
- Selected columns like overview, cast, crew, and genres
- Combined everything into a single `tags` column
- Cleaned the text, removed stopwords, and applied stemming
- Used `CountVectorizer` to turn text into vectors (limited to top 5000 words)
- Calculated similarity between movies using **cosine similarity**

## How the Model Works

- It’s a **content-based filtering** system
- NLP techniques used: tokenization and stemming
- Vectorized using **CountVectorizer**
- Similarity is calculated using **cosine similarity**
- Final data and models are stored in `vec.pkl`, `sim.pkl`, and `movies.pkl`
- All preprocessing and model training was done in the `model.ipynb` notebook

## How Recommendations Are Generated

The file `model_backend.py` takes care of:

- Loading the vectorizer and similarity matrix
- Searching for the selected movie
- Returning the top 5 most similar movies based on cosine similarity

## The Streamlit App

- `app.py` is the main file to run the app
- It lets users search or pick a movie title
- When a movie is selected, it shows a list of recommended movies instantly

## Getting Started

### Step 1: Move to the project folder

```bash
cd movie-recommendation-app
```

### Step 2: Install the required packages (if not already)

```bash
pip install streamlit pandas scikit-learn nltk
```

### Step 3: Run the app

```bash
streamlit run app/app.py
```

## Example Output

If the user selects **"Inception"**, the app might recommend:

1. Interstellar  
2. The Prestige  
3. The Matrix  
4. Shutter Island  
5. Tenet  

These are based purely on the metadata, not on user preferences or ratings.

## Tech Stack

- Python  
- Streamlit  
- Pandas  
- Scikit-learn  
- NLTK  
- CountVectorizer + Cosine Similarity

## Screenshots

![image](https://github.com/user-attachments/assets/701f098e-debc-487d-9e3f-16e671064b11)

## What I’d Like to Add Next

- Show movie posters using the TMDB API  
- Display ratings and short descriptions  
- Use collaborative filtering for better recommendations  
- Improve the design with better visuals  
- Deploy the app online using Streamlit Cloud or Render

Thanks for checking out my project! Feel free to explore or suggest improvements :)
