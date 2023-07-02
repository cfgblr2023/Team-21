from flask import Blueprint, request, jsonify

from canasu.database import db
from canasu.models.project import Project, project_schema
from canasu.models.module import Module, module_schema

module_blueprint=Blueprint('module', __name__, url_prefix='/api/module')

@module_blueprint.post('/create')
def create_module():
    name=request.json['name']
    description=request.json['description']
    hours=2
    project_id=request.json['project_id']
    if not Project.query.get(project_id):
        return jsonify({'message': 'Project not found'}), 404
    module=Module(name=name, description=description, hours=hours, project_id=project_id)
    db.session.add(module)
    db.session.commit()
    module=Module.query.filter_by(name=name).filter_by(description=description).filter_by(hours=hours).filter_by(project_id=project_id).first()
    return module_schema.jsonify(module), 201

@module_blueprint.get('/all')
def get_all_modules():
    modules=Module.query.all()
    result=module_schema.dump(modules)
    return jsonify(result)