import streamlit as st
import requests

# Replace 'your_access_key' with your actual Unsplash API access key
ACCESS_KEY = 'your_access_key'

st.markdown("<h1 style='text-align: center;'>Web Scraper</h1>", unsafe_allow_html=True)

with st.form("Search"):
    keyword = st.text_input("Enter Your keyword")
    search = st.form_submit_button("Search")
    placeholder = st.empty()

if search:
    # Unsplash API URL for searching images
    url = f"https://api.unsplash.com/search/photos?query={keyword}&client_id={ACCESS_KEY}"

    # Fetch the search results
    response = requests.get(url)
    data = response.json()

    # Check if any results were returned
    if 'results' in data and len(data['results']) > 0:
        images = data['results']
        col1, col2 = placeholder.columns(2)

        # Display images in the columns
        for i, img in enumerate(images[:4]):  # Limit to the first 4 results
            image_url = img['urls']['regular']
            if i % 2 == 0:
                col1.image(image_url)
            else:
                col2.image(image_url)
    else:
        st.write("No images found for this keyword.")
