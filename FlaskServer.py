import os # import os for os.getenv() function
from openai import OpenAI
from flask import Flask # import Flask class to create web application
from dotenv import load_dotenv # import load_dotenv for loading variables from .env

load_dotenv() # loading variables from file .env

app = Flask(__name__) # creates an instance of the Flask class

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_name = os.getenv('DB_NAME')
db_port = os.getenv('DB_PORT')

app.config[
    'SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'

@app.route("/ask", methods=['POST']) # define url-endpoint that only handles POST requests
def ask():
    data = request.get_json()
    question = data['question']
    client = OpenAI(
        api_key=os.getenv('OPENAI_API_KEY'),
    )
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        model="gpt-3.5-turbo",
    )
    answer = response.choices[0].message.content


if __name__ == '__main__':
    app.run(debug=True)