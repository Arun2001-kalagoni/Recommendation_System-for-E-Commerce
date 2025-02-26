import streamlit as st
from multiapp import MultiApp
import apps.top_products as top_products
import apps.textual_clustering as textual_clustering
import apps.collaborative_filtering as collaborative_filtering

app = MultiApp()

app.add_app("Top Products", top_products.app)
app.add_app("Textual Clustering", textual_clustering.app)
app.add_app("Collaborative Filtering", collaborative_filtering.app)

app.run()
