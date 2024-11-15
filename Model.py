import numpy as np
import pandas as pd

credits_df = pd.read_csv("movies.csv")
movies_df = pd.read_csv("credits.csv")

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

movies_df = movies_df.merge(credits_df, on='title')
movies_df = movies_df[['movie_id', 'title','overview','genres', 'keywords', 'cast', 'crew']]


import ast

def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies_df['genres']=movies_df['genres'].apply(convert)
movies_df['keywords'] = movies_df['keywords'].apply(convert)

def convert3(obj):
    L=[]
    counter = 0
    for i in ast.literal_eval(obj):
        if counter !=3:
            L.append(i['name'])
            counter += 1
        else:
            break
    return L  

movies_df['cast'] = movies_df['cast'].apply(convert3)

def fetch_director(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L
    
movies_df['crew'] = movies_df['crew'].apply(fetch_director)

movies_df['overview'] = movies_df['overview'].apply(lambda x:str(x).split())    #this helps to split the sentences into words

movies_df['genres'] = movies_df['genres'].apply(lambda x:[i.replace(" ","")for i in x])
movies_df['keywords'] = movies_df['keywords'].apply(lambda x:[i.replace(" ","")for i in x])
movies_df['cast'] = movies_df['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies_df['crew'] = movies_df['crew'].apply(lambda x:[i.replace(" ","")for i in x])

movies_df['tags'] = movies_df['overview']+movies_df['genres']+movies_df['keywords']+movies_df['cast']+movies_df['crew']

#This operation creates a view of the original dataframe rather than a new copy, which can cause the error when trying to modify the new 
#dataframe.

new_df = movies_df[['movie_id', 'title', 'tags']].copy()

new_df['tags'] = new_df['tags'].apply(lambda x:' '.join(x))   #to remove brackets and comma and convert  tags(object) to string

new_df['tags']=new_df['tags'].apply(lambda x:x.lower())  #to convert to lower case

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english') #object creation stop_words remove joining words like is,the,an etc...

#fir_transform method convert text data to matrix and theen .toarray() convert it to numpy array
#it creates a two dimentional numpy array in which each row represents a document each column represent features
vectors = cv.fit_transform(new_df['tags']).toarray()  #vector to array convertion

import nltk 
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()  #object creation (this helps to remove suffix and prefix)

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)


from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vectors)

sorted(list(enumerate(similarity[0])), reverse = True, key=lambda x:x[1])[1:6]

def recommend(movie):
    print("\n---------------------------------   Recommended Movies   ---------------------------------\n")

    # Check if the movie exists in the DataFrame
    if movie in new_df['title'].values:
        movie_index = new_df[new_df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        for i in movies_list:
            print(new_df.iloc[i[0]].title.center(87))
        print()
        print("------------------------------------------------------------------------------------------\n")
    else:
        print(f"Sorry, the movie '{movie}' is not found in our recommendations.")

# User input
movie_name = input("\nEnter the Movie Name : ")
recommend(movie_name)
