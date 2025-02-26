import streamlit as st
import pandas as pd
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

    popular_products = pd.DataFrame(amazon_ratings.groupby('ProductId')['Rating'].count())
    most_popular = popular_products.sort_values('Rating', ascending=False)
    popular_products = pd.DataFrame(most_popular.head(10))

    topProduct = load_lottie("https://assets7.lottiefiles.com/packages/lf20_ao823ilv.json")

    with st.container():
        st.subheader("Top Products")
        st.write("Displaying the most popular products to help new users get started.")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write(popular_products)
        with right_column:
            st_lottie(topProduct, height=350, key="topProduct")
