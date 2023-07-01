from canasu.database import db, ma

class Enrollment(db.Model):
    __tablename__ = 'enrollment'
    id=db.Column(db.Integer, primary_key=True)
    mentee_id=db.Column(db.Integer, db.ForeignKey('mentee.id'), nullable=False)
    project_id=db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    m_1_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_2_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_3_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_4_id=db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    m_1_completed=db.Column(db.Boolean, nullable=False)
    m_2_completed=db.Column(db.Boolean, nullable=False)
    m_3_completed=db.Column(db.Boolean, nullable=False)
    m_4_completed=db.Column(db.Boolean, nullable=False)

class EnrollmentSchema(ma.Schema):
    class Meta:
        fields = ('id','name','hours')
                  
enrollment_schema = EnrollmentSchema()