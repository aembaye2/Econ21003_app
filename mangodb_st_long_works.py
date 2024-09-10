import streamlit as st
from pymongo import MongoClient

# Read the connection details from the secrets.toml file
connection_string = st.secrets["mongo3"]["connection_string"]
database_name = st.secrets["mongo3"]["database"]
collection_name = st.secrets["mongo3"]["collection"]

# Connect to MongoDB using the connection string
cluster = MongoClient(connection_string)
db = cluster[database_name]
collection = db[collection_name]

# Example document to insert
# post = {"_id": 0, "name": "Abel", "score": 5}

# Insert the document into the collection
# collection.insert_one(post)


# Fetch all documents in the collection
documents = collection.find()

# Display the documents using st.write
for document in documents:
    st.write(document)
