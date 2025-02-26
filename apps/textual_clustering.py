import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import requests
from streamlit_lottie import st_lottie

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def app():
    product_descriptions = pd.read_csv('/Users/Arunkalagoni/Documents/projects/product_descriptions.csv')
    X = product_descriptions.iloc[:, 1]

    vectorizer = TfidfVectorizer(stop_words='english')
    X1 = vectorizer.fit_transform(X)

    model = KMeans(n_clusters=10, init='k-means++', max_iter=100, n_init=1)
    model.fit(X1)

    order_centroids = model.cluster_centers_.argsort()[:, ::-1]
    terms = vectorizer.get_feature_names_out()

    def print_cluster(i):
        for ind in order_centroids[i, :10]:
            st.write(' %s' % terms[ind])

    def show_recommendations(product):
        Y = vectorizer.transform([product])
        prediction = model.predict(Y)
        print_cluster(prediction[0])

    st.subheader("Textual Clustering")
    st.write("Product recommendations based on textual analysis.")

    search = load_lottie("https://assets4.lottiefiles.com/packages/lf20_bd97kkxh.json")

    with st.container():
        left_column, right_column = st.columns(2)
        with left_column:
            name = st.text_input("Enter a product name")
            if name:
                show_recommendations(name)
        with right_column:
            st_lottie(search, height=500, key="online_shopping")
