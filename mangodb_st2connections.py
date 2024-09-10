
# conda activate cenv311
# streamlit run mangodb_st2connections.py
import streamlit as st
from st_mongo_connection import MongoDBConnection  # pip install streamlit-pymongo

connection = st.connection("mongodb", type=MongoDBConnection)
# st.help(connection)
# Find documents in the MongoDB collection that match the provided filters.
# If 'one' is True, only the first match will be returned.
# If 'mongo_id' is False, the Mongo ID will be excluded from the results.
# df = connection.find(filters, one=False, mongo_id=False, ttl=3600, **kwargs)
df = connection.find(ttl=3600)
st.write(df)
# Find a single document in the MongoDB collection that matches the filters.
# If 'mongo_id' is False, the Mongo ID will be excluded from the results.
# connection.find_one(filters, mongo_id=False, ttl=3600, **kwargs)
