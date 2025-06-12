# ChromaDB.py

class ChromaDB_VectorStore:
    def __init__(self):
        print("[ChromaDB] Initialized mock vector store")

    def run_sql(self, query):
        return []

    def get_training_plan_generic(self, schema_df):
        return {}

    def train(self, csv=None, plan=None):
        print("[ChromaDB] Training with CSV" if csv else "[ChromaDB] Training with plan")

    def ask(self, question):
        return {"filter": {}}, {"mock_result": "This is a simulated result"}
