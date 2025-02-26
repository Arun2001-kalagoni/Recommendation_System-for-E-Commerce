import streamlit as st
import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD
import requests
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    amazon_ratings = pd.read_csv('/Users/Arunkalagoni/Documents/projects/ratings_Beauty.csv')
    amazon_ratings = amazon_ratings.dropna()

    amazon_ratings1 = amazon_ratings.head(10000)
    ratings_utility_matrix = amazon_ratings1.pivot_table(values='Rating', index='UserId', columns='ProductId', fill_value=0)

    X = ratings_utility_matrix.T
    SVD = TruncatedSVD(n_components=10)
    decomposed_matrix = SVD.fit_transform(X)
    correlation_matrix = np.corrcoef(decomposed_matrix)

    product_names = list(X.index)

    def SimilarUsers(i):
        product_ID = product_names.index(i)
        correlation_product_ID = correlation_matrix[product_ID]
        Recommend = list(X.index[correlation_product_ID > 0.90])
        Recommend.remove(i)
        for i in Recommend[0:9]:
            st.write(i)

    st.subheader("Collaborative Filtering")
    st.write("Recommending items based on purchase history.")

    filter_animation = load_lottie("https://assets7.lottiefiles.com/packages/lf20_lqge6px5.json")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            product_names = list(X.index)
            i = st.text_input("Enter a product ID")
            if i in product_names:
                SimilarUsers(i)
        with right_column:
            st_lottie(filter_animation, height=500, key="filter")
