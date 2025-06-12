import requests
import os
import re
class LLM:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "meta-llama/llama-4-scout-17b-16e-instruct"
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"
        self.conversation_history = []  # 🧠 Memory added

    def natural_language_to_mongo_query(self, question: str) -> dict:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        # Keep only last 5 turns to limit tokens
        context_messages = self.conversation_history[-10:]

        messages = context_messages + [
            {
                "role": "system",
                "content": """You are a MongoDB expert. Translate the following user question into a valid MongoDB query. 
- If it’s a filter, return a `find` query.
- If it's aggregation (count, group by, trends), return an aggregation pipeline.
- If it's not answerable, return {"info": "not answerable"}.
Return only valid Python dict or list, no backticks or explanations."""
            },
            {
                "role": "user",
                "content": f"Question: {question}"
            }
        ]

        data = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.2
        }

        response = requests.post(self.api_url, headers=headers, json=data)
        output = response.json()

        try:
            raw = output['choices'][0]['message']['content'].strip()
            raw = re.sub(r"^MongoDB Query:|```+|\n", "", raw).strip()

            if raw.count("{") > raw.count("}"):
                raw += "}"
            if raw.count("[") > raw.count("]"):
                raw += "]"

            # update conversation history
            self.conversation_history.append({"role": "user", "content": question})
            self.conversation_history.append({"role": "assistant", "content": raw})

            return eval(raw)
        except Exception as e:
            print("Error:", e)
            return {"error": "Parsing failed", "llm_response": output}

# class LLM:
#     def __init__(self):
#         self.api_key = os.getenv("GROQ_API_KEY")  # Or hardcode here for local testing
#         self.model = "meta-llama/llama-4-scout-17b-16e-instruct"
#         self.api_url = "https://api.groq.com/openai/v1/chat/completions"

#     def natural_language_to_mongo_query(self, question: str) -> dict:
#         headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json"
#         }

#         messages = [
#             {
#                 "role": "system",
#                 "content": """You are a MongoDB expert.
# Translate the following question to a MongoDB query:
# - If it’s a filter, return a find query.
# - If it's aggregation (count, group by, trends), return a MongoDB aggregation pipeline.
# - If it's unanswerable, return {"info": "not answerable"}.
# Return only valid Python dict or list format, no backticks, no explanation."""
#             },
#             {
#                 "role": "user",
#                 "content": f"Question: {question}"
#             }
#         ]

#         data = {
#             "model": self.model,
#             "messages": messages,
#             "temperature": 0.2
#         }

#         response = requests.post(self.api_url, headers=headers, json=data)
#         output = response.json()

#         try:
#             raw = output['choices'][0]['message']['content'].strip()
#             raw = re.sub(r"^MongoDB Query:|```+|\n", "", raw).strip()

#             if raw.count("{") > raw.count("}"):
#                 raw += "}"
#             if raw.count("[") > raw.count("]"):
#                 raw += "]"

#             return eval(raw)
#         except Exception as e:
#             print("Error:", e)
#             return {"error": "Parsing failed", "llm_response": output}
