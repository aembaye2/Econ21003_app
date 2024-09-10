# conda activate cenv311
# python mangodb_connect.py
import pymongo
from pymongo import MongoClient

cluster = MongoClient(
    "mongodb+srv://abelembaye:Mankiw50%40@cluster0.auak6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["quiz"]
collection = db["econ_st"]

# # Insert the first record
# post1 = {"_id": 0, "name": "Abel", "score": 5, "email": "abel@example.com"}
# collection.insert_one(post1)

# # Insert the second record
# post2 = {"_id": 1, "name": "Tom", "score": 6, "email": "tom@example.com"}
# collection.insert_one(post2)

# Insert the second record
post3 = {"_id": 3, "name": "Tommmy", "score": 7, "email": "tommmy@example.com"}
collection.insert_one(post3)
