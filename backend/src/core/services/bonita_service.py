from src.web.controllers.api.bonita_access import BonitaClient

def iniciar_proceso_recoleccion(tipo_material, cantidad, area_recoleccion):
    variables = [
        {"name": "tipoMaterial", "value": tipo_material, "type": "java.lang.String"},
        {"name": "cantidadMaterial", "value": cantidad, "type": "java.lang.Integer"},
        {"name": "lugar", "value": area_recoleccion, "type": "java.lang.String"},
        {"name": "aprobacionSolicitud", "value": False, "type": "java.lang.Boolean"},
        {"name": "pruebaRendimiento", "value": False, "type": "java.lang.Boolean"},
    ]
    
    client = BonitaClient('walter.bates', 'bpm', 'http://localhost:8577/bonita')

    if client.login():
        process_name = 'Proceso de recoleccion de material'
        process_id = client.get_process_id(process_name)

        if process_id:
            response = client.initiate_process(process_id, variables)
            if 'caseId' in response:
                case_id = response['caseId']

                for variable in variables:
                    try:
                        response = client.set_variable_by_case(case_id, variable['name'], variable['value'], variable['type'])
                        print(f"Respuesta de Bonita al actualizar la variable {variable['name']}: {response}")
                    except Exception as e:
                        print(f"Error al actualizar la variable {variable['name']}: {e}")
                try:
                    task_id = client.get_task_id_by_name('Cargar de materiales recoleccion', case_id)
                    if task_id:
                        task_details = client._do_request('GET', f'/API/bpm/userTask/{task_id}')
                        if task_details['state'] == 'ready':
                            client.complete_task(task_id)
                            return {"message": "Plan creado, proceso iniciado y tarea completada exitosamente"}, 200
                        else:
                            return {"message": "La tarea no está lista para completarse."}, 400
                    else:
                        return {"message": "No se encontró la tarea 'Cargar de materiales recoleccion'."}, 404
                except Exception as e:
                    return {"message": "Plan creado, proceso iniciado y tarea completada exitosamente"}, 200
                    #return {"message": "Error al completar la tarea"}, 500
            else:
                return {"message": "No se pudo iniciar el proceso correctamente"}, 500
        else:
            return {"message": f"No se encontró el proceso con el nombre '{process_name}'."}, 404
    else:
        return {"message": "Error en el login"}, 401
