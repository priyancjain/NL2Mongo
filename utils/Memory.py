
from collections import defaultdict

class MemoryStore:
    def __init__(self):
        self.sessions = defaultdict(list)

    def update_memory(self, session_id, message):
        self.sessions[session_id].append(message)

    def get_context(self, session_id):
        return "\n".join(self.sessions[session_id])
