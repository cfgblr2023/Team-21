from canasu.database import db, ma

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id=db.Column(db.Integer, primary_key=True)
    mentee_id=db.Column(db.Integer, db.ForeignKey('mentee.id'), nullable=False)
    project_id=db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    mentor_id=db.Column(db.Integer, db.ForeignKey('mentor.id'), nullable=True)
    admin_id=db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)
    m_1_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_2_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_3_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_4_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_1_completed=db.Column(db.Boolean, nullable=False, default=False)
    m_2_completed=db.Column(db.Boolean, nullable=False, default=False)
    m_3_completed=db.Column(db.Boolean, nullable=False, default=False)
    m_4_completed=db.Column(db.Boolean, nullable=False, default=False)
    
    project=db.relationship('Project', backref='enrollment', lazy=True)
    mentee=db.relationship('Mentee', backref='enrollment', lazy=True)
    mentor=db.relationship('Mentor', backref='enrollment', lazy=True)
    admin=db.relationship('Admin', backref='enrollment', lazy=True)

    
class EnrollmentSchema(ma.Schema):
    class Meta:
        fields = ('id', 'mentee_id', 'project_id', 'mentor_id', 'admin_id', 'm_1_id', 'm_2_id', 'm_3_id', 'm_4_id', 'm_1_completed', 'm_2_completed', 'm_3_completed', 'm_4_completed')
                  
enrollment_schema = EnrollmentSchema()