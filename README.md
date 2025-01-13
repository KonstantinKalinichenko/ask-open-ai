**Flask Server for OpenAI-Powered Q&A**

This project involves building a Flask server that provides a REST API endpoint to handle user questions.  
The server sends each question to the OpenAI API, retrieves an answer, and stores both the question and the answer in a PostgreSQL database🗄️.  
The entire application, including the Flask server and PostgreSQL database, is containerized with Docker and orchestrated using Docker Compose.  

**Technologies:**  
- Python
- Flask
- PostgreSQL
- SQL Alchemy
- Docker
- OpenAI API
- Alembic
- pytest
- GitHub
- pydantic

**Project Status:**
In Development

**Documentation and materials I used:**
1. https://flask.palletsprojects.com/en/stable/
2. https://docs.sqlalchemy.org/en/20/index.html
3. https://platform.openai.com/docs/api-reference/introduction
4. https://github.com/psycopg/psycopg2/issues/1282
5. https://github.com/openai/openai-python
6. https://www.psycopg.org/psycopg3/docs/index.html