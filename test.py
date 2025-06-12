import requests

BASE_URL = "http://127.0.0.1:5000"  # Adjust if your Flask app runs elsewhere

session_context = []

def send_question(question):
    payload = {"question": question}
    session_context.append({"role": "user", "content": question})
    print(f"\nYou: {question}")
    response = requests.post(f"{BASE_URL}/ask_mongo", json=payload)
    try:
        result = response.json()
        print("Response:", result["query"])
        return result
    except Exception as e:
        print("Error parsing response:", e)
        print(response.text)

# 🔗 Step 1: Connect Mongo
def connect_mongo():
    response = requests.post(f"{BASE_URL}/connect_mongo", json={
        "uri": "mongodb://localhost:27017",
        "db_name": "test"  # Replace with your DB name
    })
    print(" Mongo Connected:", response.json())

if __name__ == "__main__":
    connect_mongo()

    #  Step 1: Basic query
    send_question("List all students")

    #  Step 2: Context-based query
    send_question("Now show only girls")

    #  Step 3: Further context
    send_question("And those above 18")
