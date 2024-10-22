from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

from canasu.models.mentee import Mentee, mentee_schema
from canasu.models.mentor import Mentor, mentor_schema
from canasu.models.enrollment import Enrollment, enrollment_schema
from canasu.models.project import Project, project_schema

from canasu.database import db

mapping=Blueprint('mapping', __name__, url_prefix='/api/mapping')

@mapping.post('/enroll_many')
@jwt_required()
def enroll_many():
    enroll_array = request.get_json()['enroll_array']
    for enroll in enroll_array:
        enrollment = Enrollment.query.filter_by(mentee_id=enroll['mentee_id'], project_id=enroll['project_id']).first()
        if enrollment is None:
            return jsonify({'message': 'Enrollment does not exist'}), 400
        enrollment.mentor_id = enroll['mentor_id']
        db.session.commit()
    return jsonify({'message': 'Enrollments updated successfully'}), 200

@mapping.post('/enroll')
@jwt_required()
def enroll():
    enrollment = Enrollment.query.filter_by(mentee_id=request.get_json()['mentee_id'], project_id=request.get_json()['project_id']).first()
    if enrollment is None:
        return jsonify({'message': 'Enrollment does not exist'}), 400
    enrollment.mentor_id = request.get_json()['mentor_id']
    db.session.commit()
    return jsonify({'message': 'Enrollment updated successfully'}), 200

@mapping.post('/unenroll')
@jwt_required()
def unenroll():
    enrollment = Enrollment.query.filter_by(mentee_id=request.get_json()['mentee_id'], project_id=request.get_json()['project_id']).first()
    if enrollment is None:
        return jsonify({'message': 'Enrollment does not exist'}), 400
    enrollment.mentor_id = None
    db.session.commit()
    return jsonify({'message': 'Enrollment updated successfully'}), 200

@mapping.get('/automap')
def automap():
    enrollments = Enrollment.query.filter_by(mentor_id=None).all()
    mapping = []
    unmapped_mentees = []
    for enrollment in enrollments:
        mentor = Mentor.query.filter_by(project_id=enrollment.project_id).first()
        mentee = Mentee.query.filter_by(id=enrollment.mentee_id).first()
        # compare languages
        if mentor is None or mentee is None:
            unmapped_mentees.append(mentee_schema.dump(mentee))
            continue
        mentor=mentor_schema.dump(mentor)
        mentee=mentee_schema.dump(mentee)
        mentor_languages = mentor['languages'].split(',')
        mentee_languages = mentee['languages'].split(',')
        common_languages = list(set(mentor_languages).intersection(mentee_languages))
        enrollment= enrollment_schema.dump(enrollment)
        project_name = project_schema.dump(Project.query.filter_by(id=enrollment['project_id']).first())['name']
        if len(common_languages) == 0:
            unmapped_mentees.append(mentee_schema.dump(mentee))
        else:
            mapping.append({'mentor_id': mentor['id'], 
                        'mentee_id': mentee['id'], 
                        'project_id': enrollment['project_id'],
                        'mentor_name': mentor['name'],
                        'mentee_name': mentee['name'],
                        'common_languages': common_languages,
                        'project_name': project_name})
    return jsonify({'mapping': mapping, 'unmapped_mentees': unmapped_mentees}), 200
