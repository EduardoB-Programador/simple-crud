from person import Person

import pymongo
import pymongo.collection
import pymongo.database

class Connectivity():

    @staticmethod
    def get_client(connectivity_string:str) -> pymongo.MongoClient:
        return pymongo.MongoClient(connectivity_string)
    
    @staticmethod
    def get_db(client:pymongo.MongoClient, database_string:str) -> pymongo.database.Database:
        return client[database_string]

    @staticmethod
    def get_collection(db:pymongo.database.Database, collection_str:str) -> pymongo.collection.Collection:
        return db[collection_str]
    
    @staticmethod
    def insert_one(collection:pymongo.collection.Collection, person:Person) -> None:
        collection.insert_one(person.__dict__)

    @staticmethod
    def delete_one(collection:pymongo.collection.Collection, query:dict) -> None:
        collection.delete_one(query)

    @staticmethod
    def update_one(collection:pymongo.collection.Collection, query:dict, values:dict) -> None:
        collection.update_one(query, values)

    @staticmethod
    def update_many(collection:pymongo.collection.Collection, query:dict, values:dict) -> None:
        collection.update_many(query, values)

    @staticmethod
    def find(collection:pymongo.collection.Collection, query:dict|None = None, projection:dict|None = None) -> list:
        return collection.find(query, projection).to_list()