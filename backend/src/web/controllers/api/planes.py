from flask import Blueprint, request
from flasgger import swag_from

planes_blueprint = Blueprint('planes_blueprint', __name__)

@planes_blueprint.route('/planes/crear-plan', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Plan creado exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Plan creado exitosamente'}
                }
            }
        },
        400: {
            'description': 'Datos incompletos',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Datos incompletos'}
                }
            }
        }
    },
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'nombre_plan': {'type': 'string', 'example': 'Recolección Semanal'},
                    'tipo_material': {'type': 'string', 'example': 'Vidrio'},
                    'cantidad': {'type': 'integer', 'example': 100},
                    'area_recoleccion': {'type': 'string', 'example': 'Zona Norte'}
                }
            }
        }
    ]
})
def crear_plan():
    data = request.json
    nombre_plan = data.get('nombre_plan')
    tipo_material = data.get('tipo_material')
    cantidad = data.get('cantidad')  # Asegúrate de obtener este como un número
    area_recoleccion = data.get('area_recoleccion')

    # Crear un diccionario con las variables del proceso
    variables = [
        {"name": "nombre_plan", "value": nombre_plan, "type": "java.lang.String"},
        {"name": "tipo_material", "value": tipo_material, "type": "java.lang.String"},
        {"name": "cantidad", "value": cantidad, "type": "java.lang.Integer"},
        {"name": "area_recoleccion", "value": area_recoleccion, "type": "java.lang.String"},
    ]
