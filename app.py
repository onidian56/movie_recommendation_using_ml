import streamlit as st
import pickle
import pandas as pd
with open('matrix.pkl','rb') as f:
    similarity=pickle.load(f)

df=pd.read_csv('movies.csv')
st.header('Movie Prediction App')

options = df['original_title']


movie=st.selectbox('Select a Movie', options)
idx=int(df.loc[df['original_title']==movie].index[0])
similar_movies=[]
others_score=similarity[idx]
for _ in range(5):
    max_idx = -1
    max_score = -float('inf')
    for i in range(others_score.size):
        if i != idx and others_score[i] > max_score and others_score[i] != 1 and others_score[i] != -1:
            max_idx = i
            max_score = others_score[i]
    if max_idx != -1:
        similar_movies.append(df.loc[max_idx, 'original_title'])
        others_score[max_idx] = -float('inf')  # Mark as visited
st.write(f'Top 5 Movies Similar to {movie}:')
for i, movie_title in enumerate(similar_movies, 1):
    st.write(f"{i}. {movie_title}")


