from flask import Blueprint, request, jsonify
from canasu.database import db

from canasu.models.enrollment import Enrollment, enrollment_schema

enrollment = Blueprint('enrollment', __name__, url_prefix='/api/enrollment')

@enrollment.post('/create')
def create_enrollment():
    mentee_id=request.json['mentee_id']
    project_id=request.json['project_id']
    m_1_id=request.json['m_1_id']
    m_2_id=request.json['m_2_id']
    m_3_id=request.json['m_3_id']
    m_4_id=request.json['m_4_id']
    enrollment=Enrollment(mentee_id=mentee_id, project_id=project_id, m_1_id=m_1_id, m_2_id=m_2_id, m_3_id=m_3_id, m_4_id=m_4_id)
    db.session.add(enrollment)
    db.session.commit()
    enrollment=Enrollment.query.filter_by(project_id=project_id).filter_by(mentee_id=mentee_id).filter_by(m_1_id=m_1_id).filter_by(m_2_id=m_2_id).filter_by(m_3_id=m_3_id).filter_by(m_4_id=m_4_id).first()
    return enrollment_schema.jsonify(enrollment), 201
