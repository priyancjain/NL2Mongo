from flask import Flask, request, jsonify, render_template
from ChromaDB import ChromaDB_VectorStore
from utils.LLM import LLM
from utils.MongoDBLogic import MongoDBLogic
from bson import ObjectId
import re
import ast

app = Flask(__name__)

# CLASS COMPOSITION
class App(ChromaDB_VectorStore, LLM):
    def __init__(self):
        ChromaDB_VectorStore.__init__(self)
        LLM.__init__(self)

# INSTANCE DECLARATIONS
app_instance = App()
llm_instance = LLM()
mongo_instance = MongoDBLogic()  # This must come BEFORE using mongo_instance

# OBJECTID CONVERSION FUNCTION
def convert_objectid(obj):
    if isinstance(obj, list):
        return [convert_objectid(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: convert_objectid(v) for k, v in obj.items()}
    elif isinstance(obj, ObjectId):
        return str(obj)
    else:
        return obj
@app.route('/connect_mongo', methods=['POST'])
def connect_mongo():
    data = request.get_json()
    uri = data.get('uri')
    db_name = data.get('db_name')
    try:
        mongo_instance.connect_mongo(uri, db_name)
        return jsonify({'message': f'Connected to MongoDB database: {db_name}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

#  /ask_mongo ROUTE
@app.route('/ask_mongo', methods=['POST'])
def ask_mongo():
    data = request.get_json()
    question = data.get('question')
    collections = data.get('collections', [])

    # Step 1: Use the Groq LLM instance to get the Mongo query
    mongo_query = llm_instance.natural_language_to_mongo_query(question)

    # Step 2: Execute query on each collection and aggregate results
    results = {}
    for collection in collections:
        try:
            result = mongo_instance.execute_mongo_query(collection, mongo_query)
            results[collection] = result
        except Exception as e:
            results[collection] = {'error': str(e)}

    return jsonify({'query': mongo_query, 'results': results})
@app.route("/reset_memory", methods=["POST"])
def reset_memory():
    LLM.conversation_history = []
    return jsonify({"message": "Conversation history cleared."})

if __name__ == '__main__':
    app.run(debug=True)
