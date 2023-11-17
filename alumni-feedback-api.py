from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)

@app.route('/feedback', methods=['GET', 'POST'])
def alumni_feedback():
    try:
        if request.method == 'POST':
            data = request.json
            required_fields = ['category', 'question', 'answer']
            if not all(field in data for field in required_fields):
                return jsonify({"message": "Missing required fields."}), 400

            if data['category'] != 'alumni':
                return jsonify({"message": "Invalid category for feedback. Only alumni allowed."}), 400

            new_feedback = Feedback(
                category=data['category'],
                question=data['question'],
                answer=data['answer'],
                name=data.get('name', '')  # Default to an empty string if 'name' is not present
            )
            db.session.add(new_feedback)
            db.session.commit()
            return jsonify({"message": "Alumni feedback added successfully!"})

        elif request.method == 'GET':
            # Filter by answer parameter if it exists
            answer_filter = request.args.get('answer')
            if answer_filter:
                feedback_data = Feedback.query.filter_by(answer=answer_filter).all()
            else:
                feedback_data = Feedback.query.all()

            # Convert the data to a list of dictionaries
            feedback_list = [
                {
                    "id": feedback.id,
                    "category": feedback.category,
                    "question": feedback.question,
                    "answer": feedback.answer,
                    "name": feedback.name
                }
                for feedback in feedback_data
            ]

            return jsonify({"feedback": feedback_list})

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
