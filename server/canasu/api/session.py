from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import jwt_required

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

@session.post('/create')
@jwt_required()
def create_session():
    if request.json:
        mentor_id = request.json.get('mentorId')
        mentee_id = request.json.get('menteeId')
        datetime = request.json.get('datetime')
        enrollment_id = request.json.get('enrollmentId')
        hours = request.json.get('hours')
        
        session = Session(
            mentor_id=mentor_id,
            mentee_id=mentee_id,
            datetime=datetime,
            enrollment_id=enrollment_id,
            hours=hours
        )
        
        db.session.add(session)
        db.session.commit()
        
        response = {
            'message': 'Session created successfully',
            'session': session_schema.dump(session)
        }
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify({'error':'No data received'}), 400)
        
        