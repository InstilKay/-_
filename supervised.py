import streamlit as st
from bs4 import BeautifulSoup
st.title                ("UNSUPERVISED MACHINE LEARNING")
st.subheader("ASSIGNMENT")
st.subheader("K MEANS")
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
st.title("Upload files")
st.markdown("---")
image=st.file_uploader("Please upload files",type=["jpg","png"])
if image is not None:
    st.image(image)
st.title("Upload files")
st.markdown("---")
images=st.file_uploader("Please upload files",type=["jpg","png"],accept_multiple_files=True)
if image is not None:
    for image in images:
        st.image(image)

# Title of the app
st.title("K-Means Clustering with Streamlit")

# Introduction Text
st.write("""
    This app demonstrates K-Means clustering using the Streamlit library. You can specify the number of clusters, 
    and the app will generate random data points, perform clustering, and display the results.
""")

# Sidebar for user input
st.sidebar.header("User Input Parameters")

# Number of clusters input from the user
num_clusters = st.sidebar.slider("Select Number of Clusters", min_value=2, max_value=10, value=3)

# Generate random data for clustering (you can replace this with your actual dataset)
X, _ = make_blobs(n_samples=500, centers=num_clusters, cluster_std=1.0, random_state=42)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform K-Means clustering
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
kmeans.fit(X_scaled)

# Get the cluster centers and labels
cluster_centers = kmeans.cluster_centers_
labels = kmeans.labels_

# Plotting the results
fig, ax = plt.subplots(figsize=(8, 6))

# Scatter plot of the clustered data points
scatter = ax.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels, cmap="viridis", s=50)

# Mark the cluster centers
ax.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=200, c='red', marker='X')

# Add a title and labels
ax.set_title(f"K-Means Clustering (K={num_clusters})")
ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")

# Show the plot in Streamlit
st.pyplot(fig)

# Display the cluster centers and labels
st.write("Cluster Centers:")
st.write(cluster_centers)

st.write("Labels for Each Data Point:")
st.write(labels)
