from pymongo import MongoClient
from bson import ObjectId

class MongoDBLogic:
    def __init__(self):
        self.client = None
        self.db = None

    def connect_mongo(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def execute_mongo_query(self, collection_name, query):
        collection = self.db[collection_name]
        if isinstance(query, dict) and "find" in query:
            result = list(collection.find(query.get("filter", {})))
        elif isinstance(query, list):
            result = list(collection.aggregate(query))
        else:
            raise ValueError("Unsupported query format")
        return self._convert_objectid_to_str(result)

    def _convert_objectid_to_str(self, obj):
        if isinstance(obj, list):
            return [self._convert_objectid_to_str(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: self._convert_objectid_to_str(v) for k, v in obj.items()}
        elif isinstance(obj, ObjectId):
            return str(obj)
        else:
            return obj
