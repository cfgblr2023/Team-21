from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from canasu.models.mentor import Mentor, mentor_schema
from canasu.models.mentee import Mentee, mentee_schema
from canasu.models.admin import Admin, admin_schema
from canasu.models.module import Module, module_schema
from canasu.models.project import Project, project_schema
from canasu.models.enrollment import Enrollment, enrollment_schema
from canasu.database import db

mentee = Blueprint('mentee', __name__, url_prefix='/api/mentee')

@mentee.get('/<int:id>')
@jwt_required()
def menteeInfo(id):
    admin_id = get_jwt_identity()
    admin = Admin.query.get(admin_id)
    if not admin:
        return jsonify({'message': 'Not an admin'}), 404
    mentee = Mentee.query.get(id)
    if not mentee:
        return jsonify({'message': 'Mentee not found'}), 404
    mentee=mentee_schema.dump(mentee)
    enrollment=Enrollment.query.filter_by(mentee_id=mentee['id']).first()
    enrollment=enrollment_schema.dump(enrollment)
    for i in range(len(enrollment)):
        mentor=Mentor.query.get(enrollment['mentor_id'])
        mentor=mentor_schema.dump(mentor)
        enrollment['name']=mentor['name']
        enrollment['phone']=mentor['phone']
        enrollment['project']=project_schema.dump(Project.query.get(enrollment['project_id']))['name']
        enrollment['module_1']=module_schema.dump(Module.query.get(enrollment['m_1_id']))['name']
        enrollment['module_2']=module_schema.dump(Module.query.get(enrollment['m_2_id']))['name']
        enrollment['module_3']=module_schema.dump(Module.query.get(enrollment['m_3_id']))['name']
        enrollment['module_4']=module_schema.dump(Module.query.get(enrollment['m_4_id']))['name']
     
    mentee['enrollment']=enrollment
    return jsonify(mentee), 200

@mentee.get('/all')
@jwt_required()
def menteeAll():
    admin_id = get_jwt_identity()
    admin = Admin.query.get(admin_id)
    if not admin:
        return jsonify({'message': 'Not an admin'}), 404
    mentees = Mentee.query.all()
    if not mentees:
        return jsonify({'message': 'No mentees found'}), 404
    mentees=mentee_schema.dump(mentees, many=True)
    return jsonify(mentees), 200