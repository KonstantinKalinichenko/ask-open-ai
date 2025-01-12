from Database import session_factory, engine
from openai import OpenAI
from flask import request, Flask, jsonify  # import Flask class to create web application
from Models import Questions_Answers, Base
from config import settings


app = Flask(__name__) # creates an instance of the Flask class

app.config[
    'SQLALCHEMY_DATABASE_URI'] = settings.DATABASE_URL_psycopg

with app.app_context():
    Base.metadata.create_all(engine)

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

    return jsonify({"question": ques, "answer": answ}), 200

if __name__ == '__main__':
    app.run(debug=True, port='5000', host='127.0.0.1')