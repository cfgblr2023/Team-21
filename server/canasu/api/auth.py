from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

from canasu.models.mentor import Mentor, mentor_schema
from canasu.models.mentee import Mentee, mentee_schema
from canasu.models.admin import Admin, admin_schema 
from canasu.database import db

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

def send_credentials(user, role):
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)
    
    response = {
        'message': 'Logged in as {} - {}'.format(user.email, role),
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return response

@auth.post('/register/mentor')
def register_mentor():
    if request.json: 
        name = request.json.get('name')
        email = request.json.get('email')
        phone = request.json.get('phone')
        password = request.json.get('password')
        password = generate_password_hash(password)
        gender = request.json.get('gender')
        dob = request.json.get('dob')
        address = request.json.get('address')
        languages = request.json.get('languages')
        education = request.json.get('education')
        qualification = request.json.get('qualification')
        availability = request.json.get('availability')
        project_id = request.json.get('project_id')
        
        mentor = Mentor(
            name=name,
            email=email,
            phone=phone,
            password=password,
            gender=gender,
            dob=dob,
            address=address,
            languages=languages,
            education=education,
            qualification=qualification,
            availability=availability,
            project_id=project_id
        )
        
        db.session.add(mentor)
        db.session.commit()
        
        response = {
            'message': 'Mentor registered successfully',
            'mentor': mentor_schema.dump(mentor)
        }
        return jsonify(response), 201

    else:
        # Return an error response if the request body is not JSON
        response = {
            'message': 'Invalid request body'
        }
        return jsonify(response), 400

@auth.post('/register/mentee')
def register_mentee(): 
    if request.json:
        name = request.json.get('name')
        email = request.json.get('email')
        phone = request.json.get('phone')
        password = request.json.get('password')
        password = generate_password_hash(password)
        dob = request.json.get('dob')
        address = request.json.get('address')
        languages = request.json.get('languages')
        education = request.json.get('education')

        new_mentee = Mentee(name=name, email=email, phone=phone, password=password, dob=dob,
                            address=address, languages=languages, education=education)

        db.session.add(new_mentee)
        db.session.commit()

        return jsonify({'message': 'Mentee registered successfully.'}), 200

    return jsonify({'message': 'Invalid request.'}), 400
    
@auth.post('/login')
def login():
    if request.json:
        email = request.json.get('email')
        password = request.json.get('password')
        is_mentor = request.json.get('is_mentor')
        
        if is_mentor:
            mentor = Mentor.query.filter_by(email=email).first()
            if not mentor or not check_password_hash(mentor.password, password):
                return jsonify({'message': 'Invalid credentials'}), 401
            return jsonify(send_credentials(mentor, 'mentor')), 200
        elif not is_mentor:
            mentee = Mentee.query.filter_by(email=email).first()
            if not mentee or not check_password_hash(mentee.password, password):
                return jsonify({'message': 'Invalid credentials'}), 401
            return jsonify(send_credentials(mentee, 'mentee')), 200
        return jsonify({'message': 'Something Happened'}), 400
    else:
        return jsonify({'message': 'Invalid request'}), 400