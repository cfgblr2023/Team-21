from flask import Blueprint, request, jsonify, make_response

from canasu.models.session import Session, session_schema
from canasu.models.mentor import Mentor
from canasu.models.mentee import Mentee
from canasu.database import db, ma

session = Blueprint('session', __name__, url_prefix='/api/session')

@session.get('/all')
def get_all_sessions():
    sessions = Session.query.all()
    sessions = session_schema.dump(sessions)
    if not sessions:
        return make_response(jsonify({'error':'No sessions found'}), 404)
    # join based on session.mentorId, session.menteeId
    for session in sessions: 
        mentor = Mentor.query.get(session['mentorId'])
        mentee = Mentee.query.get(session['menteeId'])
        session['mentorName'] = mentor.name
        session['menteeName'] = mentee.name
    return jsonify(sessions)
        
        