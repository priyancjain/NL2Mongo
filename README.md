# NL2MONGO(NATURAL LANGUAGE TO MONGODB) Application

A powerful application that combines MongoDB with Large Language Models (LLM) to enable natural language querying of MongoDB databases. This application allows users to interact with MongoDB databases using natural language, making database operations more intuitive and accessible.

## Features

- Natural language to MongoDB query conversion using LLM
- MongoDB database connection and management
- Vector store integration with ChromaDB
- RESTful API endpoints for database operations
- Conversation history management
- Support for multiple collections
- Interactive web interface

## Prerequisites

- Python 3.x
- MongoDB instance
- Virtual environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd mongo_llm_app
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
mongo_llm_app/
├── app.py              # Main Flask application
├── ChromaDB.py         # Vector store implementation
├── requirements.txt    # Project dependencies
├── test.py            # Test cases
├── templates/         # HTML templates
├── utils/            # Utility modules
│   ├── LLM.py       # Language Model implementation
│   └── MongoDBLogic.py # MongoDB operations
└── sample_data/      # Sample data for testing
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. The application will be available at `http://localhost:5000`

### API Endpoints

1. **Connect to MongoDB**
   - Endpoint: `/connect_mongo`
   - Method: POST
   - Body:
     ```json
     {
         "uri": "mongodb://your-connection-string",
         "db_name": "your-database-name"
     }
     ```

2. **Query MongoDB using Natural Language**
   - Endpoint: `/ask_mongo`
   - Method: POST
   - Body:
     ```json
     {
         "question": "your natural language question",
         "collections": ["collection1", "collection2"]
     }
     ```

3. **Reset Conversation History**
   - Endpoint: `/reset_memory`
   - Method: POST

## Dependencies

- Flask: Web framework
- PyMongo: MongoDB driver
- Requests: HTTP library
- Additional dependencies for LLM and vector store functionality

## Development

The application uses a modular architecture with the following components:

- `App` class: Combines ChromaDB vector store and LLM functionality
- `MongoDBLogic`: Handles MongoDB operations
- `LLM`: Manages language model interactions
- `ChromaDB_VectorStore`: Handles vector storage operations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Add your license information here]

## Support

For support and questions, please [add contact information or issue reporting guidelines] 