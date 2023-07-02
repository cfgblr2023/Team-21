from flask import Blueprint, request, jsonify

from canasu.database import db
from canasu.models.project import Project, project_schema
from canasu.models.module import Module, module_schema

project_blueprint=Blueprint('project', __name__, url_prefix='/api/project')

@project_blueprint.post('/create')
def create_project():
    name=request.json['name']
    description=request.json['description']
    project=Project(name=name, description=description)
    db.session.add(project)
    db.session.commit()
    project=Project.query.filter_by(name=name).first()
    return project_schema.jsonify(project), 201

@project_blueprint.get('/<int:id>')
def get_project(id):
    project=Project.query.get(id)
    if not project:
        return jsonify({'message': 'Project not found'}), 404
    modules=Module.query.filter_by(project_id=id).all()
    project=project_schema.dump(project)
    modules=module_schema.dump(modules, many=True)
    project['modules']=modules
    return jsonify(project), 200

@project_blueprint.get('/all')
def get_all_projects():
    projects=Project.query.all()
    return project_schema.jsonify(projects, many=True), 200
