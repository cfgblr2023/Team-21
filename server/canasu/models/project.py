from canasu.database import db, ma

class Project(db.Model):
    __tablename__ = 'project'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    description=db.Column(db.String(100), nullable=False)
    
class ProjectSchema(ma.Schema):
    class Meta:
        fields = ('id','name','hours')
                  
project_schema = ProjectSchema()