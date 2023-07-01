from flask import Blueprint, request, jsonify, make_response
from canasu.models.mentor import Mentor, mentor_schema
from canasu.database import db

auth = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth.post('/register/mentor')
def register():
    if request.json: 
        name = request.json.get('name')
        email = request.json.get('email')
        phone = request.json.get('phone')
        password = request.json.get('password')
        gender = request.json.get('gender')
        dob = request.json.get('dob')
        address = request.json.get('address')
        languages = request.json.get('languages')
        education = request.json.get('education')
        qualification = request.json.get('qualification')
        availability = request.json.get('availability')
        
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
            availability=availability
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

 