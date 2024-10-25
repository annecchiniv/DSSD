from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required
from src.core.models.planRecoleccion import PlanRecoleccion
from src.core.models.usuario import User
from src.core.models.deposito import Deposito
from src.core.models.material import Material
from src.core.models.orden import Orden
from src.core.models.orden_material import OrdenMaterial
from src.core.models.deposito_material import DepositoMaterial
from src.core.services.bonita_service import iniciar_proceso_recoleccion
from src.core.models import db
from datetime import timedelta
from flasgger import swag_from

api_bp = Blueprint('api', __name__)

@api_bp.route('/')
def index():
    return "Conectado a la base de datos"


@api_bp.route('/registrar_usuario', methods=['POST'])
@swag_from({
    'responses': {
        201: {
            'description': 'Usuario registrado exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'mensaje': {'type': 'string', 'example': 'Usuario registrado exitosamente'}
                }
            }
        },
        400: {
            'description': 'El usuario ya existe',
            'schema': {
                'type': 'object',
                'properties': {
                    'mensaje': {'type': 'string', 'example': 'El usuario ya existe'}
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
                    'name': {'type': 'string', 'example': 'Juan'},
                    'lastname': {'type': 'string', 'example': 'Perez'},
                    'email': {'type': 'string', 'example': 'juanperez@ejemplo.com'},
                    'password': {'type': 'string', 'example': '1234'},
                }
            }
        }
    ]
})
def register():
    data = request.json
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"mensaje": "El usuario ya existe"}), 400

    new_user = User(name=name, lastname=lastname, email=email, password=password)

    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201



@api_bp.route('/auth/login_jwt', methods=['POST'])
@swag_from({
    'responses': {
        200: {
            'description': 'Inicio de sesión exitoso',
            'schema': {
                'type': 'object',
                'properties': {
                    'token': {'type': 'string', 'example': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'},
                    'user': {
                        'type': 'object',
                        'properties': {
                            'name': {'type': 'string', 'example': 'Juan'},
                            'email': {'type': 'string', 'example': 'juanperez@ejemplo.com'}
                        }
                    }
                }
            }
        },
        401: {
            'description': 'Credenciales incorrectas',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {'type': 'string', 'example': 'Invalid email or password'}
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
                    'email': {'type': 'string', 'example': 'juanperez@ejemplo.com'},
                    'password': {'type': 'string', 'example': '1234'}
                }
            }
        }
    ]
})
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user:
        print(f"Usuario con email {email} no encontrado")
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

    if not check_password_hash(user.password, password):
        print(f"Contraseña incorrecta {check_password_hash(user.password, password)}")
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401

    token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
    return jsonify({"token": token, "user": {"name": user.name, "lastname":user.lastname, "email": user.email}}), 200



@api_bp.route('/ordenes', methods=['GET'])
@jwt_required()
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de órdenes',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'nombre_orden': {'type': 'string', 'example': 'Orden de Vidrio'},
                        'reserva': {'type': 'string', 'example': 'Confirmada'},
                        'deposito_id': {'type': 'integer', 'example': 2},
                        'deposito_nombre': {'type': 'string', 'example': 'Depósito Norte'},
                        'materiales': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'integer', 'example': 1},
                                    'nombre': {'type': 'string', 'example': 'Vidrio'},
                                    'cantidad': {'type': 'integer', 'example': 50}
                                }
                            }
                        }
                    }
                }
            }
        }
    }
})
def listar_ordenes():
    ordenes = Orden.query.join(Deposito).all()  # Asegúrate de que esto esté bien

    resultado = []
    for orden in ordenes:
        # Recopilamos los materiales asociados a la orden
        materiales_data = [
            {
                "id": om.material.id,
                "nombre": om.material.nombre,
                "cantidad": om.cantidad  # Incluimos la cantidad
            }
            for om in orden.ordenes_materiales  # Recorremos la relación intermedia
        ]

        resultado.append({
            "id": orden.id,
            "nombre_orden": orden.nombre_orden,
            "reserva": orden.reserva,
            "deposito_id": orden.deposito_id,
            "deposito_nombre": orden.deposito.nombre,
            "materiales": materiales_data  # Incluimos los materiales en el resultado
        })

    return jsonify({"ordenes": resultado}), 200


    
@api_bp.route('/ordenes', methods=['POST'])
@jwt_required()
@swag_from({
    'responses': {
        201: {
            'description': 'Orden creada exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Orden creada exitosamente'},
                    'orden': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'example': 1},
                            'nombre_orden': {'type': 'string', 'example': 'Orden de Vidrio'},
                            'reserva': {'type': 'string', 'example': 'Confirmada'},
                            'deposito_id': {'type': 'integer', 'example': 2},
                            'materiales': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'material_id': {'type': 'integer', 'example': 1},
                                        'cantidad': {'type': 'integer', 'example': 50}
                                    }
                                }
                            }
                        }
                    }
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
                    'nombre_orden': {'type': 'string', 'example': 'Orden de Vidrio'},
                    'deposito_id': {'type': 'integer', 'example': 2},
                    'materiales': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'material_id': {'type': 'integer', 'example': 1},
                                'cantidad': {'type': 'integer', 'example': 50}
                            }
                        }
                    }
                }
            }
        }
    ]
})
def crear_orden():
    data = request.get_json()

    nombre_orden = data.get('nombre_orden')
    deposito_id = data.get('deposito_id')
    materiales = data.get('materiales', [])  # Lista de materiales y cantidades

    if not nombre_orden or not deposito_id or not materiales:
        return jsonify({"message": "Datos incompletos"}), 400

    # Crear la nueva orden
    nueva_orden = Orden(nombre_orden=nombre_orden, deposito_id=deposito_id)
    db.session.add(nueva_orden)
    db.session.commit()

    # Asociar los materiales a la orden
    for material in materiales:
        material_id = material.get('material_id')
        cantidad = material.get('cantidad')
        if material_id and cantidad:
            # Verificar si ya existe una relación entre el depósito y el material
            deposito_material = DepositoMaterial.query.filter_by(deposito_id=deposito_id, material_id=material_id).first()

            if not deposito_material:
                # Si no existe, crear la nueva relación en la tabla intermedia DepositoMaterial
                nuevo_deposito_material = DepositoMaterial(deposito_id=deposito_id, material_id=material_id)
                db.session.add(nuevo_deposito_material)
                db.session.commit()  # Guardamos la relación entre depósito y material

            # Asociar el material a la orden con la cantidad especificada
            orden_material = OrdenMaterial(orden_id=nueva_orden.id, material_id=material_id, cantidad=cantidad)
            db.session.add(orden_material)

    db.session.commit()

    return jsonify({"message": "Orden creada exitosamente", "orden": {
        "id": nueva_orden.id,
        "nombre_orden": nueva_orden.nombre_orden,
        "reserva": nueva_orden.reserva,
        "deposito_id": nueva_orden.deposito_id,
        "materiales": materiales
    }}), 201



@api_bp.route('/ordenes/<int:id>/estado', methods=['PUT'])
@jwt_required()
@swag_from({
    'responses': {
        200: {
            'description': 'Estado de la orden actualizado correctamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Estado de la orden actualizado correctamente'},
                    'reserva': {'type': 'string', 'example': 'Confirmada'}
                }
            }
        },
        404: {
            'description': 'Orden no encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Orden no encontrada'}
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
                    'reserva': {'type': 'string', 'example': 'Confirmada'}
                }
            }
        }
    ]
})
def actualizar_estado_orden(id):
    data = request.get_json()
    nueva_reserva = data.get('reserva')

    orden = Orden.query.get(id)
    
    if not orden:
        return jsonify({"message": "Orden no encontrada"}), 404

    orden.reserva = nueva_reserva
    db.session.commit()

    return jsonify({
        "message": "Estado de la orden actualizado correctamente",
        "reserva": orden.reserva
    }), 200

@api_bp.route('/depositos', methods=['GET'])
@jwt_required()
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de depósitos',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'nombre': {'type': 'string', 'example': 'Depósito Norte'},
                        'ubicacion': {'type': 'string', 'example': 'Calle 123'},
                        'materiales': {
                            'type': 'array',
                            'items': {
                                'type': 'object',
                                'properties': {
                                    'id': {'type': 'integer', 'example': 1},
                                    'nombre': {'type': 'string', 'example': 'Vidrio'}
                                }
                            }
                        },
                        'cantidad_ordenes': {'type': 'integer', 'example': 10}
                    }
                }
            }
        }
    }
})
def listar_depositos():
    depositos = Deposito.query.all()

    resultado = []
    for deposito in depositos:
        materiales = [{"id": dm.material.id, "nombre": dm.material.nombre} for dm in deposito.depositos_materiales]
        cantidad_ordenes = len(deposito.ordenes)

        resultado.append({
            "id": deposito.id,
            "nombre": deposito.nombre,
            "ubicacion":deposito.ubicacion,
            "materiales": materiales,
            "cantidad_ordenes": cantidad_ordenes
        })

    return jsonify({"depositos": resultado}), 200

@api_bp.route('/depositos', methods=['POST'])
@jwt_required()
@swag_from({
    'responses': {
        201: {
            'description': 'Depósito creado exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string', 'example': 'Depósito creado exitosamente'},
                    'deposito': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'example': 1},
                            'nombre': {'type': 'string', 'example': 'Depósito A'},
                            'ubicacion': {'type': 'string', 'example': 'Ciudad XYZ'}
                        }
                    }
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
                    'nombre': {'type': 'string', 'example': 'Depósito A'},
                    'ubicacion': {'type': 'string', 'example': 'Ciudad XYZ'}
                }
            }
        }
    ]
})
def crear_deposito():
    data = request.get_json()

    nombre = data.get('nombre')
    ubicacion = data.get('ubicacion')

    if not nombre or not ubicacion:
        return jsonify({"message": "Datos incompletos"}), 400

    # Crear el nuevo depósito
    nuevo_deposito = Deposito(nombre=nombre, ubicacion=ubicacion)
    db.session.add(nuevo_deposito)
    db.session.commit()

    return jsonify({"message": "Depósito creado exitosamente", "deposito": {
        "id": nuevo_deposito.id,
        "nombre": nuevo_deposito.nombre,
        "ubicacion": nuevo_deposito.ubicacion
    }}), 201


@api_bp.route('/materiales', methods=['GET'])
@jwt_required()
@swag_from({
    'responses': {
        200: {
            'description': 'Lista de materiales obtenida exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'materiales': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {'type': 'integer', 'example': 1},
                                'nombre': {'type': 'string', 'example': 'Plástico'}
                            }
                        }
                    }
                }
            }
        }
    }
})
def get_materiales():
    materiales = Material.query.all()  # Obtenemos todos los materiales de la base de datos
    materiales_data = [{'id': m.id, 'nombre': m.nombre} for m in materiales]  # Formateamos la respuesta
    return jsonify({'materiales': materiales_data})




    client = BonitaClient('walter.bates', 'bpm', 'http://localhost:8577/bonita')

    if client.login():
        process_name = 'Proceso de recoleccion de material'
        process_id = client.get_process_id(process_name)
        
        if process_id:
            response = client.initiate_process(process_id, variables)
            print(f"Proceso iniciado: {response}")
            return jsonify({"message": "Plan creado exitosamente"}), 200
        else:
            print(f"No se encontró el proceso con el nombre '{process_name}'.")
            return jsonify({"message": "Proceso no encontrado"}), 404
    else:
        return jsonify({"message": "Error en el login"}), 401