# Movie-Recommender-System

A content-based movie recommendation system built using the TMDB 5000 Movies dataset. It suggests similar movies based on genre, keywords, cast, crew, and overview using Natural Language Processing. The app is deployed with a simple **Streamlit** web interface.

## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Model](#model)
- [License](#license)


## Overview

- Dataset: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
- Recommendation Type: Content-Based Filtering
- Language Processing:
  - Merged features: Overview, Genres, Keywords, Cast, Crew
  - Preprocessing: Tokenization, Lowercasing, Whitespace Removal, Stemming
- Vectorization: Bag of Words (CountVectorizer)
- Similarity Measure: Cosine Similarity

## Installation

1. Clone the repository:
```bash
 git clone https://github.com/ZainAli121/Movie-Recommender-System
```
2. Install the required libraries:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run app.py
```

## Model

- Merge `movies` and `credits` on title.
- Keep relevant columns: id, title, genres, keywords, overview, cast, crew.
- Apply preprocessing:
  - Convert JSON strings to lists.
  - Extract director from crew.
  - Remove whitespaces.
  - Combine all features into one "tags" column.
  - Apply stemming using NLTK’s PorterStemmer.
- Vectorize tags with `CountVectorizer` (max_features=5000).
- Compute cosine similarity for all movie pairs.


## License

This project is licensed for educational and non-commercial use.
