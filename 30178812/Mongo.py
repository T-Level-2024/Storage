import sys
import pymongo
import time
connection_string = "mongodb+srv://30178812:Database%20Password@cluster0.i56il.mongodb.net/"
def connect_to_cluster(connection_string):
    try:
        client = pymongo.MongoClient(connection_string)
        print("Connected to MongoDB cluster!")
        return client
    except Exception as e:
        print("Error connecting to MongoDB: {}".format(e))
        return None

def list_databases(client):
    try:
        databases = client.list_database_names()
        print("Databases in the cluster:")
        for db in databases:
            print("- {}".format(db))
    except Exception as e:
        print("Error listing databases: {}".format(e))

def create_database_and_collection(client, db_name, collection_name):
    try:
        db = client[db_name]
        collection = db[collection_name]
        print("Database `{}` and collection `{}` created.".format(db_name, collection_name))
        return db, collection
    except Exception as e:
        print("Error creating database or collection: {}".format(e))
        return None, None

client = connect_to_cluster(connection_string)
if not client:
    sys.exit()
list_databases(client)
db, collection = create_database_and_collection(client, "test_"+time.strftime("%H_%M_%S__%d_%m_%Y"), "test_collection")
