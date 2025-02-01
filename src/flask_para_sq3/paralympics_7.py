import sqlite3

from flask import Blueprint, render_template

from flask_para_sq3.db import get_db

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/events')
def get_events():
    db = get_db()
    events = db.execute('SELECT * FROM Event').fetchall()
    events_text = [f'{event["year"]} {event["type"]} {event["start"]} {event["end"]}' for event in events]
    return events_text


@main.route('/add-quiz-data')
def add_sample_quiz_data():
    db = get_db()
    try:
        # Insert the data, values are hardcoded for now
        quiz = db.execute('INSERT INTO quiz (quiz_name) VALUES (?)', ('Sample Quiz',))
        question = db.execute('INSERT INTO question (question) VALUES (?)',
                              ('What year were the paralympics first held in Barcelona?',))
        db.execute('INSERT INTO quiz_question (quiz_id, question_id) VALUES (?, ?)',
                   (quiz.lastrowid, question.lastrowid))
        db.execute('INSERT INTO answer_choice (question_id, choice_text, choice_value, is_correct) VALUES (?, ?, ?, ?)',
                   (question.lastrowid, '1992', 5, 1))

        # Commit the changes made above
        db.commit()
        return 'Sample data added to the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)


@main.route('/add-student-response')
def add_student_response():
    db = get_db()
    try:
        # Insert the data, values are hardcoded for now
        db.execute('INSERT INTO student_response (student_email, score, quiz_id) VALUES (?, ?, ?)',
                   ("someone@student.mail", 5, 1))
        db.commit()
        return 'Student response added to the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)


@main.route('/update-quiz/<quiz_id>/<close_date>')
def update_quiz(quiz_id, close_date):
    db = get_db()
    try:
        db.execute('UPDATE quiz SET close_date = ? WHERE quiz_id = ?', (close_date, quiz_id))
        db.commit()
        return 'Quiz updated in the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)


@main.route('/update-question/<question_id>/<host>')
def update_question(question_id, host):
    db = get_db()
    try:
        event_id = db.execute(
            'SELECT event.event_id FROM event JOIN host_event on event.event_id = host_event.event_id JOIN host ON host_event.host_id = host.host_id WHERE host.host = ?',
            (host,)).fetchone()
        db.execute('UPDATE question SET event_id = ? WHERE question_id = ?', (event_id, question_id))
        db.commit()
        return 'Question updated in the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)


@main.route('/delete-response/<response_id>')
def delete_response(response_id):
    """Delete a student response from the database."""
    db = get_db()
    try:
        db.execute('DELETE FROM student_response WHERE response_id = ?', (response_id,))
        db.commit()
        return 'Student response deleted from the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)


@main.route('/delete-quiz/<quiz_id>')
def delete_quiz(quiz_id):
    """Delete a quiz from the database.
    Due to the ON DELETE constraints, the associated data in the other tables will also be deleted.
    """
    db = get_db()
    try:
        db.execute('DELETE FROM quiz WHERE quiz_id = ?', (quiz_id,))
        db.commit()
        return 'Quiz deleted from the database.'
    except sqlite3.Error as e:
        return 'Database error: ' + str(e)