# Movie Recommendation System

This project implements a **movie recommendation system** using the **cosine similarity algorithm**. It employs a content-based filtering approach to recommend movies similar to a user's preferences.

## Project Overview

This system utilizes movie metadata such as genres, keywords, directors, and more to represent each movie as a vector. By calculating **cosine similarity** between these vectors, the system identifies movies that closely match the user's selected movie(s).

## Features

- **Personalized Recommendations:** Suggests movies based on a user's selection.  
- **Cosine Similarity Algorithm:** Measures the similarity between movies using vectorized data.

## Dependencies

- **Python:** Version 3.x (recommended)  
- **Libraries:**
  - `pandas`: For data manipulation.
  - `numpy`: For numerical computations.
  - `scikit-learn`: For cosine similarity calculation.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/smamodia/Movie-Recommendation-System.git
    ```
2. Install the required libraries:
    ```bash
    pip install pandas numpy scikit-learn
    ```

## Usage

1. Run the main script:
    ```bash
    python script_name.py
    ```
2. The script will prompt you for a movie title or ID.
3. The system will recommend movies most similar to your selection.
