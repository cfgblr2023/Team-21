from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from canasu.models.enrollment import Enrollment, enrollment_schema
from canasu.models.admin import Admin, admin_schema
from canasu.models.mentor import Mentor, mentor_schema
from canasu.models.mentee import Mentee, mentee_schema
from canasu.models.project import Project, project_schema

admin = Blueprint('admin', __name__, url_prefix='/api/admin')

@admin.get('/list')
@jwt_required()
def list():
    admin = Admin.query.filter_by(id=get_jwt_identity()).first()
    if admin is None:
        return jsonify({'message': 'Admin not found'}), 404
    enrollments = Enrollment.query.all()
    data = []
    for enrollment in enrollments:
        mentor = Mentor.query.get(enrollment.mentor_id)
        mentee = Mentee.query.get(enrollment.mentee_id)
        enrollment=enrollment_schema.dump(enrollment)
        enrollment['project'] = project_schema.dump(Project.query.get(enrollment['project_id']))['name']
        data.append({
            'mentor': mentor_schema.dump(mentor),
            'mentee': mentee_schema.dump(mentee),
            'enrollment': enrollment
        })
    return jsonify(data), 200