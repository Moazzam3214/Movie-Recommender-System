# 🎬 Movie Recommendation System

This project is a **content-based movie recommender system** built using **Python**, **Streamlit**, and the **TMDb API**. It suggests movies similar to a selected title based on metadata like genres, cast, crew, and keywords.

---

## 🚀 Features

* Recommends top 5 similar movies for any selected title
* Displays posters for recommendations using TMDb API
* Interactive web interface via Streamlit
* Backend powered by cosine similarity on processed text features

---

## 📁 Project Structure

```
├── pickles/
│   ├── movie_dict.pkl
│   └── similarity.pkl
├── app.py                          # Streamlit app
├── movie_recommender_system.ipynb  # Data processing and model building
├── .env                            # Contains TMDb API key
└── README.md
```

---

## 🧠 How It Works

1. **Data Preprocessing** (`movie_recommender_system.ipynb`):

   * Download dataset from Kaggle (see link below)
   * Merge and clean movie metadata (`movies.csv` + `credits.csv`)
   * Extract and transform relevant columns: cast, crew, keywords, genres
   * Combine features into a single `tags` column
   * Vectorize tags using `CountVectorizer`
   * Compute cosine similarity matrix
   * Save processed movie data and similarity matrix as pickle files

2. **Recommendation App** (`app.py`):

   * Load `movie_dict.pkl` and `similarity.pkl` from the `pickles/` folder
   * Take a movie input from the user
   * Recommend 5 most similar movies
   * Fetch and display posters via TMDb API

---

## 📥 Download Dataset

Download `movies.csv` and `credits.csv` from Kaggle:
**[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)**

After downloading, place the files in a folder named `datasets/`:

```
datasets/
├── movies.csv
└── credits.csv
```

---

## 🔧 Setup Instructions

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Set up your TMDb API key**

   Create a `.env` file in the root directory with:

   ```bash
   TMDB_API_KEY=your_tmdb_api_key_here
   ```

3. **Generate Pickle Files**

   Create a folder named `pickles/`:

   ```bash
   mkdir pickles
   ```

   Then open and run all cells in `movie_recommender_system.ipynb` to generate:

   * `pickles/movie_dict.pkl`
   * `pickles/similarity.pkl`

4. **Start the app**

   ```bash
   streamlit run app.py
   ```

---

## 📝 Requirements

* numpy
* pandas
* streamlit
* requests
* scikit-learn
* nltk
* python-dotenv
* pickle-mixin

---

## 📌 Notes

* If a movie isn't found, the app will return a message or a placeholder poster.
* Poster images are fetched from TMDb — make sure your API key has valid access.

---
