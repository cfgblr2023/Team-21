from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

from canasu.models.enrollment import Enrollment, enrollment_schema
from canasu.models.admin import Admin, admin_schema
from canasu.models.mentor import Mentor, mentor_schema
from canasu.models.mentee import Mentee, mentee_schema
from canasu.models.project import Project, project_schema
from canasu.database import db

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

@admin.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    admin = Admin.query.filter_by(email=email).first()
    if admin is None:
        return jsonify({'message': 'Admin not found'}), 404
    if check_password_hash(admin.password, password):
        access_token = create_access_token(identity=admin.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@admin.post('/register')
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    name=request.json.get('name')
    phone = request.json.get('phone')
    slots=0
    if email is None or password is None or name is None or phone is None:
        return jsonify({'message': 'Missing required fields'}), 400
    if Admin.query.filter_by(email=email).first() is not None:
        return jsonify({'message': 'Admin already exists'}), 400
    admin = Admin(email=email, password=generate_password_hash(password), name=name, phone=phone, slots=slots)
    db.session.add(admin)
    db.session.commit()
    
    access_token = create_access_token(identity=admin.id)
    return jsonify({'access_token': access_token}), 200

