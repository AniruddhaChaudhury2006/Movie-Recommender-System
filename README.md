### Movie Recommendation System

This project implements a simple movie recommendation system using content-based filtering. The system suggests movies similar to a user's favorite movie based on features like genres, keywords, tagline, cast, and director.

## Table of Contents
- [Features](#features)
- [Setup](#setup)
- [Usage](#usage)
- [How it Works](#how-it-works)

## Features
- Recommends movies based on similarity to a user-provided movie title.
- Utilizes TF-IDF vectorization to convert text features into numerical representations.
- Employs cosine similarity to measure the likeness between movies.

## Setup
To run this notebook, you need the following Python libraries. You can install them using pip:

```bash
pip install numpy pandas scikit-learn difflib
```

## Usage
1.  **Load the `movies.csv` dataset**: Ensure the `movies.csv` file is available in the Colab environment.
2.  **Run all cells**: Execute all the code cells in the notebook.
3.  **Enter your favorite movie**: When prompted, enter the name of your favorite movie.
4.  **Get Recommendations**: The system will output a list of movies similar to the one you entered.

## How it Works

1.  **Data Collection and Preprocessing**: The `movies.csv` dataset is loaded. Relevant textual features (genres, keywords, tagline, cast, director) are selected and any missing values are handled by replacing them with empty strings. These features are then combined into a single string for each movie.
2.  **Text to Feature Vectors**: The combined text features are converted into numerical feature vectors using `TfidfVectorizer`. This process assigns a numerical importance to each word based on its frequency in a document and across the entire dataset.
3.  **Cosine Similarity Calculation**: `cosine_similarity` is used to compute the similarity score between all movie pairs based on their TF-IDF feature vectors. A higher score indicates greater similarity.
4.  **Movie Recommendation**: 
    *   The user inputs a movie name.
    *   `difflib.get_close_matches` is used to find the closest matching movie title in the dataset to handle potential typos.
    *   The index of the matched movie is retrieved.
    *   The similarity scores for this movie with all other movies are extracted.
    *   These scores are sorted in descending order.
    *   The top similar movies (excluding the input movie itself) are then displayed as recommendations.
