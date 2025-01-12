import os # import os for os.getenv() function
from Database import session_factory
from openai import OpenAI
from flask import request, Flask # import Flask class to create web application
from dotenv import load_dotenv # import load_dotenv for loading variables from .env
from Models import Questions_Answers
from config import settings


app = Flask(__name__) # creates an instance of the Flask class

app.config[
    'SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL_psycopg


@app.route("/ask", methods=['POST']) # define url-endpoint that only handles POST requests
def ask():
    data = request.get_json()
    ques = data['question']
    client = OpenAI(
        api_key=settings.OPENAI_API_KEY,
    )
    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": ques
            }
        ],
        model="gpt-3.5-turbo",
    )
    answ = response.choices[0].message.content
    with session_factory() as session:
        new_question = Questions_Answers(question=ques, answer=answ)
        session.add(new_question)
        session.commit()


if __name__ == '__main__':
    app.run(debug=True)