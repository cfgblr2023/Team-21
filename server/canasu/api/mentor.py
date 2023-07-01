from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from canasu.models.mentor import Mentor, mentor_schema
from canasu.models.mentee import Mentee, mentee_schema
from canasu.models.admin import Admin, admin_schema
from canasu.models.module import Module, module_schema
from canasu.models.enrollment import Enrollment, enrollment_schema
from canasu.database import db

mentor = Blueprint('mentor', __name__, url_prefix='/api/mentor')

# @jwt_required()
@mentor.get('/<int:id>')
def mentorInfo(id):
    # admin_id = get_jwt_identity()
    # admin = Admin.query.get(admin_id)
    # if not admin:
        # return jsonify({'message': 'Not an admin'}), 404
    mentor = Mentor.query.get(id)
    if not mentor:
        return jsonify({'message': 'Mentor not found'}), 404
    # join mentor and enrollment
    mentor=mentor_schema.dump(mentor)
    enrollment=Enrollment.query.filter_by(mentor_id=mentor['id']).first()
    enrollment=enrollment_schema.dump(enrollment)
    for i in range(len(enrollment)):
        mentee=Mentee.query.get(enrollment['mentee_id'])
        mentee=mentee_schema.dump(mentee)
        enrollment['name']=mentee['name']
        enrollment['phone']=mentee['phone']
        enrollment['module_1']=module_schema.dump(Module.query.get(enrollment['m_1_id']))['name']
        enrollment['module_2']=module_schema.dump(Module.query.get(enrollment['m_2_id']))['name']
        enrollment['module_3']=module_schema.dump(Module.query.get(enrollment['m_3_id']))['name']
        enrollment['module_4']=module_schema.dump(Module.query.get(enrollment['m_4_id']))['name']
     
    mentor['enrollment']=enrollment
    return jsonify(mentor), 200

@mentor.get('/all')
def mentorAll():
    mentors = Mentor.query.all()
    if not mentors:
        return jsonify({'message': 'No mentors found'}), 404
    mentors=mentor_schema.dump(mentors, many=True)
    return jsonify(mentors), 200
        
    
